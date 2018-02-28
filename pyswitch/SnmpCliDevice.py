#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import pyswitch.utilities as util
import pyswitch.snmp.mlx.base.interface
import pyswitch.snmp.mlx.base.system
import pyswitch.snmp.mlx.base.utils
import pyswitch.snmp.mlx.base.acl.acl
import pyswitch.snmp.mlx.base.services
import Pyro4

from pyswitch.snmp.snmpconnector import SnmpConnector as SNMPDevice
from pyswitch.snmp.snmpconnector import SNMPError as SNMPError
from pyswitch.snmp.snmpconnector import SnmpUtils as SNMPUtils
from pyswitch.AbstractDevice import AbstractDevice
from pyswitchlib.util.configFile import ConfigFileUtil
from pyswitchlib.exceptions import (InvalidAuthenticationCredentialsError)
import re
from pyswitch.AbstractDevice import DeviceCommError


pyswitchlib_ns_daemon_file = '/etc/pyswitchlib/.pyswitchlib_ns_daemon.uri'
pyswitchlib_daemon = 'api_daemon_virtualenv_packs'

ROUTER_ATTRS = ['interface', 'system', 'acl', 'services', 'utils']


NI_VERSIONS = {
    '5.8': {
        'interface': pyswitch.snmp.mlx.base.interface.Interface,
        'system': pyswitch.snmp.mlx.base.system.System,
        'acl': pyswitch.snmp.mlx.base.acl.acl.Acl,
        'utils': pyswitch.snmp.mlx.base.utils.Utils,
        'services': pyswitch.snmp.mlx.base.services.Services,
    },
    '5.9': {
        'interface': pyswitch.snmp.mlx.base.interface.Interface,
        'system': pyswitch.snmp.mlx.base.system.System,
        'acl': pyswitch.snmp.mlx.base.acl.acl.Acl,
        'utils': pyswitch.snmp.mlx.base.utils.Utils,
        'services': pyswitch.snmp.mlx.base.services.Services,
    },
    '6.0': {
        'interface': pyswitch.snmp.mlx.base.interface.Interface,
        'system': pyswitch.snmp.mlx.base.system.System,
        'acl': pyswitch.snmp.mlx.base.acl.acl.Acl,
        'utils': pyswitch.snmp.mlx.base.utils.Utils,
        'services': pyswitch.snmp.mlx.base.services.Services,
    },
    '6.1': {
        'interface': pyswitch.snmp.mlx.base.interface.Interface,
        'system': pyswitch.snmp.mlx.base.system.System,
        'acl': pyswitch.snmp.mlx.base.acl.acl.Acl,
        'utils': pyswitch.snmp.base.utils.Utils,
        'services': pyswitch.snmp.mlx.base.services.Services,
    },
    '6.2': {
        'interface': pyswitch.snmp.mlx.base.interface.Interface,
        'system': pyswitch.snmp.mlx.base.system.System,
        'acl': pyswitch.snmp.mlx.base.acl.acl.Acl,
        'utils': pyswitch.snmp.mlx.base.utils.Utils,
        'services': pyswitch.snmp.mlx.base.services.Services,
    },
}


