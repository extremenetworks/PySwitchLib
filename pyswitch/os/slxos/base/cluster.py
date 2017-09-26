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
from pyswitch.utilities import Util

class Cluster(object):
    """
    cluster class containing all methods and attributes for configuring mct cluster
    """

    def __init__(self, callback):
        """System init method.

                Args:
                    callback: Callback function that will be called for each action.

                Returns:
                    System Object

                Raises:
                    None
                """
        self._callback = callback

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

        return:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE
        """
        (clname, clid) = cluster_args.pop('cluster')
        isolation_mode = cluster_args.pop('client_isolation_mode', 'loose')
        hold_time = cluster_args.pop('df_hold_time', 3)
        cldeploy = cluster_args.pop('deploy', False)

        if clid not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`" + clid)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster configured"
        if isolation_mode is 'loose':
            isolation_strict = False
        else:
            isolation_strict = True
        argument = {'cluster':(clname, clid),
                    'client_interfaces_shutdown':False,
                    'client_isolation_strict':isolation_strict,
                    'designated_forwarder_hold_time':hold_time,
                    'deploy':cldeploy
                    }
        config = ('cluster_create', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:'+response.data

        return status

    def cluster_update(self, **cluster_args):
        (clname, clid) = cluster_args.pop('cluster')
        isolation_mode = cluster_args.pop('client_isolation_mode', 'loose')
        hold_time = cluster_args.pop('df_hold_time', 3)
        cldeploy = cluster_args.pop('deploy', False)

        if clid not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`" + clid)

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
            status['status_message'] = 'Exception:'+exc.message

        return status

    def cluster_delete(self, **cluster_args):
        (clname, clid) = cluster_args.pop('cluster')

        if clid not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`" + clid)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster configured"

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
        (clname, clid) = cluster_args.pop('cluster')
        (peerip, peerintf_type, peerintf) = cluster_args.pop('peer_info', None)

        status = dict()
        #set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster configured"

        if clid not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`" + clid)

        if peerip is None or peerintf is None or peerintf_type is None:
            status['status_code'] = -1
            status['status_message'] = "Peer interface and peer ip are required to add " \
                                       "cluster_peer"
            return  status

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
            status['status_message'] = 'Exception:'+exc.message

        argument = {'cluster': (clname, clid),
                    'peer_if_type': peerintf_type, 'peer_if_name':peerintf
                    }
        config = ('cluster_peer_interface_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:'+exc.message

        return status

    def cluster_peer_update(self, **cluster_args):
        (clname, clid) = cluster_args.pop('cluster')
        (peerintf_type, peerintf) = cluster_args.pop('peer_info', None)

        status = dict()
        response = None
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster configured"

        if clid not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`" + clid)

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
            status['status_message'] = 'Exception:'+exc.message

        return status

    def cluster_peer_delete(self, **cluster_args):
        (clname, clid) = cluster_args.pop('cluster')
        peerip = cluster_args.pop('peer_info', None)

        status = dict()
        #set default status buffer
        status['status_code'] = 0
        status['status_message'] = "cluster configured"

        if clid not in xrange(1, 65536):
            raise ValueError("cluster_id %s must be in range `1-65535`" + clid)

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
            status['status_message'] = 'Exception:'+exc.message

        return status

    def cluster_get(self, **cluster_args):
        (clname, clid) = cluster_args.pop('cluster')

        argument = {'cluster': (clname, clid)
                    }
        config = ('cluster_get', argument)
        try:
            response = self._callback(config, 'GET')
            print(response)
        except Exception, exc:
            print(exc.message)
