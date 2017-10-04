import pyswitch.utilities as util
from pyswitch.os.base.bgp import Bgp as BaseBgp
from pyswitch.utilities import Util


class Bgp(BaseBgp):

    """
      The Interface class holds all the actions assocaiated with the Interfaces
      of a SLXOS device.

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

        super(Bgp, self).__init__(callback)

    def retain_rt_all(self, **kwargs):
        return

    def evpn_next_hop_unchanged(self, **kwargs):
        return

    def evpn_graceful_restart(self, **kwargs):
        return

    def evpn_allowas_in(self, **kwargs):
        return

    def evpn_afi(self, **kwargs):
        """
        EVPN AFI. This method just enables/disables or gets the EVPN AFI.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method. The only parameter passed to `callback` will be the``ElementTree`` `config`

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.evpn_afi(rbridge_id='225')
            ...     output = dev.bgp.evpn_afi(rbridge_id='225', get=True)
            ...     output = dev.bgp.evpn_afi(rbridge_id='225',
            ...     delete=True)
        """

        return

    def evpn_afi_peer_activate(self, **kwargs):
        """
        Activate EVPN AFI for a peer.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
                Deactivate
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.evpn_afi(rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.11',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.evpn_afi_peer_activate(rbridge_id='225',
            ...     peer_ip='10.10.10.11')
            ...     output = dev.bgp.evpn_afi_peer_activate(rbridge_id='225',
            ...     peer_ip='10.10.10.11', get=True)
            ...     output = dev.bgp.evpn_afi_peer_activate(rbridge_id='225',
            ...     peer_ip='10.10.10.11', delete=True)
            ...     output = dev.bgp.evpn_afi(rbridge_id='225',
            ...     delete=True)
            ...     output = dev.bgp.remove_bgp(rbridge_id='225')

        """

        return

    def evpn_afi_peergroup_encapsulation(self, **kwargs):
        """BGP evpn afi peer-group encapsulation.
        Args:
            peer_group (bool): Name of the peer group
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
            delete (bool): Deletes the peer group encapsulation
                if `delete` is ``True``.
            encapsulation_type: Valid vlaues 'vxlan','mpls','nxh'

            get (bool): Get config instead of editing config. (True, False)
        Returns:
            Return value of `callback`.
        Raises:
            ValueError: if `enabled` are invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.26.8.210']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.local_asn(local_as='64101')
            ...         output = dev.bgp.neighbor_peer_group(peer_group='test')
            ...
            ...         output = dev.bgp.evpn_afi()
            ...         output = dev.bgp.evpn_afi_peergroup_activate(peer_group='test')
            ...         output = dev.bgp.evpn_afi_peergroup_nexthop(
            ...         peer_group='test')
            ...         output = dev.bgp.evpn_afi_peergroup_encapsulation(
            ...         peer_group='test', encapsulation_type='vxlan')
            ...         output = dev.bgp.evpn_afi_peergroup_encapsulation(
            ...         peer_group='test', get=True)
            ...         output
            ...         output = dev.bgp.evpn_afi_peergroup_encapsulation(
            ...         peer_group='test', delete=True)
            ...         output = dev.bgp.evpn_afi_peergroup_encapsulation(
            ...         peer_group='test', get=True)
            ...         output = dev.bgp.neighbor_peer_group(peer_group='test',delete=True)
            ['vxlan']
        """
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        peer_group = kwargs.pop('peer_group')

        callback = kwargs.pop('callback', self._callback)
        result = []
        if not get_config:
            args = dict(evpn_peer_group=peer_group)

            if not delete:
                method_name = [
                    self.method_prefix(
                        'router_bgp_address_family_l2vpn_evpn_neighbor_'
                        'evpn_peer_group_update')
                ]
                encapsulation_type = kwargs.pop('encapsulation_type')
                args['encapsulation'] = encapsulation_type

            else:
                method_name = [
                    self.method_prefix(
                        'router_bgp_address_family_l2vpn_evpn_neighbor_'
                        'evpn_peer_group_encapsulation_delete')
                ]

            method = method_name[0]
            config = (method, args)
            result = callback(config)

        elif get_config:
            method_name = self.method_prefix('router_bgp_address_family_l2vpn_evpn_neighbor_'
                                             'evpn_peer_group_encapsulation_get')
            args = dict(
                resource_depth=2,
                evpn_peer_group=peer_group)
            config = (method_name, args)
            out = callback(config, handler='get_config')
            bgp = Util(out.data)
            for peer in bgp.findall(bgp.root, './/encapsulation'):
                result.append(peer)
        return result

    def evpn_encapsulation(self, **kwargs):
        """Configure evpn_encapsulation for an EVPN neighbor.


        Args:
            ip_addr (str): IP Address of BGP neighbor.

            encapsulation_type: Valid vlaues 'vxlan','mpls','nxh'
            delete (bool): Deletes the peer  encapsulation if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.26.8.210', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='64101')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535')
            ...     output = dev.bgp.evpn_afi_peer_activate(peer_ip='10.10.10.10')
            ...     output = dev.bgp.evpn_encapsulation(
            ...     ip_addr='10.10.10.10',encapsulation_type='vxlan')
            ...     output = dev.bgp.evpn_encapsulation(
            ...     ip_addr='10.10.10.10', get=True)
            ...     output = dev.bgp.evpn_encapsulation(
            ...     ip_addr='10.10.10.10', delete=True)
        """
        callback = kwargs.pop('callback', self._callback)
        ip_addr = kwargs.pop('ip_addr')
        feature = '_neighbor_evpn_neighbor_ipv4_encapsulation'
        afi = 'l2vpn'
        if kwargs.pop('delete', False):
            args = dict()
            config = util.get_bgp_api(
                feature=feature,
                afi=afi,
                op='_delete',
                evpn_n_addr=ip_addr,
                args=args,
                os=self.os)
            return callback(config)
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                feature=feature,
                evpn_n_addr=ip_addr,
                afi=afi,
                op='_get',
                os=self.os)
            out = callback(config, handler='get_config')
            bgp = Util(out.data)
            result = []
            for peer in bgp.findall(bgp.root, './/encapsulation'):
                result.append(peer)
            return result
        encapsulation_type = kwargs.pop('encapsulation_type')
        args = dict(encapsulation=encapsulation_type)
        config = util.get_bgp_api(
            feature=feature,
            afi=afi,
            op='_update',
            evpn_n_addr=ip_addr,
            args=args,
            os=self.os)
        return callback(config)

    def vlan_add(self, **kwargs):
        """Add VNIs to the EVPN Instance
        Args:
            rbridge_id (str): rbridge-id for device.
            evpn_instance (str): Name of the evpn instance.
            vni (str): vnis to the evpn instance
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the vni configuration
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `rbridge_id`,`evpn_instance`, 'vni' is not passed.
            ValueError: if `rbridge_id`, `evpn_instance`, 'vni' is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.26.8.210']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.vlan_add(
            ...         evpn_instance="evpn1", vlan='10')
            ...         output = dev.bgp.vlan_add(evpn_instance="evpn1",
            ...         get=True)
            ...         print output
            ...         output = dev.bgp.vlan_add(evpn_instance="evpn1",vlan='10',
            ...         delete=True)

        """
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []
        if not get_config:
            evpn_instance = kwargs['evpn_instance']
            vlan = kwargs.pop('vlan', None)
            if not delete:
                method_name = [
                    self.method_prefix('evpn_evpn_instance_create'),
                    self.method_prefix('evpn_evpn_instance_vlan_vlan_add_update')]
            else:
                method_name = [
                    self.method_prefix('evpn_evpn_instance_vlan_evpn_vlan_delete'),
                    self.method_prefix('evpn_evpn_instance_delete')]
            for i in range(0, 2):
                method = method_name[i]
                vlan_args = dict(
                    evpn_instance=evpn_instance)
                if 'vlan' in method and not delete:
                    vlan_args['add_'] = vlan
                config = (method, vlan_args)
                result = callback(config)

        elif get_config:
            evpn_instance = kwargs.pop('evpn_instance', '')
            method_name = self.method_prefix('evpn_evpn_instance_vlan_vlan_add_get')
            vlan_args = dict(
                evpn_instance=evpn_instance,
                resource_depth=2)
            config = (method_name, vlan_args)
            out = callback(config, handler='get_config')
            bgp = Util(out.data)
            tmp = {'rbridge_id': None,
                   'evpn_instance': evpn_instance,
                   'vlan': bgp.find(bgp.root, './/add')}
            result.append(tmp)
        return result

    def bd_add(self, **kwargs):
        """Add VNIs to the EVPN Instance
        Args:
            rbridge_id (str): rbridge-id for device.
            evpn_instance (str): Name of the evpn instance.
            vni (str): vnis to the evpn instance
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the vni configuration
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `rbridge_id`,`evpn_instance`, 'vni' is not passed.
            ValueError: if `rbridge_id`, `evpn_instance`, 'vni' is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.26.8.210']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.bd_add(
            ...         evpn_instance="evpn1", bd='10')
            ...         output = dev.bgp.bd_add(evpn_instance="evpn1",
            ...         get=True)
            ...         print output
            ...         output = dev.bgp.bd_add(evpn_instance="evpn1",bd='10',
            ...         delete=True)

        """
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []
        if not get_config:
            evpn_instance = kwargs['evpn_instance']
            bd = kwargs.pop('bd', None)
            if not delete:
                method_name = [
                    self.method_prefix('evpn_evpn_instance_create'),
                    self.method_prefix('evpn_evpn_instance_bridge_domain_add_update')]
            else:
                method_name = [
                    self.method_prefix('evpn_evpn_instance_bridge_domain_add_delete'),
                    self.method_prefix('evpn_evpn_instance_delete')]
            for i in range(0, 2):
                method = method_name[i]
                bd_args = dict(
                    evpn_instance=evpn_instance)
                if 'bridge_domain' in method and not delete:
                    bd_args['bd_range_add'] = bd
                config = (method, bd_args)
                result = callback(config)

        elif get_config:
            evpn_instance = kwargs.pop('evpn_instance', '')
            method_name = self.method_prefix('evpn_evpn_instance_bridge_domain_add_get')
            bd_args = dict(
                evpn_instance=evpn_instance,
                resource_depth=2)
            config = (method_name, bd_args)
            out = callback(config, handler='get_config')
            bgp = Util(out.data)
            tmp = {'rbridge_id': None,
                   'evpn_instance': evpn_instance,
                   'bd': bgp.find(bgp.root, './/add')}
            result.append(tmp)
        return result

    def vni_add(self, **kwargs):
        return

    @property
    def valid_int_types(self):

        return [
            'ethernet',
            'port_channel'
        ]

    @property
    def valid_intp_types(self):
        return [
            'ethernet',
        ]

    @property
    def has_rbridge_id(self):
        return False

    @property
    def os(self):
        return 'slxos'
