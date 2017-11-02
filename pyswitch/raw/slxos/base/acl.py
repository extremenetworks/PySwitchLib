"""
Copyright 2017 Brocade Communications Systems, Inc.

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

from pyswitch.raw.base.acl import Acl as BaseAcl


class Acl(BaseAcl):
    """
    The Acl class holds all the actions assocaiated with the Access Control list
    of a SLX device.

    Attributes:
        None
    """

    os_type = "slxos"

    seq_variables_ip_std = ('seq_id', 'action', 'src_host_any_sip', 'src_host_ip',
                            'src_mask', 'count', 'log', 'copy-sflow')

    seq_variables_ip_ext = ('seq_id', 'action', 'protocol_type', 'src_host_any_sip',
                            'src_host_ip', 'src_mask', 'sport', 'sport_number_eq_neq_tcp',
                            'sport_number_lt_tcp', 'sport_number_gt_tcp',
                            'sport_number_eq_neq_udp', 'sport_number_lt_udp',
                            'sport_number_gt_udp', 'sport_number_range_lower_tcp',
                            'sport_number_range_lower_udp', 'sport_number_range_higher_tcp',
                            'sport_number_range_higher_udp', 'dst_host_any_dip', 'dst_host_ip',
                            'dst_mask', 'dport', 'dport_number_eq_neq_tcp',
                            'dport_number_lt_tcp', 'dport_number_gt_tcp',
                            'dport_number_eq_neq_udp', 'dport_number_lt_udp',
                            'dport_number_gt_udp', 'dport_number_range_lower_tcp',
                            'dport_number_range_lower_udp', 'dport_number_range_higher_tcp',
                            'dport_number_range_higher_udp', 'dscp', 'dscp-force',
                            'drop-precedence-force', 'urg', 'ack', 'push', 'fin', 'rst',
                            'sync', 'vlan', 'count', 'log', 'mirror', 'copy-sflow')

    seq_variables_mac_std = ('seq_id', 'action', 'source', 'srchost',
                             'src_mac_addr_mask', 'count', 'log', 'copy-sflow')

    seq_variables_mac_ext = ('seq_id', 'action', 'source', 'srchost',
                             'src_mac_addr_mask', 'dst', 'dsthost',
                             'dst_mac_addr_mask', 'vlan-tag-format', 'vlan',
                             'vlan-id-mask', 'outer-vlan', 'outer-vlan-id-mask',
                             'inner-vlan', 'inner-vlan-id-mask', 'ethertype',
                             'arp-guard', 'pcp', 'pcp-force', 'drop-precedence-force',
                             'count', 'log', 'mirror', 'copy-sflow')

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
        super(Acl, self).__init__(callback)
