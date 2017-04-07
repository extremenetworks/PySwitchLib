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

import pyswitch.os.base.fabric_service
import pyswitch.os.base.lldp
import pyswitch.os.base.snmp
import pyswitch.os.base.vcs
import pyswitch.os.nos.base.interface
import pyswitch.os.nos.base.bgp
import pyswitch.os.nos.base.services
import pyswitch.os.nos.base.system
import pyswitch.os.slxos.base.interface
import pyswitch.os.slxos.base.bgp
import pyswitch.os.slxos.base.services
import pyswitch.os.slxos.base.system
import pyswitch.utilities as util
from pyswitch.utilities import Util
from pyswitch.XMLAsset import XMLAsset
import re

NOS_ATTRS = ['snmp', 'interface', 'bgp',  'lldp', 'system', 'services',
             'fabric_service', 'vcs']
NOS_VERSIONS = {
    '6.0.2': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.nos.base.interface.Interface,
        'bgp': pyswitch.os.nos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.nos.base.system.System,
        'services': pyswitch.os.nos.base.services.Services,
        'fabric_service': pyswitch.os.base.fabric_service.FabricService,
        'vcs': pyswitch.os.base.vcs.VCS

    },
    '7.0.1': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.nos.base.interface.Interface,
        'bgp': pyswitch.os.nos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.nos.base.system.System,
        'services': pyswitch.os.nos.base.services.Services,
        'fabric_service': pyswitch.os.base.fabric_service.FabricService,
        'vcs': pyswitch.os.base.vcs.VCS

    },
    '7.1.0': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.nos.base.interface.Interface,
        'bgp': pyswitch.os.nos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.nos.base.system.System,
        'services': pyswitch.os.nos.base.services.Services,
        'fabric_service': pyswitch.os.base.fabric_service.FabricService,
        'vcs': pyswitch.os.base.vcs.VCS
    },
    '7.2.0': {
            'snmp': pyswitch.os.base.snmp.SNMP,
            'interface': pyswitch.os.nos.base.interface.Interface,
            'bgp': pyswitch.os.nos.base.bgp.Bgp,
            'lldp': pyswitch.os.base.lldp.LLDP,
            'system': pyswitch.os.nos.base.system.System,
            'services': pyswitch.os.nos.base.services.Services,
            'fabric_service': pyswitch.os.base.fabric_service.FabricService,
            'vcs': pyswitch.os.base.vcs.VCS
        },
}
SLXOS_VERSIONS = {
    '16.1.0': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.slxos.base.interface.Interface,
        'bgp': pyswitch.os.slxos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.slxos.base.system.System,
        'services': pyswitch.os.slxos.base.services.Services,
    },
    '16.1.1': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.slxos.base.interface.Interface,
        'bgp': pyswitch.os.slxos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.slxos.base.system.System,
        'services': pyswitch.os.slxos.base.services.Services,
    },
    '17.1.0': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.slxos.base.interface.Interface,
        'bgp': pyswitch.os.slxos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.slxos.base.system.System,
        'services': pyswitch.os.slxos.base.services.Services,
    },
    '17.1.1': {
        'snmp': pyswitch.os.base.snmp.SNMP,
        'interface': pyswitch.os.slxos.base.interface.Interface,
        'bgp': pyswitch.os.slxos.base.bgp.Bgp,
        'lldp': pyswitch.os.base.lldp.LLDP,
        'system': pyswitch.os.slxos.base.system.System,
        'services': pyswitch.os.slxos.base.services.Services,
    },
}


class DeviceCommError(Exception):
    """
    Error with device communication.
    """
    pass


class Reply:

    def __init__(self, xml):
        self.data = xml


class Device(object):
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
        self._conn = kwargs.pop('conn')
        self.host = self._conn[0]
        self._auth = kwargs.pop('auth', (None, None))
        self._callback = kwargs.pop('callback', None)
        self.os_type_val = None

        if self._callback is None:
            self._callback = self._callback_main

        self._mgr = None
        self._cli = None

        self.reconnect()

        ver = self.firmware_version
        thismodule = sys.modules[__name__]
        os_table = getattr(thismodule, '%s_VERSIONS' %
                           str(self.os_type).upper())

        for nos_attr in NOS_ATTRS:
            if nos_attr in os_table[ver]:
                setattr(
                    self,
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
    def mac_table(self):
        """list[dict]: the MAC table of the device.

        """
        table = []

        config = ('get_mac_address_table_rpc', {})

        rest_root = self._callback(config, handler='get')
        util = Util(rest_root.data)
        for entry in util.findlist(util.root, './/mac-address-table'):
            address = util.find(entry, './/mac-address')
            vlan = util.find(entry, './/vlanid')
            mac_type = util.find(entry, './/mac-type')
            state = util.find(entry, './/mac-state')
            interface = util.findNode(entry, './/forwarding-interface')
            interface_type = util.find(interface, './/interface-type')
            interface_name = util.find(interface, './/interface-name')
            interface = '%s%s' % (interface_type, interface_name)

            table.append(dict(mac_address=address, interface=interface,
                              state=state, vlan=vlan,
                              type=mac_type))

        return table

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

        (status, result) = getattr(self._mgr, call[0])(**call[1])
       

        if not status:
            op = self._mgr.get_xml_output()
            if '' != op and 'object already exists' not in op:
                raise ValueError(op)

        if handler == 'get_config':
            xml = self._mgr.get_xml_output()
            xml_ns = '<output>%s</output>' %(re.sub(' xmlns[^ \t\n\r\f\v>]+|y:', '',xml))
            return Reply(xml_ns)

        if handler == 'get':
            xml = self._mgr.get_xml_output()
            xml_ns = re.sub(' xmlns[^ \t\n\r\f\v>]+','',xml)
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

        self._mgr = XMLAsset(ip_addr=self._conn[0],auth=self._auth)
        return True

    def find_interface_by_mac(self, **kwargs):
        """Find the interface through which a MAC can be reached.
        Args:
            mac_address (str): A MAC address in 'xx:xx:xx:xx:xx:xx' format.
        Returns:
            list[dict]: a list of mac table data.
        Raises:
            KeyError: if `mac_address` is not specified.
        Examples:
            >>> from pprint import pprint
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     x = dev.find_interface_by_mac(
            ...     mac_address='10:23:45:67:89:ab')
            ...     pprint(x) # doctest: +ELLIPSIS
            [{'interface'...'mac_address'...'state'...'type'...'vlan'...}]
        """
        mac = kwargs.pop('mac_address')
        results = [x for x in self.mac_table if x['mac_address'] == mac]
        return results

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
            >>> conn = ('10.24.39.211', '22')
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
