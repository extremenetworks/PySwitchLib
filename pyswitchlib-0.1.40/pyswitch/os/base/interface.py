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
import logging
import re

from ipaddress import ip_interface

import pyswitch.utilities
import pyswitch.utilities as util
from pyswitch.exceptions import InvalidVlanId


class Interface(object):
    """
    The Interface class holds all the actions assocaiated with the Interfaces
    of a NOS device.

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
    def l2_mtu_const(self):
        return (None, None)

    @property
    def has_rbridge_id(self):
        return False

    def method_prefix(self, method):
        if self.has_rbridge_id:
            return 'rbridge_id_%s' % method
        else:
            return method

    def __init__(self, callback):
        """
        Interface init function.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            Interface Object

        Raises:
            None
        """
        self._callback = callback

    def add_vlan_int(self, vlan_id):
        """
        Add VLAN Interface. VLAN interfaces are required for VLANs even when
        not wanting to use the interface for any L3 features.

        Args:
            vlan_id: ID for the VLAN interface being created. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        try:
            config = ('vlan_create', {'vlan': vlan_id})
            self._callback(config)
            return True

        except Exception as error:
            logging.error(error)
            return False

    def get_vlan_int(self, vlan_id):
        try:
            config = ('vlan_get', {'vlan': vlan_id})
            op = self._callback(config, handler='get_config')

            if util.find(op.json, '$..Vlan') or util.find(op.json, '$..vlan'):
                return True
            else:
                return False

        except Exception as error:
            logging.error(error)
            return False

    def interface_exists(self, **kwargs):
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types
        valid_rbridge_int_types = ['ve', 'loopback']
        valid_int_types = valid_int_types + valid_rbridge_int_types

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))

        method_name = 'interface_%s_get' % (int_type)
        args = dict()
        args[int_type] = name

        if self.has_rbridge_id and int_type in valid_rbridge_int_types:
            rbridge_id = kwargs.pop('rbridge_id', '1')
            method_name = 'rbridge_id_interface_%s_get' % (int_type)
            args['rbridge_id'] = rbridge_id

        config = (method_name, args)
        op = callback(config, handler='get_config')

        if op.json != '':
            return True
        return False

    def del_vlan_int(self, vlan_id):
        """
        Delete VLAN Interface.

        Args:
            vlan_id: ID for the VLAN interface being created. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        try:
            config = ('vlan_delete', {'vlan': vlan_id})
            self._callback(config)
            return True

        except Exception as error:
            logging.error(error)
            return False

    def enable_switchport(self, inter_type, inter):
        """
        Change an interface's operation to L2.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        method_name = 'interface_%s_switchport_update' % inter_type
        kwargs = {inter_type: inter, 'basic': True}
        config = (method_name, kwargs)
        try:
            self._callback(config)
            return True
        except Exception as error:
            logging.error(error)
            return False

    def disable_switchport(self, inter_type, inter):
        """
        Change an interface's operation to L3.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        method_name = 'interface_%s_switchport_update' % inter_type
        kwargs = {inter_type: inter, 'basic': False}
        config = (method_name, kwargs)
        try:
            self._callback(config)
            return True
        except Exception as error:
            logging.error(error)
            return False

    def access_vlan(self, inter_type, inter, vlan_id):
        """
        Add a L2 Interface to a specific VLAN.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1
            vlan_id: ID for the VLAN interface being modified. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        # NOT_WORKING
        method_name = 'interface_%s_switchport_access_update' % inter_type
        kwargs = {inter_type: inter, 'accessvlan': vlan_id}
        config = (method_name, kwargs)

        try:
            self._callback(config)
            return True
        except Exception as error:
            logging.error(error)
            return False

    def del_access_vlan(self, inter_type, inter, vlan_id):
        """
        Remove a L2 Interface from a specific VLAN, placing it back into the
        default VLAN.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1
            vlan_id: ID for the VLAN interface being modified. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        # NOT_WORKING
        method_name = 'interface_%s_switchport_access_vlan_delete' % inter_type
        kwargs = {inter_type: inter}
        config = (method_name, kwargs)
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def set_ip(self, inter_type, inter, ip_addr):
        """
        Set IP address of a L3 interface.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1
            ip_addr: IP Address in <prefix>/<bits> format. Ex: 10.10.10.1/24

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        method_name = 'interface_%s_ip_address_create' % inter_type
        address = (ip_addr, False, False, False)
        kwargs = {inter_type: inter, 'address': address}
        config = (method_name, kwargs)

        try:
            self._callback(config)
            return True
        except Exception as error:
            logging.error(error)
            return False

    def remove_port_channel(self, **kwargs):
        """
        Remove a port channel interface.

        Args:
            port_int (str): port-channel number (1, 2, 3, etc).
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `port_int` is not passed.
            ValueError: if `port_int` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.channel_group(name='225/0/20',
            ...         int_type='tengigabitethernet',
            ...         port_int='1', channel_type='standard', mode='active')
            ...         output = dev.interface.remove_port_channel(
            ...         port_int='1')
        """
        port_int = kwargs.pop('port_int')
        callback = kwargs.pop('callback', self._callback)

        if re.search('^[0-9]{1,3}$', port_int) is None:
            raise ValueError('%s must be in the format of x for port channel '
                             'interfaces.' % repr(port_int))

        port_channel_args = dict()
        port_channel_args['port_channel'] = port_int

        method_name = 'interface_port_channel_delete'

        config = (method_name, port_channel_args)

        return callback(config)

    def ip_address(self, **kwargs):
        """
        Set IP Address on an Interface.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
            name (str): Name of interface id.
                 (For interface: 1/0/5, 1/0/10 etc).
            ip_addr (str): IPv4/IPv6 Virtual IP Address..
                Ex: 10.10.10.1/24 or 2001:db8::/48
            delete (bool): True is the IP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `ip_addr` is not passed.
            ValueError: if `int_type`, `name`, or `ip_addr` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        int_type = 'tengigabitethernet'
            ...        name = '225/0/4'
            ...        ip_addr = '20.10.10.1/24'
            ...        output = dev.interface.disable_switchport(inter_type=
            ...        int_type, inter=name)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
            ...        output = dev.interface.add_vlan_int('86')
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, rbridge_id='225')
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, delete=True,
            ...        rbridge_id='225')
            ...        output = dev.interface.ip_address(int_type='loopback',
            ...        name='225', ip_addr='10.225.225.225/32',
            ...        rbridge_id='225')
            ...        output = dev.interface.ip_address(int_type='loopback',
            ...        name='225', ip_addr='10.225.225.225/32', delete=True,
            ...        rbridge_id='225')
            ...        ip_addr = 'fc00:1:3:1ad3:0:0:23:a/64'
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, rbridge_id='225')
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, delete=True,
            ...        rbridge_id='225')
        """

        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))

        delete = kwargs.pop('delete', False)
        if self.has_rbridge_id:
            rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types
        valid_int_types.append('ve')
        valid_int_types.append('loopback')

        get = kwargs.pop('get', False)

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))
        ip_args = dict()
        ip_args[int_type] = name

        if not get:
            ip_addr = str(kwargs.pop('ip_addr'))
            ipaddress = ip_interface(unicode(ip_addr))

            if ipaddress.version == 4:
                method_name = 'interface_%s_ip_address_' % int_type
                ip_args['address'] = (ip_addr, False, False, False)

            elif ipaddress.version == 6:
                method_name = 'interface_%s_ipv6_address_ipv6_address_' \
                              % int_type
                if not delete:
                    ip_args['ipv6_address'] = (ip_addr, False, False)

        if int_type == 've' and self.has_rbridge_id:
            method_name = "rbridge_id_%s" % method_name
            ip_args['rbridge_id'] = rbridge_id
            if not pyswitch.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif int_type == 'loopback' and self.has_rbridge_id:
            method_name = "rbridge_id_%s" % method_name
            ip_args['rbridge_id'] = rbridge_id

        elif not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces.')

        operation = 'create'

        if delete:
            operation = 'delete'
        try:
            if get:

                method_name = 'interface_%s_ip_address_get' % int_type
                config = (method_name, ip_args)
                x = callback(config, handler='get_config')

                method_name = 'interface_%s_ipv6_address_ipv6_address_get'\
                              % int_type
                config = (method_name, ip_args)
                y = callback(config, handler='get_config')

                return {
                    'ipv4_address': util.findall(
                        x.json,
                        '$..address'),
                    'ipv6_address': util.findall(
                        y.json,
                        '$..address')}
            else:
                method_name = "%s%s" % (method_name, operation)
                config = (method_name, ip_args)
                return callback(config)
        # TODO Setting IP on port channel is not done yet.
        except AttributeError:
            return None

    def get_ip_addresses(self, **kwargs):
        """
        Get IP Addresses already set on an Interface.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
            name (str): Name of interface id.
                 (For interface: 1/0/5, 1/0/10 etc).
            version (int): 4 or 6 to represent IPv4 or IPv6 address
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            List of 0 or more IPs configure on the specified interface.

        Raises:
            KeyError: if `int_type` or `name` is not passed.
            ValueError: if `int_type` or `name` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        int_type = 'tengigabitethernet'
            ...        name = '225/0/4'
            ...        ip_addr = '20.10.10.1/24'
            ...        version = 4
            ...        output = dev.interface.disable_switchport(inter_type=
            ...        int_type, inter=name)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        result = dev.interface.get_ip_addresses(
            ...        int_type=int_type, name=name, version=version)
            ...        assert len(result) >= 1
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
            ...        ip_addr = 'fc00:1:3:1ad3:0:0:23:a/64'
            ...        version = 6
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        result = dev.interface.get_ip_addresses(
            ...        int_type=int_type, name=name, version=version)
            ...        assert len(result) >= 1
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
        """

        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        version = int(kwargs.pop('version'))

        x = self.ip_address(int_type=int_type, name=name, get=True)
        if version == 4:
            return x['ipv4_address']
        elif version == 6:
            return x['ipv6_address']

    def del_ip(self, inter_type, inter, ip_addr):
        """
        Delete IP address from a L3 interface.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1
            ip_addr: IP Address in <prefix>/<bits> format. Ex: 10.10.10.1/24

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        return self.ip_address(
            int_type=inter_type,
            name=inter,
            ip_addr=ip_addr,
            delete=True)

    def description(self, **kwargs):
        """Set interface description.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            desc (str): The description of the interface.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `desc` is not specified.
            ValueError: if `name`, `int_type`, or `desc` is not a valid
                value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.description(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/38',
            ...         desc='test')
            ...         dev.interface.description()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        get = kwargs.pop('get', False)

        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet',
            'port_channel',
            'vlan'
        ]

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))

        desc_args = dict()
        desc_args[int_type] = name
        if get:
            if int_type == 'vlan':
                method_name = 'vlan_get'
            else:
                method_name = 'interface_%s_get' % int_type

            config = (method_name, desc_args)
            x = callback(config, handler='get_config')

            return util.find(x.json, '$..description')

        desc = str(kwargs.pop('desc'))
        desc_args['description'] = desc

        if int_type == "vlan":
            if not pyswitch.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
            method_name = '%s_update' % int_type

            config = (method_name, desc_args)

        else:
            if not pyswitch.utilities.valid_interface(int_type, name):
                raise ValueError('`name` must be in the format of x/y/z for '
                                 'physical interfaces or x for port channel.')
            method_name = 'interface_%s_update' % int_type

            config = (method_name, desc_args)
        return callback(config)

    def private_vlan_type(self, **kwargs):
        """Set the PVLAN type (primary, isolated, community).

        Args:
            name (str): VLAN ID.
            pvlan_type (str): PVLAN type (primary, isolated, community)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `pvlan_type` is not specified.
            ValueError: if `name` or `pvlan_type` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> name = '90'
            >>> pvlan_type = 'isolated'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.private_vlan_type(name=name,
            ...         pvlan_type=pvlan_type)
            ...         dev.interface.private_vlan_type()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = kwargs.pop('name')
        callback = kwargs.pop('callback', self._callback)
        allowed_pvlan_types = ['isolated', 'primary', 'community']
        get = kwargs.pop('get', False)

        if not pyswitch.utilities.valid_vlan_id(name):
            raise InvalidVlanId("Incorrect name value.")

        if get:
            config = ('vlan_get', {'vlan': name})
            x = callback(config, handler='get_config')

            return util.find(x.json, '$..pvlan-type-leaf')

        pvlan_type = kwargs.pop('pvlan_type')

        if pvlan_type not in allowed_pvlan_types:
            raise ValueError("Incorrect pvlan_type")

        pvlan_args = dict(pvlan_type_leaf=pvlan_type)
        pvlan_args['vlan'] = name

        config = ('interface_vlan_private_vlan_update', pvlan_args)

        return callback(config)

    def vlan_pvlan_association_add(self, **kwargs):
        """Add a secondary PVLAN to a primary PVLAN.

        Args:
            name (str): VLAN number (1-4094).
            sec_vlan (str): The secondary PVLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `sec_vlan` is not specified.
            ValueError: if `name` or `sec_vlan` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '20'
            >>> sec_vlan = '30'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.private_vlan_type(name=name,
            ...         pvlan_type='primary')
            ...         output = dev.interface.private_vlan_type(name=sec_vlan,
            ...         pvlan_type='isolated')
            ...         output = dev.interface.vlan_pvlan_association_add(
            ...         name=name, sec_vlan=sec_vlan)
            ...         dev.interface.vlan_pvlan_association_add()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = kwargs.pop('name')
        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)

        if not pyswitch.utilities.valid_vlan_id(name):
            raise InvalidVlanId("Incorrect name value.")

        if get:
            config = ('vlan_get', {'vlan': name})
            x = callback(config, handler='get_config')

            return util.find(x.json, '$..private-vlan..association..add')

        sec_vlan = kwargs.pop('sec_vlan')

        if not pyswitch.utilities.valid_vlan_id(sec_vlan):
            raise InvalidVlanId("`sec_vlan` must be between `1` and `8191`.")
        pvlan_args = dict()
        pvlan_args['vlan'] = name
        pvlan_args['sec_assoc_add'] = sec_vlan

        config = ('interface_vlan_private_vlan_association_update',
                  pvlan_args)
        return callback(config)

    def pvlan_host_association(self, **kwargs):
        """Set interface PVLAN association.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            pri_vlan (str): The primary PVLAN.
            sec_vlan (str): The secondary PVLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `pri_vlan`, or `sec_vlan` is not
                specified.
            ValueError: if `int_type`, `name`, `pri_vlan`, or `sec_vlan`
                is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/38'
            >>> pri_vlan = '75'
            >>> sec_vlan = '100'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.private_vlan_type(name=pri_vlan,
            ...         pvlan_type='primary')
            ...         output = dev.interface.private_vlan_type(name=sec_vlan,
            ...         pvlan_type='isolated')
            ...         output = dev.interface.vlan_pvlan_association_add(
            ...         name=pri_vlan, sec_vlan=sec_vlan)
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.private_vlan_mode(
            ...         int_type=int_type, name=name, mode='host')
            ...         output = dev.interface.pvlan_host_association(
            ...         int_type=int_type, name=name, pri_vlan=pri_vlan,
            ...         sec_vlan=sec_vlan)
            ...         dev.interface.pvlan_host_association()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        get = kwargs.pop('get', False)

        callback = kwargs.pop('callback', self._callback)

        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if get:
            pvlan_args = dict()
            pvlan_args[int_type] = name
            method_name = 'interface_%s_get' % int_type
            config = (method_name, pvlan_args)
            x = callback(config, handler='get_config')

            p = util.find(
                x.json,
                '$..switchport..private-vlan..'
                'host-association..host-pri-pvlan')
            s = util.find(
                x.json,
                '$..switchport..private-vlan..'
                'host-association..host-sec-pvlan')
            return (p, s)

        pri_vlan = kwargs.pop('pri_vlan')
        sec_vlan = kwargs.pop('sec_vlan')
        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        if not pyswitch.utilities.valid_vlan_id(pri_vlan):
            raise InvalidVlanId("`sec_vlan` must be between `1` and `4095`.")
        if not pyswitch.utilities.valid_vlan_id(sec_vlan):
            raise InvalidVlanId("`sec_vlan` must be between `1` and `4095`.")

        pvlan_args = dict(host_pri_pvlan=pri_vlan, host_sec_pvlan=sec_vlan)
        pvlan_args[int_type] = name

        method_name = 'interface_%s_switchport_private_vlan_' \
                      'host_association_update' % int_type
        config = (method_name, pvlan_args)

        return callback(config)

    def admin_state(self, **kwargs):
        """Set interface administrative state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            enabled (bool): Is the interface enabled? (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `enabled` is not passed and
                `get` is not ``True``.
            ValueError: if `int_type`, `name`, or `enabled` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.admin_state(
            ...         int_type='tengigabitethernet', name='225/0/38',
            ...         enabled=False)
            ...         dev.interface.admin_state(
            ...         int_type='tengigabitethernet', name='225/0/38',
            ...         enabled=True)
            ...         output = dev.interface.add_vlan_int('87')
            ...         output = dev.interface.ip_address(int_type='ve',
            ...         name='87', ip_addr='10.0.0.1/24', rbridge_id='225')
            ...         output = dev.interface.admin_state(int_type='ve',
            ...         name='87', enabled=True, rbridge_id='225')
            ...         output = dev.interface.admin_state(int_type='ve',
            ...         name='87', enabled=False, rbridge_id='225')
            ...         output = dev.interface.ip_address(int_type='loopback',
            ...         name='225', ip_addr='10.225.225.225/32',
            ...         rbridge_id='225')
            ...         output = dev.interface.admin_state(int_type='loopback',
            ...         name='225', enabled=True, rbridge_id='225')
            ...         output = dev.interface.admin_state(int_type='loopback',
            ...         name='225', enabled=False, rbridge_id='225')
            ...         output = dev.interface.ip_address(int_type='loopback',
            ...         name='225', ip_addr='10.225.225.225/32',
            ...         rbridge_id='225', delete=True)

        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        get = kwargs.pop('get', False)
        if get:
            enabled = None
        else:
            enabled = kwargs.pop('enabled')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types
        valid_int_types.append('ve')
        valid_int_types.append('loopback')

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if not isinstance(enabled, bool) and not get:
            raise ValueError('`enabled` must be `True` or `False`.')

        state_args = dict()
        state_args[int_type] = name
        method_name = 'interface_%s_' % int_type

        if int_type == 've':
            if self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name

                state_args['rbridge_id'] = rbridge_id

            if not pyswitch.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif int_type == 'loopback':
            if self.has_rbridge_id:
                if not get:
                    method_name = "rbridge_id_%sshutdown_" % method_name
                else:
                    method_name = "rbridge_id_%s" % method_name
                state_args['rbridge_id'] = rbridge_id

        elif not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        try:
            if get:
                get_method_name = '%s%s' % (method_name, 'get')
                state_args['resource_depth'] = 1
                config = (get_method_name, state_args)
                x = callback(config, handler='get_config')
                if self.has_rbridge_id and \
                   (int_type == 've' or int_type == 'loopback'):
                    shut = util.find(x.json, '*.shutdown')
                else:
                    shut = util.find(x.json, '*.[0].shutdown')

                if shut and shut == 'true':
                    enabled = False
                else:
                    enabled = True

                return enabled

            else:

                if method_name == 'interface_ve_':
                    shutdown_name = 'global_ve_shutdown'
                else:
                    shutdown_name = 'shutdown'
                if enabled:
                    state_args[shutdown_name] = False
                else:
                    state_args[shutdown_name] = True
                update_method_name = '%s%s' % (method_name, 'update')
                config = (update_method_name, state_args)
                return callback(config)

        # TODO: Catch existing 'no shut'
        # This is in place because if the interface is already admin up,
        # `ncclient` will raise an error if you try to admin up the interface
        # again.
        except AttributeError:
            return None

    def pvlan_trunk_association(self, **kwargs):
        """Set switchport private vlan host association.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def trunk_allowed_vlan(self, **kwargs):
        """Modify allowed VLANs on Trunk (add, remove, none, all).

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            action (str): Action to take on trunk. (add, remove, none, all)
            get (bool): Get config instead of editing config. (True, False)
            vlan (str): vlan id for action. Only valid for add and remove.
            ctag (str): ctag range. Only valid for add and remove.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is invalid.

        Examples:
            >>> # Skip due to current dev work
            >>> # TODO: Reenable after dev work
            >>> def test_trunk_allowed_vlan():
            ...     import pyswitch.device
            ...     switches = ['10.24.39.212', '10.24.39.202']
            ...     auth = ('admin', 'password')
            ...     int_type = 'tengigabitethernet'
            ...     name = '226/0/4'
            ...     for switch in switches:
            ...         conn = (switch, '22')
            ...         with pyswitch.device.Device(conn=conn, auth=auth)
                            as dev:
            ...             output = dev.interface.enable_switchport(int_type,
            ...             name)
            ...             output = dev.interface.trunk_mode(name=name,
            ...             int_type=int_type, mode='trunk')
            ...             output = dev.interface.add_vlan_int('25')
            ...             output = dev.interface.add_vlan_int('8000')
            ...             output = dev.interface.trunk_allowed_vlan(
            ...             int_type=int_type, name=name, action='add',
            ...             ctag='25', vlan='8000')
            ...             dev.interface.private_vlan_mode()
            ...             # doctest: +IGNORE_EXCEPTION_DETAIL
            >>> test_trunk_allowed_vlan() # doctest: +SKIP
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        get = kwargs.pop('get', False)

        callback = kwargs.pop('callback', self._callback)

        int_types = self.valid_int_types
        valid_actions = ['add', 'remove', 'none', 'all']

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" %
                             repr(int_types))
        allowed_vlan_args = {int_type: name}

        if get:

            method_name = 'interface_%s_switchport_trunk_allowed_vlan_get' \
                          % int_type
            config = (method_name, allowed_vlan_args)
            x = callback(config, handler='get_config')

            add = util.find(x.json, '$..add')

            return add

        action = kwargs.pop('action')
        ctag = kwargs.pop('ctag', None)
        vlan = kwargs.pop('vlan', None)

        if action not in valid_actions:
            raise ValueError('%s must be one of: %s' %
                             (action, valid_actions))

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        ctag_actions = ['add', 'remove']

        if ctag and not vlan:
            raise ValueError('vlan must be set when ctag is set ')

        if ctag and action not in ctag_actions:
            raise ValueError('%s must be in %s when %s is set '
                             % (repr(action),
                                repr(ctag_actions),
                                repr(ctag)))

        if not ctag:

            method_name = 'interface_%s_switchport_trunk_allowed_vlan_update'\
                          % int_type
            operation = '%s_' % action
            allowed_vlan_args[operation] = vlan
        else:

            method_name = 'interface_%s_switchport_trunk_' \
                          'allowed_vlan_%s_update' % (
                              int_type, action)
            allowed_vlan_args[action] = vlan
            allowed_vlan_args['trunk_ctag_range'] = ctag

        config = (method_name, allowed_vlan_args)
        return callback(config)

    def private_vlan_mode(self, **kwargs):
        """Set PVLAN mode (promiscuous, host, trunk).

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mode (str): The switchport PVLAN mode.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/38'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.private_vlan_mode(
            ...         int_type=int_type, name=name, mode='trunk_host')
            ...         dev.interface.private_vlan_mode()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        get = kwargs.pop('get', False)
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)

        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']
        valid_modes = ['host', 'promiscuous', 'trunk_host',
                       'trunk_basic', 'trunk_promiscuous']

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        pvlan_args = dict()
        pvlan_args[int_type] = name

        if get:
            method_name = 'interface_%s_get' % int_type
            config = (method_name, pvlan_args)
            x = callback(config, handler='get_config')

            if util.find(
                    x.json,
                    '$..switchport..mode..private-vlan..trunk..host'):
                return 'trunk_host'
            elif util.find(x.json, '$..switchport..mode..'
                                   'private-vlan..trunk..basic'):
                return 'trunk_basic'
            elif util.find(x.json, '$..switchport..mode..'
                                   'private-vlan..trunk..promiscuous'):
                return 'trunk_promiscuous'

            elif util.find(x.json, '$..switchport..mode..private-vlan..host'):
                return 'host'
            elif util.find(x.json, '$..switchport..mode..'
                                   'private-vlan..promiscuous'):
                return 'promiscuous'
            return None

        mode = kwargs.pop('mode').lower()
        if mode not in valid_modes:
            raise ValueError('%s must be one of: %s' % (mode, valid_modes))

        if 'trunk' in mode:

            method_name = 'interface_%s_switchport_mode_' \
                          'private_vlan_trunk_update' % (
                              int_type)
            pvlan_args[mode] = True
        else:

            method_name = 'interface_%s_switchport_mode_' \
                          'private_vlan_update' % (
                              int_type)
            pvlan_args[mode] = True

        config = (method_name, pvlan_args)
        return callback(config)

    def tag_native_vlan(self, **kwargs):
        """Set tagging of native VLAN on trunk.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mode (str): Trunk port mode (trunk, trunk-no-default-native).
            enabled (bool): Is tagging of the VLAN enabled on trunks?
                (True, False)
            callback (function): A function executed upon completion oj the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `state` is not specified.
            ValueError: if `int_type`, `name`, or `state` is not valid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.trunk_mode(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/38', mode='trunk')
            ...         output = dev.interface.tag_native_vlan(name='225/0/38',
            ...         int_type='tengigabitethernet')
            ...         output = dev.interface.tag_native_vlan(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/38', enabled=False)
            ...         dev.interface.tag_native_vlan()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        get = kwargs.pop('get', False)

        callback = kwargs.pop('callback', self._callback)

        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        tag_args = dict()
        tag_args[int_type] = name

        if get:
            method_name = 'interface_%s_switchport_trunk_tag_native_vlan_get'\
                          % int_type

            config = (method_name, tag_args)
            x = callback(config, handler='get_config')

            native_vlan_status = util.find(x.json, '$..native-vlan')
            if native_vlan_status == 'true':
                return True
            return None

        enabled = kwargs.pop('enabled', True)

        if not isinstance(enabled, bool):
            raise ValueError("Invalid state.")

        method_name = 'interface_%s_switchport_trunk_tag_native_vlan_update'\
                      % int_type

        if not enabled:
            tag_args['native_vlan'] = False
        else:
            tag_args['native_vlan'] = True
        try:
            config = (method_name, tag_args)
            return callback(config)
        # TODO: Catch existing 'no switchport tag native-vlan'
        except AttributeError:
            return None

    def switchport_pvlan_mapping(self, **kwargs):
        """Switchport private VLAN mapping.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            pri_vlan (str): The primary PVLAN.
            sec_vlan (str): The secondary PVLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/37'
            >>> pri_vlan = '3000'
            >>> sec_vlan = ['3001', '3002']
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.private_vlan_type(name=pri_vlan,
            ...         pvlan_type='primary')
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.private_vlan_mode(
            ...         int_type=int_type, name=name, mode='trunk_promiscuous')
            ...         for spvlan in sec_vlan:
            ...             output = dev.interface.private_vlan_type(
            ...             name=spvlan, pvlan_type='isolated')
            ...             output = dev.interface.vlan_pvlan_association_add(
            ...             name=pri_vlan, sec_vlan=spvlan)
            ...             output = dev.interface.switchport_pvlan_mapping(
            ...             int_type=int_type, name=name, pri_vlan=pri_vlan,
            ...             sec_vlan=spvlan)
            ...         dev.interface.switchport_pvlan_mapping()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s"
                             % repr(int_types))

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError("`name` must be in the format of x/y/x for "
                             "physical interfaces or x for port channel.")
        pvlan_args = {int_type: name}
        if kwargs.pop('get', False):
            pvlan_args['resource_depth'] = 3
            method_name = 'interface_%s_switchport_private_vlan_mapping_get' \
                          % int_type
            config = (method_name, pvlan_args)
            x = callback(config, handler='get_config')

            pri_vlan = util.find(x.json, '$..promis-pri-pvlan')
            sec_vlan = util.find(x.json, '$..promis-sec-pvlan-range')
            return {'pri_vlan': pri_vlan, 'sec_vlan': sec_vlan}

        pri_vlan = kwargs.pop('pri_vlan')
        sec_vlan = kwargs.pop('sec_vlan')

        if not pyswitch.utilities.valid_vlan_id(pri_vlan, extended=True):
            raise InvalidVlanId("`pri_vlan` must be between `1` and `4096`")

        if not pyswitch.utilities.valid_vlan_id(sec_vlan, extended=True):
            raise InvalidVlanId("`sec_vlan` must be between `1` and `4096`")

        pvlan_args['mapping'] = (pri_vlan, 'add', sec_vlan)

        delete = kwargs.pop('delete', False)
        if delete:
            method_name = 'interface_%s_switchport_' \
                          'private_vlan_mapping_delete' % int_type
        else:
            method_name = 'interface_%s_switchport_' \
                          'private_vlan_mapping_create' % int_type

        config = (method_name, pvlan_args)
        return callback(config)

    def mtu(self, **kwargs):
        """Set interface mtu.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mtu (str): Value between 1522 and 9216
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mtu` is not specified.
            ValueError: if `int_type`, `name`, or `mtu` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.mtu(mtu='1666',
            ...         int_type='tengigabitethernet', name='225/0/38')
            ...         dev.interface.mtu() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)

        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if kwargs.pop('get', False):
            method_name = 'interface_%s_get' % int_type
            config = (method_name, {int_type: name, 'resource_depth': 3})
            op = callback(config, handler='get_config')

            return util.find(op.json, '$..mtu')

        mtu = kwargs.pop('mtu')
        minimum_mtu, maximum_mtu = self.l2_mtu_const

        if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
            raise ValueError(
                "Incorrect mtu value %s-%s" %
                (minimum_mtu, maximum_mtu))

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        method_name = 'interface_%s_update' % int_type

        config = (method_name, {int_type: name, 'mtu': mtu})
        return callback(config)

    def ip_mtu(self, **kwargs):
        """Set interface mtu.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mtu (str): Value between 1300 and 9018
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mtu` is not specified.
            ValueError: if `int_type`, `name`, or `mtu` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.ip_mtu(mtu='1666',
            ...         int_type='tengigabitethernet', name='225/0/38')
            ...         dev.interface.ip_mtu() # doctest:
            +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        version = kwargs.pop('version', 4)

        callback = kwargs.pop('callback', self._callback)

        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if kwargs.pop('get', False):
            method_name = 'interface_%s_get' % int_type
            config = (method_name, {int_type: name})
            op = callback(config, handler='get_config')

            ipv4_mtu = util.find(op.json, '$..ip..mtu')
            ipv6_mtu = util.find(op.json, '$..ipv6..mtu')
            return {'ipv4': ipv4_mtu, 'ipv6': ipv6_mtu}

        mtu = kwargs.pop('mtu')

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces.')
        if version == 6:
            minimum_mtu, maximum_mtu = self.l3_ipv6_mtu_const
            method_name = 'interface_%s_ipv6_mtu_update' % int_type
        else:
            minimum_mtu, maximum_mtu = self.l3_mtu_const
            method_name = 'interface_%s_ip_ip_config_update' % int_type

        if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
            raise ValueError(
                "Incorrect mtu value %s-%s" %
                (minimum_mtu, maximum_mtu))

        config = (method_name, {int_type: name, 'mtu': mtu})

        return callback(config)

    def v6_nd_suppress_ra(self, **kwargs):
        """Disable IPv6 Router Advertisements

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `rbridge_id` is not specified.
            ValueError: if `int_type`, `name`, or `rbridge_id` is not a valid
                value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.add_vlan_int('10')
            ...         output = dev.interface.v6_nd_suppress_ra(name='10',
            ...         int_type='ve', rbridge_id='225')
            ...         dev.interface.v6_nd_suppress_ra()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        callback = kwargs.pop('callback', self._callback)
        enabled = kwargs.pop('enabled', True)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet',
            've'
        ]

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))
        nd_suppress_args = dict()
        nd_suppress_args[int_type] = name

        if kwargs.pop('get', False):
            if int_type == 've':
                rbridge_id = kwargs.pop('rbridge_id', "1")
                nd_suppress_args['rbridge_id'] = rbridge_id
                method_name = 'rbridge_id_interface_%s_ipv6_get' % int_type
            else:
                method_name = 'interface_%s_ipv6_get' % int_type

            config = (method_name, nd_suppress_args)
            op = callback(config, handler='get_config')

            if util.find(op.json, '$..nd..suppress-ra.all'):
                return True
            return None

        if int_type == "ve":
            if not pyswitch.utilities.valid_vlan_id(name):
                raise ValueError("`name` must be between `1` and `8191`")

            rbridge_id = kwargs.pop('rbridge_id', "1")

            nd_suppress_args['rbridge_id'] = rbridge_id
            nd_suppress_args['suppress_ra_all'] = enabled

            method_name = 'rbridge_id_interface_ve_ipv6_nd_suppress_ra_update'

        else:
            if not pyswitch.utilities.valid_interface(int_type, name):
                raise ValueError("`name` must match "
                                 "`^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$`")

            nd_suppress_args['suppress_ra_all'] = enabled
            method_name = 'interface_%s_ipv6_nd_suppress_ra_update' % int_type

        config = (method_name, nd_suppress_args)
        return callback(config)

    def vrrp_vrid(self, **kwargs):
        int_type = kwargs.pop('int_type').lower()
        version = kwargs.pop('version', 4)
        name = kwargs.pop('name', )
        get = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ve']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        arguments = {int_type: name}

        if get:
            if version == 4:
                method_name = 'interface_%s_vrrp_group_get' % int_type
            else:
                method_name = 'interface_%s_ipv6_vrrp_roup_get' % int_type
            if int_type == 've' and self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name
                arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            config = (method_name, arguments)
            x = callback(config)

            return util.find(x.json, '$..vrid')

        vrid = kwargs.pop('vrid')
        if version == 4:
            method_name = 'interface_%s_vrrp_group_' % int_type
            vrid_name = 'vrrp'
        else:
            method_name = 'interface_%s_ipv6_vrrp_group_' % int_type
            vrid_name = 'vrrpv3_group'

        if int_type == 've' and self.has_rbridge_id:
            method_name = "rbridge_id_%s" % method_name
            arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            if version == 6:
                vrid_name = 'vrrpv3'

        arguments[vrid_name] = (vrid, '3')
        if delete:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%screate" % method_name
        config = (method_name, arguments)
        return callback(config)

    def vrrp_vip(self, **kwargs):
        """Set VRRP VIP.
        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            vrid (str): VRRPv3 ID.
            vip (str): IPv4/IPv6 Virtual IP Address.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vip` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vip` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.anycast_mac(rbridge_id='225',
            ...         mac='aabb.ccdd.eeff', delete=True)
            ...         output = dev.services.vrrp(ip_version='6',
            ...         enabled=True, rbridge_id='225')
            ...         output = dev.services.vrrp(enabled=True,
            ...         rbridge_id='225')
            ...         output = dev.interface.set_ip('tengigabitethernet',
            ...         '225/0/18', '10.1.1.2/24')
            ...         output = dev.interface.vrrp_vip(
                        int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='fe80::cafe:beef:1000:1/64')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='2001:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         output = dev.interface.add_vlan_int('89')
            ...         output = dev.interface.ip_address(name='89',
            ...         int_type='ve', ip_addr='172.16.1.1/24',
            ...         rbridge_id='225')
            ...         output = dev.interface.ip_address(name='89',
            ...         int_type='ve', rbridge_id='225',
            ...         ip_addr='2002:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         dev.interface.vrrp_vip(int_type='ve', name='89',
            ...         vrid='1', vip='172.16.1.2/24', rbridge_id='225')
            ...         dev.interface.vrrp_vip(int_type='ve', name='89',
            ...         vrid='1', vip='fe80::dafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         dev.interface.vrrp_vip(int_type='ve', name='89',
            ...         vrid='1', vip='2002:4818:f000:1ab:cafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         output = dev.services.vrrp(ip_version='6',
            ...         enabled=False, rbridge_id='225')
            ...         output = dev.services.vrrp(enabled=False,
            ...         rbridge_id='225')
        """
        int_type = kwargs.pop('int_type').lower()
        version = kwargs.pop('version', 4)
        name = kwargs.pop('name', )
        get = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ve']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        arguments = {int_type: name}

        vrid = kwargs.pop('vrid')
        if get:
            if version == 4:
                method_name = 'interface_%s_vrrp_group_virtual_ip_get' \
                              % int_type
                vrid_name = 'vrrp'
            else:
                method_name = 'interface_%s_ipv6_vrrp_group_virtual_ip_get'\
                              % int_type
                vrid_name = 'vrrpv3_group'

            if int_type == 've' and self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name
                arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
                if version == 6:
                    vrid_name = 'vrrpv3'
            arguments[vrid_name] = (vrid, '3')
            config = (method_name, arguments)
            x = callback(config)

            return util.find(x.json, '$..virtual-ipaddr')

        vip = kwargs.pop('vip', '')
        if vip != '':
            ipaddress = ip_interface(unicode(vip))
            version = ipaddress.version
        else:
            version = 4

        if version == 4:
            method_name = 'interface_%s_vrrp_group_virtual_ip_' % int_type
            vrid_name = 'vrrp'
        else:
            method_name = 'interface_%s_ipv6_vrrp_group_virtual_ip_' \
                          % int_type
            vrid_name = 'vrrpv3_group'

        if int_type == 've' and self.has_rbridge_id:
            method_name = "rbridge_id_%s" % method_name
            arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            if version == 6:
                vrid_name = 'vrrpv3'

        arguments[vrid_name] = (vrid, '3')

        arguments['virtual_ip'] = str(ipaddress.ip)
        if delete:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%screate" % method_name
        config = (method_name, arguments)
        return callback(config)

    def vrrp_state(self, **kwargs):
        """Set VRRP state (enabled, disabled).

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def vrrp_preempt(self, **kwargs):
        """Set VRRP preempt mode (enabled, disabled).

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def vrrp_priority(self, **kwargs):
        """Set VRRP priority.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            vrid (str): VRRPv3 ID.
            priority (str): VRRP Priority.
            ip_version (str): Version of IP (4, 6).
            callback (function): A function executed upon completion of the
                method.  The only parameter passevrrpe_spf_basicd to
                `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `vrid`, `priority`, or
                `ip_version` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, `priority`, or
                `ip_version` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.anycast_mac(rbridge_id='225',
            ...         mac='aabb.ccdd.eeff', delete=True)
            ...         output = dev.services.vrrp(ip_version='6',
            ...         enabled=True, rbridge_id='225')
            ...         output = dev.services.vrrp(enabled=True,
            ...         rbridge_id='225')
            ...         output = dev.interface.set_ip('tengigabitethernet',
            ...         '225/0/18', '10.1.1.2/24')
            ...         output = dev.interface.ip_address(name='225/0/18',
            ...         int_type='tengigabitethernet',
            ...         ip_addr='2001:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1', vip='10.1.1.1/24')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='fe80::cafe:beef:1000:1/64')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='2001:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         dev.interface.vrrp_priority(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1', ip_version='4',
            ...         priority='66')
            ...         dev.interface.vrrp_priority(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1', ip_version='6',
            ...         priority='77')
            ...         output = dev.interface.add_vlan_int('88')
            ...         output = dev.interface.ip_address(int_type='ve',
            ...         name='88', ip_addr='172.16.10.1/24', rbridge_id='225')
            ...         output = dev.interface.ip_address(int_type='ve',
            ...         name='88', rbridge_id='225',
            ...         ip_addr='2003:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         dev.interface.vrrp_vip(int_type='ve', name='88',
            ...         vrid='1', vip='172.16.10.2/24', rbridge_id='225')
            ...         dev.interface.vrrp_vip(int_type='ve', name='88',
            ...         rbridge_id='225', vrid='1',
            ...         vip='fe80::dafe:beef:1000:1/64')
            ...         dev.interface.vrrp_vip(int_type='ve', rbridge_id='225',
            ...         name='88', vrid='1',
            ...         vip='2003:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         dev.interface.vrrp_priority(int_type='ve', name='88',
            ...         rbridge_id='225', vrid='1', ip_version='4',
            ...         priority='66')
            ...         dev.interface.vrrp_priority(int_type='ve', name='88',
            ...         rbridge_id='225', vrid='1', ip_version='6',
            ...         priority='77')
            ...         output = dev.services.vrrp(ip_version='6',
            ...         enabled=False, rbridge_id='225')
            ...         output = dev.services.vrrp(enabled=False,
            ...         rbridge_id='225')
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')

        version = int(kwargs.pop('ip_version'))

        get = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        arguments = {int_type: name}

        if get:
            if version == 4:
                method_name = 'interface_%s_vrrp_group_get' % int_type
                vrid_name = 'vrrp'
            else:
                method_name = 'interface_%s_ipv6_vrrp_group_get' % int_type
                vrid_name = 'vrrpv3_group'

            if int_type == 've':
                if self.has_rbridge_id:
                    method_name = "rbridge_id_%s" % method_name
                    arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
                if version == 6:
                    vrid_name = 'vrrpv3'
            arguments[vrid_name] = (vrid, '3')
            config = (method_name, arguments)
            x = callback(config)

            return util.find(x.json, '$..priority')

        priority = kwargs.pop('priority')

        if version == 4:
            method_name = 'interface_%s_vrrp_group_' % int_type
            vrid_name = 'vrrp'
        else:
            method_name = 'interface_%s_ipv6_vrrp_group_' % int_type
            vrid_name = 'vrrpv3_group'

        if int_type == 've':
            if self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name
                arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            if version == 6:
                vrid_name = 'vrrpv3'

        arguments[vrid_name] = (vrid, '3')

        if delete:
            method_name = "%sdelete" % method_name
        else:
            arguments['priority'] = priority
            method_name = "%supdate" % method_name
        config = (method_name, arguments)
        return callback(config)

    def vrrp_advertisement_interval(self, **kwargs):
        """Set VRRP advertisement interval.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def proxy_arp(self, **kwargs):
        """Set interface administrative state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            enabled (bool): Is proxy-arp enabled? (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `state` is not passed.
            ValueError: if `int_type`, `name`, or `state` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.proxy_arp(int_type='tengigabitethernet',
            ...         name='225/0/12', enabled=True)
            ...         dev.interface.proxy_arp(int_type='tengigabitethernet',
            ...         name='225/0/12', enabled=False)
            ...         output = dev.interface.add_vlan_int('86')
            ...         output = dev.interface.ip_address(int_type='ve',
            ...         name='86', ip_addr='172.16.2.1/24', rbridge_id='225')
            ...         output = dev.interface.proxy_arp(int_type='ve',
            ...         name='86', enabled=True, rbridge_id='225')
            ...         output = dev.interface.proxy_arp(int_type='ve',
            ...         name='86', enabled=False, rbridge_id='225')
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        enabled = kwargs.pop('enabled', True)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        if not isinstance(enabled, bool):
            raise ValueError('`enabled` must be `True` or `False`.')

        method_name = 'interface_%s_ip_arp_aging_timeout_update' % int_type
        get_method_name = 'interface_%s_get' % int_type
        proxy_arp_args = dict()
        proxy_arp_args[int_type] = name

        if int_type == 've':
            method_name = "rbridge_id_%s" % method_name
            get_method_name = "rbridge_id_%s" % get_method_name
            proxy_arp_args['rbridge_id'] = rbridge_id
            if not pyswitch.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'phyiscal interfaces or x for port channel.')

        if kwargs.pop('get', False):
            config = (get_method_name, proxy_arp_args)
            output = callback(config, handler='get_config')

            item = util.find(output.json, '$..ip..proxy-arp')

            if item:
                return True
            else:
                return None

        if not enabled:
            proxy_arp_args['proxy_arp'] = False
        else:
            proxy_arp_args['proxy_arp'] = True

        try:
            config = (method_name, proxy_arp_args)
            return callback(config)
        # TODO: Catch existing 'no proxy arp'
        # This is in place because if proxy arp is already disabled,
        # `ncclient` will raise an error if you try to disable it again.
        except AttributeError:
            return None

    def port_channel_minimum_links(self, **kwargs):
        """Set minimum number of links in a port channel.

        Args:
            name (str): Port-channel number. (1, 5, etc)
            minimum_links (str): Minimum number of links in channel group.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `minimum_links` is not specified.
            ValueError: if `name` is not a valid value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.port_channel_minimum_links(
            ...         name='1', minimum_links='2')
            ...         dev.interface.port_channel_minimum_links()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = str(kwargs.pop('name'))

        callback = kwargs.pop('callback', self._callback)

        if kwargs.pop('get', False):
            ve_args = dict()
            ve_args['port_channel'] = name
            config = ('interface_port_channel_get', ve_args)

            output = callback(config, handler='get_config')
            return util.find(output.json, '$..minimum-links')

        minimum_links = str(kwargs.pop('minimum_links'))

        if not pyswitch.utilities.valid_interface('port_channel', name):
            raise ValueError("`name` must match `^[0-9]{1,3}${1,3}$`")

        config = (
            'interface_port_channel_update', {
                'port_channel': name, 'minimum_links': minimum_links})

        return callback(config)

    def channel_group(self, **kwargs):
        """set channel group mode.

        args:
            int_type (str): type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): name of interface. (1/0/5, 1/0/10, etc)
            port_int (str): port-channel number (1, 2, 3, etc).
            channel_type (str): tiype of port-channel (standard, brocade)
            mode (str): mode of channel group (active, on, passive).
            delete (bool): Removes channel group configuration from this
                interface if `delete` is ``True``.
            callback (function): a function executed upon completion of the
                method.  the only parameter passed to `callback` will be the
                ``elementtree`` `config`.

        returns:
            return value of `callback`.

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.

        examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.channel_group(name='225/0/20',
            ...         int_type='tengigabitethernet',
            ...         port_int='1', channel_type='standard', mode='active')
            ...         dev.interface.channel_group()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)

        int_types = self.valid_intp_types

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))

        if kwargs.pop('get', False):
            method_name = 'interface_%s_channel_group_mode_get' % int_type
            arguments = {int_type: name}
            config = (method_name, arguments)
            op = callback(config, handler='get_config')

            port_int = util.find(op.json, '$..port-int')
            channel_type = util.find(op.json, '$..type')
            mode = util.find(op.json, '$..mode')
            return {
                'port_int': port_int,
                'channel_type': channel_type,
                'mode': mode}

        delete = kwargs.pop('delete', False)
        if delete is True:
            method_name = 'interface_%s_channel_group_mode_delete' % int_type
            arguments = {int_type: name}
            config = (method_name, arguments)
            return callback(config)

        channel_type = kwargs.pop('channel_type')
        port_int = kwargs.pop('port_int')
        mode = kwargs.pop('mode')

        valid_modes = ['active', 'on', 'passive']

        if mode not in valid_modes:
            raise ValueError("`mode` must be one of: %s" % repr(valid_modes))

        valid_types = ['brocade', 'standard']

        if channel_type not in valid_types:
            raise ValueError("`channel_type` must be one of: %s" %
                             repr(valid_types))

        if not pyswitch.utilities.valid_interface('port_channel', port_int):
            raise ValueError("incorrect port_int value.")

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError("incorrect name value.")

        arguments = {
            int_type: name,
            'mode': mode,
            'port_int': port_int,
            'type': channel_type}

        method_name = 'interface_%s_channel_group_update' % int_type
        config = (method_name, arguments)

        return callback(config)

    def port_channel_vlag_ignore_split(self, **kwargs):
        """Ignore VLAG Split.

        Args:
            name (str): Port-channel number. (1, 5, etc)
            enabled (bool): Is ignore split enabled? (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `enable` is not specified.
            ValueError: if `name` is not a valid value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.port_channel_vlag_ignore_split(
            ...         name='1', enabled=True)
            ...         dev.interface.port_channel_vlag_ignore_split()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = str(kwargs.pop('name'))
        enabled = bool(kwargs.pop('enabled', True))
        callback = kwargs.pop('callback', self._callback)

        vlag_ignore_args = dict()
        vlag_ignore_args['port_channel'] = name

        if not pyswitch.utilities.valid_interface('port_channel', name):
            raise ValueError("`name` must match x")

        method_name = 'interface_port_channel_vlag_ignore_split_update'
        config = (method_name, vlag_ignore_args)

        if not enabled:
            vlag_ignore_args['ignore_split'] = False
        else:
            vlag_ignore_args['ignore_split'] = True

        return callback(config)

    def access_mode(self, **kwargs):
        """Set trunk mode (trunk, trunk-no-default-vlan).

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mode (str): Trunk port mode (trunk, trunk-no-default-native).
            callback (function): A function executed upon completion oj the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is not valid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.trunk_mode(name='225/0/38',
            ...         int_type='tengigabitethernet', mode='trunk')
            ...         dev.interface.trunk_mode()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')

        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        valid_modes = ['access']

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        mode_args = dict()
        mode_args[int_type] = name

        method_name = 'interface_%s_switchport_mode_update' % int_type
        get_method_name = 'interface_%s_switchport_mode_get' % int_type

        if get:
            config = (get_method_name, mode_args)
            op = callback(config, handler='get_config')
            return util.find(op.json, '$..vlan-mode')

        mode = kwargs.pop('mode').lower()
        if mode not in valid_modes:
            raise ValueError("Incorrect mode value")
        mode_args['vlan_mode'] = mode

        config = (method_name, mode_args)
        return callback(config)

    def trunk_mode(self, **kwargs):
        """Set trunk mode (trunk, trunk-no-default-vlan).

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mode (str): Trunk port mode (trunk, trunk-no-default-native).
            callback (function): A function executed upon completion oj the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is not valid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.trunk_mode(name='225/0/38',
            ...         int_type='tengigabitethernet', mode='trunk')
            ...         dev.interface.trunk_mode()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')

        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        valid_modes = ['trunk', 'trunk-no-default-native']

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        mode_args = dict()
        mode_args[int_type] = name

        method_name = 'interface_%s_switchport_mode_update' % int_type
        get_method_name = 'interface_%s_switchport_mode_get' % int_type

        if get:
            config = (get_method_name, mode_args)
            op = callback(config, handler='get_config')
            return util.find(op.json, '$..vlan-mode')

        mode = kwargs.pop('mode').lower()
        if mode not in valid_modes:
            raise ValueError("Incorrect mode value")
        mode_args['vlan_mode'] = mode

        config = (method_name, mode_args)
        return callback(config)

    def transport_service(self, **kwargs):
        """Configure VLAN Transport Service.

        Args:
            vlan (str): The VLAN ID.
            service_id (str): The transport-service ID.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `vlan` or `service_id` is not specified.
            ValueError: if `vlan` is invalid.

        Examples:
            >>> # Skip due to current work in devel
            >>> # TODO: Reenable
            >>> def test_transport_service():
            ...     import pyswitch.device
            ...     switches = ['10.24.39.212', '10.24.39.202']
            ...     auth = ('admin', 'password')
            ...     vlan = '6666'
            ...     service_id = '1'
            ...     for switch in switches:
            ...      conn = (switch, '22')
            ...      with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...             output = dev.interface.add_vlan_int(vlan)
            ...             output = dev.interface.spanning_tree_state(
            ...             int_type='vlan', name=vlan, enabled=False)
            ...             output = dev.interface.transport_service(vlan=vlan,
            ...             service_id=service_id)
            ...             dev.interface.transport_service()
            ...             # doctest: +IGNORE_EXCEPTION_DETAIL
            >>> test_transport_service() # doctest: +SKIP
        """
        vlan = kwargs.pop('vlan')
        service_id = kwargs.pop('service_id')
        callback = kwargs.pop('callback', self._callback)

        if not pyswitch.utilities.valid_vlan_id(vlan, extended=True):
            raise InvalidVlanId("vlan must be between `1` and `8191`")

        service_args = dict(vlan=vlan, transport_service=service_id)

        config = ('vlan_update', service_args)
        return callback(config)

    def lacp_timeout(self, **kwargs):
        """Set lacp timeout.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            timeout (str):  Timeout length.  (short, long)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `timeout` is not specified.
            ValueError: if `int_type`, `name`, or `timeout is not valid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/39'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.channel_group(name=name,
            ...         int_type=int_type, port_int='1',
            ...         channel_type='standard', mode='active')
            ...         output = dev.interface.lacp_timeout(name=name,
            ...         int_type=int_type, timeout='long')
            ...         dev.interface.lacp_timeout()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        timeout = kwargs.pop('timeout')
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
        ]

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        valid_timeouts = ['long', 'short']
        if timeout not in valid_timeouts:
            raise ValueError("Incorrect timeout value")

        timeout_args = dict(timeout=timeout)
        timeout_args[int_type] = name

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError("Incorrect name value.")
        method_name = 'interface_%s_lacp_update' % int_type

        config = (method_name, timeout_args)
        return callback(config)

    def switchport(self, **kwargs):
        """Set interface switchport status.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            enabled (bool): Is the interface enabled? (True, False)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type` or `name` is not specified.
            ValueError: if `name` or `int_type` is not a valid
                value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.switchport(name='225/0/19',
            ...         int_type='tengigabitethernet')
            ...         output = dev.interface.switchport(name='225/0/19',
            ...         int_type='tengigabitethernet', enabled=False)
            ...         dev.interface.switchport()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        enabled = kwargs.pop('enabled', True)
        callback = kwargs.pop('callback', self._callback)
        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s"
                             % repr(int_types))
        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        switchport_args = dict()
        switchport_args[int_type] = name
        method_name = 'interface_%s_switchport_update' % int_type
        get_method_name = 'interface_%s_switchport_get' % int_type
        if kwargs.pop('get', False):
            config = (get_method_name, switchport_args)
            op = callback(config, handler='get_config')

            x = util.find(op.json, '$..switchport')
            if isinstance(x, list):
                if x[0] == 'true':
                    return True
            return None

        if not enabled:
            switchport_args['basic'] = False
        else:
            switchport_args['basic'] = True
        config = (method_name, switchport_args)
        return callback(config)

    def acc_vlan(self, **kwargs):
        """Set access VLAN on a port.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            vlan (str): VLAN ID to set as the access VLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `vlan` is not specified.
            ValueError: if `int_type`, `name`, or `vlan` is not valid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/30'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.add_vlan_int('736')
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.acc_vlan(int_type=int_type,
            ...         name=name, vlan='736')
            ...         dev.interface.acc_vlan()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type')
        name = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s"
                             % repr(int_types))
        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        vlan_args = {int_type: name}

        if kwargs.pop('get', False):
            method_name = 'interface_%s_switchport_access_get' % int_type
            config = (method_name, vlan_args)
            op = callback(config, handler='get_config')

            return util.find(op.json, '$..vlan')

        vlan = kwargs.pop('vlan')
        if not pyswitch.utilities.valid_vlan_id(vlan):
            raise InvalidVlanId("`name` must be between `1` and `4096`")

        if kwargs.pop('delete', False):
            method_name = 'interface_%s_switchport_access_vlan_delete'\
                          % int_type
        else:
            vlan_args['accessvlan'] = vlan
            method_name = 'interface_%s_switchport_access_update' % int_type

        config = (method_name, vlan_args)
        return callback(config)

    @property
    def interfaces(self):
        """list[dict]: A list of dictionary items describing the operational
        state of interfaces.
        This method currently only lists the Physical Interfaces (
        Gigabitethernet, tengigabitethernet, fortygigabitethernet,
        hundredgigabitethernet) and Loopback interfaces.  It currently
        excludes VLAN interfaces, FCoE, Port-Channels, Management and Fibre
        Channel ports.
        """

        result = []
        has_more = ''
        last_interface_name = ''
        last_interface_type = ''

        while (has_more == '') or (has_more == 'true'):
            request_interface = self.get_interface_detail_request(
                last_interface_name, last_interface_type)
            interface_result = self._callback(request_interface, 'get')

            has_more = util.find(interface_result.json, '$..has-more')

            for item in util.findlist(interface_result.json, '$..interface'):
                interface_type = util.find(item, '$..interface-type')
                interface_name = util.find(item, '$..interface-name')
                last_interface_type = interface_type
                last_interface_name = interface_name
                if "gigabitethernet" in interface_type:
                    interface_role = util.find(item, '$..port-role')
                    if_name = util.find(item, '$..if-name')
                    interface_state = util.find(item, '$..if-state')
                    interface_proto_state = util.find(
                        item, '$..line-protocol-state')

                    interface_mac = util.find(item,
                                              '$..current-hardware-address')

                    item_results = {'interface-type': interface_type,
                                    'interface-name': interface_name,
                                    'interface-role': interface_role,
                                    'if-name': if_name,
                                    'interface-state': interface_state,
                                    'interface-proto-state':
                                    interface_proto_state,
                                    'interface-mac': interface_mac}
                    result.append(item_results)
        # Loopback interfaces. Probably for other non-physical interfaces, too.
        ip_result = []

        request_interface = ('get_ip_interface_rpc', {})
        interface_result = self._callback(request_interface, 'get')

        for interface in util.find(interface_result.json, '$..interface'):
            int_type = util.find(interface, '$..interface-type')
            int_name = util.find(interface, '$..interface-name')
            if int_type == 'unknown':
                continue

            int_state = util.find(interface, '$..if-state')
            int_proto_state = util.find(interface, '$..line-protocol-state')

            ip_address = util.find(interface, '$..ipv4')
            results = {'interface-type': int_type,
                       'interface-name': int_name,
                       'interface-role': None,
                       'if-name': None,
                       'interface-state': int_state,
                       'interface-proto-state': int_proto_state,
                       'interface-mac': None,
                       'ip-address': ip_address}
            x = next((x for x in result if int_type == x['interface-type'] and
                      int_name == x['interface-name']), None)
            if x is not None:
                results.update(x)
            ip_result.append(results)
        return ip_result

    @staticmethod
    def get_interface_detail_request(last_interface_name,
                                     last_interface_type):
        """ Creates a new Netconf request based on the last received
        interface name and type when the hasMore flag is true
        """
        arguments = {}

        if last_interface_name != '':
            last_received_int = (last_interface_type, last_interface_name)
            arguments = {'last_rcvd_interface': last_received_int}

        return ('get_interface_detail_rpc', arguments)

    def single_interface_detail(self, **kwargs):
        """list[dict]: A list of dictionary items describing the
        interface type, name, role, mac, admin and operational
        state of interfaces of all rbridges.
        This method currently only lists the Physical Interfaces (
        Gigabitethernet, tengigabitethernet, fortygigabitethernet,
        hundredgigabitethernet) and port-channel
        """

        result = []
        int_type = kwargs.pop('int_type')
        name = kwargs.pop('name')

        int_types = self.valid_intp_types
        int_types.append('port-channel')

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s"
                             % repr(int_types))

        arguments = {'interface_type': int_type, 'interface_name': name}

        request_interface = ('get_interface_detail_rpc', arguments)
        interface_result = self._callback(request_interface, 'get')

        for item in util.findlist(interface_result.json, 'interface'):
            interface_type = util.find(item, '$..interface-type')
            interface_name = util.find(item, '$..interface-name')

            if "gigabitethernet" '' in interface_type or \
                    "port-channel" in interface_type or 'ethernet'\
                    in interface_type:
                if "gigabitethernet" in interface_type or 'ethernet'\
                        in interface_type:
                    interface_role = util.find(item, '$..port-role')
                else:
                    interface_role = "None"
                if_name = util.find(item, '$..if-name')
                interface_state = util.find(item, '$..if-state')
                interface_proto_state = util.find(
                    item, '$..line-protocol-state')

                interface_mac = util.find(item,
                                          '$..current-hardware-address')
                item_results = {'interface-type': interface_type,
                                'interface-name': interface_name,
                                'interface-role': interface_role,
                                'if-name': if_name,
                                'interface-state': interface_state,
                                'interface-proto-state':
                                interface_proto_state,
                                'interface-mac': interface_mac}
                result.append(item_results)

        return result

    @property
    def interface_detail(self):
        """list[dict]: A list of dictionary items describing the
        interface type, name, role, mac, admin and operational
        state of interfaces of all rbridges.
        This method currently only lists the Physical Interfaces (
        Gigabitethernet, tengigabitethernet, fortygigabitethernet,
        hundredgigabitethernet) and port-channel
        """

        result = []
        has_more = ''
        last_interface_name = ''
        last_interface_type = ''

        while (has_more == '') or (has_more == 'true'):
            request_interface = self.get_interface_detail_request(
                last_interface_name, last_interface_type)
            interface_result = self._callback(request_interface, 'get')

            has_more = util.find(interface_result.json, '$..has-more')

            for item in util.findlist(interface_result.json, 'interface'):
                interface_type = util.find(item, '$..interface-type')
                interface_name = util.find(item, '$..interface-name')
                last_interface_type = interface_type
                last_interface_name = interface_name
                if "gigabitethernet" '' in interface_type or \
                        "port-channel" in interface_type or 'ethernet'\
                        in interface_type:
                    if "gigabitethernet" in interface_type or 'ethernet'\
                            in interface_type:
                        interface_role = util.find(item, '$..port-role')
                    else:
                        interface_role = "None"
                    if_name = util.find(item, '$..if-name')
                    interface_state = util.find(item, '$..if-state')
                    interface_proto_state = util.find(
                        item, '$..line-protocol-state')

                    interface_mac = util.find(item,
                                              '$..current-hardware-address')
                    item_results = {'interface-type': interface_type,
                                    'interface-name': interface_name,
                                    'interface-role': interface_role,
                                    'if-name': if_name,
                                    'interface-state': interface_state,
                                    'interface-proto-state':
                                    interface_proto_state,
                                    'interface-mac': interface_mac}
                    result.append(item_results)

        return result

    @property
    def switchport_list(self):
        """list[dict]:A list of dictionary items describing the details
         of list of dictionary items describing the details of switch port"""

        result = []
        request_interface = self.get_interface_switchport_request()
        interface_result = self._callback(request_interface, 'get')

        for interface in util.findlist(interface_result.json,
                                       '$..switchport'):


            vlans = []
            interface_type = util.findText(interface, 'interface-type')
            interface_name = util.findText(interface, 'interface-name')

            mode = util.findText(interface, 'mode')
            intf = util.findText(interface, 'active-vlans')
            for vlan_node in util.findlist(intf, 'vlanid'):
                vlans.append(vlan_node)
            results = {'vlan-id': vlans,
                       'mode': mode,
                       'interface-name': interface_name,
                       'interface_type': interface_type}
            result.append(results)
        return result

    @property
    def vlans(self):
        """list[dict]: A list of dictionary items describing the details of
        vlan interfaces.
        This method fetches the VLAN interfaces
        Examples:
            >>> import pyswitch.device
            >>> switch = '10.24.39.202'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.add_vlan_int('736')
            ...     interfaces = dev.interface.vlans
            ...     is_vlan_interface_present = False
            ...     for interface in interfaces:
            ...         if interface['vlan-id'] == '736':
            ...             is_vlan_interface_present = True
            ...             break
            ...     dev.interface.del_vlan_int('736')
            ...     assert is_vlan_interface_present
            True
        """

        result = []
        has_more = ''
        last_vlan_id = ''
        while (has_more == '') or (has_more == 'true'):
            request_interface = self.get_vlan_brief_request(last_vlan_id)
            interface_result = self._callback(request_interface, 'get')

            has_more = util.find(interface_result.json, 'has-more')
            last_vlan_id = util.find(interface_result.json, 'last-vlan-id')

            for interface in util.findlist(interface_result.json, 'vlan'):
                vlan_id = util.find(interface, 'vlan-id')
                vlan_type = util.find(interface, 'vlan-type')
                vlan_name = util.find(interface, 'vlan-name')
                vlan_state = util.find(
                    interface, 'vlan-state')
                ports = []

                for intf in util.findlist(interface, 'interface'):
                    interface_type = util.find(
                        intf, 'interface-type')
                    interface_name = util.find(
                        intf, 'interface-name')
                    tag = util.find(intf, 'tag')
                    port_results = {'interface-type': interface_type,
                                    'interface-name': interface_name,
                                    'tag': tag}
                    ports.append(port_results)
                results = {'interface-name': vlan_name,
                           'vlan-state': vlan_state,
                           'vlan-id': vlan_id,
                           'vlan-type': vlan_type,
                           'interface': ports}
                result.append(results)
        return result

    @staticmethod
    def get_interface_switchport_request():
        """Creates a new Netconf request"""

        return ('get_interface_switchport_rpc', {})

    @staticmethod
    def get_vlan_brief_request(last_vlan_id):
        """ Creates a new Netconf request based on the last received
        vlan id when the hasMore flag is true
        """

        arguments = {}

        if last_vlan_id != '':
            arguments = {'last_rcvd_vlan_id': last_vlan_id}

        return ('get_vlan_brief_rpc', arguments)

    @property
    def port_channels(self):
        """list[dict]: A list of dictionary items of port channels.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.202']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.channel_group(name='226/0/1',
            ...         int_type='tengigabitethernet',
            ...         port_int='1', channel_type='standard', mode='active')
            ...         result = dev.interface.port_channels
            ...         is_port_channel_exist = False
            ...         for port_chann in result:
            ...             if port_chann['interface-name']=='port-channel-1':
            ...                 for interfaces in port_chann['interfaces']:
            ...                     for keys, values in interfaces.items():
            ...                         if '226/0/1' in values:
            ...                             is_port_channel_exist = True
            ...                             break
            ...         output = dev.interface.remove_port_channel(
            ...         port_int='1')
            ...         assert is_port_channel_exist
        """

        result = []
        has_more = ''
        last_aggregator_id = ''
        while (has_more == '') or (has_more == 'true'):
            request_port_channel = self.get_port_chann_detail_request(
                last_aggregator_id)
            port_channel_result = self._callback(request_port_channel, 'get')

            has_more = util.find(port_channel_result.json, 'has-more')
            if has_more == 'true':
                for x in util.findlist(port_channel_result.json, 'lacp'):
                    last_aggregator_id = util.find(x, 'aggregator-id')

            for item in util.findlist(port_channel_result.json, 'lacp'):
                interface_list = []
                aggregator_id = util.findText(
                    item, 'aggregator-id')
                aggregator_type = util.findText(
                    item, 'aggregator-type')
                is_vlag = util.findText(item, 'isvlag')
                aggregator_mode = util.findText(
                    item, 'aggregator-mode')
                system_priority = util.findText(
                    item, 'system-priority')
                actor_system_id = util.findText(
                    item, 'actor-system-id')
                partner_oper_priority = util.findText(
                    item, 'partner-oper-priority')
                partner_system_id = util.findText(
                    item, 'partner-system-id')
                admin_key = util.findText(
                    item, 'admin-key')
                oper_key = util.findText(item, 'oper-key')
                partner_oper_key = util.findText(
                    item, 'partner-oper-key')
                rx_link_count = util.findText(
                    item, 'rx-link-count')
                tx_link_count = util.findText(
                    item, 'tx-link-count')
                individual_agg = util.findText(
                    item, 'individual-agg')
                ready_agg = util.findText(
                    item, 'ready-agg')
                for item1 in util.findlist(item, 'aggr-member'):
                    rbridge_id = util.findText(
                        item1, 'rbridge-id')
                    int_type = util.findText(
                        item1, 'interface-type')
                    int_name = util.findText(
                        item1, 'interface-name')
                    actor_port = util.findText(
                        item1, 'actor-port')
                    sync = util.findText(item1, 'sync')
                    port_channel_interface = {'rbridge-id': rbridge_id,
                                              'interface-type': int_type,
                                              'interface-name': int_name,
                                              'actor_port': actor_port,
                                              'sync': sync}
                    interface_list.append(port_channel_interface)
                results = {'interface-name': 'port-channel-' + aggregator_id,
                           'interfaces': interface_list,
                           'aggregator_id': aggregator_id,
                           'aggregator_type': aggregator_type,
                           'is_vlag': is_vlag,
                           'aggregator_mode': aggregator_mode,
                           'system_priority': system_priority,
                           'actor_system_id': actor_system_id,
                           'partner-oper-priority': partner_oper_priority,
                           'partner-system-id': partner_system_id,
                           'admin-key': admin_key,
                           'oper-key': oper_key,
                           'partner-oper-key': partner_oper_key,
                           'rx-link-count': rx_link_count,
                           'tx-link-count': tx_link_count,
                           'individual-agg': individual_agg,
                           'ready-agg': ready_agg}

                result.append(results)
        return result

    @staticmethod
    def get_node_value(node, node_name, urn):
        value = node.find(node_name % urn)
        if value is not None:
            return value.text
        else:
            return ''

    @staticmethod
    def get_port_chann_detail_request(last_aggregator_id):
        """ Creates a new Netconf request based on the last received
        aggregator id when the hasMore flag is true
        """

        arguments = {}

        if last_aggregator_id != '':
            arguments = {'last_aggregator_id': last_aggregator_id}

        return ('get_port_channel_detail_rpc', arguments)

    def vrrpe_spf_basic(self, **kwargs):
        """Set vrrpe short path forwarding to default.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            enable (bool): If vrrpe short path fowarding should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            vrid (str): vrrpe router ID.
            rbridge_id (str): rbridge-id for device. Only required when type
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrid` is not passed.
            ValueError: if `int_type`, `name`, `vrid` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.services.vrrpe(ip_version='6',
            ...         enable=True, rbridge_id='225')
            ...         output = dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89', vrid='1',
            ...         vip='2002:4818:f000:1ab:cafe:beef:1000:1/64',
            ...         output = dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89',
            ...         vrid='1', vip='2002:4818:f000:1ab:cafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         output = dev.services.vrrpe(enable=False,
            ...         rbridge_id='225')
            ...         output = dev.interface.vrrpe_spf_basic(int_type='ve',
            ...         name='89', vrid='1', rbridge_id='1')
        """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        version = kwargs.pop('version', 4)
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        vrid = kwargs.pop('vrid')

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        arguments = {int_type: name}
        if get:
            if version == 4:
                method_name = 'interface_%s_vrrp_extended_group_' \
                              'short_path_forwarding_get' % int_type
                vrid_name = 'vrrpe'
            else:
                method_name = 'interface_%s_ipv6_vrrp_extended_group_' \
                              'short_path_forwarding_get' % int_type
                vrid_name = 'vrrpv3e_group'
            if int_type == 've':
                if self.has_rbridge_id:
                    method_name = "rbridge_id_%s" % method_name
                    arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
                if version == 6:
                    vrid_name = 'vrrpv3e'
            arguments[vrid_name] = vrid
            config = (method_name, arguments)
            x = callback(config)

            basic = util.find(x.json, '$..basic')
            if basic and basic == 'true':
                return True
            else:
                return None

        if version == 4:
            method_name = 'interface_%s_vrrp_extended_group_' \
                          'short_path_forwarding_' % int_type
            vrid_name = 'vrrpe'
        else:
            method_name = 'interface_%s_ipv6_vrrp_extended_' \
                          'group_short_path_forwarding_' % int_type
            vrid_name = 'vrrpv3e_group'

        if int_type == 've':
            if self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name
                arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            if version == 6:
                vrid_name = 'vrrpv3e'

        arguments[vrid_name] = vrid
        if not enable:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%supdate" % method_name
            arguments['basic'] = True
        config = (method_name, arguments)
        return callback(config)

    def vrrpe_vrid(self, **kwargs):
        int_type = kwargs.pop('int_type').lower()
        version = kwargs.pop('version', 4)
        name = kwargs.pop('name', )
        get = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ve']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        arguments = {int_type: name}

        if get:
            if version == 4:
                method_name = 'interface_%s_vrrp_extended_group_get'\
                              % int_type
            else:
                method_name = 'interface_%s_ipv6_vrrp_extended_group_get'\
                              % int_type
            if int_type == 've' and self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name
                arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            config = (method_name, arguments)
            x = callback(config)
            vr_list = util.findlist(x.json, '$..vrrp-extended-group')
            result = []
            for vr in vr_list:
                vrid = util.find(vr, '$..vrid')
                result.append(vrid)

            return result

        vrid = kwargs.pop('vrid')
        if version == 4:
            method_name = 'interface_%s_vrrp_extended_group_' % int_type
            vrid_name = 'vrrpe'
        else:
            method_name = 'interface_%s_ipv6_vrrp_extended_group_' % int_type
            vrid_name = 'vrrpv3e_group'

        if int_type == 've':
            if self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name
                arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            if version == 6:
                vrid_name = 'vrrpv3e'

        arguments[vrid_name] = vrid
        if delete:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%screate" % method_name
        config = (method_name, arguments)
        return callback(config)

    def vrrpe_vip(self, **kwargs):
        """Set vrrpe VIP.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, ve, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, VE name etc).
            vrid (str): vrrpev3 ID.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, the VIP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            vip (str): IPv4/IPv6 Virtual IP Address.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vip` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vip` is invalid.

        Returns:
            Return value of `callback`.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output =dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89', rbridge_id = '1',
            ...         vrid='11', vip='10.0.1.10')
            ...         output = dev.interface.vrrpe_vip(get=True,
            ...         int_type='ve', name='89', rbridge_id = '1')
            ...         output =dev.interface.vrrpe_vip(delete=True,
            ...         int_type='ve', name='89', rbridge_id = '1',vrid='1',
            ...         vip='10.0.0.10')
        """
        int_type = kwargs.pop('int_type').lower()
        version = kwargs.pop('version', 4)
        name = kwargs.pop('name', )
        get = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ve']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        arguments = {int_type: name}

        if get:
            if version == 4:
                method_name = 'interface_%s_vrrp_extended_group_get' % \
                              int_type
                vrid_name = 'vrrpe'
            else:
                method_name = 'interface_%s_ipv6_vrrp_extended_group_get' %\
                              int_type
                vrid_name = 'vrrpv3e_group'

            if int_type == 've':
                if self.has_rbridge_id:
                    method_name = "rbridge_id_%s" % method_name
                    arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
                if version == 6:
                    vrid_name = 'vrrpv3e'
            result = []
            arguments['resource_depth'] = 3
            config = (method_name, arguments)
            x = callback(config)
            vr_list = util.findlist(x.json, '$..vrrp-extended-group')
            for vr in vr_list:
                vip = util.find(vr, '$..virtual-ipaddr')
                vrid = util.find(vr, '$..vrid')
                if vip:
                    result.append({'vrid': vrid, 'vip': vip})

            return result

        vrid = kwargs.pop('vrid')
        vip = kwargs.pop('vip', '')
        if vip != '':
            ipaddress = ip_interface(unicode(vip))
            version = ipaddress.version
        else:
            version = 4

        if version == 4:
            method_name = 'interface_%s_vrrp_extended_group_virtual_ip_' %\
                          int_type
            vrid_name = 'vrrpe'
        else:
            method_name = 'interface_%s_ipv6_vrrp_extended_group_virtual_ip_'\
                          % int_type
            vrid_name = 'vrrpv3e_group'

        if int_type == 've':
            if self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name
                arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            if version == 6:
                vrid_name = 'vrrpv3e'

        arguments[vrid_name] = vrid

        arguments['virtual_ip'] = str(ipaddress.ip)
        if delete:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%screate" % method_name
        config = (method_name, arguments)
        return callback(config)

    def vrrpe_vmac(self, **kwargs):
        """Set vrrpe virtual mac.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            vrid (str): vrrpev3 ID.
            enable (bool): If vrrpe virtual MAC should be enabled
                or disabled.Default:``True``.
            get (bool): Get config instead of editing config. (True, False)
            virtual_mac (str):Virtual mac-address in the format
            02e0.5200.00xx.
            rbridge_id (str): rbridge-id for device. Only required
            when type is 've'.
            callback (function): A function executed upon completion
            of the  method.  The only parameter passed to `callback`
            will be the ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vmac` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vmac` is invalid.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vmac` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vmac` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.services.vrrpe(enable=False,
            ...         rbridge_id='225')
            ...         output = dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89',vrid='1',
            ...         vip='2002:4818:f000:1ab:cafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         output = dev.services.vrrpe(enable=False,
            ...         rbridge_id='225')
            ...         output = dev.interface.vrrpe_vmac(int_type='ve',
            ...         name='89', vrid='1', rbridge_id='1',
            ...         virtual_mac='aaaa.bbbb.cccc')
        """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        enable = kwargs.pop('enable', True)
        version = kwargs.pop('version', 4)
        get = kwargs.pop('get', False)
        virtual_mac = kwargs.pop('virtual_mac', '02e0.5200.00xx')

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        arguments = {int_type: name}

        if get:
            if version == 4:
                method_name = 'interface_%s_vrrp_extended_group_' \
                              'get' % int_type
                vrid_name = 'vrrpe'
            else:
                method_name = 'interface_%s_ipv6_vrrp_extended_group_' \
                              'get' % int_type
                vrid_name = 'vrrpv3e_group'

            if int_type == 've':
                if self.has_rbridge_id:
                    method_name = "rbridge_id_%s" % method_name
                    arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
                if version == 6:
                    vrid_name = 'vrrpv3e'
            arguments[vrid_name] = vrid
            config = (method_name, arguments)
            x = callback(config)

            return util.find(x.json, '$..virtual-mac')

        if version == 4:
            method_name = 'interface_%s_vrrp_extended_group_virtual_mac_' \
                          % int_type
            vrid_name = 'vrrpe'
            vmac_name = 'virtual_mac'
        else:
            method_name = 'interface_%s_ipv6_vrrp_extended_group_virtual' \
                          '_mac_02e0_5200_00xx_' % int_type
            vrid_name = 'vrrpv3e_group'
            vmac_name = 'vmac'

        if int_type == 've':
            if self.has_rbridge_id:
                method_name = "rbridge_id_%s" % method_name
                arguments['rbridge_id'] = kwargs.pop('rbridge_id', 1)
            if version == 6:
                vrid_name = 'vrrpv3e'

        arguments[vrid_name] = vrid

        if not enable:
            method_name = "%sdelete" % method_name
        else:
            if version == 6:
                virtual_mac = True
            arguments[vmac_name] = virtual_mac
            method_name = "%supdate" % method_name
        config = (method_name, arguments)
        return callback(config)

    def ve_interfaces(self, **kwargs):
        """list[dict]: A list of dictionary items describing the operational
        state of ve interfaces along with the ip address associations.

        Args:
            rbridge_id (str): rbridge-id for device.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.ve_interfaces()
            ...     output = dev.interface.ve_interfaces(rbridge_id='1')
        """

        rbridge_id = kwargs.pop('rbridge_id', None)
        ip_result = []
        if self.has_rbridge_id:
            request_interface = (
                'get_ip_interface_rpc', {
                    'rbridge_id': rbridge_id})
        else:
            request_interface = (
                'get_ip_interface_rpc', {})

        interface_result = self._callback(request_interface, 'get')

        for interface in util.findlist(interface_result.json, '$..interface'):
            int_type = util.find(interface, '$..interface-type')
            int_name = util.find(interface, '$..interface-name')
            int_state = util.find(interface, '$..if-state')
            int_proto_state = util.find(interface, '$..line-protocol-state')
            ip_address = util.find(interface, '$..ipv4')
            if_name = util.find(interface, '$..if-name')
            results = {'interface-type': int_type,
                       'interface-name': int_name,
                       'if-name': if_name,
                       'interface-state': int_state,
                       'interface-proto-state': int_proto_state,
                       'ip-address': ip_address}
            ip_result.append(results)
        return ip_result

    def conversational_mac(self, **kwargs):
        """Enable conversational mac learning on vdx switches

        Args:
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the mac-learning. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.conversational_mac()
            ...     output = dev.interface.conversational_mac(get=True)
            ...     output = dev.interface.conversational_mac(delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        method_name = 'mac_address_table_learning_mode_'

        arguments = dict()
        if kwargs.pop('get', False):
            method_name = "%sget" % method_name
            config = (method_name, arguments)
            output = callback(config, handler='get_config')
            item = util.find(output.json, '$..learning-mode')

            if item is not None:
                return True
            return None
        if kwargs.pop('delete', False):
            method_name = "%sdelete" % method_name
        else:
            method_name = "%supdate" % method_name
            arguments['learning_mode'] = 'conversational'
        config = (method_name, arguments)
        return callback(config)

    def add_int_vrf(self, **kwargs):
        """
        Add L3 Interface in Vrf.

        Args:
            int_type:L3 interface type on which the vrf needs to be configured.
            name:L3 interface name on which the vrf needs to be configured.
            vrf_name: Vrf name with which the L3 interface needs to be
             associated.
            enable (bool): If vrf fowarding should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrf` is not passed.
                      (int_type need not be passed if get=True)
            ValueError: if `int_type`, `name`, `vrf` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.add_int_vrf(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/38',
            ...         vrf_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.add_int_vrf(
            ...         get=True,int_type='tengigabitethernet',
            ...         name='225/0/38',
            ...         vrf_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.add_int_vrf(
            ...         get=True, name='225/0/38',
            ...         rbridge_id='1')
            ...         output = dev.interface.add_int_vrf(
            ...         enable=False,int_type='tengigabitethernet',
            ...         name='225/0/39',
            ...         vrf_name='101',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        name = kwargs.pop('name')

        int_type = kwargs.pop('int_type').lower()
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        if self.has_rbridge_id:
            rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types
        valid_int_types.append('ve')

        vrf_args = {int_type: name}

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        method_name = 'interface_%s_vrf_forwarding_' % \
                      int_type
        if int_type == 've':
            if self.has_rbridge_id:
                method_name = 'rbridge_id_%s' % method_name
                vrf_args['rbridge_id'] = rbridge_id
            if not pyswitch.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')
        if get:
            method_name = '%sget' % method_name
            config = (method_name, vrf_args)
            x = callback(config, handler='get_config')

            return util.find(x.json, '$..forwarding')
        if not enable:
            method_name = '%sdelete' % method_name
            config = (method_name, vrf_args)
            return callback(config)

        vrf_name = kwargs.pop('vrf_name', 'Default')
        vrf_args['forwarding'] = vrf_name

        method_name = '%supdate' % method_name
        config = (method_name, vrf_args)
        return callback(config)

    def int_ipv4_arp_aging_timout(self, **kwargs):
        """
        Add "ip arp aging-time-out <>".

        Args:
            int_type:L3 Interface type on which the ageout time needs to be
             configured.
            name:L3 Interface name on which the ageout time needs to be
             configured.
            arp_aging_timeout: Arp age out time in <0..240>.
            enable (bool): If ip arp aging time out needs to be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device.
             Only required when type is 've'.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `arp_aging_timeout` is not passed.
            ValueError: if `int_type`, `name`, `arp_aging_timeout` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.int_ipv4_arp_aging_timout(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/38',
            ...         arp_aging_timeout='20',
            ...         rbridge_id='1')
            ...         output = dev.interface.int_ipv4_arp_aging_timout(
            ...         get=True,int_type='tengigabitethernet',
            ...         name='225/0/39',
            ...         arp_aging_timeout='40',
            ...         rbridge_id='9')
            ...         output = dev.interface.int_ipv4_arp_aging_timout(
            ...         enable=False,int_type='tengigabitethernet',
            ...         name='225/0/39',
            ...         arp_aging_timeout='40',
            ...         rbridge_id='9')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        arp_aging_timeout = kwargs.pop('arp_aging_timeout', '')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']

        ageout_args = dict()
        ageout_args[int_type] = name

        method_name = 'interface_%s_ip_arp_aging_timeout_' % int_type
        if int_type == 've':
            method_name = 'rbridge_id_%s' % method_name
            ageout_args['rbridge_id'] = rbridge_id
            if not pyswitch.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        if get:
            method_name = '%sget' % method_name
            config = (method_name, ageout_args)
            output = callback(config, handler='get_config')

            return util.find(output.json, '$..arp-aging-timeout')

        if not enable:
            method_name = '%sdelete' % method_name

        else:
            if (int(arp_aging_timeout) < 0) or (int(arp_aging_timeout) > 240):
                raise ValueError('arp_aging_timeout must be within 0-240')
            if int_type not in valid_int_types:
                raise ValueError('`int_type` must be one of: %s' %
                                 repr(valid_int_types))

            ageout_args['arp_aging_timeout'] = arp_aging_timeout
            method_name = '%supdate' % method_name

        config = (method_name, ageout_args)
        return callback(config)

    def overlay_gateway_name(self, **kwargs):
        """Configure Name of Overlay Gateway on vdx switches

        Args:
            gw_name: Name of Overlay Gateway
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the overlay gateway config.
                           (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `gw_name` is not passed.
            ValueError: if `gw_name` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.overlay_gateway_name(gw_name='Leaf')
            ...     output = dev.interface.overlay_gateway_name(get=True)
            ...     output = dev.interface.overlay_gateway_name(gw_name='Leaf',
            ...              delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)
        if not get_config:
            gw_name = kwargs.pop('gw_name')
            config = ('overlay_gateway_create', {'overlay_gateway': gw_name})

        if get_config:
            config = ('overlay_gateway_get', {})

            output = callback(config, handler='get_config')

            return util.find(output.json, '$..name')

        if kwargs.pop('delete', False):
            config = ('overlay_gateway_delete', {'overlay_gateway': gw_name})

        return callback(config)

    def overlay_gateway_activate(self, **kwargs):
        """Activates the Overlay Gateway Instance on VDX switches

        Args:
            gw_name: Name of Overlay Gateway
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the activate config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `gw_name` is not passed.
            ValueError: if `gw_name` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.overlay_gateway_activate(
            ...     gw_name='Leaf')
            ...     output = dev.interface.overlay_gateway_activate(
            ...     get=True)
            ...     output = dev.interface.overlay_gateway_activate(
            ...     gw_name='Leaf', delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)
        if not get_config:
            gw_name = kwargs.pop('gw_name')

            config = (
                'overlay_gateway_update', {
                    'overlay_gateway': gw_name, 'activate': True})

        if get_config:

            config = config = ('overlay_gateway_get', {'resource_depth': 2})
            output = callback(config, handler='get_config')

            activate = util.find(output.json, '$..activate')
            if activate:
                return True
            else:
                return None

        if kwargs.pop('delete', False):
            config = (
                'overlay_gateway_update', {
                    'overlay_gateway': gw_name, 'activate': False})

        return callback(config)

    def overlay_gateway_type(self, **kwargs):
        """Configure Overlay Gateway Type on vdx switches

        Args:
            gw_name: Name of Overlay Gateway
            gw_type: Type of Overlay Gateway(hardware-vtep/
                     layer2-extension/nsx)
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the overlay gateway type.
                           (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `gw_name`, 'gw_type' is not passed.
            ValueError: if `gw_name`, 'gw_type' is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...    output = dev.interface.overlay_gateway_type(gw_name='Leaf',
            ...              gw_type='layer2-extension')
            ...    output = dev.interface.overlay_gateway_name(get=True)
        """

        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)

        if not get_config:
            gw_name = kwargs.pop('gw_name')
            gw_type = kwargs.pop('gw_type')

            config = (
                'overlay_gateway_update', {
                    'overlay_gateway': gw_name, 'gw_type': gw_type})

        if get_config:
            config = config = ('overlay_gateway_get', {'resource_depth': 2})
            output = callback(config, handler='get_config')

            return util.find(output.json, '$..type')

        return callback(config)

    def overlay_gateway_loopback_id(self, **kwargs):
        """Configure Overlay Gateway ip interface loopback

        Args:
            gw_name: Name of Overlay Gateway  <WORD:1-32>
            loopback_id:  Loopback interface Id <NUMBER: 1-255>
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the overlay gateway loop back id.
                           (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `gw_name`, 'loopback_id' is not passed.
            ValueError: if `gw_name`, 'loopback_id' is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.overlay_gateway_loopback_id(
            ...     gw_name='Leaf', loopback_id='10')
            ...     output = dev.interface.overlay_gateway_loopback_id(
            ...     get=True)
            ...     output = dev.interface.overlay_gateway_loopback_id(
            ...     gw_name='Leaf', loopback_id='10', delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)
        gw_name = kwargs.pop('gw_name')

        if get_config:
            config = config = (
                'overlay_gateway_ip_interface_loopback_get', {
                    'overlay_gateway': gw_name, 'resource_depth': 2})
            output = callback(config, handler='get_config')

            return util.find(output.json, '$..loopback-id')

        if kwargs.pop('delete', False):
            config = (
                'overlay_gateway_ip_interface_loopback_delete',
                {'overlay_gateway': gw_name}
            )
        else:
            loopback_id = kwargs.pop('loopback_id')

            config = (
                'overlay_gateway_ip_interface_loopback_update',
                {'overlay_gateway': gw_name, 'loopback_id': loopback_id})

        return callback(config)

    def overlay_gateway_vlan_vni_auto(self, **kwargs):
        """Configure Overlay Gateway Vlan VNI mapping auto on VDX switches

        Args:
            gw_name: Name of Overlay Gateway
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete vlan to vni auto mapping. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `gw_name` is not passed.
            ValueError: if `gw_name` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.overlay_gateway_vlan_vni_auto(
            ...     gw_name='Leaf')
            ...     output = dev.interface.overlay_gateway_vlan_vni_auto(
            ...     get=True)
            ...     output = dev.interface.overlay_gateway_vlan_vni_auto(
            ...     gw_name='Leaf', delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)
        if not get_config:
            gw_name = kwargs.pop('gw_name')

            config = ('overlay_gateway_map_vlan_vni_update', {
                'overlay_gateway': gw_name, 'auto': True})

        if get_config:
            gw_name = kwargs.pop('gw_name')
            config = (
                'overlay_gateway_map_vlan_vni_get', {
                    'overlay_gateway': gw_name})
            output = callback(config, handler='get_config')
            if util.find(output.json, '$..auto') is not None:
                return True
            else:
                return None

        if kwargs.pop('delete', False):
            config = (
                'overlay_gateway_map_vlan_vni_delete', {
                    'overlay_gateway': gw_name})

        return callback(config)

    def overlay_gateway_attach_rbridge_id(self, **kwargs):
        """Configure Overlay Gateway attach rbridge id

        Args:
            gw_name: Name of Overlay Gateway  <WORD:1-32>
            rbridge_id:  Single or range of rbridge id to be added/removed
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the attached rbridge list
                           (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `gw_name`, 'rbridge_id' is not passed.
            ValueError: if `gw_name`, 'rbridge_id' is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.overlay_gateway_attach_rbridge_id(
            ...     gw_name='Leaf', rbridge_id='10')
            ...     output = dev.interface.overlay_gateway_attach_rbridge_id(
            ...     get=True)
            ...     output = dev.interface.overlay_gateway_attach_rbridge_id(
            ...     gw_name='Leaf', rbridge_id='1-2', delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        if not get_config:
            gw_name = kwargs.pop('gw_name')
            rbridge_id = kwargs.pop('rbridge_id')
            if delete is True:

                config = ('overlay_gateway_attach_rbridge_id_update', {
                    'overlay_gateway': gw_name, 'rb_remove': rbridge_id})
            else:
                config = ('overlay_gateway_attach_rbridge_id_update', {
                    'overlay_gateway': gw_name, 'rb_add': rbridge_id})
        if get_config:
            config = config = ('overlay_gateway_get', {'resource_depth': 4})
            output = callback(config, handler='get_config')

            return util.find(output.json, '$..attach..rbridge-id..add')

        return callback(config)

    def ipv6_link_local(self, **kwargs):
        """Configure ipv6 link local address on interfaces on vdx switches

        Args:
            int_type: Interface type on which the ipv6 link local needs to be
             configured.
            name: 'Ve' or 'loopback' interface name.
            rbridge_id (str): rbridge-id for device.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the mac-learning. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name` is not passed.
            ValueError: if `int_type`, `name` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...    output = dev.interface.ipv6_link_local(name='500',
            ...     int_type='ve',rbridge_id='1')
            ...    output = dev.interface.ipv6_link_local(get=True,name='500',
            ...     int_type='ve',rbridge_id='1')
            ...    output = dev.interface.ipv6_link_local(delete=True,
            ...     name='500', int_type='ve', rbridge_id='1')
        """

        int_type = kwargs.pop('int_type').lower()
        ve_name = kwargs.pop('name')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['loopback', 've']
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        link_args = dict(rbridge_id=rbridge_id)

        link_args[int_type] = ve_name
        method_name = 'rbridge_id_interface_%s_ipv6_address_' \
                      'use_link_local_only_update' % int_type
        get_method_name = 'rbridge_id_interface_%s_get' % int_type

        if kwargs.pop('get', False):
            config = (get_method_name, link_args)
            output = callback(config, handler='get_config')

            item = util.find(output.json,
                             '$..ipv6..address..use-link-local-only')

            if item:
                return True
            else:
                return None

        if kwargs.pop('delete', False):
            link_args['use_link_local_only'] = False
        else:
            link_args['use_link_local_only'] = True
        config = (method_name, link_args)
        return callback(config)

    def fabric_neighbor(self, **kwargs):
        """Set fabric neighbor discovery state.
        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            enabled (bool): Is fabric neighbor discovery enabled? (True, False)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, or `enabled` is not specified.
            ValueError: if `int_type`,`name`, or `enabled` is not a valid value
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.fabric_neighbor(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/40')
            ...         output = dev.interface.fabric_neighbor(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/40',
            ...         enabled=False)
            ...         output = dev.interface.fabric_neighbor(
            ...         get=True, int_type='tengigabitethernet',
            ...         name='225/0/40',
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        enabled = kwargs.pop('enabled', True)
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
        ]

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" %
                             repr(int_types))

        if not isinstance(enabled, bool):
            raise ValueError('`enabled` must be `True` or `False`.')

        fabric_isl_args = {int_type: name}

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError("`name` must match `^[0-9]{1,3}/[0-9]{1,3}/[0-9]"
                             "{1,3}$`")

        method_name = 'interface_%s_fabric_neighbor_discovery_' % int_type

        if not enabled:
            method_name = '%sdelete' % method_name
        elif kwargs.pop('get', False):
            method_name = '%sget' % method_name
            config = (method_name, fabric_isl_args)
            x = callback(config, handler='get_config')

            if util.find(x.json, "$..disable"):
                return None
            return True
        else:
            fabric_isl_args['disable'] = True
            method_name = '%supdate' % method_name
        config = (method_name, fabric_isl_args)
        return callback(config)

    def create_ve(self, **kwargs):
        """
        Add Ve Interface .
        Args:
            ve_name: Ve name with which the Ve interface needs to be
             created.
            enable (bool): If vrf fowarding should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            ValueError: if `ve_name` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.create_ve(
             ...         ve_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_ve(
            ...         get=True,
            ...         ve_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_ve(
            ...         get=True,
            ...         rbridge_id='1')
            ...         output = dev.interface.create_ve(
            ...         enable=False,
            ...         ve_name='101',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        ve_name = kwargs.pop('ve_name', '')

        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        ve_args = dict()
        if self.has_rbridge_id:
            rbridge_id = kwargs.pop('rbridge_id', '1')
            ve_args['rbridge_id'] = rbridge_id
        if get:
            enable = None

        method_name = self.method_prefix('interface_ve_')

        if get:
            config = (self.method_prefix('interface_ve_get'), ve_args)

            output = callback(config, handler='get_config')
            return util.findall(output.json, '$..name')

        ve_args['ve'] = ve_name
        if not enable:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%screate" % method_name
        config = (method_name, ve_args)
        return callback(config)

    def create_loopback(self, **kwargs):
        """
        Add loopback Interface .
        Args:
            lb_name: loopback name with which the Ve interface needs to be
             created.
            enable (bool): If vrf fowarding should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            ValueError: if `ve_name` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.create_loopback(
             ...         lb_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_loopback(
            ...         get=True,
            ...         rbridge_id='1')
            ...         output = dev.interface.create_loopback(
            ...         enable=False,
            ...         lb_name='101',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        lb_name = kwargs.pop('lb_name', '')

        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        ve_args = dict()
        if self.has_rbridge_id:
            rbridge_id = kwargs.pop('rbridge_id', '1')
            ve_args['rbridge_id'] = rbridge_id
        if get:
            enable = None

        method_name = self.method_prefix('interface_loopback_')

        if get:
            config = (self.method_prefix('interface_loopback_get'), ve_args)

            output = callback(config, handler='get_config')

            return util.findall(output.json, '$..id')

        ve_args['loopback'] = lb_name
        if not enable:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%screate" % method_name
        config = (method_name, ve_args)
        return callback(config)

    def create_portchannel(self, **kwargs):
        """
        Add loopback Interface .
        Args:
            name: loopback name with which the portChannel interface needs to
             created.
            enable (bool): If vrf fowarding should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            ValueError: if `ve_name` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.create_portchannel(
             ...         name='100')
            ...         output = dev.interface.create_portchannel(
            ...         get=True)
            ...         output = dev.interface.create_portchannel(
            ...         enable=False,
            ...         name='101')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        name = kwargs.pop('name', '')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        ve_args = dict()
        ve_args['port_channel'] = name
        if get:
            enable = None

        method_name = 'interface_port_channel_'

        if get:
            config = ('interface_port_channel_get', ve_args)

            output = callback(config, handler='get_config')
            return util.find(output.json, '$..Port-channel')

        if not enable:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%screate" % method_name
        config = (method_name, ve_args)
        return callback(config)
    """
    Version 7.0.1
    """

    def ip_unnumbered(self, **kwargs):
        """Configure an unnumbered interface.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
            name (str): Name of interface id.
                 (For interface: 1/0/5, 1/0/10 etc).
            delete (bool): True is the IP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            donor_type (str): Interface type of the donor interface.
            donor_name (str): Interface name of the donor interface.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `donor_type`, or `donor_name` is
                not passed.
            ValueError: if `int_type`, `name`, `donor_type`, or `donor_name`
                are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.interface.ip_address(int_type='loopback',
            ...        name='1', ip_addr='4.4.4.4/32', rbridge_id='230')
            ...        int_type = 'tengigabitethernet'
            ...        name = '230/0/20'
            ...        donor_type = 'loopback'
            ...        donor_name = '1'
            ...        output = dev.interface.disable_switchport(inter_type=
            ...        int_type, inter=name)
            ...        output = dev.interface.ip_unnumbered(int_type=int_type,
            ...       name=name, donor_type=donor_type, donor_name=donor_name)
            ...        output = dev.interface.ip_unnumbered(int_type=int_type,
            ...        name=name, donor_type=donor_type, donor_name=donor_name,
            ...        get=True)
            ...        output = dev.interface.ip_unnumbered(int_type=int_type,
            ...        name=name, donor_type=donor_type, donor_name=donor_name,
            ...        delete=True)
            ...        output = dev.interface.ip_address(int_type='loopback',
            ...        name='1', ip_addr='4.4.4.4/32', rbridge_id='230',
            ...        delete=True)
            ...        output = dev.interface.ip_unnumbered(int_type='hodor',
            ...       donor_name=donor_name, donor_type=donor_type, name=name)
            ...        # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ValueError
        """
        arguments = dict()

        arguments[kwargs['int_type']] = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)

        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet']

        if kwargs['int_type'] not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))

        if kwargs.pop('get', False):
            method_name = 'interface_%s_ip_unnumbered_ip_donor_' \
                          'interface_name_get' % kwargs[
                              'int_type']
            config = (method_name, arguments)
            op = callback(config, handler="get_config")

            donor_type = util.find(op.json, '$..ip-donor-interface-type')
            donor_name = util.find(op.json, '$..ip-donor-interface-name')
            return {'donor_type': donor_type, 'donor_name': donor_name}

        if kwargs.pop('delete', False):
            method_name = 'interface_%s_ip_unnumbered_ip_donor_i' \
                          'nterface_name_delete' % kwargs[
                              'int_type']
            config = (method_name, arguments)
        else:
            arguments['ip_donor_interface_name'] = kwargs.pop('donor_name')
            arguments['ip_donor_interface_type'] = kwargs.pop('donor_type')
            method_name = 'interface_%s_ip_unnumbered_ip_' \
                          'donor_interface_name_update' % kwargs[
                              'int_type']
            config = (method_name, arguments)
        return callback(config)

    def anycast_mac(self, **kwargs):
        """Configure an anycast MAC address.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
             mac (str): MAC address to configure
                 (example: '0011.2233.4455').
            delete (bool): True is the IP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `mac` is not passed.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.services.vrrp(ip_version='6',
            ...        enabled=True, rbridge_id='230')
            ...        output = dev.services.vrrp(enabled=True,
            ...        rbridge_id='230')
            ...        output = dev.services.vrrp(ip_version='6',
            ...        enabled=False, rbridge_id='230')
            ...        output = dev.services.vrrp(enabled=False,
            ...        rbridge_id='230')
            ...        output = dev.interface.anycast_mac(rbridge_id='230',
            ...        mac='0011.2233.4455')
            ...        output = dev.interface.anycast_mac(rbridge_id='230',
            ...        mac='0011.2233.4455', get=True)
            ...        output = dev.interface.anycast_mac(rbridge_id='230',
            ...        mac='0011.2233.4455', delete=True)
            ...        output = dev.services.vrrp(ip_version='6', enabled=True,
            ...        rbridge_id='230')
            ...        output = dev.services.vrrp(enabled=True,
            ...        rbridge_id='230')
        """
        callback = kwargs.pop('callback', self._callback)
        rbridge_id = kwargs['rbridge_id']

        arguments = {'rbridge_id': rbridge_id}
        if kwargs.pop('get', False):
            method_name = 'rbridge_id_ip_anycast_gateway_mac_get'
            config = (method_name, arguments)
            op = callback(config, handler="get_config")
            return util.find(op.json, '$..ip-anycast-gateway-mac')

        if kwargs.pop('delete', False):
            method_name = 'rbridge_id_ip_anycast_gateway_mac_delete'
            config = (method_name, arguments)
        else:
            arguments = {'rbridge_id': rbridge_id,
                         'ip_anycast_gateway_mac': kwargs.pop('mac')
                         }
            method_name = 'rbridge_id_ip_anycast_gateway_mac_update'
            config = (method_name, arguments)
        return callback(config)

    def bfd(self, **kwargs):
        """Configure BFD for Interface.

        Args:
            name (str): name of the interface to configure (230/0/1 etc)
            int_type (str): interface type (gigabitethernet etc)
            tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            rx (str): BFD receive interval in milliseconds (300, 500, etc)
            multiplier (str): BFD multiplier.  (3, 7, 5, etc)
            delete (bool): True if BFD configuration should be deleted.
                Default value will be False if not specified.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `tx`, `rx`, or `multiplier` is not passed.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.interface.bfd(name='230/0/4', rx='300',
            ...        tx='300', multiplier='3', int_type='tengigabitethernet')
            ...        output = dev.interface.bfd(name='230/0/4', rx='300',
            ...        tx='300', multiplier='3',
            ...        int_type='tengigabitethernet', get=True)
            ...        output = dev.interface.bfd(name='230/0/4', rx='300',
            ...        tx='300', multiplier='3',
            ...        int_type='tengigabitethernet', delete=True)
        """
        int_type = str(kwargs.pop('int_type').lower())

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet']

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))

        if kwargs.pop('get', False):
            method_name = 'interface_%s_bfd_interval_get' % int_type
            config = (method_name, {int_type: kwargs.pop('name')})
            x = callback(config, handler="get_config")
            tx = util.find(x.json, '$..min-tx')
            rx = util.find(x.json, '$..min-rx')
            multiplier = util.find(x.json, '$..multiplier')

            return {'tx': tx, 'rx': rx, 'multiplier': multiplier}

        if kwargs.pop('delete', False):
            arguments = {
                int_type: kwargs.pop('name')
            }
            method_name = 'interface_%s_bfd_interval_delete' % int_type
            config = (method_name, arguments)
        else:
            arguments = {
                int_type: kwargs.pop('name'),
                'min_tx': kwargs.pop('tx'),
                'min_rx': kwargs.pop('rx'),
                'multiplier': kwargs.pop('multiplier'),
            }
            method_name = 'interface_%s_bfd_interval_update' % int_type
            config = (method_name, arguments)
        return callback(config)

    def vrf(self, **kwargs):
        """Create a vrf.
        Args:
            vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): False, the vrf is created and True if its to
                be deleted (True, False). Default value will be False if not
                specified.
            rbridge_id (str): rbridge-id for device.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id`,`vrf_name` is not passed.
            ValueError: if `rbridge_id`, `vrf_name` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vrf(vrf_name=vrf1,
            ...         rbridge_id='225')
            ...         output = dev.interface.vrf(rbridge_id='225',
            ...         get=True)
            ...         output = dev.interface.vrf(vrf_name=vrf1,
            ...         rbridge_id='225',delete=True)

        """
        if self.has_rbridge_id:
            rbridge_id = kwargs['rbridge_id']
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []

        if not get_config:
            vrf_name = kwargs['vrf_name']
            if self.has_rbridge_id:
                vrf_args = dict(rbridge_id=rbridge_id, vrf=vrf_name)
            else:
                vrf_args = dict(vrf=vrf_name)
            config = (self.method_prefix('vrf_create'), vrf_args)

            if delete:
                config = (self.method_prefix('vrf_delete'), vrf_args)
            result = callback(config)

        elif get_config:
            if self.has_rbridge_id:
                vrf_args = dict(rbridge_id=rbridge_id)
            else:
                vrf_args = dict()
            config = (self.method_prefix('vrf_get'), vrf_args)
            output = callback(config, handler='get_config')
            for vrf_name in util.findall(output.json, '$..vrf-name'):
                if self.has_rbridge_id:
                    tmp = {'rbridge_id': rbridge_id, 'vrf_name': vrf_name}
                else:
                    tmp = {'vrf_name': vrf_name}
                result.append(tmp)
        return result

    def vrf_route_distiniguisher(self, **kwargs):
        """Configure Route distiniguisher.
        Args:
            rbridge_id (str): rbridge-id for device.
            vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
            rd (str): Route distiniguisher <ASN:nn or IP-address:nn>
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): False, the vrf rd is configured and True if its to
                be deleted (True, False). Default value will be False if not
                specified.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id`,`vrf_name`, 'rd' is not passed.
            ValueError: if `rbridge_id`, `vrf_name`, 'rd' is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         vrf_name=vrf1, rbridge_id='2', rd='10.0.1.1:101')
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         vrf_name=vrf1, rbridge_id='2', rd='100:101')
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         rbridge_id='2', get=True)
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         rbridge_id='2', vrf_name='vrf2', get=True)
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         vrf_name=vrf1, rbridge_id='2', rd='100:101',
            ...         delete=True)

        """
        if self.has_rbridge_id:
            rbridge_id = kwargs['rbridge_id']
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []

        if not get_config:
            vrf_name = kwargs['vrf_name']
            rd = kwargs['rd']
            rd_args = dict(vrf=vrf_name,
                           route_distiniguisher=rd)
            if self.has_rbridge_id:
                rd_args['rbridge_id'] = rbridge_id

            config = (self.method_prefix('vrf_update'), rd_args)

            if delete:
                config = (self.method_prefix('vrf_delete'), rd_args)

            result = callback(config)

        elif get_config:
            vrf_name = kwargs.pop('vrf_name', '')
            rd_args = dict(vrf=vrf_name)
            if self.has_rbridge_id:
                rd_args['rbridge_id'] = rbridge_id

            config = (self.method_prefix('vrf_get'), rd_args)
            output = callback(config, handler='get_config')

            vrfname = util.find(output.json, '$..vrf-name')
            rd = util.findText(output.json, '$..rd')
            if self.has_rbridge_id:
                tmp = {'rbridge_id': rbridge_id, 'vrf_name': vrfname,
                       'rd': rd}
            else:
                tmp = {'vrf_name': vrfname,
                       'rd': rd}
            result.append(tmp)
        return result

    def vrf_afi(self, **kwargs):
        """Configure Target VPN Extended Communities
           Args:
               rbridge_id (str): rbridge-id for device.
               vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
               afi (str): Address family (ip/ipv6).
               get (bool): Get config instead of editing config.
                           List all the details of
                           all afi under all vrf(True, False)

               delete (bool): True to delet the ip/ipv6 address family
                   Default value will be False if not specified.
               callback (function): A function executed upon completion of the
                   method.  The only parameter passed to `callback` will be the
                   ``ElementTree`` `config`.
           Returns:
               Return value of `callback`.
           Raises:
               KeyError: if `rbridge_id`,`vrf_name`, 'afi', 'rt', 'rt_value'
                         is not passed.
               ValueError: if `rbridge_id`, `vrf_name`, 'afi', 'rt', rt_value
                           is invalid.
           Examples:
               >>> import pyswitch.device
               >>> switches = ['10.24.39.211', '10.24.39.203']
               >>> auth = ('admin', 'password')
               >>> for switch in switches:
               ...    conn = (switch, '22')
               ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
               ...         output = dev.interface.vrf_vni(rbridge_id="1",
               ...         afi="ip", rt='import', rt_value='101:101',
               ...         vrf_name="vrf1")
               ...         output = dev.interface.vrf_vni(rbridge_id="1",
               ...         afi="ip", rt='import', rt_value='101:101',
               ...         vrf_name="vrf1",delete_rt=True)
               ...         output = dev.interface.vrf_vni(rbridge_id="1",
               ...         afi="ip", rt='import', rt_value='101:101',
               ...         vrf_name="vrf1",delete_afi=True)
               ...         output = dev.interface.vrf_vni(rbridge_id="1",
               ...         afi="ip", get=True)
               ...         output = dev.interface.vrf_vni(rbridge_id="1",
               ...         afi="ip", vrf_name="vrf2", get=True)

           """

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if not get_config:
            afi = kwargs['afi']
            afi = 'ipv4' if (afi == 'ip') else afi
            vrf_name = kwargs['vrf_name']
            rt_args = dict(vrf=vrf_name)
            if self.has_rbridge_id:
                rt_args['rbridge_id'] = kwargs['rbridge_id']

            if delete is True:
                method_name = self.method_prefix(
                    'vrf_address_family_%s_unicast_delete' % afi)
                config = (method_name, rt_args)

            else:
                method_name = self.method_prefix(
                    'vrf_address_family_%s_unicast_create' % afi)
                config = (method_name, rt_args)

            callback(config)

        elif get_config:
            vrf_name = kwargs.pop('vrf_name', '')

            rt_args = dict(vrf=vrf_name)
            if self.has_rbridge_id:
                rt_args['rbridge_id'] = kwargs['rbridge_id']

            method_name = self.method_prefix('vrf_get')
            config = (method_name, rt_args)
            output = callback(config, handler='get_config')

            ipv4_unicast = util.find(
                output.json, '$..address-family..ipv4..unicast')
            ipv4_unicast_enabled = True if ipv4_unicast else False
            ipv6_unicast = util.find(
                output.json, '$..address-family..ipv6..unicast')
            ipv6_unicast_enabled = True if ipv6_unicast else False
            return {'ipv4': ipv4_unicast_enabled, 'ipv6': ipv6_unicast_enabled}

    def vrf_afi_rt_evpn(self, **kwargs):
        """Configure Target VPN Extended Communities
        Args:
            rbridge_id (str): rbridge-id for device.
            vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
            rt (str): Route Target(import/export/both).
            rt_value (str): Route Target Value  ASN:nn Target
                            VPN Extended Community.
            afi (str): Address family (ip/ipv6).
            get (bool): Get config instead of editing config.
                        List all the details of
                        all afi under all vrf(True, False)
            delete_rt (bool): True to delete the route-target under
                              address family (True, False).
                              Default value will be False if not
                              specified.
            delete_afi (bool): True to delet the ip/ipv6 address family
                Default value will be False if not specified.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id`,`vrf_name`, 'afi', 'rt', 'rt_value'
                      is not passed.
            ValueError: if `rbridge_id`, `vrf_name`, 'afi', 'rt', rt_value
                        is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", rt='import', rt_value='101:101',
            ...         vrf_name="vrf1")
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", rt='import', rt_value='101:101',
            ...         vrf_name="vrf1",delete_rt=True)
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", rt='import', rt_value='101:101',
            ...         vrf_name="vrf1",delete_afi=True)
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", get=True)
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", vrf_name="vrf2", get=True)

        """
        rbridge_id = kwargs['rbridge_id']

        get_config = kwargs.pop('get', False)
        delete_rt = kwargs.pop('delete_rt', False)
        delete_afi = kwargs.pop('delete_afi', False)
        callback = kwargs.pop('callback', self._callback)
        result = []

        if not get_config:
            afi = kwargs['afi']
            afi = 'ipv4' if (afi == 'ip') else afi
            vrf_name = kwargs['vrf_name']
            rt = kwargs['rt']
            rt_value = kwargs['rt_value']
            rt_args = dict(rbridge_id=rbridge_id, vrf=vrf_name)

            if delete_afi is True:
                method_name = 'rbridge_id_vrf_' \
                              'address_family_%s_unicast_delete' % afi
                config = (method_name, rt_args)
            elif delete_rt is True:
                method_name = 'rbridge_id_vrf_address_family_%s_unicast_' \
                              'route_target_delete' % afi
                config = (method_name, rt_args)
            else:
                method_name = 'rbridge_id_vrf_address_family_%s_unicast_' \
                              'create' % afi
                config = (method_name, rt_args)
                callback(config)

                method_name = 'rbridge_id_vrf_address_family_%s_unicast_' \
                              'route_target_create' % afi
                rt_args['route_target'] = (rt, rt_value)
                config = (method_name, rt_args)

            result = callback(config)

        elif get_config:
            vrf_name = kwargs.pop('vrf_name', '')

            rt_args = dict(rbridge_id=rbridge_id, vrf=vrf_name)

            method_name = 'rbridge_id_vrf_get'
            config = (method_name, rt_args)
            output = callback(config, handler='get_config')

            for vrf_node in util.findall(output.json, '$..vrf'):
                vrf_name = util.find(vrf_node, '$..vrf-name')
                ipv4 = util.find(vrf_node, '$..ipv4')
                ipv4_action = util.findall(ipv4, '$..action')
                ipv4_rt = util.findall(ipv4, '$..target-community')

                if len(ipv4_action):
                    tmp = {'rbridge_id': rbridge_id, 'vrf_name': vrf_name,
                           'afi': 'ip', 'rt': ipv4_action, 'rtvalue': ipv4_rt}
                    result.append(tmp)

                ipv6 = util.find(vrf_node, '$..ipv6')
                ipv6_action = util.findall(ipv6, '$..action')
                ipv6_rt = util.findall(ipv6, '$..target-community')

                if len(ipv6_action):
                    tmp = {
                        'rbridge_id': rbridge_id,
                        'vrf_name': vrf_name,
                        'afi': 'ipv6',
                        'rt': ipv6_action,
                        'rtvalue': ipv6_rt}
                    result.append(tmp)

        return result

    def conversational_arp(self, **kwargs):
        """Enable conversational arp learning on VDX switches

        Args:
            rbridge_id (str): rbridge-id for device.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the conversation arp learning.
                          (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id` is not passed.
            ValueError: if `rbridge_id` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.conversational_arp(rbridge_id="1")
            ...     output = dev.interface.conversational_arp(rbridge_id="1",
                             get=True)
            ...     output = dev.interface.conversational_arp(rbridge_id="1",
                             delete=True)
        """

        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)

        arp_args = dict(rbridge_id=rbridge_id)

        if kwargs.pop('get', False):
            method_name = 'rbridge_id_get'
            config = (method_name, arp_args)
            output = callback(config, handler='get_config')

            item = util.find(output.json, '$..aging-mode')
            conversational = util.find(item, '$..conversational')
            if conversational is not None:
                return True
            else:
                return None
        if kwargs.pop('delete', False):
            method_name = 'rbridge_id_host_table_aging_mode_' \
                          'conversational_update'
            arp_args['conversational'] = False
        else:
            method_name = 'rbridge_id_host_table_aging_mode_' \
                          'conversational_update'
            arp_args['conversational'] = True
        config = (method_name, arp_args)
        return callback(config)

    def arp_suppression(self, **kwargs):
        """
        Enable Arp Suppression on a Vlan.

        Args:
            name:Vlan name on which the Arp suppression needs to be enabled.
            enable (bool): If arp suppression should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `name` is not passed.
            ValueError: if `name` is invalid.
           output2 = dev.interface.arp_suppression(name='89')
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.arp_suppression(
            ...         name='89')
            ...         output = dev.interface.arp_suppression(
            ...         get=True,name='89')
            ...         output = dev.interface.arp_suppression(
            ...         enable=False,name='89')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        name = kwargs.pop('name')
        enable = kwargs.pop('enable', True)

        callback = kwargs.pop('callback', self._callback)
        get = kwargs.pop('get', False)
        arp_args = dict(vlan=name)
        if name:
            if not pyswitch.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")

        if get:
            method_name = 'vlan_get'
            config = (method_name, arp_args)

            output = callback(config, handler='get_config')

            item = util.find(output.json, '$..suppress-arp')
            enable_item = util.find(item, '$..enable')

            if enable_item is not None:
                return True
            else:
                return None
        if not enable:
            method_name = 'interface_vlan_suppress_arp_update'
            arp_args['suppress_arp_enable'] = False
        else:
            method_name = 'interface_vlan_suppress_arp_update'
            arp_args['suppress_arp_enable'] = True

        config = (method_name, arp_args)
        return callback(config)

    def create_evpn_instance(self, **kwargs):
        """
        Add evpn instance.

        Args:
            evpn_instance_name: Instance name for evpn
            enable (bool): If evpn instance needs to be configured
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if 'evpn_instance_name' is not passed.
            ValueError: if 'evpn_instance_name' is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.create_evpn_instance(
            ...         evpn_instance_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_evpn_instance(
            ...         get=True,
            ...         evpn_instance_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_evpn_instance(
            ...         enable=False,
            ...         evpn_instance_name='101',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_evpn_instance(
            ...         get=True,
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        evpn_args = dict(rbridge_id=rbridge_id)

        if evpn_instance_name != '':
            evpn_args['evpn_instance'] = evpn_instance_name

        if get:
            enable = None

        method_name = 'rbridge_id_evpn_instance_create'
        evpn_args['rbridge_id'] = rbridge_id
        config = (method_name, evpn_args)

        if get:
            method_name = 'rbridge_id_evpn_instance_get'
            config = (method_name, evpn_args)
            output = callback(config, handler='get_config')

            instance_name = util.find(output.json, '$..instance-name')
            ignore_as = util.find(output.json, '$..ignore-as')
            duplicate_mac_timer_value = util.find(
                output.json, '$..duplicate-mac-timer-value')
            max_count = util.find(output.json, '$..max-count')
            auto = util.find(output.json, '$..rd..auto')
            return {'instance_name': instance_name, 'ignore_as': ignore_as,
                    'duplicate_mac_timer_value': duplicate_mac_timer_value,
                    'max_count': max_count, 'rd_auto': auto}
        if not enable:
            method_name = 'rbridge_id_evpn_instance_delete'
            config = (method_name, evpn_args)
        return callback(config)

    def evpn_instance_rd_auto(self, **kwargs):
        """
        Add RD auto under EVPN instance.

        Args:
            rbridge_id: Rbrdige id .
            instance_name: EVPN instance name.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output=dev.interface.evpn_instance_rd_auto(
            ...         evpn_instance_name='100',
            ...         rbridge_id='1')
         """
        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        # enable = kwargs.pop('enable', True)
        # get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)

        evpn_args = dict(rbridge_id=rbridge_id)

        method_name = 'rbridge_id_evpn_instance_rd_auto_update'
        evpn_args['rbridge_id'] = rbridge_id
        evpn_args['evpn_instance'] = evpn_instance_name
        evpn_args['auto'] = True
        config = (method_name, evpn_args)

        return callback(config)

    def evpn_instance_rt_both_ignore_as(self, **kwargs):
        """
        Add evpn instance route target ignore AS.

        Args:
            evpn_instance_name: Instance name for evpn
            enable (bool): If target community needs to be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if 'evpn_instance_name' is not passed.
            ValueError: if 'evpn_instance_name' is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...conn = (switch, '22')
            ...with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ... output=dev.interface.evpn_instance_rt_both_ignore_as(
            ... evpn_instance_name='100',
            ... rbridge_id='1')
            ... output=dev.interface.evpn_instance_rt_both_ignore_as(
            ... get=True,
            ... evpn_instance_name='100',
            ... rbridge_id='1')
            ... output=dev.interface.evpn_instance_rt_both_ignore_as(
            ... enable=False,
            ... evpn_instance_name='101',
            ... rbridge_id='1')
            ... output=dev.interface.evpn_instance_rt_both_ignore_as(
            ... get=True,
            ... rbridge_id='1')
            ...   # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        evpn_args = dict(rbridge_id=rbridge_id)
        if get:
            enable = None

        if get:
            evpn_args['resource_depth'] = 3
            method_name = 'rbridge_id_evpn_instance_get'
            config = (method_name, evpn_args)
            output = callback(config, handler='get_config')
            evpn_instance_item = util.find(output.json, '$..ignore-as')
            return evpn_instance_item

        evpn_args['import_'] = 'auto'
        evpn_args['evpn_instance'] = evpn_instance_name

        if not enable:
            method_name = 'rbridge_id_evpn_instance_route_target_import_delete'

        else:
            method_name = 'rbridge_id_evpn_instance_route_target_import_create'
            config = (method_name, evpn_args)
            callback(config)

            method_name = 'rbridge_id_evpn_instance_route_target_import_update'
            evpn_args['ignore_as'] = True

        config = (method_name, evpn_args)
        return callback(config)

    def evpn_instance_duplicate_mac_timer(self, **kwargs):
        """
        Add "Duplicate MAC timer value" under evpn instance.

        Args:
            evpn_instance_name: Instance name for evpn
            duplicate_mac_timer_value: Duplicate MAC timer value.
            enable (bool): If target community needs to be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if 'evpn_instance_name' is not passed.
            ValueError: if 'evpn_instance_name' is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        output=dev.interface.evpn_instance_duplicate_mac_timer(
            ...         evpn_instance_name='100',
            ...         duplicate_mac_timer_value='10'
            ...         rbridge_id='1')
            ...        output=dev.interface.evpn_instance_duplicate_mac_timer(
            ...         get=True,
            ...         evpn_instance_name='100',
            ...         duplicate_mac_timer_value='10'
            ...         rbridge_id='1')
            ...        output=dev.interface.evpn_instance_duplicate_mac_timer(
            ...         enable=False,
            ...         evpn_instance_name='101',
            ...         duplicate_mac_timer_value='10'
            ...         rbridge_id='1')
            ...        output=dev.interface.evpn_instance_duplicate_mac_timer(
            ...         get=True,
            ...         evpn_instance_name='101',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        duplicate_mac_timer_value = kwargs.pop('duplicate_mac_timer_value',
                                               '180')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)

        evpn_args = dict(rbridge_id=rbridge_id)
        if get:
            enable = None

        if get:
            evpn_args['resource_depth'] = 3
            method_name = 'rbridge_id_evpn_instance_get'
            config = (method_name, evpn_args)
            output = callback(config, handler='get_config')
            evpn_instance_item = util.find(
                output.json, '$..duplicate-mac-timer-value')
            return evpn_instance_item

        evpn_args['evpn_instance'] = evpn_instance_name

        if not enable:
            method_name = 'rbridge_id_evpn_instance_' \
                          'duplicate_mac_timer_delete'
            config = (method_name, evpn_args)
        else:

            evpn_args['duplicate_mac_timer_value'] = duplicate_mac_timer_value
            method_name = 'rbridge_id_evpn_instance_' \
                          'duplicate_mac_timer_update'
            config = (method_name, evpn_args)

        return callback(config)

    def evpn_instance_mac_timer_max_count(self, **kwargs):
        """
        Add "Duplicate MAC max count" under evpn instance.

        Args:
            evpn_instance_name: Instance name for evpn
            max_count: Duplicate MAC max count.
            enable (bool): If target community needs to be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if 'evpn_instance_name' is not passed.
            ValueError: if 'evpn_instance_name' is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        output=dev.interface.evpn_instance_mac_timer_max_count(
            ...         evpn_instance_name='100',
            ...         max_count='10'
            ...         rbridge_id='1')
            ...        output=dev.interface.evpn_instance_mac_timer_max_count(
            ...         get=True,
            ...         evpn_instance_name='100',
            ...         max_count='10'
            ...         rbridge_id='1')
            ...        output=dev.interface.evpn_instance_mac_timer_max_count(
            ...         enable=False,
            ...         evpn_instance_name='101',
            ...         max_count='10'
            ...         rbridge_id='1')
            ...        output=dev.interface.evpn_instance_mac_timer_max_count(
            ...         get=True,
            ...         evpn_instance_name='101',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        max_count = kwargs.pop('max_count', 5)
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)

        evpn_args = dict(rbridge_id=rbridge_id)
        if get:
            enable = None

        if get:
            evpn_args['resource_depth'] = 3
            method_name = 'rbridge_id_evpn_instance_get'
            config = (method_name, evpn_args)
            output = callback(config, handler='get_config')
            evpn_instance_item = util.find(output.json, '$..max-count')
            return evpn_instance_item

        evpn_args['evpn_instance'] = evpn_instance_name

        if not enable:
            method_name = 'rbridge_id_evpn_instance_' \
                          'duplicate_mac_timer_delete'
            config = (method_name, evpn_args)
        else:
            evpn_args['max_count'] = max_count
            method_name = 'rbridge_id_evpn_instance_' \
                          'duplicate_mac_timer_update'
            config = (method_name, evpn_args)

        return callback(config)

    def mac_move_detect_enable(self, **kwargs):
        """Enable mac move detect enable on vdx switches
        Args:
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the mac-move-detect-enable.
                           (True, False)
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
            ...     output = dev.interface.mac_move_detect_enable()
            ...     output = dev.interface.mac_move_detect_enable(get=True)
            ...     output = dev.interface.mac_move_detect_enable(delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        method_name = 'mac_address_table_mac_move_action_'

        if kwargs.pop('get', False):
            method_name = '%sget' % method_name
            output = callback((method_name, {}), handler='get_config')
            item = util.find(output.json, '$..detect')
            if item is not None:
                return True
            else:
                return None
        args = {}
        if kwargs.pop('delete', False):
            method_name = '%supdate' % method_name
            args['mac_move_detect_enable'] = False
        else:
            method_name = '%supdate' % method_name
            args['mac_move_detect_enable'] = True

        return callback((method_name, args))

    def mac_move_limit(self, **kwargs):
        """Configure mac move limit on vdx switches
        Args:
            mac_move_limit: set the limit of mac move limit
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the mac move limit.(True, False)
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
            ...     output = dev.interface.mac_move_limit()
            ...     output = dev.interface.mac_move_limit(get=True)
            ...     output = dev.interface.mac_move_limit(delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        method_name = 'mac_address_table_mac_move_action_'
        if kwargs.pop('get', False):
            method_name = '%sget' % method_name
            output = callback((method_name, {}), handler='get_config')
            item = util.find(output.json, '$..limit')
            if item is not None:
                return item
            else:
                return '20'
        args = {}
        if kwargs.pop('delete', False):
            method_name = '%supdate' % method_name
            args['mac_move_limit'] = '20'
        else:
            mac_move_limit = kwargs.pop('mac_move_limit')
            method_name = '%supdate' % method_name
            args['mac_move_limit'] = mac_move_limit

        return callback((method_name, args))

    def port_channel_speed(self, **kwargs):
        """Set/get/delete speed in a port channel.

        Args:
            name (str): Port-channel number. (1, 5, etc)
            po_speed (str): speed
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `po_speed` is not specified.
            ValueError: if `name` is not a valid value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.port_channel_speed(
            ...         name='1', po_speed='40000')
            ...         output = dev.interface.port_channel_speed(
            ...         name='1', get=True)
            ...         output = dev.interface.port_channel_speed(
            ...         name='1', delete=True)
            Traceback (most recent call last):
            KeyError
        """
        name = str(kwargs.pop('name'))

        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if kwargs.pop('get', False):
            args = dict()
            args['port_channel'] = name
            config = ('interface_port_channel_speed_get', args)

            output = callback(config, handler='get_config')
            return util.find(output.json, '$..speed')

        if not pyswitch.utilities.valid_interface('port_channel', name):
            raise ValueError("`name` must match `^[0-9]{1,3}${1,3}$`")

        if delete:
            config = ('interface_port_channel_speed_delete',
                      {'port_channel': name})
        else:
            po_speed = str(kwargs.pop('po_speed'))
            config = ('interface_port_channel_speed_update',
                      {'port_channel': name, 'po_speed': po_speed})
        return callback(config)
