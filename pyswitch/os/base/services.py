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

from pyswitch.utilities import Util


class Services(object):
    """
    The Services class holds all relevent methods and attributes for enabling
    and disabling NOS services, such as VRRP.

    Attributes:
        None
    """

    def __init__(self, callback):
        """
        Services object init.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            Services Object

        Raises:
            None
        """
        self._callback = callback

    @property
    def arp(self):
        """dict: arp details
        Examples:
        >>> import pyswitch.device
        >>> switches = ['10.24.39.231']
        >>> auth = ('admin', 'password')
        >>> for switch in switches:
        ...     conn = (switch, '22')
        ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
        ...         output = dev.services.arp
        """

        config = ('get_arp_rpc', {})
        results = self._callback(config, handler='get')
        util = Util(results.data)
        result = []

        for item in util.findlist(util.root, './/arp-entry'):
            ip_address = util.find(item, './/ip-address')
            mac_address = util.find(item, './/mac-address')
            interface_type = util.find(item, './/interface-type')
            interface_name = util.find(item, './/interface-name')
            is_resolved = util.find(item, './/is-resolved')
            age = util.find(item, './/age')
            entry_type = util.find(item, './/entry-type')
            item_results = {'ip-address': ip_address,
                            'mac-address': mac_address,
                            'interface-type': interface_type,
                            'interface-name': interface_name,
                            'is-resolved': is_resolved,
                            'age': age,
                            'entry-type': entry_type
                            }
            result.append(item_results)
        return result

    @property
    def mac_table(self):
        """list[dict]: the MAC table of the device.
         Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.231']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.mac_table
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

            table.append(dict(mac_address=address, interface_type=interface_type,
                              interface_name=interface_name, interface=interface,
                              state=state, vlan=vlan, type=mac_type))

        return table

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
            >>> conn = ('10.24.39.231', '22')
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
