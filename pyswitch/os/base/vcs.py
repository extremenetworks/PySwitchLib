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

from ipaddress import ip_interface

from pyswitch.utilities import Util



class VCS(object):
    """
    VCS class containing all VCS methods and attributes.
    """

    def __init__(self, callback):
        """VCS init method.
        Args:
            callback: Callback function that will be called for each action.
        Returns:
            VCS Object
        Raises:
            None
        """
        self._callback = callback

    @property
    def vcs_nodes(self):
        """dict: vcs node details
        """

        show_vcs = ('show_vcs_rpc', {})

        results = self._callback(show_vcs, handler='get')
        util = Util(results.data)
        result = []
        for nodes in util.findlist(util.root, './/vcs-nodes'):
            for item in util.findlist(nodes, './/vcs-node-info'):
                serial_number = util.find(item, './/node-serial-num')
                node_status = util.find(item, './/node-status')
                vcs_id = util.find(item, './/node-vcs-id')
                rbridge_id = util.find(item, './/node-rbridge-id')
                switch_mac = util.find(item, './/node-switch-mac')
                switch_wwn = util.find(item, './/node-switch-wwn')
                switch_name = util.find(item, './/node-switchname')
                node_is_principal = util.find(item, './/node-is-principal')
                switch_ip = ''
                for switch_ip_addr in util.findlist(
                        item, './/node-public-ip-addresses'):
                    switch_ip = util.find(switch_ip_addr,
                                          './/node-public-ip-address')
                    break
                item_results = {'node-serial-num': serial_number,
                                'node-status': node_status,
                                'node-vcs-id': vcs_id,
                                'node-rbridge-id': rbridge_id,
                                'node-switch-mac': switch_mac,
                                'node-switch-wwn': switch_wwn,
                                'node-switch-ip': switch_ip,
                                'node-switchname': switch_name,
                                'node-is-principal': node_is_principal}

                result.append(item_results)

        return result

    def vcs_vip(self, **kwargs):
        """Set VCS Virtual IP.

        Args:
            vip (str): IPv4/IPv6 Virtual IP Address.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            delete (bool): Deletes the virtual ip if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `vip` is not passed.
            ValueError: if `vip` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.vcs_vip(vip='10.1.1.1/24')
            ...         dev.interface.vcs_vip(vip='fe80::cafe:beef:1000:1/64')
            ...         dev.interface.vcs_vip(vip='10.1.1.1/24',get=True)
            ...         dev.interface.vcs_vip(vip='fe80::cafe:beef:1000:1/64',
            ...                               get=True)
            ...         dev.interface.vcs_vip(vip='fe80::cafe:beef:1000:1/64',
            ...                               delete=True)
            ...         dev.interface.vcs_vip(vip='10.1.1.1/24',get=True)
            ...         dev.interface.vcs_vip(vip='fe80::cafe:beef:1000:1/64',
            ...                               get=True)
            ...         dev.interface.vcs_vip(vip='10.1.1.1/24',delete=True)
            ...         dev.interface.vcs_vip(vip='fe80::cafe:beef:1000:1/64',
            ...                               delete=True)
        """

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if not get_config:
            vip = str(kwargs.pop('vip'))
            ipaddress = ip_interface(unicode(vip))
            vcs_args = dict(address=vip)
            if ipaddress.version == 4:
                method_name = 'vcs_virtual_ip_address_'
            elif ipaddress.version == 6:
                method_name = 'vcs_virtual_ipv6_address_'

            if not delete:
                method_name = "%screate" % method_name
                config = (method_name, vcs_args)

            else:
                method_name = "%sdelete" % method_name
                config = (method_name, vcs_args)

        elif get_config:
            vip_info = {}

            method_name = 'vcs_virtual_ip_address_get'

            config = (method_name, {})
            op = callback(config, handler='get_config')
            util = Util(op.data)

            vip_info['ipv4_vip'] = util.find(util.root, './/address/address')
		

            method_name = 'vcs_virtual_ipv6_address_get'

            config = (method_name, {})

            op = callback(config, handler='get_config')
            util = Util(op.data)

            vip_info['ipv6_vip'] = util.find(util.root, './/address/address')
            return vip_info

        return callback(config)
