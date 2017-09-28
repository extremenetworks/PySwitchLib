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

from pyswitch.utilities import Util


class Mct(object):
    """
    The MCT class holds all relevent methods and attributes for the MCT
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

    def mct_client_create(self, **kwargs):
        """ Configure/get/delete mct client under the mct cluster

        Args:
            cluster_name (str): MCT Cluster Name.
            cluster_id (int): . MCT Cluster ID.
            client_name (str): MCT Client Name.
            client_id (int): . MCT Client ID. (Valid Values: 1-512)
            client_deploy (bool): Deploy. (True, False)
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `cluster_name`, `cluster_id`
                      `client_name`, `client_id` are  not specified.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     dev.mct.mct_client_create(client_deploy=True,
            ...         cluster_id=1, cluster_name='pod-cluster')
            ...         client_id=1, client_name='client1')
            ...     output = dev.mct.mct_client_create(get=True,
            ...         cluster_id=1, cluster_name='pod-cluster')
            ...         client_id=1, client_name='client1')
            ...     print output
            ...     dev.mct.mct_client_create(delete=True,
            ...         cluster_id=1, cluster_name='pod-cluster')
            ...         client_id=1, client_name='client1')
        """
        cluster_name = kwargs.pop('cluster_name')
        cluster_id = kwargs.pop('cluster_id')
        client_name = kwargs.pop('client_name', None)
        client_id = kwargs.pop('client_id', None)
        client_deploy = kwargs.pop('client_deploy', None)

        mct_args = {}
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if cluster_id not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`"
                             % (cluster_id))
        if client_id is not None and not xrange(1, 513):
            raise ValueError("client_id %s must be in range `1-512`"
                             % (client_id))

        mct_args = dict(cluster=(cluster_name, str(cluster_id)))
        if delete:
            method_name = 'cluster_client_delete'
            mct_args.update(client=(client_name, str(client_id)))
            config = (method_name, mct_args)
            return callback(config)
        if not get_config:
            method_name = 'cluster_client_create'
            mct_args.update(client=(client_name, str(client_id)),
                            client_deploy=client_deploy)
            config = (method_name, mct_args)
            return callback(config)
        elif get_config:
            method_name = 'cluster_client_get'
            mct_args.update(client=(client_name, str(client_id)))
            config = (method_name, mct_args)
            output = callback(config, handler='get_config')
            if output.data != '<output></output>':
                result = True
            else:
                result = False
        return result

    def mct_client_interface_create(self, **kwargs):
        """ Configure/get/delete mct client interface under the mct client

        Args:
            cluster_name (str): MCT Cluster Name.
            cluster_id (int): . MCT Cluster ID.
            client_name (str): MCT Client Name.
            client_id (int): . MCT Client ID. (Valid Values: 1-512)
            intf_type (str): Type of interface. ['Ethernet', 'Port_channel']
            intf_name (str): Intername name.
            client_deploy (bool): Deploy. (True, False)
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `intf_name`, `cluster_name`, `cluster_id`
                      `client_name`, `client_id` are  not specified.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     dev.mct.mct_client_interface_create(client_deploy=True,
            ...              cluster_id=1, cluster_name='pod-cluster')
            ...              client_id=1, client_name='client1',
            ...              intf_type='Ethernet', intf_name='0/35')
            ...     output = dev.mct.mct_client_interface_create(get=True,
            ...              cluster_id=1, cluster_name='pod-cluster')
            ...              client_id=1, client_name='client1')
            ...    print output
            ...    dev.mct.mct_client_interface_create(delete=True,
            ...        cluster_id=1, cluster_name='pod-cluster')
            ...        client_id=1, client_name='client1')
        """
        cluster_name = kwargs.pop('cluster_name')
        cluster_id = kwargs.pop('cluster_id')
        client_name = kwargs.pop('client_name', None)
        client_id = kwargs.pop('client_id', None)

        mct_args = {}
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if cluster_id not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`"
                             % (cluster_id))
        if client_id is not None and not xrange(1, 513):
            raise ValueError("client_id %s must be in range `1-512`"
                             % (client_id))

        mct_args = dict(cluster=(cluster_name, str(cluster_id)))
        if delete:
            method_name = 'cluster_client_client_interface_delete'
            mct_args.update(client=(client_name, str(client_id)))
            config = (method_name, mct_args)
            return callback(config)
        if not get_config:
            intf_name = kwargs.pop('intf_name')
            intf_type = kwargs.pop('intf_type', 'Ethernet')
            if intf_type == 'ethernet':
                intf_type = 'Ethernet'
            if intf_type == 'port_channel':
                intf_type = 'Port-channel'
            if intf_type not in ['Ethernet', 'Port-channel']:
                raise ValueError('intf_type %s must be either'
                                 '`Ethernet or Port-channel`'
                                 % (intf_type))
            method_name = 'cluster_client_client_interface_update'
            mct_args.update(client=(client_name, str(client_id)),
                            if_type=intf_type, if_value=intf_name)
            config = (method_name, mct_args)
            return callback(config)
        elif get_config:
            method_name = 'cluster_client_client_interface_get'
            mct_args.update(client=(client_name, str(client_id)))
            config = (method_name, mct_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            if output.data != '<output></output>':
                result = util.find(util.root, './/if-value')
            else:
                result = None

        return result

    def mct_client_deploy(self, **kwargs):
        """ Configure/get/delete mct client deploy.

        Args:
            cluster_name (str): MCT Cluster Name.
            cluster_id (int): . MCT Cluster ID.
            client_name (str): MCT Client Name.
            client_id (int): . MCT Client ID. (Valid Values: 1-512)
            client_deploy (bool): Deploy. (True, False)
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): Delete config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `client_deploy`, `cluster_name`, `cluster_id`
                      `client_name`, `client_id` are  not specified.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitchdevice.Device(conn=conn, auth=auth) as dev:
            ...     dev.mct.mct_client_deploy(client_deploy=True,
            ...              cluster_id=1, cluster_name='pod-cluster')
            ...              client_id=1, client_name='client1')
            ...     output = dev.mct.mct_client_deploy(get=True,
            ...              cluster_id=1, cluster_name='pod-cluster')
            ...              client_id=1, client_name='client1')
            ...     print output
            ...     dev.mct.mct_client_deploy(delete=True,
            ...              cluster_id=1, cluster_name='pod-cluster')
            ...              client_id=1, client_name='client1')
        """
        cluster_name = kwargs.pop('cluster_name')
        cluster_id = kwargs.pop('cluster_id')
        client_name = kwargs.pop('client_name')
        client_id = kwargs.pop('client_id')
        client_deploy = kwargs.pop('client_deploy', None)

        mct_args = {}
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if cluster_id not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`"
                             % (cluster_id))
        if client_id not in xrange(1, 513):
            raise ValueError("client_id %s must be in range `1-512`"
                             % (client_id))

        mct_args = dict(cluster=(cluster_name, str(cluster_id)))
        if delete:
            method_name = 'cluster_client_deploy_delete'
            mct_args.update(client=(client_name, str(client_id)))
            config = (method_name, mct_args)
            return callback(config)
        if not get_config:
            method_name = 'cluster_client_deploy_update'
            mct_args.update(client=(client_name, str(client_id)),
                            client_deploy=client_deploy)
            config = (method_name, mct_args)
            return callback(config)
        elif get_config:
            method_name = 'cluster_client_deploy_get'
            mct_args.update(client=(client_name, str(client_id)))
            config = (method_name, mct_args)
            output = callback(config, handler='get_config')
            if output.data != '<output></output>':
                result = True
            else:
                result = False

        return result

    def mct_cluster_create(self, **kwargs):
        """Configure Name of MCT cluster

        Args:
            cluster_name: Name of Overlay Gateway
            cluster_id: Name of Overlay Gateway
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
            ...     output = dev.mct.mct_cluster_create(
            ...              cluster_name='Leaf', cluster_id=10)
            ...     output = dev.mct.mct_cluster_create(get=True)
            ...     print output
            ...     dev.mct.mct_cluster_create(delete=True)
        """
        cluster_name = kwargs.pop('cluster_name', None)
        cluster_id = kwargs.pop('cluster_id', None)

        mct_args = {}
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if cluster_id is not None and not xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`"
                             % (cluster_id))

        if delete:
            mct_args = dict(cluster=(cluster_name, str(cluster_id)))
            method_name = 'cluster_delete'
            config = (method_name, mct_args)
            return callback(config)
        if not get_config:
            mct_args = dict(cluster=(cluster_name, str(cluster_id)))
            method_name = 'cluster_create'
            config = (method_name, mct_args)
            return callback(config)
        elif get_config:
            method_name = 'cluster_get'
            config = (method_name, mct_args)
            output = callback(config, handler='get_config')
            util = Util(output.data)
            result = util.find(util.root, './/cluster-name'),\
                util.find(util.root, './/cluster-id')

        return result
