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
            'loopback',
            've'
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

    def bridge_domain(self, **kwargs):
        """Configure/get/delete bridge-domain.

        Args:
            bridge_domain (str): bridge domain number.
            bridge_domain_service_type (str): service type. ('p2mp', 'p2p')
            vc_id_num (str): VC Id under the VPLS Instance
            statistics (bool): Configure Statistics. (True, False)
            pw_profile_name (str): Pw-profile name (Max Size - 64).
            bpdu_drop_enable (bool): Drop BPDU packets. (True, False)
            local_switching (bool): Configure local switching. (True, False)
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the bd.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `bridge_domain`  is not specified.
            KeyError: if `vc_id_num` is not speciied.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.bridge_domain(
            ...         get=True, bridge_domain='100')
            ...         output = dev.interface.bridge_domain(
            ...         delete=True, bridge_domain='100')
            ...         output = dev.interface.bridge_domain(
            ...         bridge_domain='100', vc_id_num='200')
            Traceback (most recent call last):
            KeyError
        """

        bridge_domain = kwargs.pop('bridge_domain')
        bridge_domain_service = kwargs.pop('bridge_domain_service_type', 'p2mp')
        statistics = kwargs.pop('statistics', None)
        pw_profile_name = kwargs.pop('pw_profile_name', None)
        bpdu_drop_enable = kwargs.pop('bpdu_drop_enable', None)
        local_switching = kwargs.pop('local_switching', None)

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if bridge_domain_service not in ['p2mp', 'p2p']:
            raise ValueError("`bridge_domain_service_type` must match one of them "
                             "`p2mp, p2p`")

        bd_args = dict(bridge_domain=(bridge_domain, bridge_domain_service))
        if delete:
            config = (self.method_prefix('bridge_domain_delete'),
                                         bd_args)
            return callback(config)

        if not get_config:
            vc_id_num = kwargs.pop('vc_id_num')
            bd_args = dict(bridge_domain=(bridge_domain,bridge_domain_service),
                           vc_id_num=vc_id_num, statistics=statistics,
                           pw_profile_name=pw_profile_name,
                           bpdu_drop_enable=bpdu_drop_enable,
                           local_switching=local_switching)
            config = (self.method_prefix('bridge_domain_create'),
                                         bd_args)
            result = callback(config)
        elif get_config:
            config = (self.method_prefix('bridge_domain_get'),
                                         bd_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            bridge_domain_id = util.find(util.root, './/bridge-domain-id')
            if bridge_domain_id is not None:
                bridge_domain_type = util.find(util.root, './/bridge-domain-type')
                vc_id = util.find(util.root, './/vc-id')
                pw_profile =  util.find(util.root, './/pw-profile')
                statistics = util.find(util.root, './/statistics')
                bpdu_drop_enable = util.find(util.root, './/bpdu-drop-enable')
                local_switching = util.find(util.root, './/local-switching')
                result = {'bridge_domain_id': bridge_domain_id,
                          'bridge_domain_type' : bridge_domain_type,
                          'vc_id': vc_id, 'pw_profile': pw_profile,
                          'statistics': statistics,
                          'bpdu_drop_enable': bpdu_drop_enable,
                          'local_switching': local_switching}
            else:
                result = None
        return result

    def bridge_domain_peer(self, **kwargs):
        """Configure/get/delete PW Peer related configuration.

        Args:
            bridge_domain (str): bridge domain number.
            bridge_domain_service_type (str): service type. ('p2mp', 'p2p')
            peer_ip (str): PW Peer Ip for remote peer
            load_balance (bool): load-balance. (True, False)
            cos (str): cos value. <cos value: 0..7>
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete peer_ips on bd.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `bridge_domain`  is not specified.
            KeyError: if `peer_ip` is not speciied.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.bridge_domain_peer(
            ...         get=True, bridge_domain='100', peer_ip='1.1.1.1')
            ...         output = dev.interface.bridge_domain_peer(
            ...         delete=True, bridge_domain='100', peer_ip='1.1.1.1')
            ...         output = dev.interface.bridge_domain_peer(
            ...         bridge_domain='100', peer_ip='1.1.1.1', cos='1',
            ...         load_balance=True)
            Traceback (most recent call last):
            KeyError
        """

        bridge_domain = kwargs.pop('bridge_domain')
        bridge_domain_service = kwargs.pop('bridge_domain_service_type', 'p2mp')
        load_balance = kwargs.pop('load_balance', None)
        cos = kwargs.pop('cos', None)
        peer_ip = str(kwargs.pop('peer_ip'))

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if bridge_domain_service not in ['p2mp', 'p2p']:
            raise ValueError("`bridge_domain_service_type` must match one of them "
                             "`p2mp, p2p`")
        if cos is not None and cos not in range(0,8):
            raise ValueError("`cos' value should be in-between `0-7`")

        bd_args = dict(bridge_domain=(bridge_domain,bridge_domain_service),
                       peer=(peer_ip, load_balance, cos))
        if delete:
            config = (self.method_prefix('bridge_domain_peer_delete'),
                                         bd_args)
            return callback(config)

        if not get_config:
            config = (self.method_prefix('bridge_domain_peer_create'),
                                         bd_args)
            result = callback(config)
        elif get_config:
            config = (self.method_prefix('bridge_domain_peer_get'),
                                         bd_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            peer_ip = util.find(util.root, './/peer-ip')
            if peer_ip is not None:
                load_balance = util.find(util.root, './/load_balance')
                cos = util.find(util.root, './/cos')
                lsp = util.find(util.root, './/lsp')
                result = {'peer_ip': peer_ip, 'load_balance': load_balance,
                          'cos': cos, 'lsp': lsp}
            else:
                result = None
        return result

    def bridge_domain_logical_interface(self, **kwargs):
        """Configure/get/delete logical-interface on a bridge-domain.
        Args:
            bridge_domain (str): bridge domain number.
            bridge_domain_service_type (str): service type. ('p2mp', 'p2p')
            intf_type (str): Type of interface. ['ethernet', 'port_channel']
            lif_name  (str): Logical Interface name.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete single/all LIFs on a bd.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `bridge_domain` or `lif_name` is not specified.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.bridge_domain_logical_interface(
            ...         get=True, bridge_domain='100', lif_name='1/34.1')
            ...         output = dev.interface.bridge_domain_logical_interface(
            ...         delete=True, bridge_domain='100', lif_name='1/34.1')
            ...         output = dev.interface.bridge_domain_logical_interface(
            ...         bridge_domain='100', lif_name='1/34.1')
            ...         output = dev.interface.bridge_domain_logical_interface(
            ...         delete=True, bridge_domain='100')
            Traceback (most recent call last):
            KeyError
        """

        bridge_domain = kwargs.pop('bridge_domain')
        bridge_domain_service = kwargs.pop('bridge_domain_service_type', 'p2mp')
        intf_type = kwargs.pop('intf_type', 'ethernet')
        lif_name = kwargs.pop('lif_name', None)

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if bridge_domain_service not in ['p2mp', 'p2p']:
            raise ValueError("`bridge_domain_service_type` must "
                             "match one of them "
                             "`p2mp, p2p`")
        if intf_type not in ['ethernet', 'port_channel']:
            raise ValueError("`intf_ype` must match one of them "
                             "`ethernet, port_channel`")
        if intf_type == 'port_channel':
            bd_args = dict(bridge_domain=\
                          (bridge_domain,bridge_domain_service))
        else:
            bd_args = dict(bridge_domain=\
                          (bridge_domain,bridge_domain_service))

        if lif_name is not None and intf_type == 'port_channel':
            bd_args.update(port_channel=lif_name)
        elif lif_name is not None and intf_type == 'ethernet':
            bd_args.update(ethernet=lif_name)

        if delete:
            if lif_name is None:
                method_name = 'bridge_domain_logical_interface_delete'
            else:
                method_name = 'bridge_domain_logical_interface_%s_delete' %\
                              intf_type
            config = (method_name, bd_args)
            return callback(config)
        if not get_config:
            method_name = 'bridge_domain_logical_interface_%s_create' %\
                           intf_type
            config = (method_name, bd_args)
            result = callback(config)
        elif get_config:
            method_name = 'bridge_domain_logical_interface_%s_get' %\
                           intf_type
            config = (method_name, bd_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if intf_type == 'port_channel':
                result = util.find(util.root, './/pc-lif-bind-id')
            else:
                result = util.find(util.root, './/lif-bind-id')
        return result

    def logical_interface_create(self, **kwargs):
        """Configure/get/delete logical interface on an ethernet/port-channel.
        Args:
            intf_type (str): Type of interface. ['ethernet', 'port_channel']
            intf_name (str): Intername name.
            lif_name  (str): Logical Interface name.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete single/all lifs on intf.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `intf_name`  is not specified.
            KeyError: if `lif_name` is not speciied.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.logical_interface_create(
            ...         get=True, intf_name='0/34')
            ...         output = dev.interface.logical_interface_create(
            ...         delete=True, intf_name='0/34')
            ...         output = dev.interface.logical_interface_create(
            ...         intf_name='0/34', lif_name='0/34.1')
            ...         output = dev.interface.logical_interface_create(
            ...         intf_name='111', lif_name='111.1',
            ...         intf_type='port_channel')
            ...         output = dev.interface.logical_interface_create(
            ...         delete=True, intf_name='0/34', lif_name='0/34.1')
            Traceback (most recent call last):
            KeyError
        """

        intf_type = kwargs.pop('intf_type', 'ethernet')
        intf_name = kwargs.pop('intf_name', None)
        lif_name = kwargs.pop('lif_name', None)

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if intf_type not in ['ethernet', 'port_channel']:
            raise ValueError("`intf_ype` must match one of them "
                             "`ethernet, port_channel`")

        if intf_type == 'port_channel':
            lg_args = dict(port_channel=intf_name)
        else:
            lg_args = dict(ethernet=intf_name)

        if delete:
            if lif_name is not None and intf_type == 'port_channel':
                lg_args.update(port_channel_=lif_name)
            elif lif_name is not None and intf_type == 'ethernet':
                lg_args.update(ethernet_=lif_name)
            method_name = 'interface_%s_logical_interface_%s_delete' %\
                          (intf_type, intf_type)
            config = (method_name, lg_args)
            return callback(config)
        if not get_config:
            if intf_type == 'port_channel':
                lg_args = dict(port_channel=intf_name, port_channel_=lif_name)
            else:
                lg_args = dict(ethernet=intf_name, ethernet_=lif_name)
            method_name = 'interface_%s_logical_interface_%s_create' %\
                          (intf_type, intf_type)
            config = (method_name, lg_args)
            result = callback(config)
        elif get_config:
            method_name = 'interface_%s_logical_interface_%s_get' %\
                          (intf_type, intf_type)
            config = (method_name, lg_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if intf_type == 'port_channel':
                result = util.findall(util.root, './/pc-instance-id')
            else:
                result = util.findall(util.root, './/instance-id')
        return result

    def logical_interface_tag_vlan(self, **kwargs):
        """Configure/get/delete outer-vlan,inner-vlan on a LIF
        Args:
            intf_type (str): Type of interface. ['ethernet', 'port_channel']
            intf_name (str): Intername name.
            lif_name  (str): Logical Interface name.
            outer_tag_vlan_id (str): Outer vlan ID
            inner_vlan (bool): Enable inner vlan.(True, False)
            inner_tag_vlan_id (str): Inner vlan ID
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the tag vlan.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `lif_name`, `intf_name` `outer_tag_vlan_id` 
                      is not specified.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.logical_interface_tag_vlan(
            ...         get=True, intf_name='1/34', lif_name='1/34.1')
            ...         output = dev.interface.logical_interface_tag_vlan(
            ...         delete=True, intf_name='1/34', lif_name='1/34.1')
            ...         output = dev.interface.logical_interface_tag_vlan(
            ...         intf_name='111', lif_name='111.1', inner_vlan=True,
            ...         outer_tag_vlan_id='100', inner_tag_vlan_id='200')
            Traceback (most recent call last):
            KeyError
        """
        intf_type = kwargs.pop('intf_type', 'ethernet')
        intf_name = kwargs.pop('intf_name', None)
        lif_name = kwargs.pop('lif_name', None)

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if intf_type not in ['ethernet', 'port_channel']:
            raise ValueError("`intf_ype` must match one of them "
                             "`ethernet, port_channel`")

        if intf_type == 'port_channel':
            lg_args = dict(port_channel=intf_name, port_channel_=lif_name)
        else:
            lg_args = dict(ethernet=intf_name, ethernet_=lif_name)

        if delete:
            method_name = 'interface_%s_logical_interface_%s_vlan_delete' %\
                          (intf_type, intf_type)
            config = (method_name, lg_args)
            return callback(config)
        if not get_config:
            outer_tagged_vlan_id = kwargs.pop('outer_tag_vlan_id')
            if not pyswitch.utilities.valid_vlan_id(outer_tagged_vlan_id):
                raise InvalidVlanId("Invalid outer Vlan value.")
            inner_vlan = kwargs.pop('inner_vlan', None)
            if intf_type == 'port_channel':
                lg_args = dict(port_channel=intf_name, port_channel_=lif_name,
                               outer_tagged_vlan_id=outer_tagged_vlan_id)
            else:
                lg_args = dict(ethernet=intf_name, ethernet_=lif_name,
                               outer_tagged_vlan_id=outer_tagged_vlan_id)
            if inner_vlan:
                inner_tagged_vlan_id = kwargs.pop('inner_tag_vlan_id')
                if not pyswitch.utilities.valid_vlan_id(inner_tagged_vlan_id):
                    raise InvalidVlanId("Invalid inner Vlan value.")
                lg_args['inner_vlan'] = inner_vlan
                lg_args['inner_tagged_vlan_id'] = inner_tagged_vlan_id
            method_name = 'interface_%s_logical_interface_%s_vlan_update' %\
                          (intf_type, intf_type)
            config = (method_name, lg_args)
            result = callback(config)
        elif get_config:
            method_name = 'interface_%s_logical_interface_%s_vlan_get' %\
                          (intf_type, intf_type)
            config = (method_name, lg_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            outer_vlan = util.find(util.root, './/outer-tagged-vlan-id')
            inner_vlan = util.find(util.root, './/inner-tagged-vlan-id')
            result  = dict(outer_vlan=outer_vlan,inner_vlan=inner_vlan)
        return result

    def logical_interface_untag_vlan(self, **kwargs):
        """Configure/get/delete untag-vlan on a LIF
        Args:
            intf_type (str): Type of interface. ['ethernet', 'port_channel']
            intf_name (str): Intername name.
            lif_name  (str): Logical Interface name.
            untag_vlan_id (str): Outer vlan ID
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the untag vlan on lif.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `intf_name` is not specified.
            KeyError: if `lif_name` or `untag_vlan_id` is not speciied.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.logical_interface_untag_vlan(
            ...         get=True, intf_name='1/34', lif_name='1/34.1')
            ...         output = dev.interface.logical_interface_untag_vlan(
            ...         delete=True, intf_name='1/34', lif_name='1/34.1')
            ...         output = dev.interface.logical_interface_untag_vlan(
            ...         intf_name='111', lif_name='111.1',
            ...         untag_vlan_id='100')
            Traceback (most recent call last):
            KeyError
        """
        intf_type = kwargs.pop('intf_type', 'ethernet')
        intf_name = kwargs.pop('intf_name', None)
        lif_name = kwargs.pop('lif_name', None)

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if intf_type not in ['ethernet', 'port_channel']:
            raise ValueError("`intf_ype` must match one of them "
                             "`ethernet, port_channel`")

        if intf_type == 'port_channel':
            lg_args = dict(port_channel=intf_name, port_channel_=lif_name)
        else:
            lg_args = dict(ethernet=intf_name, ethernet_=lif_name)

        if delete:
            method_name = 'interface_%s_logical_interface_%s_'\
                          'untagged_vlan_delete' % (intf_type, intf_type)
            config = (method_name, lg_args)
            return callback(config)
        if not get_config:
            untagged_vlan_id = kwargs.pop('untag_vlan_id')
            if not pyswitch.utilities.valid_vlan_id(untagged_vlan_id):
                raise InvalidVlanId("Invalid untagged Vlan value.")
            if intf_type == 'port_channel':
                lg_args = dict(port_channel=intf_name, port_channel_=lif_name,
                               untagged_vlan_id=untagged_vlan_id)
            else:
                lg_args = dict(ethernet=intf_name, ethernet_=lif_name,
                               untagged_vlan_id=untagged_vlan_id)
            method_name = 'interface_%s_logical_interface_%s_untagged_'\
                          'vlan_update' % (intf_type, intf_type)
            config = (method_name, lg_args)
            result = callback(config)
        elif get_config:
            method_name = 'interface_%s_logical_interface_%s_untagged_'\
                           'vlan_get' % (intf_type, intf_type)
            config = (method_name, lg_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/untagged-vlan-id')
        return result

    def ip_ospf(self, **kwargs):
        """Configure/get ospf on an interface
        Args:
            intf_type (str): Type of interface.
            intf_name (str): Intername name.
            area (str): OSPF areas.
            auth_change_wait_time (str): Authentication Change Wait time
                                         (MD5 and non MD5).
            hello_interval (str): Time between HELLO packets.
            dead_interval (str): Interval after which a neighbor
                                 is declared dead.
            retransmit_interval (str): Time between retransmitting lost
                                       link state advertisements.
            transmit_delay (str): Link state transmit delay.
            cost (str): Interface cost.
            network (str): Interface type.
                           ['broadcast', 'non-broadcast', 'point-to-point']
            intf_ldp_sync (str): Set LDP-SYNC operation mode on this interface.
                                 [enable, disable]
            mtu_ignore (bool): To disable OSPF MTU mismatch detection.
            active (bool):  Active information.
            passive (bool): Passive information.
            priority (str): Router priority.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `intf_name`, `area` is not specified.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.ip_ospf(intf_type='loopback',
            ...         get=True, intf_name='11')
            ...         output = dev.interface.ip_ospf(intf_type='loopback',
            ...         area='0', intf_name='11')
            Traceback (most recent call last):
            KeyError
        """
        intf_type = kwargs.pop('intf_type', 'ethernet')
        intf_name = kwargs.pop('intf_name')
        auth_change_wait_time = kwargs.pop('auth_change_wait_time', None)
        hello_interval = kwargs.pop('hello_interval', None)
        dead_interval = kwargs.pop('dead_interval', None)
        retransmit_interval = kwargs.pop('retransmit_interval', None)
        transmit_delay = kwargs.pop('transmit_delay', None)
        cost = kwargs.pop('cost', None)
        network = kwargs.pop('network', None)
        intf_ldp_sync = kwargs.pop('intf_ldp_sync', None)
        mtu_ignore = kwargs.pop('mtu_ignore', None)
        active= kwargs.pop('active', None)
        passive = kwargs.pop('passive', None)
        priority = kwargs.pop('priority', None)
        valid_int_types = self.valid_int_types

        if intf_type not in self.valid_int_types:
            raise ValueError('intf_type must be one of: %s' %
                             repr(valid_int_types))
        ospf_args = {}
        get_config = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)

        ospf_args[intf_type] = intf_name
        if not get_config:
            area = kwargs.pop('area')
            ospf_args.update(area=area,
                         auth_change_wait_time=auth_change_wait_time,
                         hello_interval=hello_interval,
                         dead_interval=dead_interval,
                         retransmit_interval=retransmit_interval,
                         transmit_delay=transmit_delay, cost=cost,
                         network=network, intf_ldp_sync=intf_ldp_sync,
                         mtu_ignore=mtu_ignore, active=active,
                         passive=passive, priority=priority)
            method_name = 'interface_%s_ip_ospf_update' % intf_type
            config = (method_name, ospf_args)
            return callback(config)
        elif get_config:
            method_name = 'interface_%s_ip_ospf_get' % intf_type
            config = (method_name, ospf_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            ospf = util.find(util.root, './/area')
            if ospf is not None:
                 active = util.find(util.root, './/active')
                 passive = util.find(util.root, './/passive')
                 mtu_ignore = util.find(util.root, './/mtu-ignore')
                 result = { 'area' : ospf, 'active' : active,
                            'passive' : passive, 'mtu_ignore' : mtu_ignore}
            else:
                 result = None
        return result

    def ip_router_isis(self, **kwargs):
        """Configure/get/delete ISIS on an interface

        Args:
            intf_type (str): Type of interface.
            intf_name (str): Intername name.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the router isis on intf.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `intf_name` is not specified.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.ip_router_isis(
            ...         intf_type='loopback', get=True, intf_name='11')
            ...         output = dev.interface.ip_router_isis(
            ...         intf_type='loopback', delete=True, intf_name='11')
            ...         output = dev.interface.ip_router_isis(
            ...         intf_type='loopback', intf_name='11')
            Traceback (most recent call last):
            KeyError
        """
        intf_type = kwargs.pop('intf_type', 'ethernet')
        intf_name = kwargs.pop('intf_name')

        if intf_type not in self.valid_int_types:
            raise ValueError('intf_type must be one of: %s' %
                             repr(valid_int_types))
        isis_args = {}
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        isis_args[intf_type] = intf_name
        if delete:
            method_name = 'interface_%s_ip_router_isis_delete' % intf_type
            config = (method_name, isis_args)
            return callback(config)
        if not get_config:
            isis_args['interface_ip_router_isis'] = True
            method_name = 'interface_%s_ip_router_isis_update' % intf_type
            config = (method_name, isis_args)
            return callback(config)
        elif get_config:
            method_name = 'interface_%s_ip_router_isis_get' % intf_type
            config = (method_name, isis_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/isis')
        return result
