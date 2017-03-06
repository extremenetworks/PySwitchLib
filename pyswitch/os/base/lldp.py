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
import pyswitch.utilities as util


class LLDP(object):
    """LLDP class containing LLDP methods and attributes.
    """

    def __init__(self, callback):
        """LLDP init method.

        Args:
            callback (function): Callback function that will be called for each
                action.

        Returns:
            LLDP Object

        Raises:
            None
        """
        self._callback = callback

    def neighbors(self, **kwargs):
        """list[dict]: A list of dictionary items describing the operational
        state of LLDP.
        """

        result = []
        has_more = ''
        last_ifindex = ''
        rbridge_id = None
        if 'rbridge_id' in kwargs:
            rbridge_id = kwargs.pop('rbridge_id')
        while (has_more == '') or (has_more == 'true'):
            request_lldp = self.get_lldp_neighbors_request(last_ifindex,
                                                           rbridge_id)

            lldp_result = self._callback(request_lldp, handler='get')

            has_more = util.find(lldp_result.json, '$..has-more')

            for item in util.findlist(lldp_result.json, '$..lldp-neighbor-detail'):

                local_int_name = util.findText(item, '$..local-interface-name')
                local_int_mac = util.findText(item, '$..local-interface-mac')
                last_ifindex = util.findText(
                    item, '$..local-interface-ifindex')
                remote_int_name = util.findText(
                    item, '$..remote-interface-name')
                remote_int_mac = util.findText(item, '$..remote-interface-mac')
                remote_chas_id = util.findText(item, '$..remote-chassis-id')

                remote_sys_name = util.findText(item, '$..remote-system-name')

                remote_sys_desc = util.findText(
                    item, '$..remote-system-description')

                remote_mgmt_addr = util.findText(
                    item, '$..remote-management-address')

                if 'Fo ' in local_int_name:
                    local_int_name = local_int_name.replace(
                        'Fo ',
                        'FortyGigabitEthernet '
                    )
                if 'Te ' in local_int_name:
                    local_int_name = local_int_name.replace(
                        'Te ',
                        'TenGigabitEthernet '
                    )
                if 'Eth ' in local_int_name:
                    local_int_name = local_int_name.replace(
                        'Eth ',
                        'Ethernet '
                    )

                item_results = {'local-int-name': local_int_name,
                                'local-int-mac': local_int_mac,
                                'remote-int-name': remote_int_name,
                                'remote-int-mac': remote_int_mac,
                                'remote-chassis-id': remote_chas_id,
                                'remote-system-name': remote_sys_name,
                                'remote-system-description': remote_sys_desc,
                                'remote-management-address': remote_mgmt_addr}
                result.append(item_results)

        return result

    def get_lldp_neighbors_request(self, last_ifindex, rbridge_id):
        """ Creates a new Netconf request based on the last received or if
        rbridge_id is specifed
        ifindex when the hasMore flag is true
        """
        arguments = {}

        if rbridge_id is not None:
            arguments = {'rbridge_id': rbridge_id}
        elif last_ifindex != '':
            arguments = {'last_rcvd_ifindex': last_ifindex}

        return ('get_lldp_neighbor_detail_rpc', arguments)


0
