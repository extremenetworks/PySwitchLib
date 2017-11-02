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

import abc


class Acl(object):
    """
    The Acl class holds all the functions assocaiated with the
    Access Control list.
    Attributes:
        None
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, callback):
        """
        ACL init function.
        Args:
            callback: Callback function that will be called for each action.
        Returns:
            ACL Object
        Raises:
            ValueError
        """
        self._callback = callback

    @abc.abstractmethod
    def create_acl(self, **parameters):
        """
        Create an Access Control List.
        Args:
            parameters contains:
                address_type (str): ACL address type, ip or ipv6 or mac.
                acl_type (str): ACL type, extended or standard.
                acl_name (str): Unique name for ACL.
        Returns:
            Return value of `string` message.
        Examples:
        """
        return

    @abc.abstractmethod
    def delete_acl(self, **parameters):
        """
        Delete Access Control List.
        Args:
            parameters contains:
                acl_name (str): Name of the access list.
        Returns:
            Return value of `string` message.
        Examples:
        """
        return

    @abc.abstractmethod
    def parse_params_for_add_l2_acl_rule(self, **parameters):
        """
        Parse params of rule to be added to l2 Access Control List.
        Args:
            parameters contains:
                acl_name (str): Name of the access list.

                seq_id: integer
                action: string enum: - deny - permit
                source: string: Source filter, can be 'any' or 'host', or the
                    actual MAC in HHHH.HHHH.HHHH format.
                srchost: string: The source MAC in HHHH.HHHH.HHHH format.
                    The value is required only when the source is 'host'.
                src_mac_addr_mask: string : Mask for the source MAC in
                    HHHH.HHHH.HHHH format.
                dst: string: Destination filter, can be 'any' or 'host',
                    or the actual MAC of the destination in
                    HHHH.HHHH.HHHH format.
                dsthost: string : Destination MAC in HHHH.HHHH.HHHH format.
                    The value is required only when the dst is 'host'
                dst_mac_addr_mask: string: Mask for the destination MAC
                    in HHHH.HHHH.HHHH format.
                vlan: VLAN IDs - 'any' or 1-4096
                ethertype: EtherType, can be 'arp', 'fcoe', 'ipv4-15' 'ipv6' or
                    custom value between 1536 and 65535.
                arp_guard: string : Enables arp-guard for the rule
                drop_precedence_force: Matches the specified value against the
                    drop_precedence value of the packet to filter.
                    Allowed values are 0 through 2.
                log: Enables the logging
                mirror: Enables mirror for the rule
                priority
                priority_force
                priority_mapping
        Returns:
            Return value of `string` message.
        Examples:
        """
        return

    @abc.abstractmethod
    def add_l2_acl_rule(self, **parameters):
        """
        Delete Access Control List.
        Args:
            parameters contains:
                acl_name (str): Name of the access list.

                seq_id: integer
                action: string enum: - deny - permit - hard-drop
                source: string: Source filter, can be 'any' or 'host',
                    or the actual MAC in HHHH.HHHH.HHHH format.
                src_mac_addr_mask: string : Mask for the source MAC in
                    HHHH.HHHH.HHHH format.
                dst: string: Destination filter, can be 'any' or 'host',
                    or the actual MAC of the destination in
                    HHHH.HHHH.HHHH format.
                dst_mac_addr_mask: Mask for the destination MAC in
                    HHHH.HHHH.HHHH format.
                vlan: VLAN IDs - 'any' or 1-4096.
                ethertype: EtherType can be 'arp', 'fcoe', 'ipv4-15', 'ipv6' or
                    custom value between 1536 and 65535.
                arp_guard: string : Enables arp-guard for the rule
                drop_precedence_force: string : Matches the specified value
                    against the drop_precedence value of the packet to filter.
                    Allowed values are 0 through 2.
                log: Enables the logging
                mirror: Enables mirror for the rule

        Returns:
            Return value of `string` message.
        Examples:
        """
        return

    @abc.abstractmethod
    def delete_l2_acl_rule(self, **parameters):
        """
        Delete Rule from Access Control List.
        Args:
            parameters contains:
                acl_name: Name of the access list.
                seq_id: Sequence number of the rule. For add operation,
                    if not specified, the rule is added at the end of the list.
        Returns:
            Return value of `string` message.
        Examples:
        """
        return

    @abc.abstractmethod
    def is_valid_seq_id(self, seq_id, acl_name):
        """
        is_valid_seq_id checks for existane of seq_id.
        Args:
            acl_name (str): Name of the access list.
            seq_id, action, source, srchost,
        Returns:
            Return True
        Raises:
            Exception, ValueError for invalid seq_id.
        Examples:
        """
        return

    @abc.abstractmethod
    def add_ipv4_rule_acl(self, **parameters):
        """
        Apply Access Control List on interface.
        Args:
            parameters contains:
                acl_name: (string) Name of the access list
                seq_id: (integer) Sequence number of the rule,
                    if not specified, the rule is added at the end of the list.
                    Valid range is 0 to 4294967290
                action: (string) Action performed by ACL rule
                    - permit
                    - deny
                protocol_type: (string) Type of IP packets to be filtered
                    based on protocol. Valid values are <0-255> or key words
                    tcp, udp, icmp or ip
                source: (string) Source address filters
                    { any | S_IPaddress/mask(0.0.0.255) |
                    host,S_IPaddress } [ source-operator [ S_port-numbers ] ]
                destination: (string) Destination address filters
                    { any | S_IPaddress/mask(0.0.0.255) |
                    host,S_IPaddress } [ source-operator [ S_port-numbers ] ]
                dscp: (string) Matches the specified value against the DSCP
                    value of the packet to filter.
                     Allowed values are 0 through 63.
                drop_precedence_force: (string) Matches the drop_precedence
                    value of the packet.  Allowed values are 0 through 2.
                urg: (string) Enables urg for the rule
                ack: (string) Enables ack for the rule
                push: (string) Enables push for the rule
                fin: (string) Enables fin for the rule
                rst: (string) Enables rst for the rule
                sync: (string) Enables sync for the rule
                vlan_id: (integer) VLAN interface to which the ACL is bound
                count: (string) Enables statistics for the rule
                log: (string) Enables logging for the rule
                    (Available for permit or deny only)
                mirror: (string) Enables mirror for the rule
                copy_sflow: (string) Enables copy-sflow for the rule
        Returns:
            Return True
        Raises:
            Exception, ValueError for invalid seq_id.
        """
        return

    def delete_ipv4_acl_rule(self, **parameters):
        """
        Delete Rule from Access Control List.
        Args:
            parameters contains:
                acl_name: Name of the access list.
                seq_id: Sequence number of the rule. For add operation,
                    if not specified, the rule is added at the end of the list.
        Returns:
            Return value of `string` message.
        Raise:
            Raises ValueError, Exception
        Examples:
        """
        return

    def _process_cli_output(self, method, config, output):
        """
        Parses CLI response from switch.

        Args:
            output string contains the response from switch.

        Returns:
            None

        Raises:
            ValueError, Exception
        """

        ret = method + ' : Successful'

        for line in output.split('\n'):
            if 'Invalid input ' in line or 'error' in line.lower():
                ret = method + ' [ ' + config + ' ]: failed ' + line

        return ret
