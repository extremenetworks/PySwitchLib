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

from pyswitch.snmp.snmpconnector import SnmpConnector as SNMPDevice
from pyswitch.snmp.snmpconnector import SNMPError as SNMPError
from pyswitch.snmp.snmpconnector import SnmpUtils as SNMPUtils
from pyswitch.AbstractDevice import AbstractDevice
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException

ROUTER_ATTRS = ['interface']

NI_VERSIONS = {
    '6.1': {
        'interface': pyswitch.snmp.mlx.base.interface.Interface,
    },
}


class DeviceCommError(Exception):
    """
    Error with device communication.
    """
    pass


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
        self._auth = kwargs.pop('auth', (None, None))
        self._test = kwargs.pop('test', False)
        self._callback = kwargs.pop('callback', None)
        self._snmpversion = kwargs.pop('snmpver', 2)
        self._snmpport = kwargs.pop('snmpport', 161)
        self._snmpv2c = kwargs.pop('snmpv2c', 'public')
        self._sysobj = sysobj

        if self._callback is None:
            self._callback = self._callback_main

        self._mgr = {}

        self.reconnect()

        # self._os_type = version_list[0][2]
        self.devicetype = SNMPUtils.SNMP_DEVICE_MAP[sysobj]
        fwmap = SNMPUtils.DEVICE_FIRMWARE_MAP[self.devicetype]
        self._os_type = fwmap[0]
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
        fwmap = SNMPUtils.DEVICE_FIRMWARE_MAP[self.devicetype]
        return self._mgr['snmp'].get_os_version(fwmap[1])

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
            elif handler == "cli-set":
                self._mgr['cli'].enable()
                value = self._mgr['cli'].send_config_set(call)
            elif handler == "cli-get":
                value = self._mgr['cli'].send_command(call)
        except (SNMPError) as error:
            raise DeviceCommError(error)
        except:
            raise DeviceCommError

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
                                           community=self._snmpv2c)
        if 'cli' not in self._mgr:
            #  FIXME: Revisit this logic
            opt = {'device_type': 'brocade_netiron'}
            opt['ip'] = self.host
            opt['username'] = self._auth[0]
            opt['password'] = self._auth[1]
            opt['global_delay_factor'] = 0.5
            #  FIXME: Do we need to catch error??
            net_connect = None
            try:
                net_connect = ConnectHandler(**opt)
            except (NetMikoTimeoutException, NetMikoAuthenticationException,) as error:
                reason = error.message
                raise ValueError('Failed to execute valueerror cli on due to %s', reason)
            except SSHException as error:
                reason = error.message
                raise ValueError('Failed to execute cli on due to %s', reason)
            except Exception as error:
                reason = error.message
                raise ValueError('Failed to execute due to %s', reason)

            if net_connect is not None:
                self._mgr['cli'] = net_connect

        return True

    def find_interface_by_mac(self, **kwargs):
        pass

    def close(self):
        if 'snmp' in self._mgr:
            del self._mgr['snmp']
        if 'cli' in self._mgr:
            self._mgr['cli'].disconnect()
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
