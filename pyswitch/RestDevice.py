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
import re
import sys
import json

import pyswitch.os.base.fabric_service
import pyswitch.os.base.lldp
import pyswitch.os.base.snmp
import pyswitch.os.base.vcs
import pyswitch.os.nos.base.bgp
import pyswitch.os.nos.base.interface
import pyswitch.os.nos.base.services
import pyswitch.os.nos.base.system
import pyswitch.os.slxos.base.bgp
import pyswitch.os.slxos.base.interface
import pyswitch.os.slxos.base.isis
import pyswitch.os.slxos.base.mpls
import pyswitch.os.base.firmware
import pyswitch.os.base.utils
import pyswitch.os.slxos.base.ospf
import pyswitch.os.slxos.base.mct
import pyswitch.os.slxos.base.services
import pyswitch.os.slxos.base.system
import pyswitch.os.slxos.base.cluster
import pyswitch.os.slxos.slxr.interface
import pyswitch.os.slxos.slxs.interface
import pyswitch.utilities as util
from pyswitch.AbstractDevice import AbstractDevice
from pyswitch.XMLAsset import XMLAsset

NOS_ATTRS = ['snmp', 'interface', 'bgp', 'lldp', 'system', 'services',
             'fabric_service', 'vcs', 'isis', 'ospf', 'mpls', 'mct', 'firmware', 'cluster',
             'utils']

NOS_VERSIONS = {
    '6.0': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.nos.base.interface.Interface,
        'bgp': pyswitch.os.nos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.nos.base.system.System,
        'services': pyswitch.os.nos.base.services.Services,
        'fabric_service': pyswitch.os.base.fabric_service.FabricService,
        'vcs': pyswitch.os.base.vcs.VCS,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'utils': pyswitch.os.base.utils.Utils

    },
    '7.0': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.nos.base.interface.Interface,
        'bgp': pyswitch.os.nos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.nos.base.system.System,
        'services': pyswitch.os.nos.base.services.Services,
        'fabric_service': pyswitch.os.base.fabric_service.FabricService,
        'vcs': pyswitch.os.base.vcs.VCS,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'utils': pyswitch.os.base.utils.Utils
    },
    '7.1': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.nos.base.interface.Interface,
        'bgp': pyswitch.os.nos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.nos.base.system.System,
        'services': pyswitch.os.nos.base.services.Services,
        'fabric_service': pyswitch.os.base.fabric_service.FabricService,
        'vcs': pyswitch.os.base.vcs.VCS,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'utils': pyswitch.os.base.utils.Utils
    },
    '7.2': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.nos.base.interface.Interface,
        'bgp': pyswitch.os.nos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.nos.base.system.System,
        'services': pyswitch.os.nos.base.services.Services,
        'fabric_service': pyswitch.os.base.fabric_service.FabricService,
        'vcs': pyswitch.os.base.vcs.VCS,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'utils': pyswitch.os.base.utils.Utils
    },
    '7.3': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.nos.base.interface.Interface,
        'bgp': pyswitch.os.nos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.nos.base.system.System,
        'services': pyswitch.os.nos.base.services.Services,
        'fabric_service': pyswitch.os.base.fabric_service.FabricService,
        'vcs': pyswitch.os.base.vcs.VCS,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'utils': pyswitch.os.base.utils.Utils
    },
}
SLXOS_VERSIONS = {
    '16r.1': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.slxos.slxr.interface.Interface,
        'bgp': pyswitch.os.slxos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.slxos.base.system.System,
        'services': pyswitch.os.slxos.base.services.Services,
        'isis': pyswitch.os.slxos.base.isis.Isis,
        'ospf': pyswitch.os.slxos.base.ospf.Ospf,
        'mpls': pyswitch.os.slxos.base.mpls.Mpls,
        'mct': pyswitch.os.slxos.base.mct.Mct,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'utils': pyswitch.os.base.utils.Utils
    },
    '17r.1': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.slxos.slxr.interface.Interface,
        'bgp': pyswitch.os.slxos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.slxos.base.system.System,
        'services': pyswitch.os.slxos.base.services.Services,
        'isis': pyswitch.os.slxos.base.isis.Isis,
        'ospf': pyswitch.os.slxos.base.ospf.Ospf,
        'mpls': pyswitch.os.slxos.base.mpls.Mpls,
        'mct': pyswitch.os.slxos.base.mct.Mct,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'utils': pyswitch.os.base.utils.Utils
    },
    '17r.2': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.slxos.slxr.interface.Interface,
        'bgp': pyswitch.os.slxos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.slxos.base.system.System,
        'services': pyswitch.os.slxos.base.services.Services,
        'isis': pyswitch.os.slxos.base.isis.Isis,
        'ospf': pyswitch.os.slxos.base.ospf.Ospf,
        'mpls': pyswitch.os.slxos.base.mpls.Mpls,
        'mct': pyswitch.os.slxos.base.mct.Mct,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'utils': pyswitch.os.base.utils.Utils
    },
    '17s.1': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.slxos.slxs.interface.Interface,
        'bgp': pyswitch.os.slxos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.slxos.base.system.System,
        'services': pyswitch.os.slxos.base.services.Services,
        'isis': pyswitch.os.slxos.base.isis.Isis,
        'ospf': pyswitch.os.slxos.base.ospf.Ospf,
        'mpls': pyswitch.os.slxos.base.mpls.Mpls,
        'mct': pyswitch.os.slxos.base.mct.Mct,
        'firmware': pyswitch.os.base.firmware.Firmware,
        'cluster': pyswitch.os.slxos.base.cluster.Cluster,
        'utils': pyswitch.os.base.utils.Utils
    },
}


