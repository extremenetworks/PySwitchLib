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
