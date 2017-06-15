# 2017.01.30 15:56:30 IST
# Embedded file name: pyswitch/mpls.py
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

from ipaddress import ip_interface

import pyswitch.utilities as util
from pyswitch.utilities import Util


class Mpls(object):
    """
    The MPLS class holds all relevent methods and attributes for the MPLS
    capabilities of the SLXOS device.

    Attributes:
        None
    """

    @property
    def valid_int_types(self):

        return [
            'ethernet',
            've'
        ]

    @property
    def valid_intp_types(self):

        return []

    @property
    def os(self):
        return 'slxos'


    def __init__(self, callback):
        """
        MPLS object init.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            MPLS Object

        Raises:
            None
        """
        self._callback = callback
        self._cli = None

    def mpls_interface(self, **kwargs):
        """ Configure/get/delete router mpls interface 

        Args:
            intf_type (str): Type of interface.['ethernet', 've']
            intf_name (str): Intername name.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `intf_name` is not specified.
            ValueError: if `intf_type` is not valid.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_interface(get=True)
            ...     output = dev.mpls.mpls_interface(get=True, intf_name='111',
            ...                                      intf_type='ve')
            ...     output = dev.mpls.mpls_interface(intf_name='111',
            ...                                      intf_type='ve')
            ...     output = dev.mpls.mpls_interface(delete=True,
            ...                                      intf_name='111',
            ...                                      intf_type='ve')
        """

        intf_type = kwargs.pop('intf_type', 'ethernet')
        intf_name = kwargs.pop('intf_name', None)

        if intf_type not in self.valid_int_types:
            raise ValueError('intf_type must be one of: %s' %
                             repr(valid_int_types))

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(mpls_interface=(intf_type, intf_name))
        if delete:
            method_name = 'router_mpls_mpls_interface_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            method_name = 'router_mpls_mpls_interface_create'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            if intf_name is None:
                mpls_args= {}
            method_name = 'router_mpls_mpls_interface_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data == '<output></output>':
                result = None
            else:
                if intf_name is None:
                    result = util.findall(util.root, './/interface-name')
                else:
                    result = util.find(util.root, './/interface-name')
        return result

    def mpls_interface_ldp_enable(self, **kwargs):
        """ Configure/get/delete router mpls interface 

        Args:
            intf_type (str): Type of interface.['ethernet', 've']
            intf_name (str): Intername name.
            ldp_enable (bool). Enable LDP on the interfaces. (True, False)
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `intf_name` is not specified.
            ValueError: if `intf_type` is not valid.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_interface_ldp_enable(get=True,
            ...                          intf_name='111', intf_type='ve')
            ...     output = dev.mpls.mpls_interface_ldp_enable(intf_name='111',
            ...                          ldp_enable=True, intf_type='ve')
            ...     output = dev.mpls.mpls_interface_ldp_enable(delete=True,
            ...                                      intf_name='111',
            ...                                      intf_type='ve')
        """

        intf_type = kwargs.pop('intf_type', 'ethernet')
        intf_name = kwargs.pop('intf_name')
        ldp_enable = kwargs.pop('ldp_enable', True)

        if intf_type not in self.valid_int_types:
            raise ValueError('intf_type must be one of: %s' %
                             repr(valid_int_types))

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(mpls_interface=(intf_type, intf_name))
        if delete:
            method_name = 'router_mpls_mpls_interface_ldp_enable_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args.update(mpls_interface_ldp_enable=ldp_enable)
            method_name = 'router_mpls_mpls_interface_ldp_enable_update'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_mpls_interface_ldp_enable_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/ldp-enable')
        return result

    def mpls_path_create(self, **kwargs):
        """ Configure/get/delete router mpls path

        Args:
            path_name (str). Define path name.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `path_name` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_path_create(get=True,
            ...                                        path_name='test')
            ...     output = dev.mpls.mpls_path_create(delete=True,
            ...                                        path_name='test')
            ...     output = dev.mpls.mpls_path_create(path_name='test')
        """

        path_name = kwargs.pop('path_name', None)

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if delete:
            mpls_args = dict(path=path_name)
            method_name = 'router_mpls_path_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args = dict(path=path_name)
            method_name = 'router_mpls_path_create'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            if path_name is not None:
                mpls_args = dict(path=path_name)
            method_name = 'router_mpls_path_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if path_name is not None:
                result = util.find(util.root, './/path-name')
            else:
                result = util.findall(util.root, './/path-name')
        return result

    def mpls_path_hop_create(self, **kwargs):
        """ Configure/get/delete router mpls path hop ip

        Args:
            path_name (str). Define path name
            path_hop_ip (str). Path IP address
            path_hop_type (str). Path type. ['strict', 'loose']
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `path_name`,`path_hop_ip` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_path_hop_create(get=True,
            ...              path_hop_ip='1.1.1.1', path_name='test')
            ...     output = dev.mpls.mpls_path_hop_create(delete=True,
            ...              path_hop_ip='1.1.1.1', path_name='test')
            ...     output = dev.mpls.mpls_path_hop_create(
            ...              path_hop_type='strict',
            ...              path_hop_ip='1.1.1.1', path_name='test')
        """

        path_name = kwargs.pop('path_name')
        path_hop_ip = kwargs.pop('path_hop_ip')
        path_hop_type = kwargs.pop('path_hop_type', None)

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(path=path_name, path_hop=(path_hop_ip, path_hop_type))
        if delete:
            method_name = 'router_mpls_path_hop_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            if path_hop_type not in ['strict', 'loose']:
                raise ValueError("`path_hop_type` must match one of them "
                                 "`strict', 'loose`")
            method_name = 'router_mpls_path_hop_create'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_path_hop_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                hop_ip = util.find(util.root, './/path-hop-ip')
                hop_type = util.find(util.root, './/path-hop-type')
                result = {'hop_ip':hop_ip, 'hop_type':hop_type}
            else:
                result = None
        return result

    def mpls_lsp_create(self, **kwargs):
        """ Configure/get/delete router mpls lsp 

        Args:
            lsp_name (str). Define lsp name
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `lsp_name` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_lsp_create(get=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls__lsp_create(delete=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_create(
            ...              lsp_name='test')
        """

        lsp_name = kwargs.pop('lsp_name', None)

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if delete:
            mpls_args = dict(lsp=lsp_name)
            method_name = 'router_mpls_lsp_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args = dict(lsp=lsp_name)
            method_name = 'router_mpls_lsp_create'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            if lsp_name is not None:
                mpls_args = dict(lsp=lsp_name)
            method_name = 'router_mpls_lsp_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                if lsp_name is not None:
                    result = util.find(util.root, './/lsp-name')
                else:
                    result = util.findall(util.root, './/lsp-name')
            else:
                result = None
        return result

    def mpls_lsp_primary_path(self, **kwargs):
        """ Configure/get/delete router mpls lsp primary path

        Args:
            lsp_name (str). Define lsp name
            lsp_primary_path (str). Define lsp primary path name
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `lsp_name` and `lsp_primary_path` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_lsp_primary_path(get=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_primary_path(delete=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_primary_path(
            ...              lsp_name='test_lsp',
            ...              lsp_primary_path='test')
        """

        lsp_name = kwargs.pop('lsp_name')
        lsp_primary_path = kwargs.pop('lsp_primary_path', None)

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(lsp=lsp_name)
        if delete:
            method_name = 'router_mpls_lsp_primary_path_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args.update(lsp_primary_path=lsp_primary_path)
            method_name = 'router_mpls_lsp_primary_path_update'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_lsp_primary_path_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                result = util.find(util.root, './/primary-path')
            else:
                result = None
        return result

    def mpls_lsp_secondary_path(self, **kwargs):
        """ Configure/get/delete router mpls lsp secondary path

        Args:
            lsp_name (str). Define lsp name
            lsp_secondary_path (str). Define lsp primary path name
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `lsp_name` and `lsp_secondary_path` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_lsp_secondary_path(get=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_secondary_path(delete=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_secondary_path(
            ...              lsp_name='test_lsp',
            ...              lsp_secondary_path='test')
        """

        lsp_name = kwargs.pop('lsp_name')
        lsp_secondary_path = kwargs.pop('lsp_secondary_path', None)

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(lsp=lsp_name)
        if delete:
            method_name = 'router_mpls_lsp_secondary_path_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args.update(secondary_path=lsp_secondary_path)
            method_name = 'router_mpls_lsp_secondary_path_create'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_lsp_secondary_path_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                result = util.find(util.root, './/secpath-name')
            else:
                result = None
        return result

    def mpls_lsp_cos(self, **kwargs):
        """ Configure/get/delete router mpls lsp cos value

        Args:
            lsp_name (str). Define lsp name
            lsp_cos (int). Configure class of service.[0-7]
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `lsp_name` and `lsp_cos` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_lsp_cos(get=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_cos(delete=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_cos(
            ...              lsp_name='test_lsp',
            ...              lsp_cos=7)
        """

        lsp_name = kwargs.pop('lsp_name')
        lsp_cos = kwargs.pop('lsp_cos', None)
        if lsp_cos is not None and lsp_cos not in range(0,8):
            raise ValueError('`lsp_cos` must be in range[0-7]')

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(lsp=lsp_name)
        if delete:
            method_name = 'router_mpls_lsp_cos_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args.update(lsp_cos=lsp_cos)
            method_name = 'router_mpls_lsp_cos_update'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_lsp_cos_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                result = util.find(util.root, './/cos')
            else:
                result = None
        return result

    def mpls_lsp_enable(self, **kwargs):
        """ Configure/get/delete router mpls lsp enable 

        Args:
            lsp_name (str). Define lsp name
            lsp_enable (bool): Enable LSP . (True, False)
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `lsp_name` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_lsp_enable(get=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_enable(delete=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_enable(
            ...              lsp_name='test_lsp',
            ...              lsp_enable=True)
        """

        lsp_name = kwargs.pop('lsp_name')
        lsp_enable = kwargs.pop('lsp_enable', True)

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(lsp=lsp_name)
        if delete:
            method_name = 'router_mpls_lsp_enable_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args.update(lsp_enable=lsp_enable)
            method_name = 'router_mpls_lsp_enable_update'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_lsp_enable_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                result = util.find(util.root, './/enable')
            else:
                result = None
        return result

    def mpls_lsp_destination_address(self, **kwargs):
        """ Configure/get/delete router mpls lsp destination address 

        Args:
            lsp_name (str). Define lsp name
            lsp_dest_address (str) : Define LSP destination address
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `lsp_name` and lsp_dest_address is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_lsp_destination_address(get=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_destination_address(delete=True,
            ...              lsp_name='test')
            ...     output = dev.mpls.mpls_lsp_destination_address(
            ...              lsp_name='test_lsp',
            ...              lsp_dest_address='1.1.1.1')
        """

        lsp_name = kwargs.pop('lsp_name')
        lsp_dest_address = kwargs.pop('lsp_dest_address', None)

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(lsp=lsp_name)
        if delete:
            method_name = 'router_mpls_lsp_to_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args.update(lsp_dest_address=lsp_dest_address)
            method_name = 'router_mpls_lsp_to_update'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_lsp_to_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                result = util.find(util.root, './/to')
            else:
                result = None
        return result

    def mpls_policy(self, **kwargs):
        """ Configure/get/delete router mpls policy 

        Args:
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            None.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_policy(get=True)
            ...     output = dev.mpls.mpls_policy(delete=True)
            ...     output = dev.mpls.mpls_policy()
        """

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if delete:
            method_name = 'router_mpls_policy_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            method_name = 'router_mpls_policy_create'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_policy_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                ospf_area_decimal = util.find(util.root, './/ospf-area-as-decimal')
                ospf_area_ip = util.find(util.root, './/ospf-area-as-ip-address')
                ospf_area_all = util.find(util.root, './/all')
                isis = util.find(util.root, './/isis')
                result = dict(ospf_area_decimal=ospf_area_decimal,
                              ospf_area_ip=ospf_area_ip,
                              ospf_area_all=ospf_area_all,
                              isis=isis)
            else:
                result = None
        return result

    def mpls_policy_te_ospf(self, **kwargs):
        """ Configure/get/delete router mpls traffic engineering ospf 

        Args:
            Choose only one among the args while configuring..
            [ospf_area_as_ip_address, ospf_area_as_decimal, ospf_area_all]

            ospf_area_as_ip_address (str): OSPF IP Address
            ospf_area_as_decimal (int): OSPF Area
            ospf_area_all (bool): Advertise all OSPF areas.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `ospf_area_as_ip_address` or `ospf_area_all`
                      `ospf_area_as_decimal` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_policy_te_ospf(get=True)
            ...     output = dev.mpls.mpls_policy_te_ospf(delete=True)
            ...     output = dev.mpls.mpls_policy_te_ospf(
            ...              ospf_area_as_ip_address='1.1.1.1')
            ...     output = dev.mpls.mpls_policy_te_ospf(
            ...              ospf_area_as_decimal=0)
            ...     output = dev.mpls.mpls_policy_te_ospf(
            ...              ospf_area_all=True)
        """

        ospf_area_as_ip_address = kwargs.pop('ospf_area_as_ip_address', None)
        ospf_area_as_decimal = kwargs.pop('ospf_area_as_decimal', None)
        ospf_area_all = kwargs.pop('ospf_area_all', None)
        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if delete:
            method_name = 'router_mpls_policy_traffic_'\
                          'engineering_ospf_area_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args.update(ospf_area_as_ip_address=ospf_area_as_ip_address,
                             ospf_area_as_decimal=ospf_area_as_decimal,
                             ospf_area_all=ospf_area_all)
            method_name = 'router_mpls_policy_traffic_'\
                          'engineering_ospf_area_update'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_policy_traffic_'\
                           'engineering_ospf_area_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                if util.find(util.root, './/ospf-area-as-decimal') is not None:
                    result = util.find(util.root, './/ospf-area-as-decimal')
                elif util.find(util.root, './/ospf-area-as-ip-address') is not None:
                    result = util.find(util.root, './/ospf-area-as-ip-address')
                else:
                    result = util.find(util.root, './/all')
            else:
                result = None

        return result

    def mpls_policy_te_isis(self, **kwargs):
        """ Configure/get/delete router mpls traffic engineering isis

        Args:
            isis_set_level (str): Advertise via IS-IS.
                                  ['level-2', 'level-1']
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `isis_set_level` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_policy_te_isis(get=True)
            ...     output = dev.mpls.mpls_policy_te_isis(delete=True)
            ...     output = dev.mpls.mpls_policy_te_isis(
            ...              isis_set_level='level-1')
        """

        isis_set_level = kwargs.pop('isis_set_level', None)

        if isis_set_level is not None and isis_set_level\
                not in ['level-2', 'level-1']:
            raise ValueError('`isis_set_level` must be of type '
                             '[level-2, level-1]')
        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if delete:
            method_name = 'router_mpls_policy_traffic_'\
                          'engineering_isis_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            mpls_args.update(isis_set_level=isis_set_level)
            method_name = 'router_mpls_policy_traffic_'\
                          'engineering_isis_update'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_policy_traffic_'\
                           'engineering_isis_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                result = util.find(util.root, './/isis')
            else:
                result = None

        return result
   
    def mpls_lsp_get_details(self, **kwargs):
        """ get all router mpls lsp details

        Args:
            lsp_name (str). Define lsp name
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `lsp_name` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.mpls.mpls_lsp_get_details(
            ...              lsp_name='test')
        """

        lsp_name = kwargs.pop('lsp_name')

        mpls_args = {}

        get_config = kwargs.pop('get', True)
        callback = kwargs.pop('callback', self._callback)
        mpls_args = dict(lsp=lsp_name)
        method_name = 'router_mpls_lsp_get'
        config = (method_name, mpls_args)
        output = callback(config, handler='get_config')
        util = Util(output.data)
        if output.data != '<output></output>':
            lsp_name = util.find(util.root, './/lsp-name')
            lsp_destn_addr = util.find(util.root, './/to')
            lsp_primary_path = util.find(util.root, './/primary-path')
            lsp_secondary_path = util.find(util.root, './/secpath-name')
            lsp_cos = util.find(util.root, './/cos')
            lsp_enable = util.find(util.root, './/enable')
            result = {'lsp_name':lsp_name,
                      'lsp_destn_addr':lsp_destn_addr,
                      'lsp_primary_path':lsp_primary_path,
                      'lsp_secondary_path':lsp_secondary_path,
                      'lsp_cos':lsp_cos, 'lsp_enable':lsp_enable}
        else:
            result = None
        return result