class Reply:
    def __init__(self, xml):
        self.data = xml


# pylint: disable=E1101
class RestDevice(AbstractDevice):
    """
    Device object holds the state for a single NOS device.

    Attributes:
        bgp: BGP related actions and attributes.
        interface: Interface related actions and attributes.
        snmp: SNMP related actions and attributes.
        lldp: LLDP related actions and attributes.
        system: System level actions and attributes.
    """

    def __init__(self, **kwargs):
        """

        """
        self.base = kwargs.pop('base')
        self._conn = kwargs.pop('conn')
        self.host = self._conn[0]
        self._auth = kwargs.pop('auth', (None, None))
        if 'auth_snmp' in kwargs:
            auth_snmp = kwargs.pop('auth_snmp', (None, None, None, None))
            self._auth = (auth_snmp[0], auth_snmp[1])
        self._callback = kwargs.pop('callback', None)
        self.os_type_val = None
        self._rest_proto = None
        self.platform_type_val = None

        if len(self._conn) >= 3:
            self._rest_proto = self._conn[2]

        if self._callback is None:
            self._callback = self._callback_main

        self._mgr = None
        self._cli = None

        self.reconnect()

        fullver = self.firmware_version
        thismodule = sys.modules[__name__]
        os_table = getattr(thismodule, '%s_VERSIONS' %
                           str(self.os_type).upper())

        if fullver in os_table:
            ver = fullver
        else:
            ver = util.get_two_tuple_version(fullver)

        for nos_attr in NOS_ATTRS:
            if nos_attr in os_table[ver]:
                """
                  utils class should be considered as
                  special as it can execute CLI commands
                  wherever REST is not supported. Hence
                  we need to pass the host and auth parameters.
                """
                if nos_attr == 'utils':
                    setattr(
                        self.base,
                        nos_attr,
                        os_table[ver][nos_attr](
                            self._callback, self.host, self._auth))
                else:
                    setattr(
                        self.base,
                        nos_attr,
                        os_table[ver][nos_attr](
                            self._callback))

        setattr(self, 'asset', self._mgr)

    def __enter__(self):
        if not self._mgr:
            self.reconnect()

        return self

    def __exit__(self, exctype, excisnt, exctb):

        if self._mgr:
            self._mgr._session.close()

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
            return self._mgr.connected
        else:
            return False

    @property
    def platform_type(self):
        """
          currently this code works for SLX and NOS.
          In future if new OS gets added then the rest request
          will vary
        """
        if self.platform_type_val is None:
            response = self._mgr.run_command(command="show chassis \| inc Chassis")
            output = response[1][0][self.host]['response']['text']
            dict_output = json.loads(output)
            self.platform_type_val = dict_output['output'][0].split(":")[1].strip()
        return self.platform_type_val

    @property
    def os_type(self):
        if self.os_type_val is None:
            self.os_type_val = self._mgr.get_os_type()
        return self.os_type_val

    @property
    def suports_rbridge(self):
        return self.os_type == 'nos'

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
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.231']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.firmware_version

        """

        return self._mgr.get_os_version()

    def _callback_main(self, call, handler='edit_config', target='running',
                       source='startup'):
        """
        Callback for NETCONF calls.
        Args:
            call: An Element Tree element containing the XML of the NETCONF
                call you intend to make to the device.
            handler: Type of ncclient call to make.
                get_config: NETCONF standard get config.
                get: ncclient dispatch. For custom RPCs.
                edit_config: NETCONF standard edit.
                delete_config: NETCONF standard delete.
                copy_config: NETCONF standard copy.
            target: Target configuration location for action. Only used for
                edit_config, delete_config, and copy_config.
            source: Source of configuration information for copying
                configuration. Only used for copy_config.
        Returns:
            None
        Raises:
            None
        """
        """
        print 'asset.%s(%s)' % (call[0], ", ".join(
            ["=".join([key, '\'%s\'' % str(val) if isinstance(val, str)
                       else str(val)]) for key, val in
                call[1].items()]))
        """
        if self._mgr.get_os_type() != 'nos':
            call[1].pop('rbridge_id', None)

        (status, result) = getattr(self._mgr, call[0])(**call[1])

        if not status:
            op = self._mgr.get_xml_output()
            if '' != op and 'object already exists' not in op:
                raise ValueError(op)

        if handler == 'get_config':
            xml = self._mgr.get_xml_output()
            xml_ns = '<output>%s</output>' % (re.sub(' xmlns[^ \t\n\r\f\v>]+|y:', '', xml))
            return Reply(xml_ns)

        if handler == 'get':
            xml = self._mgr.get_xml_output()
            xml_ns = re.sub(' xmlns[^ \t\n\r\f\v>]+', '', xml)
            return Reply(xml_ns)
        return Reply(self._mgr.get_xml_output())

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

        self._mgr = XMLAsset(ip_addr=self._conn[0], auth=self._auth, rest_proto=self._rest_proto)
        return True

    def close(self):
        """Close REST session.
        Args:
            None
        Returns:
            None
        Raises:
            None
        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22', 'http')
            >>> auth = ('admin', 'password')
            >>> dev = pyswitch.device.Device(conn=conn, auth=auth)
            >>> dev.connection
            True
            >>> dev.close() # doctest: +ELLIPSIS
            <?xml...<rpc-reply...<ok/>...
            >>> dev.connection
            False
        """
        if self._mgr:
            self._mgr._session.close()


if __name__ == '__main__':
    import time

    start = time.time()

    conn = ('10.26.8.156', '22', 'http')
    # conn = ('10.24.84.173', '22')
    auth = ('admin', 'password')

    from pyswitch.device import Device

    dev = Device(conn=conn, auth=auth)

    dev.interface.add_vlan_int(vlan_id='234')
    print dev.firmware_version
    # print dev.os_type
    # print dev.suports_rbridge
    print dev.interface.port_channels
    # print dev.mac_table

    """
    from pyswitch.device import Device
    dev = Device(conn=conn, auth=auth)
    for vlan_id in range(2,4090):
        dev.interface.add_vlan_int(vlan_id=vlan_id)
    """
    end = time.time()
    print(end - start)
