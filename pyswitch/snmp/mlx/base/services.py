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

import pyswitch.utilities
import re


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

    def vrrpe(self, **kwargs):
        """Enable or Disable Vrrpe.
        Args:
            ip_version (str): The IP version ('4' or '6') for which vrrpe
                should be enabled/disabled.  Default: `4`.
            enable (bool): If vrrpe should be enabled or disabled.  Default:
                ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.
        Returns:
            Return True.

        Raises:
            ValueError if VRRP-E set/get fails

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.12.91', '10.24.12.95']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.services.vrrpe(enable=False)
            ...         dev.services.vrrpe(enable=True)
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

        if get:
            try:
                cli_cmd = 'show ip vrrp-extended'
                output = callback(cli_cmd, handler='cli-get')
                if(re.search(r'is not enabled', output)):
                    ipv4_vrrpe = False
                else:
                    ipv4_vrrpe = True

                cli_cmd = 'show ipv6 vrrp-extended'
                output = callback(cli_cmd, handler='cli-get')
                if(re.search(r'is not enabled', output)):
                    ipv6_vrrpe = False
                else:
                    ipv6_vrrpe = True

                return {'ipv4_vrrpe': ipv4_vrrpe, 'ipv6_vrrpe': ipv6_vrrpe}

            except Exception as error:
                reason = error.message
                raise ValueError('Failed to get VRRP-E status %s' % (reason))

        cli_arr = []
        if int(ip_version) == 4:
            if not enable:
                cli_arr.append('no router vrrp-extended')
            else:
                cli_arr.append('router vrrp-extended')
        else:
            if not enable:
                cli_arr.append('no ipv6 router vrrp-extended')
            else:
                cli_arr.append('ipv6 router vrrp-extended')

        try:
            cli_res = callback(cli_arr, handler='cli-set')
            pyswitch.utilities.check_mlx_cli_set_error(cli_res)
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to create VRRP-E router %s' % (reason))
