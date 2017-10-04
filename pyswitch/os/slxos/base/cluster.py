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


class Cluster(object):
    """
    cluster class containing all methods and attributes for configuring mct cluster
    """

    def __init__(self, callback):
        """Cluster init method.

                Args:
                    callback: Callback function that will be called for each action.

                Returns:
                    None

                Raises:
                    None
                """
        self._callback = callback

    def cluster_validate(self, cluster_name, cluster_id):
        if cluster_id not in xrange(1, 65536):
            raise ValueError("cluster_id %d must be in range `1-65535`", cluster_id)
        if len(cluster_name) not in xrange(1, 64):
            raise ValueError("cluster_name %s must be in range `1-64`", cluster_name)

    def cluster_create(self, **cluster_args):
        """
        Method to create cluster
        args:
            cluster_args:
                 cluster: Mandatory
                    cluster_name(str): name of the cluster
                    cluster_id(str): cluster id
                 peer_info: Optional, 3 tuple of (peer_ip, peer_interface_type, peer_interface)
                     peer_ip(str): Peer Ip address
                     peer_interface_type: Peer interface type. Has to be one of ['Ethernet', 'Ve']
                     peer_interface(str): Interface if (X/Y) format.
                 client_isolation_mode: optional. 'loose' or 'strict'. By default 'loose'
                 df_hold_time: optional, designated forwarder hold time. Bu default 3 sec.
                 deploy: optional, 'True' or 'False'. by default 'False'

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.cluster.cluster_create(cluster=('F47-F48','3'))
            ...     response1 = device.cluster.cluster_get(cluster=('F47-F48','3'))
            ...     response2 = device.cluster.cluster_delete(cluster=('F47-F48','3'))
            ...
        """
        (clname, clid) = cluster_args.pop('cluster')
        isolation_mode = cluster_args.pop('client_isolation_mode', 'loose')
        hold_time = cluster_args.pop('df_hold_time', 3)
        cldeploy = cluster_args.pop('deploy', False)

        self.cluster_validate(clname, int(clid))

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster created"
        if isolation_mode is 'loose':
            isolation_strict = False
        else:
            isolation_strict = True
        argument = {'cluster': (clname, clid),
                    'client_interfaces_shutdown': False,
                    'client_isolation_strict': isolation_strict,
                    'designated_forwarder_hold_time': hold_time,
                    'deploy': cldeploy
                    }
        config = ('cluster_create', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def cluster_update(self, **cluster_args):
        """
        Method to update cluster
        args:
            cluster_args:
                 cluster: Mandatory
                    cluster_name(str): name of the cluster
                    cluster_id(str): cluster id
                 client_isolation_mode: optional. 'loose' or 'strict'. By default 'loose'
                 hold_time: optional, designated forwarder hold time. Bu default 3 sec.
                 deploy: optional, 'True' or 'False'. by default 'False'

        return:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.cluster.cluster_create(cluster=('F47-F48','3'))
            ...     response1 = device.cluster.cluster_update(cluster=('F47-F48','3'), deploy=True)
            ...     response2 = device.cluster.cluster_get(cluster=('F47-F48','3'))
            ...     response3 = device.cluster.cluster_delete(cluster=('F47-F48','3'))
            ...
        """
        (clname, clid) = cluster_args.pop('cluster')
        isolation_mode = cluster_args.pop('client_isolation_mode', 'loose')
        hold_time = cluster_args.pop('df_hold_time', 3)
        cldeploy = cluster_args.pop('deploy', False)

        self.cluster_validate(clname, int(clid))

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster updated"
        if isolation_mode is 'loose':
            isolation_strict = False
        else:
            isolation_strict = True
        argument = {'cluster': (clname, clid),
                    'client_interfaces_shutdown': False,
                    'client_isolation_strict': isolation_strict,
                    'designated_forwarder_hold_time': hold_time,
                    'deploy': cldeploy
                    }
        config = ('cluster_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def cluster_delete(self, **cluster_args):
        """
        Method to delete cluster
        args:
            cluster_args:
                 cluster: Mandatory
                    cluster_name(str): name of the cluster
                    cluster_id(str): cluster id
        return:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE
        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.cluster.cluster_create(cluster=('F47-F48','3'))
            ...     response1 = device.cluster.cluster_get(cluster=('F47-F48','3'))
            ...     response2 = device.cluster.cluster_delete(cluster=('F47-F48','3'))
            ...
        """
        (clname, clid) = cluster_args.pop('cluster')

        self.cluster_validate(clname, int(clid))

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster deleted"

        argument = {'cluster': (clname, clid),
                    }
        config = ('cluster_delete', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def cluster_peer_create(self, **cluster_args):
        """
        Method to create cluster peer
        args:
            cluster_args:
                 cluster: Mandatory
                    cluster_name(str): name of the cluster
                    cluster_id(str): cluster id
                 peer_info: Optional, 3 tuple of (peer_ip, peer_interface_type, peer_interface)
                     peer_ip(str): Peer Ip address
                     peerintf_type: Peer interface type.
                     peerintf(str): Interface if (X/Y) format.
        return:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE
        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.cluster.cluster_create(cluster=('F47-F48','3'))
            ...     response1 = device.cluster.cluster_peer_create(cluster=('F47-F48','3'),
            ...                                peer_info=('21.0.0.47', 'Ethernet', '0/1'))
            ...     response2 = device.cluster.cluster_get(cluster=('F47-F48','3'))
            ...     response3 = device.cluster.cluster_peer_delete(cluster=('F47-F48','3'),
            ...                                           peer_info=('21.0.0.47'))
            ...     response4 = device.cluster.cluster_delete(cluster=('F47-F48','3'))
            ...
        """
        (clname, clid) = cluster_args.pop('cluster')
        (peerip, peerintf_type, peerintf) = cluster_args.pop('peer_info')

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster peer created"

        self.cluster_validate(clname, int(clid))

        if peerip is None or peerintf is None or peerintf_type is None:
            status['status_code'] = -1
            status['status_message'] = "Peer interface and peer ip are required to add " \
                                       "cluster_peer"
            return status

        argument = {'cluster': (clname, clid),
                    'peer': peerip,
                    }
        config = ('cluster_peer_create', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
                return status
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        argument = {'cluster': (clname, clid),
                    'peer_if_type': peerintf_type, 'peer_if_name': peerintf
                    }
        config = ('cluster_peer_interface_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def cluster_peer_update(self, **cluster_args):
        """
        Method to update cluster peer
        args:
            cluster_args:
                 cluster: Mandatory
                    cluster_name(str): name of the cluster
                    cluster_id(str): cluster id
                 peer_info: Optional, 3 tuple of (peer_ip, peer_interface_type, peer_interface)
                     peerintf_type: Peer interface type.
                     peerintf(str): Interface if (X/Y) format.
        return:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE
        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.cluster.cluster_create(cluster=('F47-F48','3'))
            ...     response1 = device.cluster.cluster_peer_create(cluster=('F47-F48','3'),
            ...                                peer_info=('21.0.0.47', 'Ethernet', '0/1'))
            ...     response2 = device.cluster.cluster_peer_update(cluster=('F47-F48','3'),
            ...                                           peer_info=('Ethernet', '0/1'))
            ...     response3 = device.cluster.cluster_get(cluster=('F47-F48','3'))
            ...     response4 = device.cluster.cluster_peer_delete(cluster=('F47-F48','3'),
            ...                                           peer_info=('21.0.0.47'))
            ...     response5 = device.cluster.cluster_delete(cluster=('F47-F48','3'))
            ...
        """
        (clname, clid) = cluster_args.pop('cluster')
        (peerintf_type, peerintf) = cluster_args.pop('peer_info')

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster configured"

        self.cluster_validate(clname, int(clid))

        argument = {'cluster': (clname, clid),
                    'peer_if_type': peerintf_type, 'peer_if_name': peerintf
                    }
        config = ('cluster_peer_interface_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def cluster_peer_delete(self, **cluster_args):
        """
        Method to update cluster peer. It deletes the peer interface also
        args:
            cluster_args:
                 cluster: Mandatory
                    cluster_name(str): name of the cluster
                    cluster_id(str): cluster id
                 peer_info: peer ip address
        return:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE
        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.84.148'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.cluster.cluster_create(cluster=('F47-F48','3'))
            ...     response1 = device.cluster.cluster_peer_create(cluster=('F47-F48','3'),
            ...                                peer_info=('21.0.0.47', 'Ethernet', '0/1'))
            ...     response2 = device.cluster.cluster_peer_update(cluster=('F47-F48','3'),
            ...                                           peer_info=('Ethernet', '0/1'))
            ...     response3 = device.cluster.cluster_get(cluster=('F47-F48','3'))
            ...     response4 = device.cluster.cluster_peer_delete(cluster=('F47-F48','3'),
            ...                                           peer_info=('21.0.0.47'))
            ...     response5 = device.cluster.cluster_delete(cluster=('F47-F48','3'))
            ...
        """
        (clname, clid) = cluster_args.pop('cluster')
        peerip = cluster_args.pop('peer_info')

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster peer deleted"

        self.cluster_validate(clname, int(clid))

        # Delete the cluster peer interface first
        argument = {'cluster': (clname, clid),
                    }
        config = ('cluster_peer_interface_delete', argument)

        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
                return status
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message
            return status

        # Delete the cluster peer now
        argument = {'cluster': (clname, clid),
                    'peer': peerip,
                    }
        config = ('cluster_peer_delete', argument)

        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
                return status
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def cluster_get(self, **cluster_args):
        """
        Method to get cluster peer
        args:
            cluster_args:
                 cluster: Mandatory
                    cluster_name(str): name of the cluster
                    cluster_id(str): cluster id
        return:
            Returns dictionary keys (cluster_name, cluster_id, peer_interface,
            peer_ip, deploy).
        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.84.148'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.cluster.cluster_create(cluster=('F47-F48','3'))
            ...     response1 = device.cluster.cluster_peer_create(cluster=('F47-F48','3'),
            ...                                peer_info=('21.0.0.47', 'Ethernet', '0/1'))
            ...     response2 = device.cluster.cluster_peer_update(cluster=('F47-F48','3'),
            ...                                           peer_info=('Ethernet', '0/1'))
            ...     response3 = device.cluster.cluster_get(cluster=('F47-F48','3'))
            ...     response4 = device.cluster.cluster_peer_delete(cluster=('F47-F48','3'),
            ...                                           peer_info=('21.0.0.47'))
            ...     response5 = device.cluster.cluster_delete(cluster=('F47-F48','3'))
            ...
        """
        (clname, clid) = cluster_args.pop('cluster')

        argument = {'cluster': (clname, clid),
                    'resource_depth': 5
                    }
        config = ('cluster_get', argument)
        cluster_data = dict()

        # initialize default response dictionary
        cluster_data['cluster_name'] = ''
        cluster_data['cluster_id'] = ''
        cluster_data['peer_interface'] = ''
        cluster_data['peer_ip'] = ''
        cluster_data['deploy'] = ''
        try:
            response = self._callback(config, 'GET')
            root = ET.fromstring(response.data)

            cluster_name_node = root.find('{urn:brocade.com:mgmt:brocade-mct}cluster-name')
            if cluster_name_node is not None:
                cluster_data['cluster_name'] = cluster_name_node.text
            cluster_id_node = root.find('{urn:brocade.com:mgmt:brocade-mct}cluster-id')
            if cluster_id_node is not None:
                cluster_data['cluster_id'] = cluster_id_node.text
            peer_interface_node = root.find('{urn:brocade.com:mgmt:brocade-mct}peer-interface')
            if peer_interface_node is not None:
                peer_interface_type_node = peer_interface_node.find(
                    '{urn:brocade.com:mgmt:brocade-mct}peer-if-type')
                peer_interface_name_node = peer_interface_node.find(
                    '{urn:brocade.com:mgmt:brocade-mct}peer-if-name')
                if peer_interface_type_node is not None and peer_interface_name_node is not None:
                    cluster_data['peer_interface'] = \
                        peer_interface_type_node.text + peer_interface_name_node.text
            peer_node = root.find('{urn:brocade.com:mgmt:brocade-mct}peer')
            if peer_node is not None:
                peer_ip_node = peer_node.find('{urn:brocade.com:mgmt:brocade-mct}peer-ip')
                if peer_ip_node is not None:
                    cluster_data['peer_ip'] = peer_ip_node.text
            deploy_node = root.find('{urn:brocade.com:mgmt:brocade-mct}deploy')
            if deploy_node is not None:
                cluster_data['deploy'] = deploy_node.text

            return (cluster_data)
        except Exception, exc:
            raise ValueError("Failed to get cluster (%s, %s) details Err:%s", clname, clid,
                             exc.message)
