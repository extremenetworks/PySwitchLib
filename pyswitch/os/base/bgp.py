# 2017.01.30 15:56:30 IST
# Embedded file name: pyswitch/bgp.py
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
from ipaddress import ip_interface
import pyswitch.utilities as util


class Bgp(object):
    """
    The BGP class holds all relevent methods and attributes for the BGP
    capabilities of the NOS device.

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

    @property
    def os(self):
        return 'slxos'

    def method_prefix(self, method, args=None):
        if self.has_rbridge_id:
            return 'rbridge_id_%s' % method
        else:
            if args:
                args.pop('rbridge_id', None)
            return method

    def __init__(self, callback):
        """
        BGP object init.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            BGP Object

        Raises:
            None
        """
        self._callback = callback
        self._cli = None

    @property
    def enabled(self, **kwargs):
        """bool: ``True`` if BGP is enabled; ``False`` if BGP is disabled.
        """
        rbridge_id = kwargs.pop('rbridge_id', 1)
        config = util.get_bgp_api(rbridge_id=rbridge_id, op='_get', os=self.os)
        bgp_config = self._callback(config, handler='get_config')
        if bgp_config and bgp_config.json:
            return True
        return False

    def local_asn(self, **kwargs):
        """Set BGP local ASN.

        Args:
            local_as (str): Local ASN of NOS deice.
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will
                configured in a VCS fabric.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `local_as` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225', get=True)
            ...     dev.bgp.local_asn() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        vrf = kwargs.pop('vrf', 'default')
        afi = kwargs.pop('afi', None)
        is_get_config = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        feature = '_local_as'
        op = '_update'
        if is_get_config:
            if afi and afi == 'ipv6':
                afi = 'ipv4'
            args = dict(resource_depth=2)
            config = util.get_bgp_api(
                vrf=vrf,
                feature='_local_as',
                op='_get',
                afi=afi,
                rbridge_id=rbridge_id,
                args=args,
                os=self.os)
            bgp_config = callback(config, handler='get_config')
            local_as = util.findall(bgp_config.json, '$..local-as')
            local_as = local_as[0] if local_as else None
            return local_as
        config = util.get_bgp_api(rbridge_id=rbridge_id, op='_create',
                                  os=self.os)
        callback(config)
        if vrf != 'default':
            """
            local as will be kept per vrf in backend
            no local as config for ipv6
            hence afi will ipv4
            """
            feature = ''
            op = '_create'

        args = dict()
        if not afi or afi != 'ipv6':
            local_as = kwargs.pop('local_as')
            args = dict(local_as=str(local_as))

        config = util.get_bgp_api(
            vrf=vrf,
            afi=afi,
            feature=feature,
            rbridge_id=rbridge_id,
            args=args,
            op=op,
            os=self.os)
        return callback(config)

    def remove_bgp(self, **kwargs):
        """Remove BGP process completely.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will
                configured in a VCS fabric.
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
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.remove_bgp(rbridge_id='225')
        """
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        afi = kwargs.pop('afi', None)
        config = util.get_bgp_api(
            vrf=vrf,
            afi=afi,
            rbridge_id=rbridge_id,
            op='_delete',
            os=self.os)
        return callback(config)

    def neighbor(self, **kwargs):
        """Add BGP neighbor.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            remote_as (str): Remote ASN of BGP neighbor.
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `remote_as` or `ip_addr` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10', get=True,
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     output = dev.bgp.neighbor(remote_as='65535', get=True,
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     delete=True, rbridge_id='225')
            ...     output = dev.bgp.neighbor(delete=True, rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     dev.bgp.neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            NotImplementedError
            KeyError
        """
        ip_addr = kwargs.get('ip_addr')
        remote_as = kwargs.get('remote_as', None)
        vrf = kwargs.get('vrf', 'default')
        rbridge_id = kwargs.get('rbridge_id', '1')
        delete = kwargs.get('delete', False)
        get = kwargs.get('get', False)
        callback = kwargs.get('callback', self._callback)
        ip_addr = ip_interface(unicode(ip_addr))
        afi = 'ipv4' if ip_addr.version == 4 else 'ipv6'
        n_addr = str(ip_addr.ip)
        if delete:
            raise NotImplementedError
        if get:
            return self.get_bgp_neighbors(**kwargs)

        if not delete and remote_as is None:
            raise ValueError(
                'When configuring a neighbor, '
                'you must specify its remote-as.')
        ret = self._neighbor_ip_address(
            afi, n_addr, rbridge_id, remote_as, vrf, callback, 'create')
        return ret

    def _neighbor_ip_address(self, afi='ipv4', n_addr=None, rbridge_id=1,
                             remote_as='1', vrf='default',
                             callback=None, op='create'):
        if afi == 'ipv4':
            if vrf == 'default':
                self._neighbor_ipv4_address(
                    afi, n_addr, rbridge_id, remote_as, callback, op)
            else:
                self._neighbor_ipv4_vrf_address(
                    afi, n_addr, rbridge_id, remote_as, vrf, callback, op)
        if afi == 'ipv6':
            if vrf == 'default':
                self._neighbor_ipv6_address(
                    afi, n_addr, rbridge_id, remote_as, callback, op)
            else:
                self._neighbor_ipv6_vrf_address(
                    afi, n_addr, rbridge_id, remote_as, vrf, callback, op)

    def _neighbor_ipv4_address(self, afi='ipv4', n_addr=None,
                               rbridge_id=1, remote_as='1',
                               callback=None, op='create'):
        args = dict(rbridge_id=rbridge_id, neighbor_addr=n_addr,
                    remote_as=remote_as)
        api = self.method_prefix('router_bgp_neighbor_neighbor_addr_create',
                                 args)
        config = (api, args)
        callback(config)
        args = dict(rbridge_id=rbridge_id, af_ipv4_neighbor_address=n_addr)
        api = self.method_prefix('router_bgp_address_family_ipv4_unicast_'
                                 'neighbor_af_ipv4_neighbor_address_create',
                                 args)
        config = (api, args)
        callback(config)
        args = dict(activate=True)
        config = util.get_bgp_api(
            n_addr=n_addr,
            afi=afi,
            feature='_neighbor_af_ipv4_neighbor_address',
            rbridge_id=rbridge_id,
            args=args,
            os=self.os)
        return callback(config)

    def _neighbor_ipv6_address(self, afi='ipv6', n_addr=None,
                               rbridge_id=1, remote_as='1',
                               callback=None, op='create'):
        args = dict(rbridge_id=rbridge_id, neighbor_ipv6_addr=n_addr,
                    remote_as=remote_as)

        api = self.method_prefix('router_bgp_neighbor_neighbor_ipv6_'
                                 'addr_create', args)
        config = (api, args)
        callback(config)

        args = dict(rbridge_id=rbridge_id, af_ipv6_neighbor_address=n_addr)
        api = self.method_prefix('router_bgp_address_family_ipv6_unicast_'
                                 'neighbor_af_ipv6_neighbor_address_create',
                                 args)
        config = (api, args)
        callback(config)
        args = dict(activate=True)
        config = util.get_bgp_api(
            n_addr=n_addr,
            afi=afi,
            feature='_neighbor_af_ipv6_neighbor_address',
            rbridge_id=rbridge_id,
            args=args,
            os=self.os)
        return callback(config)

    def _neighbor_ipv4_vrf_address(
            self, afi='ipv4', n_addr=None, rbridge_id=1, remote_as='1',
            vrf=None, callback=None, op='create'):
        args = dict(rbridge_id=rbridge_id, af_vrf=vrf)
        api = self.method_prefix('router_bgp_address_family_ipv4_unicast'
                                 '_vrf_create', args)
        config = (api, args)
        callback(config)
        args = dict(
            rbridge_id=rbridge_id,
            af_vrf=vrf,
            remote_as=remote_as,
            af_ipv4_neighbor_addr=n_addr)
        api = self.method_prefix('router_bgp_address_family_ipv4_unicast_'
                                 'vrf_neighbor_af_ipv4_neighbor_addr_create',
                                 args)
        config = (api, args)
        callback(config)
        args = dict(activate=True)
        config = util.get_bgp_api(
            n_addr=n_addr,
            vrf=vrf,
            afi=afi,
            feature='_neighbor_af_ipv4_neighbor_addr',
            rbridge_id=rbridge_id,
            args=args,
            os=self.os)
        return callback(config)

    def _neighbor_ipv6_vrf_address(
            self, afi='ipv6', n_addr=None, rbridge_id=1, remote_as='1',
            vrf=None, callback=None, op='create'):
        args = dict(rbridge_id=rbridge_id, af_ipv6_vrf=vrf)
        api = self.method_prefix('router_bgp_address_family_ipv6_unicast'
                                 '_vrf_create', args)
        config = (api, args)
        callback(config)
        args = dict(
            rbridge_id=rbridge_id,
            af_ipv6_vrf=vrf,
            af_ipv6_neighbor_addr=n_addr,
            remote_as=remote_as)
        api = self.method_prefix('router_bgp_address_family_ipv6_unicast_'
                                 'vrf_neighbor_af_ipv6_neighbor_addr_create',
                                 args)
        config = (api, args)
        callback(config)
        args = dict(activate=True)
        config = util.get_bgp_api(
            n_addr=n_addr,
            vrf=vrf,
            afi=afi,
            feature='_neighbor_af_ipv6_neighbor_addr',
            rbridge_id=rbridge_id,
            args=args,
            os=self.os)
        return callback(config)

    def _neighbor_activate(self, n_addr, afi, rbridge_id, vrf, callback):
        feature = '_neighbor_af_{afi}_neighbor_address'.format(afi=afi)
        args = dict(activate=True)
        config = util.get_bgp_api(
            n_addr=n_addr,
            afi=afi,
            rbridge_id=rbridge_id,
            feature=feature,
            vrf=vrf,
            args=args,
            os=self.os)
        return callback(config)

    def get_bgp_neighbors(self, **kwargs):
        """Get BGP neighbors configured on a device.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will
                configured in a VCS fabric.
            vrf (str): The VRF for this BGP process.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            List of 0 or more BGP Neighbors on the specified
            rbridge.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     result = dev.bgp.get_bgp_neighbors(rbridge_id='225')
            ...     assert len(result) >= 1
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     delete=True, rbridge_id='225')
            ...     output = dev.bgp.neighbor(delete=True, rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     dev.bgp.neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            NotImplementedError
            KeyError
        """
        callback = kwargs.pop('callback', self._callback)
        vrf = kwargs.pop('vrf', 'default')
        remote_as = kwargs.pop('remote_as', None)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        ip_addr = kwargs.pop('ip_addr', None)
        result = []
        if vrf == 'default':
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                op='_get',
                resource_depth=2,
                feature='_neighbor_neighbor_addr',
                os=self.os)
            output = callback(config, handler='get_config')
            ns = util.find(output.json, '$..neighbor-addr')
            ns = ns if ns else []
            if isinstance(ns, dict):
                ret = []
                ret.append(ns)
            else:
                ret = ns
            for n in ret:
                peer_ip = util.find(n, '$..address')
                peer_remote_as = util.find(n, '$..remote-as')
                item_results = {'neighbor-address': peer_ip,
                                'remote-as': peer_remote_as}
                if ip_addr and remote_as and ip_addr == peer_ip and \
                        peer_remote_as == remote_as:
                    return item_results
                result.append(item_results)

            ns = util.find(output.json, '$..neighbor-ipv6-addr')
            ns = ns if ns else []
            if isinstance(ns, dict):
                ret = []
                ret.append(ns)
            else:
                ret = ns
            for n in ret:
                peer_ip = util.find(n, '$..address')
                peer_remote_as = util.find(n, '$..remote-as')
                item_results = {'neighbor-address': util.find(n, '$..address'),
                                'remote-as': util.find(n, '$..remote-as')}
                if ip_addr and remote_as and ip_addr == peer_ip and \
                        peer_remote_as == remote_as:
                    return item_results
                result.append(item_results)
            if ip_addr and remote_as:
                return None
            return result
        feature = '_neighbor_af_ipv4_neighbor_addr'
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            afi='ipv4',
            vrf=vrf,
            op='_get',
            feature=feature,
            resource_depth=2,
            args=dict(),
            os=self.os)
        output = callback(config, handler='get_config')
        ns = util.find(output.json, '$..af-ipv4-neighbor-addr')
        ns = ns if ns else []
        if isinstance(ns, dict):
            ret = []
            ret.append(ns)
        else:
            ret = ns
        for n in ret:
            peer_ip = util.find(n, '$..address')
            peer_remote_as = util.find(n, '$..remote-as')
            item_results = {'neighbor-address': util.find(n, '$..address'),
                            'remote-as': util.find(n, '$..remote-as')}
            if ip_addr and remote_as and ip_addr == peer_ip and \
                    peer_remote_as == remote_as:
                return item_results
            result.append(item_results)

        feature = '_neighbor_af_ipv6_neighbor_addr'
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            afi='ipv6',
            vrf=vrf,
            op='_get',
            feature=feature,
            resource_depth=2,
            args=dict(),
            os=self.os)
        output = callback(config, handler='get_config')
        ns = util.find(output.json, '$..af-ipv6-neighbor-addr')
        ns = ns if ns else []
        if isinstance(ns, dict):
            ret = []
            ret.append(ns)
        else:
            ret = ns
        for n in ret:
            peer_ip = util.find(n, '$..address')
            peer_remote_as = util.find(n, '$..remote-as')
            item_results = {'neighbor-address': util.find(n, '$..address'),
                            'remote-as': util.find(n, '$..remote-as')}
            if ip_addr and remote_as and ip_addr == peer_ip and \
                    peer_remote_as == remote_as:
                return item_results
            result.append(item_results)

        return result

    def redistribute(self, **kwargs):
        """Set BGP redistribute properties.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            source (str): Source for redistributing. (connected)
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `source` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.redistribute(source='connected',
            ...     rbridge_id='225')
            ...     output = dev.bgp.redistribute(source='connected',
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.redistribute(source='connected',
            ...     rbridge_id='225', delete=True)
            ...     dev.bgp.redistribute() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
            ...     dev.bgp.redistribute(source='connected', rbridge_id='225',
            ...     afi='hodor') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
            ...     dev.bgp.redistribute(source='hodor', rbridge_id='225',
            ...     afi='ipv4') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
            ...     output = dev.bgp.redistribute(source='connected', afi='x',
            ...     rbridge_id='225') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        source = kwargs.pop('source', 'connected')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        afi = kwargs.pop('afi', 'ipv4')
        vrf = kwargs.pop('vrf', 'default')
        callback = kwargs.pop('callback', self._callback)
        feature = '_redistribute_connected'
        if afi not in ('ipv4', 'ipv6'):
            raise AttributeError('Invalid AFI.')
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                op='_get',
                feature=feature,
                args=dict(),
                os=self.os)
            output = callback(config, handler='get_config')
            output = util.findall(output.json, '$..redistribute-connected')
            output = True if output and output[0] == 'true' else False
            return output
        if kwargs.pop('delete', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                op='_delete',
                feature=feature,
                args=dict(),
                os=self.os)
            return callback(config)
        if source != 'connected':
            raise AttributeError('Invalid source.')
        args = dict(redistribute_connected=True)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            afi=afi,
            vrf=vrf,
            op='_update',
            feature=feature,
            args=args,
            os=self.os)
        return callback(config)

    def max_paths(self, **kwargs):
        """Set BGP max paths property.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            paths (str): Number of paths for BGP ECMP (default: 8).
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.max_paths(paths='8',
            ...     rbridge_id='225')
            ...     output = dev.bgp.max_paths(paths='8',
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.max_paths(paths='8',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225')
            ...     output = dev.bgp.max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.max_paths(paths='8', afi='ipv5',
            ...     rbridge_id='225') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        afi = kwargs.pop('afi', 'ipv4')
        afi = 'ipv4' if not afi else afi
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        paths = kwargs.pop('paths', '8')
        feature = '_maximum_paths'
        if afi not in ('ipv4', 'ipv6'):
            raise AttributeError('Invalid AFI.')
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                op='_get',
                feature=feature,
                args=dict(),
                os=self.os)
            output = callback(config, handler='get_config')
            output = util.findall(output.json, '$..load-sharing-value')
            output = output[0] if output else None
            return output
        if kwargs.pop('delete', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                op='_delete',
                feature=feature,
                args=dict(),
                os=self.os)
            return callback(config)
        args = dict(load_sharing_value=paths)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            afi=afi,
            vrf=vrf,
            feature=feature,
            args=args,
            os=self.os)
        return callback(config)

    def recursion(self, **kwargs):
        """Set BGP next hop recursion property.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.recursion(rbridge_id='225')
            ...     output = dev.bgp.recursion(rbridge_id='225', get=True)
            ...     output = dev.bgp.recursion(rbridge_id='225', delete=True)
            ...     output = dev.bgp.max_paths(rbridge_id='225', afi='ipv6')
            ...     output = dev.bgp.max_paths(rbridge_id='225', afi='ipv6',
            ...     get=True)
            ...     output = dev.bgp.max_paths(rbridge_id='225', afi='ipv6',
            ...     delete=True)
            ...     output = dev.bgp.max_paths(rbridge_id='225', afi='ipv5')
            ...     # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
            ...     output = dev.bgp.recursion(rbridge_id='225', afi='hodor')
            ...     # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        afi = kwargs.pop('afi', 'ipv4')
        afi = 'ipv4' if not afi else afi
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        vrf = kwargs.pop('vrf', 'default')
        delete = kwargs.pop('delete', False)
        feature = ''
        inp = False if delete else True
        if afi not in ('ipv4', 'ipv6'):
            raise AttributeError('Invalid AFI.')
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id, afi=afi, vrf=vrf,
                op='_get', os=self.os)
            output = callback(config, handler='get_config')
            output = util.findall(output.json, '$..next-hop-recursion')
            output = True if output and output[0] == 'true' else False
            return output
        if afi == 'ipv4' or vrf != 'default':
            args = dict(next_hop_recursion=inp)
        elif afi == 'ipv6' and vrf == 'default':
            args = dict(ipv6_ucast_next_hop_recursion=inp)
        if delete:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                op='_delete',
                args=args,
                os=self.os)
            return callback(config)
        if vrf == 'default':
            feature = feature + '_default_vrf'
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            afi=afi,
            vrf=vrf,
            feature=feature,
            args=args,
            os=self.os)
        return callback(config)

    def graceful_restart(self, **kwargs):
        """Set BGP next hop recursion property.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.graceful_restart(rbridge_id='225')
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     get=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     delete=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     afi='ipv6')
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     afi='ipv6', get=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     afi='ipv6', delete=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     afi='ipv5') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        afi = kwargs.pop('afi', 'ipv4')
        afi = 'ipv4' if not afi else afi
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        vrf = kwargs.pop('vrf', 'default')
        feature = '_graceful_restart' if vrf == 'default' else ''
        args = dict(graceful_restart_status=True)
        if afi not in ('ipv4', 'ipv6', 'evpn'):
            raise AttributeError('Invalid AFI.')
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                feature=feature,
                op='_get',
                os=self.os)
            output = callback(config, handler='get_config')
            output = util.findall(output.json, '$..graceful-restart-status')
            output = True if output and output[0] == 'true' else False
            return output
        if kwargs.pop('delete', False):
            args = dict(graceful_restart_status=False)
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                feature=feature,
                op='_update',
                os=self.os,
                args=args)
            return callback(config)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            afi=afi,
            vrf=vrf,
            feature=feature,
            os=self.os,
            args=args)
        return callback(config)

    def multihop(self, **kwargs):
        """Set BGP multihop property for a neighbor.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            neighbor (str): Address family to configure. (ipv4, ipv6)
            count (str): Number of hops to allow. (1-255)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `neighbor` is not a valid IPv4 or IPv6
                address.
            ``KeyError``: When `count` is not specified.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.230']
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     auth = ('admin', 'password')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.bgp.local_asn(local_as='65535', rbridge_id='225')
            ...         dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...         remote_as='65535', rbridge_id='225')
            ...         dev.bgp.neighbor(remote_as='65535', rbridge_id='225',
            ...         ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...         dev.bgp.multihop(neighbor='10.10.10.10', count='5',
            ...         rbridge_id='225')
            ...         dev.bgp.multihop(get=True, neighbor='10.10.10.10',
            ...         count='5', rbridge_id='225')
            ...         dev.bgp.multihop(count='5', rbridge_id='225',
            ...         neighbor='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...         dev.bgp.multihop(get=True, count='5', rbridge_id='225',
            ...         neighbor='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...         dev.bgp.multihop(delete=True, neighbor='10.10.10.10',
            ...         count='5', rbridge_id='225')
            ...         dev.bgp.multihop(delete=True, count='5',
            ...         rbridge_id='225',
            ...         neighbor='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...         dev.bgp.neighbor(ip_addr='10.10.10.10', delete=True,
            ...         rbridge_id='225')
            ...         dev.bgp.neighbor(delete=True, rbridge_id='225',
            ...         ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...         output = dev.bgp.multihop(rbridge_id='225', count='5')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            NotImplementedError
            KeyError
        """
        callback = kwargs.pop('callback', self._callback)
        ip_addr = ip_interface(unicode(kwargs.pop('neighbor')))
        rbridge_id = kwargs.pop('rbridge_id', '1')
        afi = 'ipv4' if ip_addr.version == 4 else 'ipv6'
        vrf = kwargs.pop('vrf', 'default')
        count = kwargs.pop('count')
        feature_tmp = '_neighbor{0}_ebgp_multihop'
        if vrf == 'default':
            if 'ipv4' == afi:
                feature = feature_tmp.format('_neighbor_addr')
            elif 'ipv6' == afi:
                feature = feature_tmp.format('_neighbor_ipv6_addr')
            afi = None
        elif 'ipv4' == afi:
            feature = feature_tmp.format('_af_ipv4_neighbor_addr')
        elif 'ipv6' == afi:
            feature = feature_tmp.format('_af_ipv6_neighbor_addr')
        args = dict(ebgp_multihop_count=count)
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                feature=feature,
                n_addr=str(
                    ip_addr.ip),
                op='_get',
                os=self.os)
            output = callback(config, handler='get_config')
            output = util.findall(output.json, '$..ebgp-multihop-count')
            output = output[0] if output else None
            return output
        if kwargs.pop('delete', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                feature=feature,
                n_addr=str(
                    ip_addr.ip),
                op='_delete',
                os=self.os)
            return callback(config)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            afi=afi,
            vrf=vrf,
            feature=feature,
            n_addr=str(
                ip_addr.ip),
            args=args,
            os=self.os)
        return callback(config)

    def update_source(self, **kwargs):
        """Set BGP update source property for a neighbor.

        This method currently only supports loopback interfaces.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            neighbor (str): Address family to configure. (ipv4, ipv6)
            int_type (str): Interface type (loopback)
            int_name (str): Interface identifier (1, 5, 7, etc)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `neighbor` is not a valid IPv4 or IPv6
                address.
            ``KeyError``: When `int_type` or `int_name` are not specified.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.230']
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     auth = ('admin', 'password')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.ip_address(int_type='loopback', name='6',
            ...         rbridge_id='225', ip_addr='6.6.6.6/32')
            ...         dev.interface.ip_address(int_type='loopback', name='6',
            ...         ip_addr='0:0:0:0:0:ffff:606:606/128', rbridge_id='225')
            ...         dev.bgp.local_asn(local_as='65535', rbridge_id='225')
            ...         dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...         remote_as='65535', rbridge_id='225')
            ...         dev.bgp.neighbor(remote_as='65535', rbridge_id='225',
            ...         ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...         dev.bgp.update_source(neighbor='10.10.10.10',
            ...         rbridge_id='225', int_type='loopback', int_name='6')
            ...         dev.bgp.update_source(get=True, neighbor='10.10.10.10',
            ...         rbridge_id='225', int_type='loopback', int_name='6')
            ...         dev.bgp.update_source(rbridge_id='225', int_name='6',
            ...         neighbor='2001:4818:f000:1ab:cafe:beef:1000:1',
            ...         int_type='loopback')
            ...         dev.bgp.update_source(get=True, rbridge_id='225',
            ...         neighbor='2001:4818:f000:1ab:cafe:beef:1000:1',
            ...         int_type='loopback', int_name='6')
            ...         dev.bgp.update_source(neighbor='10.10.10.10',
            ...         rbridge_id='225', delete=True, int_type='loopback',
            ...         int_name='6')
            ...         dev.bgp.update_source(delete=True, int_type='loopback',
            ...         rbridge_id='225', int_name='6',
            ...         neighbor='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...         dev.bgp.neighbor(ip_addr='10.10.10.10', delete=True,
            ...         rbridge_id='225')
            ...         dev.bgp.neighbor(delete=True, rbridge_id='225',
            ...         ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...         dev.interface.ip_address(int_type='loopback', name='6',
            ...         rbridge_id='225', ip_addr='6.6.6.6/32', delete=True)
            ...         dev.interface.ip_address(int_type='loopback', name='6',
            ...         ip_addr='0:0:0:0:0:ffff:606:606/128', rbridge_id='225',
            ...         delete=True)
            ...         output = dev.bgp.update_source(rbridge_id='225',
            ...         int_type='loopback')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            NotImplementedError
            KeyError
        """
        feature_tmp = '_neighbor{0}_update_source'
        callback = kwargs.pop('callback', self._callback)
        ip_addr = ip_interface(unicode(kwargs.pop('neighbor')))
        rbridge_id = kwargs.pop('rbridge_id', '1')
        afi = 'ipv4' if ip_addr.version == 4 else 'ipv6'
        vrf = kwargs.pop('vrf', 'default')
        int_type = kwargs.pop('int_type')
        int_name = kwargs.pop('int_name')
        if vrf == 'default':
            if 'ipv4' == afi:
                feature = feature_tmp.format('_neighbor_addr')
            elif 'ipv6' == afi:
                feature = feature_tmp.format('_neighbor_ipv6_addr')
            afi = None
        elif 'ipv4' == afi:
            feature = feature_tmp.format('_af_ipv4_neighbor_addr')
        elif 'ipv6' == afi:
            feature = feature_tmp.format('_af_ipv6_neighbor_addr')
        if int_type == 'loopback':
            args = dict(loopback=int_name)
            feature += '_loopback'
        else:
            args = dict(
                interface_type=int_type,
                ethernet=str(int_name),
                rbridge_id=rbridge_id)
            feature += '_ethernet'
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                feature=feature,
                n_addr=str(
                    ip_addr.ip),
                op='_get',
                os=self.os)
            ret = callback(config)
            search = '$..{0}'.format(int_type)
            ret = util.findall(ret.json, search)
            ret = ret[0] if ret else None
            return ret
        if kwargs.pop('delete', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                afi=afi,
                vrf=vrf,
                feature=feature,
                n_addr=str(
                    ip_addr.ip),
                op='_delete',
                os=self.os)
            return callback(config)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            afi=afi,
            vrf=vrf,
            feature=feature,
            n_addr=str(
                ip_addr.ip),
            args=args,
            os=self.os)
        return callback(config)

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
        callback = kwargs.pop('callback', self._callback)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        feature = '_address_family_l2vpn_evpn'
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
        peer_ip = kwargs.pop('peer_ip')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        ip_addr = ip_interface(unicode(peer_ip))
        afi = 'ipv4' if ip_addr.version == 4 else 'ipv6'
        feature = '_address_family_l2vpn_evpn_neighbor_evpn_neighbor' \
                  '_{afi}'.format(afi=afi)

        if kwargs.pop('delete', False):
            args = dict(activate=False)
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                evpn_n_addr=peer_ip,
                op='_update',
                args=args,
                os=self.os)
            return callback(config)
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                evpn_n_addr=peer_ip,
                resource_depth=2,
                op='_get',
                os=self.os)
            ret = callback(config, handler='get_config')
            ret = util.find(ret.json, '$..activate')
            return ret
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            evpn_n_addr=peer_ip,
            op='_create',
            os=self.os)
        ret = callback(config)
        args = dict(activate=True)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            evpn_n_addr=peer_ip,
            op='_update',
            args=args,
            os=self.os)
        return callback(config)

    def bfd(self, **kwargs):
        """Configure BFD for BGP globally.

        Args:
            rbridge_id (str): Rbridge to configure.  (1, 225, etc)
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
            >>> import pynos.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230')
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230', get=True)
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230', delete=True)
        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        get = kwargs.pop('get', False)
        feature = '_bfd_interval'
        callback = kwargs.pop('callback', self._callback)
        if delete:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                op='_delete',
                os=self.os)
            return callback(config)
        if get:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                resource_depth=2,
                op='_get',
                os=self.os)
            ret = callback(config, handler='get_config')
            min_tx = util.find(ret.json, '$..min-tx')
            min_rx = util.find(ret.json, '$..min-rx')
            multiplier = util.find(ret.json, '$..multiplier')
            item = dict(min_tx=min_tx, min_rx=min_rx, multiplier=multiplier)
            return item
        min_tx = kwargs.pop('tx')
        min_rx = kwargs.pop('rx')
        multiplier = kwargs.pop('multiplier')
        args = dict(min_tx=min_tx, min_rx=min_rx, multiplier=multiplier)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            op='_update',
            args=args,
            os=self.os)
        return callback(config)

    def retain_rt_all(self, **kwargs):
        """Retain route targets.

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
            ...     output = dev.bgp.retain_rt_all(rbridge_id='225')
            ...     output = dev.bgp.retain_rt_all(rbridge_id='225', get=True)
            ...     output = dev.bgp.retain_rt_all(rbridge_id='225',
            ...     delete=True)
        """
        callback = kwargs.pop('callback', self._callback)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        afi = 'l2vpn'
        feature = '_retain_route_target'
        if kwargs.pop('delete', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                afi=afi,
                op='_delete',
                os=self.os)
            return callback(config)
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                resource_depth=2,
                afi=afi,
                op='_get',
                os=self.os)
            ret = callback(config, handler='get_config')
            ret = util.find(ret.json, '$..all')
            ret = True if ret and ret[0] == 'true' else False
            return ret
        args = dict(all=True)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            afi=afi,
            op='_update',
            args=args,
            os=self.os)
        return callback(config)

    def evpn_next_hop_unchanged(self, **kwargs):
        """Configure next hop unchanged for an EVPN neighbor.

        You probably don't want this method.  You probably want to configure
        an EVPN neighbor using `BGP.neighbor`.  That will configure next-hop
        unchanged automatically.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
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
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.evpn_next_hop_unchanged(rbridge_id='225',
            ...     ip_addr='10.10.10.10')
            ...     output = dev.bgp.evpn_next_hop_unchanged(rbridge_id='225',
            ...     ip_addr='10.10.10.10', get=True)
            ...     output = dev.bgp.evpn_next_hop_unchanged(rbridge_id='225',
            ...     ip_addr='10.10.10.10', delete=True)
        """
        callback = kwargs.pop('callback', self._callback)
        ip_addr = kwargs.pop('ip_addr')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        feature = '_neighbor_evpn_neighbor_ipv4'
        afi = 'l2vpn'
        if kwargs.pop('delete', False):
            args = dict(next_hop_unchanged=False)
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                afi=afi,
                op='_update',
                evpn_n_addr=ip_addr,
                args=args,
                os=self.os)
            return callback(config)
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                evpn_n_addr=ip_addr,
                afi=afi,
                op='_get',
                os=self.os)
            out = callback(config, handler='get_config')
            out = util.find(out.json, '$..next-hop-unchanged')
            return out
        args = dict(next_hop_unchanged=True)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            afi=afi,
            op='_update',
            evpn_n_addr=ip_addr,
            args=args,
            os=self.os)
        return callback(config)

    def evpn_allowas_in(self, **kwargs):
        """Configure allowas_in for an EVPN neighbor.

        You probably don't want this method.  You probably want to configure
        an EVPN neighbor using `BGP.neighbor`.  That will configure next-hop
        unchanged automatically.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
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
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.evpn_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10')
            ...     output = dev.bgp.evpn_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10', get=True)
            ...     output = dev.bgp.evpn_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10', delete=True)
        """
        callback = kwargs.pop('callback', self._callback)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        ip_addr = kwargs.pop('ip_addr')
        feature = '_neighbor_evpn_neighbor_ipv4'
        afi = 'l2vpn'
        if kwargs.pop('delete', False):
            feature = feature + '_allowas_in'
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                afi=afi,
                op='_delete',
                evpn_n_addr=ip_addr,
                os=self.os)
            return callback(config)
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                evpn_n_addr=ip_addr,
                afi=afi,
                op='_get',
                resource_depth=2,
                os=self.os)
            out = callback(config, handler='get_config')
            out = util.findall(out.json, '$..allowas-in')
            return out
        allowas_in = kwargs.pop('allowas_in', '5')
        args = dict(allowas_in=allowas_in)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            afi=afi,
            op='_update',
            evpn_n_addr=ip_addr,
            args=args,
            os=self.os)
        return callback(config)

    def af_ip_allowas_in(self, **kwargs):
        """Set BGP allowas-in for IPV4 and IPV6

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            allowas_in (str): Values for allowas_in (default: 5).
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.l

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10', get=True)
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10', delete=True)
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1', afi='ipv6')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1', get=True,
            ...     afi='ipv6')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1', delete=True,
            ...     afi='ipv6')
        """
        afi = kwargs.pop('afi', 'ipv4')
        callback = kwargs.pop('callback', self._callback)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        allowas_in = int(kwargs.pop('allowas_in', 5))
        vrf = kwargs.pop('vrf', 'default')
        ip_addr = kwargs.pop('ip_addr')
        feature_tmp = '{0}_neighbor{1}'
        if afi not in ('ipv4', 'ipv6'):
            raise AttributeError('Invalid AFI.')
        if vrf == 'default':
            if 'ipv4' == afi:
                feature = feature_tmp.format(
                    '_address_family_ipv4_unicast',
                    '_af_ipv4_neighbor_address')
            elif 'ipv6' == afi:
                feature = feature_tmp.format(
                    '_address_family_ipv6_unicast',
                    '_af_ipv6_neighbor_address')
            afi = None
        else:
            if 'ipv4' == afi:
                feature = feature_tmp.format('', '_af_ipv4_neighbor_addr')
            elif 'ipv6' == afi:
                feature = feature_tmp.format('', '_af_ipv6_neighbor_addr')

        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                vrf=vrf,
                n_addr=str(ip_addr),
                rbridge_id=rbridge_id,
                op='_get',
                afi=afi,
                feature=feature,
                resource_depth=2,
                os=self.os)
            out = callback(config, handler='get_config')
            ret = util.findall(out.json, '$..allowas-in')[0]
            return ret
        if kwargs.pop('delete', False):
            feature = feature + '_allowas_in'
            config = util.get_bgp_api(
                vrf=vrf,
                n_addr=str(ip_addr),
                rbridge_id=rbridge_id,
                afi=afi,
                feature=feature,
                os=self.os)
            return callback(config)
        args = dict(allowas_in=allowas_in)
        feature = feature + '_allowas_in'
        config = util.get_bgp_api(
            vrf=vrf,
            n_addr=str(ip_addr),
            rbridge_id=rbridge_id,
            op='_update',
            afi=afi,
            feature=feature,
            args=args,
            os=self.os)
        return callback(config)

    def peer_bfd_timers(self, **kwargs):
        """Configure BFD for BGP globally.

        Args:
            rbridge_id (str): Rbridge to configure.  (1, 225, etc)
            peer_ip (str): Peer IPv4 address for BFD setting.
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
            >>> import pynos.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.bgp.neighbor(ip_addr='10.10.10.20',
            ...        remote_as='65535', rbridge_id='230')
            ...        output = dev.bgp.peer_bfd_timers(peer_ip='10.10.10.20',
            ...        rx='300', tx='300', multiplier='3', rbridge_id='230')
            ...        output = dev.bgp.peer_bfd_timers(peer_ip='10.10.10.20',
            ...        rx='300', tx='300', multiplier='3', rbridge_id='230',
            ...        get=True)
            ...        output = dev.bgp.peer_bfd_timers(peer_ip='10.10.10.20',
            ...        rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230', delete=True)
            ...        output = dev.bgp.neighbor(ip_addr='10.10.10.20',
            ...        delete=True, rbridge_id='230', remote_as='65535')
        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        peer_ip = kwargs.pop('peer_ip')
        min_tx = kwargs.pop('tx')
        min_rx = kwargs.pop('rx')
        vrf = kwargs.pop('vrf', 'default')
        multiplier = kwargs.pop('multiplier')
        delete = kwargs.pop('delete', False)
        get = kwargs.pop('get', False)
        feature_tmp = '_neighbor{0}_bfd_interval'
        ip_addr = ip_interface(unicode(peer_ip))
        afi = 'ipv4' if ip_addr.version == 4 else 'ipv6'
        callback = kwargs.pop('callback', self._callback)
        if vrf == 'default':
            if 'ipv4' == afi:
                feature = feature_tmp.format('_neighbor_addr')
            elif 'ipv6' == afi:
                feature = feature_tmp.format('_neighbor_ipv6_addr')
            afi = None
        elif 'ipv4' == afi:
            feature = feature_tmp.format('_af_ipv4_neighbor_addr')
        elif 'ipv6' == afi:
            feature = feature_tmp.format('_af_ipv6_neighbor_addr')
        if delete:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                vrf=vrf,
                afi=afi,
                n_addr=peer_ip,
                op='_delete',
                os=self.os)
            return callback(config)
        if get:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                vrf=vrf,
                afi=afi,
                n_addr=peer_ip,
                resource_depth=2,
                op='_get',
                os=self.os)
            ret = callback(config, handler='get_config')
            item = {'min_tx': util.findall(ret.json, '$..min-tx'),
                    'min_rx': util.findall(ret.json, '$..min-rx'),
                    'multiplier': util.findall(ret.json, '$..multiplier')}
            return item
        args = dict(min_tx=min_tx, min_rx=min_rx, multiplier=multiplier)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            vrf=vrf,
            afi=afi,
            n_addr=peer_ip,
            op='_update',
            args=args,
            os=self.os)
        return callback(config)

    def enable_peer_bfd(self, **kwargs):
        """BFD enable for each specified peer.

        Args:
            rbridge_id (str): Rbridge to configure.  (1, 225, etc)
            peer_ip (str): Peer IPv4 address for BFD setting.
            delete (bool): True if BFD configuration should be deleted.
                Default value will be False if not specified.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.
        Returns:
            XML to be passed to the switch.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.bgp.neighbor(ip_addr='10.10.10.20',
            ...        remote_as='65535', rbridge_id='230')
            ...        output = dev.bgp.enable_peer_bfd(peer_ip='10.10.10.20',
            ...        rbridge_id='230')
            ...        output = dev.bgp.enable_peer_bfd(peer_ip='10.10.10.20',
            ...        rbridge_id='230',get=True)
            ...        output = dev.bgp.enable_peer_bfd(peer_ip='10.10.10.20',
            ...        rbridge_id='230', delete=True)
            ...        output = dev.bgp.neighbor(ip_addr='10.10.10.20',
            ...        delete=True, rbridge_id='230', remote_as='65535')
        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        peer_ip = kwargs.pop('peer_ip')
        delete = kwargs.pop('delete', False)
        get = kwargs.pop('get', False)
        feature_tmp = '_neighbor{0}_bfd'
        callback = kwargs.pop('callback', self._callback)
        vrf = kwargs.pop('vrf', 'default')
        ip_addr = ip_interface(unicode(peer_ip))
        afi = 'ipv4' if ip_addr.version == 4 else 'ipv6'
        if vrf == 'default':
            if 'ipv4' == afi:
                feature = feature_tmp.format('_neighbor_addr')
            elif 'ipv6' == afi:
                feature = feature_tmp.format('_neighbor_ipv6_addr')
            afi = None
        elif 'ipv4' == afi:
            feature = feature_tmp.format('_af_ipv4_neighbor_addr')
        elif 'ipv6' == afi:
            feature = feature_tmp.format('_af_ipv6_neighbor_addr')
        if delete:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                vrf=vrf,
                afi=afi,
                n_addr=peer_ip,
                op='_delete',
                os=self.os)
            return callback(config)
        if get:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id,
                feature=feature,
                vrf=vrf,
                afi=afi,
                n_addr=peer_ip,
                resource_depth=2,
                op='_get',
                os=self.os)
            ret = callback(config, handler='get_config')
            ret = util.findall(ret.json, '$..bfd-enable')
            ret = True if ret and ret[0] == 'true' else False
            return ret
        args = dict(bfd_enable=True)
        config = util.get_bgp_api(
            rbridge_id=rbridge_id,
            feature=feature,
            vrf=vrf,
            afi=afi,
            n_addr=peer_ip,
            op='_update',
            args=args,
            os=self.os)
        return callback(config)

    def vni_add(self, **kwargs):
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
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.vni_add(rbridge_id='2',
            ...         evpn_instance="leaf1", vni='10')
            ...         output = dev.bgp.vni_add(rbridge_id='2',
            ...         evpn_instance="leaf1", vni='10', delete=True)
            ...         output = dev.bgp.vni_add(rbridge_id='2',
            ...         evpn_instance="leaf1", vni='10', delete=True)
            ...         output = dev.bgp.vni_add(rbridge_id='2',
            ...         get=True)

        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []
        if not get_config:
            evpn_instance = kwargs['evpn_instance']
            vni = kwargs.pop('vni', None)
            if not delete:
                method_name = [
                    self.method_prefix('evpn_instance_create'),
                    self.method_prefix('evpn_instance_vni_evpn_vni_create')]
            else:
                method_name = [
                    self.method_prefix('evpn_instance_vni_evpn_vni_delete'),
                    self.method_prefix('evpn_instance_delete')]
            for i in range(0, 2):
                method = method_name[i]
                vni_args = dict(
                    rbridge_id=rbridge_id,
                    evpn_instance=evpn_instance)
                if self.os != 'nos':
                    vni_args.pop('rbridge_id', None)
                if 'vni' in method:
                    vni_args['evpn_vni'] = vni
                config = (method, vni_args)
                result = callback(config)

        elif get_config:
            evpn_instance = kwargs.pop('evpn_instance', '')
            method_name = self.method_prefix('evpn_instance_vni_get')
            vni_args = dict(
                rbridge_id=rbridge_id,
                evpn_instance=evpn_instance,
                resource_depth=2)
            if self.os != 'nos':
                vni_args.pop('rbridge_id', None)
            config = (method_name, vni_args)
            out = callback(config, handler='get_config')
            tmp = {'rbridge_id': rbridge_id,
                   'evpn_instance': evpn_instance,
                   'vni': util.findall(out.json, '$..vni-number')}
            if self.os != 'nos':
                tmp.pop('rbridge_id', None)
            result.append(tmp)
        return result

    def vrf_redistribute_connected(self, **kwargs):
        """Enable redistribute connected on vrf address family.

        Args:
            afi (str): Address family to configure. (ipv4, ipv6)
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the redistribute connected
                if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `vrf' is not expected
            AttributeError: if 'afi' is not in ipv4,ipv6. Default = ipv4

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     device.bgp.vrf_redistribute_connected(vrf='vrf101',
            ...     rbridge_id='4')
            ...     device.bgp.vrf_redistribute_connected(vrf='vrf101',
            ...     get=True, rbridge_id='4')
            ...     device.bgp.vrf_redistribute_connected(vrf='vrf101',
            ...     delete=True, rbridge_id='4')
        """
        return self.redistribute(**kwargs)

    def vrf_unicast_address_family(self, **kwargs):
        """Add BGP v4/v6 address family.

        Args:
            afi (str): Address family to configure. (ipv4, ipv6)
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the redistribute connected
                if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `vrf' is not expected
            AttributeError: if 'afi' is not in ipv4,ipv6. Default = ipv4

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     device.bgp.vrf_unicast_address_family(delete=True,
            ...     vrf='vrf101', rbridge_id='4')
            ...     device.bgp.vrf_unicast_address_family(get=True,
            ...     vrf='vrf101', rbridge_id='4')
            ...     device.bgp.vrf_unicast_address_family(vrf='vrf101',
            ...     rbridge_id='4')
        """
        afi = kwargs.pop('afi', 'ipv4')
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        if afi not in ('ipv4', 'ipv6'):
            raise AttributeError('Invalid AFI.')
        if kwargs.pop('get', False):
            config = util.get_bgp_api(
                rbridge_id=rbridge_id, afi=afi, vrf=vrf,
                op='_get', os=self.os)
            result = callback(config, handler='get_config')
            if vrf != 'default':
                result = util.findall(result.json, '$..vrf-name')[0]
                result = True if result == vrf else False
            else:
                result = True if result else False
        elif delete:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id, afi=afi, vrf=vrf,
                op='_delete', os=self.os)
            result = callback(config)
        else:
            config = util.get_bgp_api(
                rbridge_id=rbridge_id, afi=afi, vrf=vrf,
                op='_create', os=self.os)
            result = callback(config)
        return result

    def vrf_max_paths(self, **kwargs):
        """Set BGP max paths property on VRF address family.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            paths (str): Number of paths for BGP ECMP (default: 8).
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.vrf_max_paths(paths='8',
            ...     rbridge_id='225')
            ...     output = dev.bgp.vrf_max_paths(
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.vrf_max_paths(paths='8',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.vrf_max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225')
            ...     output = dev.bgp.vrf_max_paths(afi='ipv6',
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.vrf_max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.vrf_max_paths(paths='8', afi='ipv5',
            ...     rbridge_id='225') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        return self.max_paths(**kwargs)

    def default_vrf_unicast_address_family(self, **kwargs):
        """Create default address family (ipv4/ipv6) under router bgp.

        Args:
            afi (str): Address family to configure. (ipv4, ipv6)
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                              configured in a VCS fabric.
            delete (bool): Deletes the redistribute connected under default vrf
                if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `afi' is not expected
            AttributeError: if 'afi' is not in ipv4,ipv6.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     device.bgp.default_vrf_unicast_address_family(delete=True,
            ...     rbridge_id='4')
            ...     device.bgp.default_vrf_unicast_address_family(get=True,
            ...     rbridge_id='4')
            ...     device.bgp.default_vrf_unicast_address_family(
            ...     rbridge_id='4', afi='ipv6')
        """
        return self.vrf_unicast_address_family(**kwargs)

    def default_vrf_redistribute_connected(self, **kwargs):
        """Enable redistribute connected on default vrf address family.

        Args:
            afi (str): Address family to configure. (ipv4, ipv6)
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the redistribute connected under default vrf
                if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `afi' is not expected
            AttributeError: if 'afi' is not in ipv4,ipv6. Default = ipv4

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     device.bgp.default.vrf_redistribute_connected(
            ...     rbridge_id='4')
            ...     device.bgp.default.vrf_redistribute_connected(
            ...     get=True, rbridge_id='4')
            ...     device.bgp.default.vrf_redistribute_connected(
            ...     delete=True, rbridge_id='4')
        """
        return self.redistribute(**kwargs)

    def default_vrf_max_paths(self, **kwargs):
        """Set BGP max paths property on default VRF address family.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            paths (str): Number of paths for BGP ECMP (default: 8).
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...     rbridge_id='225')
            ...     output = dev.bgp.default_vrf_max_paths(
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...              afi='ipv6', rbridge_id='225')
            ...     output = dev.bgp.default_vrf_max_paths(
            ...              afi='ipv6', rbridge_id='225', get=True)
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...              afi='ipv6', rbridge_id='225', delete=True)
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...              afi='ipv5', rbridge_id='225')
            Traceback (most recent call last):
            AttributeError
        """
        return self.max_paths(**kwargs)

    def as4_capability(self, **kwargs):
        """Set Spanning Tree state.
        Args:
            enabled (bool): Is AS4 Capability enabled? (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            ValueError: if `enabled` are invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.local_asn(local_as='65535',
            ...         rbridge_id='225')
            ...         output = dev.bgp.as4_capability(
            ...         rbridge_id='225', enabled=True)
            ...         output = dev.bgp.as4_capability(
            ...         rbridge_id='225', enabled=False)
        """
        enabled = kwargs.pop('enabled', True)
        callback = kwargs.pop('callback', self._callback)
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')

        if not isinstance(enabled, bool):
            raise ValueError('%s must be `True` or `False`.' % repr(enabled))
        if vrf == 'default':
            args = dict(rbridge_id=rbridge_id, as4_enable=enabled)
            api = 'router_bgp_capability_update'
            method_name = self.method_prefix(api, args)
            return callback(method_name, args)
        else:
            return

    def evpn_graceful_restart(self, **kwargs):
        """Set BGP evpn graceful restart property.
        """

        api = 'rbridge_id_router_bgp_address_family_l2vpn_evpn_' \
              'graceful_restart_update'
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        args = dict(rbridge_id=rbridge_id, graceful_restart_status=True)
        return callback((api, args))