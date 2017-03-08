from pyswitch.os.base.bgp import Bgp as BaseBgp
import pyswitch.utilities as util


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

    def evpn_next_hop_unchanged(self, **kwargs):
        return

    def evpn_afi(self, **kwargs):
        """EVPN AFI. This method just enables/disables or gets the EVPN AFI.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
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
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.evpn_afi(rbridge_id='225')
            ...     output = dev.bgp.evpn_afi(rbridge_id='225', get=True)
            ...     output = dev.bgp.evpn_afi(rbridge_id='225',
            ...     delete=True)
        """
        return
        callback = kwargs.pop('callback', self._callback)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        feature = '_address_family_evpn'
        if kwargs.pop('delete', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                op='_delete',
                os=self.os)
            return callback(config)
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id, feature=feature,
                op='_get', os=self.os)
            ret = callback(config, handler='get_config')
            ret = True if ret and ret.json else False
            return ret
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            op='_create',
            os=self.os)
        return callback(config)

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
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
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
        peer_ip = kwargs.pop('peer_ip')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        feature = '_address_family_evpn_neighbor'
        if kwargs.pop('delete', False):
            args = dict(evpn_nbr_activate=False, af_evpn_neighbor=peer_ip)
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                op='_update',
                args=args,
                os=self.os)
            return callback(config)
        if kwargs.pop('get', False):
            args = dict(af_evpn_neighbor=peer_ip)
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                args=args,
                resource_depth=2,
                op='_get',
                os=self.os)
            ret = callback(config, handler='get_config')
            ret = util.find(ret.json, '$..activate')
            return ret
        args = dict(af_evpn_neighbor=peer_ip)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            args=args,
            op='_create',
            os=self.os)
        ret = callback(config)
        args = dict(evpn_nbr_activate=True, af_evpn_neighbor=peer_ip)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            op='_update',
            args=args,
            os=self.os)
        return callback(config)

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
