import pyswitch.utilities
from pyswitch.utilities import Util
from pyswitch.exceptions import InvalidVlanId
from pyswitch.os.base.interface import Interface as BaseInterface


class Interface(BaseInterface):
    """
      The Interface class holds all the actions assocaiated with the Interfaces
      of a NOS device.

      Attributes:
          None
      """

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

        super(Interface, self).__init__(callback)

    @property
    def valid_int_types(self):

        return [
            'ethernet',
            'port_channel'
        ]

    @property
    def valid_intp_types(self):
        return [
            'ethernet'

        ]

    @property
    def l2_mtu_const(self):
        minimum_mtu = 1548
        maximum_mtu = 9216
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_mtu_const(self):
        minimum_mtu = 1300
        maximum_mtu = 9194
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_ipv6_mtu_const(self):
        minimum_mtu = 1300
        maximum_mtu = 9194
        return (minimum_mtu, maximum_mtu)

    @property
    def has_rbridge_id(self):
        return False

    def fabric_isl(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def fabric_trunk(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def ip_anycast_gateway(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def spanning_tree_state(self, **kwargs):
        """Set Spanning Tree state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, vlan, port_channel etc).
            name (str): Name of interface or VLAN id.
                (For interface: 1/0/5, 1/0/10 etc).
                (For VLANs 0, 1, 100 etc).
                (For Port Channels 1, 100 etc).
            enabled (bool): Is Spanning Tree enabled? (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `enabled` is not passed.
            ValueError: if `int_type`, `name`, or `enabled` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         enabled = True
            ...         int_type = 'tengigabitethernet'
            ...         name = '225/0/37'
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         enabled = False
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         int_type = 'vlan'
            ...         name = '102'
            ...         enabled = False
            ...         output = dev.interface.add_vlan_int(name)
            ...         output = dev.interface.enable_switchport(
            ...             int_type, name)
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         enabled = False
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         output = dev.interface.del_vlan_int(name)
            ...         int_type = 'port_channel'
            ...         name = '2'
            ...         enabled = False
            ...         output = dev.interface.channel_group(name='225/0/20',
            ...                              int_type='tengigabitethernet',
            ...                              port_int=name,
            ...                              channel_type='standard',
            ...                              mode='active')
            ...         output = dev.interface.enable_switchport(
            ...             int_type, name)
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         enabled = False
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         output = dev.interface.remove_port_channel(
            ...             port_int=name)
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        get = kwargs.pop('get', False)

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))
        state_args = dict()
        state_args[int_type] = name
        if get:
            method_name = 'interface_%s_spanning_tree_get' % int_type
            if int_type == 'vlan':
                method_name = 'vlan_spanning_tree_get'
            config = (method_name, state_args)
            x = callback(config, handler='get_config')
            util = Util(x.data)
            shutdown_status = util.find(util.root, './/shutdown')
            if shutdown_status and shutdown_status == 'false':
                return True
            return False

        enabled = kwargs.pop('enabled')
        if not isinstance(enabled, bool):
            raise ValueError('%s must be `True` or `False`.' % repr(enabled))

        if int_type == 'vlan':
            if not pyswitch.utilities.valid_vlan_id(name):
                raise InvalidVlanId(
                    '%s must be between 0 to 8191.' % int_type)
            shutdown_name = 'stp_shutdown'
            method_name = 'interface_%s_spanning_tree_update' % int_type

        else:
            if not pyswitch.utilities.valid_interface(int_type, name):
                raise ValueError('`name` must be in the format of x/y/z for '
                                 'physical interfaces or x for port channel.')
            shutdown_name = 'shutdown'
            method_name = 'interface_%s_spanning_tree_update' % int_type

        if enabled:
            state_args[shutdown_name] = False
        else:
            state_args[shutdown_name] = True
        try:
            config = (method_name, state_args)
            return callback(config)
        # TODO: Catch existing 'no shut'
        # This is in place because if the interface spanning tree is already
        # up,`ncclient` will raise an error if you try to admin up the
        # interface again.
        # TODO: add logic to shutdown STP at protocol level too.
        except AttributeError:
            return None

    def vlan_router_ve(self, **kwargs):
        """Configure/get/delete router interface ve on a vlan.

        Args:
            vlan_id (str): Vlan number.
            ve_config (str) : router ve interface
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the router ve on the vlan.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `vlan_id`  is not specified.
            ValueError: if `vlan_id` is not a valid value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vlan_router_ve(
            ...         get=True, vlan_id='100')
            ...         output = dev.interface.vlan_router_ve(
            ...         delete=True, vlan_id='100')
            ...         output = dev.interface.vlan_router_ve(
            ...         vlan_id='100', ve_config='200')
            Traceback (most recent call last):
            KeyError
        """
        vlan = kwargs.pop('vlan_id')
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if not pyswitch.utilities.valid_vlan_id(vlan):
            raise InvalidVlanId(
                '%s must be between 0 to 8191.' % vlan)
        if delete:
            ve_args = dict(vlan=vlan)
            config = (self.method_prefix('vlan_router_interface_ve_delete'),
                                         ve_args)
            return callback(config)

        if not get_config:
            ve_config = kwargs.pop('ve_config')
            ve_args = dict(vlan=vlan, ve_config=ve_config)
            config = (self.method_prefix('vlan_router_interface_ve_update'),
                                         ve_args)
            result = callback(config)
        elif get_config:
            ve_args = dict(vlan=vlan)
            config = (self.method_prefix('vlan_router_interface_ve_get'),
                                         ve_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/Ve')
        return result
