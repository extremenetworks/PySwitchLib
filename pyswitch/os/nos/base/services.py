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

import xml.etree.ElementTree as ET
from pyswitch.utilities import Util
from pyswitch.os.base.services import Services as BaseServices

class Services(BaseServices):
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
        super(Services, self).__init__(callback)

    @property
    def arp(self):
        """dict: trill link details
                """

        config = ('get_arp_rpc',{})
        results = self._callback(config, handler='get')
        util = Util(results.data)
        result = []

        for item in util.findlist(util.root,'.//arp-entry' ):
            ip_address = util.find(item,'.//ip-address' )
            mac_address = util.find(item,'.//mac-address' )
            interface_type = util.find(item,'.//interface-type' )
            interface_name = util.find(item,'.//interface-name' )
            is_resolved = util.find(item,'.//is-resolved' )
            age = util.find(item,'.//age' )
            entry_type = util.find(item,'.//entry-type' )
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

    def vrrp(self, **kwargs):
        """Enable or Disable VRRP.

        Args:
            ip_version (str): The IP version ('4' or '6') for which VRRP should
                be enabled/disabled.  Default: `4`.
            enable (bool): If VRRP should be enabled or disabled.  Default:
                ``True``.
            rbridge_id (str): The rbridge ID of the device on which VRRP will
                be enabled/disabled.  Default: `1`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.local_asn(rbridge_id='225')
            ...         output = dev.bgp.local_asn(rbridge_id='225',
            ...         enable=False)
            ...         output = dev.bgp.local_asn(rbridge_id='225',
            ...         ip_version='6')
            ...         output = dev.bgp.local_asn(rbridge_id='225',
            ...         enable=False, ip_version='6')
            ...         dev.services.vrrp() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        ip_version = kwargs.pop('ip_version', '4')
        get = kwargs.pop('get', False)
        enable = kwargs.pop('enable', True)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        if get:
            enable = None

        vrrp_args = dict(rbridge_id=rbridge_id)
        vrrp_method = 'rbridge_id_protocol_vrrp_update'
        if ip_version == '6':
            vrrp_method = 'rbridge_id_ipv6_protocol_vrrp_update'

        if get:
            config = ('rbridge_id_protocol_vrrp_get', vrrp_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv4_vrrp = util.find(util.root, './/vrrp')
            ipv4_vrrp = ipv4_vrrp if ipv4_vrrp else False

            config = ('rbridge_id_ipv6_protocol_vrrp_get', vrrp_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv6_vrrp = util.find(util.root, './/vrrp')
            ipv6_vrrp = ipv6_vrrp if ipv6_vrrp else False
            return {'ipv4_vrrp': ipv4_vrrp, 'ipv6_vrrp': ipv6_vrrp}

        if not enable:
            vrrp_args['vrrp'] = False
        else:
            vrrp_args['vrrp'] = True

        config = (vrrp_method, vrrp_args)
        return callback(config)

    def vrrpe(self, **kwargs):
        """Enable or Disable Vrrpe.
        Args:
            ip_version (str): The IP version ('4' or '6') for which vrrpe
                should be enabled/disabled.  Default: `4`.
            enable (bool): If vrrpe should be enabled or disabled.  Default:
                ``True``.
            get (bool): Get config instead of editing config. (True, False)
            rbridge_id (str): The rbridge ID of the device on which vrrpe will
                be enabled/disabled.  Default: `1`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.services.vrrpe(rbridge_id='25',enable=False)
            ...         dev.services.vrrpe(rbridge_id='25',enable=True)
            ...         dev.services.vrrpe()
            Traceback (most recent call last):
            KeyError
        """
        ip_version = kwargs.pop('ip_version', '4')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        if get:
            enable = None

        vrrpe_args = dict(rbridge_id=rbridge_id)
        vrrpe_method = 'rbridge_id_protocol_vrrp_extended_update'
        if ip_version == '6':
            vrrpe_method = 'rbridge_id_ipv6_protocol_vrrp_extended_update'

        if get:
            config = ('rbridge_id_protocol_vrrp_extended_get', vrrpe_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv4_vrrpe = util.find(util.root, './/vrrp-extended')
            ipv4_vrrpe = ipv4_vrrpe if ipv4_vrrpe else False

            config = ('rbridge_id_ipv6_protocol_vrrp_extended_get', vrrpe_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv6_vrrpe = util.find(util.root, './/vrrp-extended')
            ipv6_vrrpe = ipv6_vrrpe if ipv6_vrrpe else False

            return {'ipv4_vrrpe': ipv4_vrrpe, 'ipv6_vrrpe': ipv6_vrrpe}

        if not enable:
            vrrpe_args['vrrp_extended'] = False
        else:
            vrrpe_args['vrrp_extended'] = True

        config = (vrrpe_method, vrrpe_args)
        return callback(config)