class SnmpCliDevice(AbstractDevice):

    """
    Device object holds the state for a single NOS device.

    Attributes:
        bgp: BGP related actions and attributes.
        interface: Interface related actions and attributes.
        snmp: SNMP related actions and attributes.
        lldp: LLDP related actions and attributes.
        system: System level actions and attributes.
    """

    def __init__(self, sysobj, **kwargs):
        """

        """
        self.base = kwargs.pop('base')
        self._conn = kwargs.pop('conn')
        self.host = self._conn[0]
        auth_snmp = kwargs.pop('auth_snmp', (None, None, None, None))
        self._auth = (auth_snmp[0], auth_snmp[1])
        self._test = kwargs.pop('test', False)
        self._callback = kwargs.pop('callback', None)
        self._enablepass = auth_snmp[2]
        snmpconfig = auth_snmp[3]
        self._snmpversion = snmpconfig['version']
        self._snmpport = snmpconfig['snmpport']
        self._snmpv2c = snmpconfig['snmpv2c']
        self._v3user = snmpconfig['v3user']
        self._v3auth = snmpconfig['v3auth']
        self._v3priv = snmpconfig['v3priv']
        self._authpass = snmpconfig['authpass']
        self._privpass = snmpconfig['privpass']
        self._sysobj = sysobj
        self._proxied = None
        ns_daemon_dict = ConfigFileUtil().read(filename=pyswitchlib_ns_daemon_file)

        if pyswitchlib_daemon in ns_daemon_dict:
            uri = ns_daemon_dict[pyswitchlib_daemon]
            with Pyro4.Proxy(uri) as pyro_proxy:
                pyro_proxy._pyroBind()
                self._proxied = pyro_proxy

        if self._callback is None:
            self._callback = self._callback_main

        self._mgr = {}

        self.reconnect()

        # self._os_type = version_list[0][2]
        devicemap = SNMPUtils.SNMP_DEVICE_MAP[sysobj]
        self.platform_type_val = devicemap[0]
        self._os_type = devicemap[1]
        self.fullver = self.firmware_version
        # self.fullver = version_list[0][1]

        thismodule = sys.modules[__name__]
        os_table = getattr(thismodule, '%s_VERSIONS' %
                           str(self.os_type).upper())

        if self.fullver in os_table:
            ver = self.fullver
        else:
            ver = util.get_two_tuple_version(self.fullver)

        for router_attr in ROUTER_ATTRS:
            if router_attr in os_table[ver]:
                setattr(
                    self.base,
                    router_attr,
                    os_table[ver][router_attr](
                        self._callback))
        # setattr(self.base, 'snmp', NI_VERSIONS['6.1.0T163']['snmp'](self._callback))

        setattr(self, 'asset', self._mgr)

    def __enter__(self):
        if 'cli' not in self._mgr or 'snmp' not in self._mgr:
            self.reconnect()

        return self

    def __exit__(self, exctype, excisnt, exctb):
        if 'cli' in self._mgr or 'snmp' in self._mgr:
            self.close()

    @property
    def connection(self):
        """
        Poll if object is still connected to device in question.
        Args:
            None
        Returns:
            bool: True if connected, False if not.
        Raises:
            None
        """
        if self._test is False:
            return self._mgr['snmp'].connected
        return False

    @property
    def mac_table(self):
        """list[dict]: the MAC table of the device.

        """
        pass

    @property
    def os_type(self):
        return self._os_type

    @property
    def suports_rbridge(self):
        return False

    @property
    def firmware_version(self):
        """
        Returns firmware version.

        Args:
            None

        Returns:
            Dictionary

        Raises:
            None

        """
        oid = SNMPUtils.DEVICE_FIRMWARE_MAP[self.os_type]
        return self._mgr['snmp'].get_os_version(oid)

    @property
    def platform_type(self):
        return self.platform_type_val

    def _callback_main(self, call, handler='snmp-get', target='running',
                       source='startup'):
        """
        Callback for SNMP/CLI calls.
        Args:
           handler: supports following values
              'snmp-get'  - To get specific OID
              'snmp-walk' - Table walk. Refer hnmp table method
              'snmp-set'  - Snmp Set operation
              'snmp-set-multiple' - Set multiple OIDs
              'cli-set'   - Set operation through CLI session
              'cli-get'   - Get command output through CLI session

           call: Based on the handler call format varies
              'snmp-get' - OID value. E.g '1.2.2.23.3.3.3.1.0'

              'snmp-set' - Tuple (OID, value) or (OID, value, type)
                           E.g. ('1.3.6.1.2.1.17.7.1.4.3.1.5.30', 6) or
                                ('1.3.6.1.2.1.17.7.1.4.3.1.5.30', 6, INTEGER)

              'snmp-set-multiple' - list of tuple [(OID, value), (OID, value)...]
                           E.g.
                           [('1.3.6.1.2.1.17.7.1.4.3.1.5.30', 6),
                            ('1.3.6.1.2.1.17.7.1.4.3.1.1.40', 'vlan40')]

              'cli-set'  - List of commands ['cmd1', 'cmd2', 'cmd3'...]
                           E.g.
                           ['int eth 0/1', 'enable', 'int eth 0/2', 'enable']

              'cli-get'  - Command string E.g 'show ip in brief'

              'snmp-walk' - Dict format:
                    config = {'oid': <oidval>,
                              'columns': {colid: colname, ...}
                              'fetch_all': <True/False>
                              'colmap': { colname: { value: 'newval', .....}}
                             }
                    Refer https://github.com/trehn/hnmp for columns and colmap
                    parameter.

                    E.g.
                    config = {}
                    config['oid'] = '1.3.6.1.2.1.47.1.1.1.1'
                    config['columns'] = { 2: 'phydescr', 16: 'assetid'}
                    config['fetch_all'] = False
                    config['colmap'] = { "assetid": { 2: "chassis", 1: "module"} }

        Returns:
            None
        Raises:
             SNMP/CLI execution error
        """

        try:

            if handler == 'snmp-get':
                value = self._mgr['snmp'].get(call)
            elif handler == 'snmp-walk':
                oid = call.get('oid')
                col = call.get('columns', None)
                fetch = call.get('fetch_all', False)
                colmap = call.get('colmap', None)
                value = self._mgr['snmp'].table(oid, columns=col,
                                                column_value_mapping=colmap,
                                                fetch_all_columns=fetch)
            elif handler == 'snmp-set':
                if len(call) == 3:
                    value = self._mgr['snmp'].set(call[0], call[1], call[2])
                else:
                    value = self._mgr['snmp'].set(call[0], call[1])
            elif handler == 'snmp-set-multiple':
                value = self._mgr['snmp'].set_multiple(call)
            elif handler == 'cli-set' or handler == 'cli-get':
                value = self._proxied.cli_execution(handler, self.host, call)
        except SNMPError:
            raise
        except Exception:
            raise

        return value

    def reconnect(self):
        """
        Reconnect session with device.

        Args:
            None

        Returns:
            bool: True if reconnect succeeds, False if not.

        Raises:
            None
        """
        if 'snmp' not in self._mgr:
            self._mgr['snmp'] = SNMPDevice(host=self.host, port=self._snmpport,
                                           version=self._snmpversion,
                                           community=self._snmpv2c,
                                           username=self._v3user,
                                           authproto=self._v3auth,
                                           authkey=self._authpass,
                                           privproto=self._v3priv,
                                           privkey=self._privpass)
        if 'cli' not in self._mgr:
            self._proxied.netmiko_acquire()
            try:
                opt = {'device_type': 'brocade_netiron'}
                opt['ip'] = self.host
                opt['username'] = self._auth[0]
                opt['password'] = self._auth[1]
                opt['global_delay_factor'] = 0.25
                if self._enablepass:
                    opt['secret'] = self._enablepass
                self._proxied.create_netmiko_connection(opt)
                self._mgr['cli'] = True
            except ValueError as error:
                msg = error.message
                if re.search(r'Netmiko Authentication Exception', msg):
                    raise InvalidAuthenticationCredentialsError(msg)
                else:
                    raise DeviceCommError(msg)
            except Exception as error:
                reason = error.message
                raise DeviceCommError("Connection object failed %s" % reason)
            finally:
                self._proxied.netmiko_release()

        return True

    def find_interface_by_mac(self, **kwargs):
        pass

    def close(self):
        if 'snmp' in self._mgr:
            del self._mgr['snmp']
        if 'cli' in self._mgr:
            del self._mgr['cli']


if __name__ == '__main__':
    import time
    from pyswitch.device import Device

    start = time.time()

    conn = ('10.24.85.107', '22')
    auth = ('admin', 'admin')

    dev = Device(conn=conn, auth=auth)
    vers = dev.firmware_version
    print vers
    print dev.os_type
    print dev.suports_rbridge

    end = time.time()
    print(end - start)
