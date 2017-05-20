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
        callback = kwargs.pop('callback', self._callback)
        if get:
            enable = None

        vrrp_args = dict()
        vrrp_method = 'protocol_vrrp_update'
        if ip_version == '6':
            vrrp_method = 'ipv6_protocol_vrrp_update'

        if get:
            config = ('protocol_vrrp_get', vrrp_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv4_vrrp = util.find(util.root, './/vrrp')
            ipv4_vrrp = ipv4_vrrp if ipv4_vrrp and ipv4_vrrp == 'true' \
                else False

            config = ('ipv6_protocol_vrrp_get', vrrp_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv6_vrrp = util.find(util.root, './/vrrp')
            ipv6_vrrp = ipv6_vrrp if ipv6_vrrp and ipv6_vrrp == 'true' \
                else False
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

        callback = kwargs.pop('callback', self._callback)
        if get:
            enable = None

        vrrpe_args = dict()
        vrrpe_method = 'protocol_vrrp_extended_update'
        if ip_version == '6':
            vrrpe_method = 'ipv6_protocol_vrrp_extended_update'

        if get:
            config = ('protocol_vrrp_extended_get', vrrpe_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv4_vrrpe = util.find(util.root, './/vrrp-extended')
            ipv4_vrrpe = ipv4_vrrpe if ipv4_vrrpe and ipv4_vrrpe == 'true'\
                else False

            config = ('ipv6_protocol_vrrp_extended_get', vrrpe_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv6_vrrpe = util.find(util.root, './/vrrp-extended')
            ipv6_vrrpe = ipv6_vrrpe if ipv6_vrrpe and ipv6_vrrpe == 'true' \
                else False

            return {'ipv4_vrrpe': ipv4_vrrpe, 'ipv6_vrrpe': ipv6_vrrpe}

        if not enable:
            vrrpe_args['vrrp_extended'] = False
        else:
            vrrpe_args['vrrp_extended'] = True

        config = (vrrpe_method, vrrpe_args)
        return callback(config)

    def isis(self, **kwargs):
        """Enable or Disable isis.
        Args:
            enable (bool): If ISIS should be enabled or disabled.
                           Default: ``True``.
            get (bool): Get config instead of editing config. (True, False)
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
            ...         dev.services.isis(get=True)
            ...         dev.services.isis(enable=False)
            ...         dev.services.isis()
            Traceback (most recent call last):
            KeyError
        """
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)

        if get:
            enable = None
        isis_args = {}
        if get:
            config = ('router_isis_get', isis_args)
            x = callback(config, handler='get_config')
            if x.data == '<output></output>':
                return False
            else:
                return True
        if not enable:
            config = ('router_isis_delete', isis_args)
        else:
            config = ('router_isis_create', isis_args)

        return callback(config)

    def ospf(self, **kwargs):
        """Enable or Disable OSPF.
        Args:
            ip_version (str): The IP version ('4' or '6') for which OSPF
                should be enabled/disabled.  Default: `4`.
            enable (bool): If OSPF should be enabled or disabled.
                           Default: ``True``.
            vrf (str): Create a VRF. Default: `default-vrf`
            get (bool): Get config instead of editing config. (True, False)
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
            ...         dev.services.ospf(get=True, vrf='111')
            ...         dev.services.ospf(enable=True, vrf='111')
            ...         dev.services.ospf(enable=False, vrf='111')
            Traceback (most recent call last):
            KeyError
        """
        ip_version = kwargs.pop('ip_version', '4')
        enable = kwargs.pop('enable', True)
        vrf = kwargs.pop('vrf', 'default-vrf')

        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        if get:
            enable = None

        ospf_args = dict(ospf=vrf)
        if get:
            config = ('router_ospf_get', ospf_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)
            ipv4_ospf = util.find(util.root, './/ospf//vrf')
            ipv4_ospf = ipv4_ospf if ipv4_ospf else False

            config = ('ipv6_router_ospf_get', ospf_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)

            ipv6_ospf = util.find(util.root, './/ospf//vrf')
            ipv6_ospf = ipv6_ospf if ipv6_ospf  else False

            return {'ipv4_ospf': ipv4_ospf, 'ipv6_ospf': ipv6_ospf}

        if not enable:
            method_name = 'router_ospf_delete' if ip_version == '4'\
                else 'ipv6_router_ospf_delete'
        else:
            method_name = 'router_ospf_create' if ip_version == '4'\
                else 'ipv6_router_ospf_create'
        config = (method_name, ospf_args)
        return callback(config)
