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
            ...     output = dev.mpls.mpls_interface(get=True, intf_name='111',
            ...                                      intf_type='ve')
            ...     output = dev.mpls.mpls_interface(intf_name='111',
            ...                                      intf_type='ve')
            ...     output = dev.mpls.mpls_interface(delete=True,
            ...                                      intf_name='111',
            ...                                      intf_type='ve')
        """

        intf_type = kwargs.pop('intf_type', 'ethernet')
        intf_name = kwargs.pop('intf_name')

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
            method_name = 'router_mpls_mpls_interface_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data == '<output></output>':
                result = None
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

        path_name = kwargs.pop('path_name')

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(path=path_name)
        if delete:
            method_name = 'router_mpls_path_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            method_name = 'router_mpls_path_create'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_path_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/path-name')
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
            ...     output = dev.mpls.mpls_path_hop_create(get=True,
            ...              path_hop_ip='1.1.1.1', path_name='test')
            ...     output = dev.mpls.mpls_path_hop_create(delete=True,
            ...              path_hop_ip='1.1.1.1', path_name='test')
            ...     output = dev.mpls.mpls_path_hop_create(
            ...              path_hop_type='strict',
            ...              path_hop_ip='1.1.1.1', path_name='test')
        """

        lsp_name = kwargs.pop('lsp_name')

        mpls_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        mpls_args = dict(lsp=lsp_name)
        if delete:
            method_name = 'router_mpls_lsp_delete'
            config = (method_name, mpls_args)
            return callback(config)
        if not get_config:
            method_name = 'router_mpls_lsp_create'
            config = (method_name, mpls_args)
            return callback(config)
        elif get_config:
            method_name = 'router_mpls_lsp_get'
            config = (method_name, mpls_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                result = util.find(util.root, './/lsp-name')
            else:
                result = None
        return result
