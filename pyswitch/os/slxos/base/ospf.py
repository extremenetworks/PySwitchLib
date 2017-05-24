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


class Ospf(object):
    """
    The OSPF class holds all relevent methods and attributes for the OSPF
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

    def ospf_area(self, **kwargs):
        """ Configure/get/delete area under router ospf 

        Args:
            ip_version (str): ('4' or '6') address family
                              Default: `4`.
            area (str): OSPF areas.
            vrf (str): Create a VRF. Default: `default-vrf`
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
            ...     output = dev.ospf.ospf_area(get=True, vrf='111')
            ...     output = dev.ospf.ospf_area(delete=True, vrf='111')
            ...     output = dev.ospf.ospf_area(vrf='111', area='10')
        """
        ip_version = kwargs.pop('ip_version', '4')
        vrf = kwargs.pop('vrf', 'default-vrf')
        area = kwargs.pop('area', None)
        ospf_args = {}
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        afi = 'ipv4' if ip_version == '4' else 'ipv6'
        ospf_args = dict(ospf=vrf, area=area)
        if delete:
            method_name = 'router_ospf_area_delete' if ip_version == '4'\
                else 'ipv6_router_ospf_area_delete'
            config = (method_name, ospf_args)
            return callback(config)
        if not get_config:
            method_name = 'router_ospf_area_create' if ip_version == '4'\
                else 'ipv6_router_ospf_area_create'
            config = (method_name, ospf_args)
            return callback(config)
        elif get_config:
            method_name = 'router_ospf_area_get' if ip_version == '4'\
                else 'ipv6_router_ospf_area_get'
            config = (method_name, ospf_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/area-id')
        return result
