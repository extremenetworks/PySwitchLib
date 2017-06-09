# 2017.01.30 15:56:30 IST
# Embedded file name: pyswitch/isis.py
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


class Isis(object):
    """
    The ISIS class holds all relevent methods and attributes for the ISIS 
    capabilities of the SLXOS device.

    Attributes:
        None
    """

    @property
    def valid_int_types(self):

        return []

    @property
    def valid_intp_types(self):

        return []

    @property
    def os(self):
        return 'slxos'


    def __init__(self, callback):
        """
        ISIS object init.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            ISIS Object

        Raises:
            None
        """
        self._callback = callback
        self._cli = None

    def address_family(self, **kwargs):
        """ Configure address Family 

        Args:
            ip_version (str): ('4' or '6') address family
                              Default: `4`.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            None 

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.isis.address_family_ipv4_unicast(get=True)
            ...     output = dev.isis.address_family_ipv4_unicast()
            ...     output = dev.isis.address_family_ipv4_unicast(delete=True)
        """
        ip_version = kwargs.pop('ip_version', '4')
        isis_args = {}
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        afi = 'ipv4' if ip_version == '4' else 'ipv6'
        if delete:
            method_name = 'router_isis_address_family_%s_unicast_delete' % afi 
            config = (method_name, isis_args)
            return callback(config)
        if not get_config:
            method_name = 'router_isis_address_family_%s_unicast_create' % afi
            config = (method_name, isis_args)
            return callback(config)
        elif get_config:
            method_name = 'router_isis_address_family_%s_unicast_get' % afi
            config = (method_name, isis_args)
            x = callback(config, handler='get_config')
            if x.data == '<output></output>':
                return False
            else:
                return True

    def log_adjacency(self, **kwargs):
        """ Configure log adjacency 

        Args:
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.isis.log_adjacency(get=True)
            ...     output = dev.isis.log_adjacency()
            ...     output = dev.isis.log_adjacency(delete=True)
        """
        isis_args = {}
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if delete:
            method_name = 'router_isis_log_adjacency_delete'
            config = (method_name, isis_args)
            return callback(config)
        if not get_config:
            isis_args['adjacency'] = True
            method_name = 'router_isis_log_adjacency_update'
            config = (method_name, isis_args)
            return callback(config)
        elif get_config:
            method_name = 'router_isis_log_adjacency_get'
            config = (method_name, isis_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/adjacency')
            return result

    def net_address(self, **kwargs):
        """ Configure net NSAP Address

        Args:
            net (str): NSAP Address. <HH.HHHH.HHHH.HHHH.00>
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `net` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.isis.net_address(get=True)
            ...     output = dev.isis.net_address(
            ...     net='49.0001.0100.1001.0006.00')
            ...     output = dev.isis.net_address(delete=True)
        """

        isis_args = {}

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if delete:
            method_name = 'router_isis_net_delete'
            config = (method_name, isis_args)
            return callback(config)
        if not get_config:
            net = kwargs.pop('net')
            isis_args['net'] = net 
            method_name = 'router_isis_net_create'
            config = (method_name, isis_args)
            return callback(config)
        elif get_config:
            method_name = 'router_isis_net_get'
            config = (method_name, isis_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/net-cmd')
            return result
