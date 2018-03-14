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

import socket
from aclparam_parser import AclParamParser


class Ipv6Acl(AclParamParser):
    """
    The Ipv6Acl class holds all the functions assocaiated with
    IPv6 Access Control list.
    Attributes:
        None
    """

    def parse_vlan(self, **parameters):
        """
        parse the vlan param
        Args:
            parameters contains:
                vlan_id(integer): 1-4096
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'vlan_id' not in parameters:
            return None

        vlan = parameters['vlan_id']

        if not vlan:
            return None

        if vlan > 0 and vlan < 4096:
            return 'vlan ' + str(vlan)

        raise ValueError("The \'vlan\' value {} is invalid."
                         " Specify \'1-4095\' supported values")

    def parse_protocol(self, **parameters):
        """
        parse the protocol param
        Args:
            parameters contains:
                protocol_type: (string) Type of IP packets to be filtered
                    based on protocol. Valid values are <0-255> or
                    key words tcp, udp, icmp or ip
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'protocol_type' not in parameters or \
                not parameters['protocol_type']:
            raise ValueError("\'protocol_type\' is required for MLX device")

        protocol_type = parameters['protocol_type']

        if protocol_type.isdigit():
            if int(protocol_type) >= 0 and int(protocol_type) <= 255:
                return protocol_type

        if protocol_type in ['ahp', 'esp', 'icmp', 'ipv6',
                             'sctp', 'tcp', 'udp']:
            return protocol_type

        raise ValueError("The \'protocol\' value {} is invalid. Specify one "
                         "of these - ahp, esp, icmp, ipv6, sctp, tcp, udp "
                         "or a number between 0 and 255"
                         .format(protocol_type))

    def _validate_ipv6(self, addr):
        addr = ' '.join(addr.split())
        try:
            socket.inet_pton(socket.AF_INET6, addr)
        except socket.error as se:
            raise ValueError(str(se) + 'Invalid address: ' + addr)

    def _validate_op_str(self, op_str):
        op_str = ' '.join(op_str.split()).split()

        if len(op_str) == 2:
            if op_str[0] in ['neq', 'lt', 'gt', 'eq']:
                return True
        elif len(op_str) == 3 and op_str[0] == 'range':
            return True

        raise ValueError('Invalid tcp-udp-operator: ' + ' '.join(op_str))

    def _parse_source_destination(self, protocol_type, input_param):

        v6_str = input_param
        op_str = ''
        op_index = -1
        for tcp_udp_op in ['range', 'neq', 'lt', 'gt', 'eq']:
            op_index = input_param.find(tcp_udp_op)
            if op_index >= 0:
                op_str = input_param[op_index:]
                v6_str = input_param[0:op_index]
                break

        if protocol_type not in ['tcp', 'udp'] and op_str:
            raise ValueError("tcp udp operator is supported only for."
                             "protocol_type = tcp or udp")

        if op_str:
            self._validate_op_str(op_str)

        if v6_str[0:3] == "any":
            return v6_str + ' ' + op_str

        if v6_str[0:4] == "host":
            self._validate_ipv6(v6_str[5:])
            return v6_str + ' ' + op_str

        if '/' in v6_str:
            self._validate_ipv6(v6_str.split('/')[0])
            return v6_str + ' ' + op_str

        ip, mask = v6_str.split()
        self._validate_ipv6(ip)
        self._validate_ipv6(mask)
        return v6_str + ' ' + op_str

    def parse_source(self, **parameters):
        """
        parse the source param.
        Args:
            parameters contains:
                source (string): Source filter, can be of below format
                    Len=1 or 3  X:X::X:X/M IPv6 source prefix (2:2::2:2/64)
                    Len=1 or 3  any Any source host (any)
                    Len=2 or 4  IPv6 source address (2:2::2:2 0:0::FFFF:FFFF)
                    Len=2 or 4  host A single source host (host 2:2::2:2)
                    followed by [ source-operator [ S_port-numbers ] ]
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'source' not in parameters or not parameters['source']:
            raise ValueError("Missing \'source\' is parameters")

        if 'protocol_type' not in parameters or \
                not parameters['protocol_type']:
            raise ValueError("\'protocol_type\' is required for MLX device")

        src = parameters['source']
        src = ' '.join(src.split())

        return self._parse_source_destination(parameters['protocol_type'], src)

    def parse_destination(self, **parameters):
        """
        parse the destination param.
        Args:
            parameters contains:
                destination (string): destination filter, can be of format:
                    X:X::X:X/M IPv6 destination prefix (2:2::2:2/64)
                    any Any destination host (any)
                    IPv6 destination address (2:2::2:2 0:0::FFFF:FFFF)
                    host A single destination host (host 2:2::2:2)
                        followed by [ destination-operator [ S_port-numbers ] ]
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'destination' not in parameters or not parameters['destination']:
            raise ValueError("\'destination\' is required param")

        if 'protocol_type' not in parameters or \
                not parameters['protocol_type']:
            raise ValueError("\'protocol_type\' is required for MLX device")

        dst = parameters['destination']
        dst = ' '.join(dst.split())

        return self._parse_source_destination(parameters['protocol_type'], dst)

    def parse_dscp_mapping(self, **parameters):
        """
        parse the dscp mapping param.
        Args:
            parameters contains:
                dscp: (string) Matches the specified value against the DSCP
                    value of the packet to filter.
                     Allowed values are 0 through 63.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'dscp' not in parameters:
            return None

        if not parameters['dscp']:
            return None

        dscp_mapping = parameters['dscp']
        dscp_mapping = ' '.join(dscp_mapping.split())

        if dscp_mapping.isdigit():
            if int(dscp_mapping) >= 0 and int(dscp_mapping) <= 63:
                return 'dscp ' + dscp_mapping

        raise ValueError("Invalid dscp_mapping {}. Supported range is "
                         "<0-63>".format(dscp_mapping))

    def parse_fragment(self, **parameters):
        """
        parse the dscp mapping param.
        Args:
            parameters contains:
                dscp: (string) Matches the specified value against the DSCP
                    value of the packet to filter.
                     Allowed values are 0 through 63.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'fragment' not in parameters:
            return None

        if 'protocol_type' not in parameters or \
                not parameters['protocol_type']:
            raise ValueError("\'protocol_type\' is required for MLX device")

        if parameters['fragment']:
            if parameters['protocol_type'] != 'ipv6':
                raise ValueError("\'fragment\' can be set for ipv6 only.")
            return 'fragments'

        return None

    def parse_drop_precedence(self, **parameters):
        """
        parse the drop_precedence param
        Args:
            parameters contains:
                drop_precedence( string): Matches the specified value
                    against the drop_precedence value of the packet to
                    filter.  Allowed values are 0 through 3.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence' not in parameters:
            return None

        if not parameters['drop_precedence']:
            return None

        drop_precedence = parameters['drop_precedence']

        if drop_precedence.isdigit():
            if int(drop_precedence) >= 0 or int(drop_precedence) <= 3:
                    return 'drop-precedence ' + drop_precedence

        raise ValueError("The \'drop-precedence\' value {} is invalid."
                         " Supported range is 0 to 3".format(drop_precedence))

    def parse_drop_precedence_force(self, **parameters):
        """
        parse the drop_precedence_force param
        Args:
            parameters contains:
                drop_precedence_force( string): Matches the specified value
                    against the drop_precedence_force value of the packet to
                    filter.  Allowed values are 0 through 3.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence_force' not in parameters:
            return None

        if not parameters['drop_precedence_force']:
            return None

        drop_precedence_force = parameters['drop_precedence_force']

        if drop_precedence_force.isdigit():
            if int(drop_precedence_force) >= 0 or \
               int(drop_precedence_force) <= 3:
                return 'drop-precedence-force ' + drop_precedence_force

        raise ValueError("The \'drop-precedence-force\' value {} is invalid."
                         " Supported range is 0 to 3"
                         .format(drop_precedence_force))

    def parse_dscp_marking(self, **parameters):
        """
        parse the dscp mapping param.
        Args:
            parameters contains:
                dscp: (string) Matches the specified value against the DSCP
                    value of the packet to filter.
                     Allowed values are 0 through 63.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'dscp_marking' not in parameters:
            return None

        if not parameters['dscp_marking']:
            return None

        dscp_marking = parameters['dscp_marking']
        dscp_marking = ' '.join(dscp_marking.split())

        if dscp_marking.isdigit():
            if int(dscp_marking) >= 0 and int(dscp_marking) <= 63:
                return 'dscp-marking ' + dscp_marking

        raise ValueError("Invalid dscp_marking {}. Supported range is "
                         "<0-63>".format(dscp_marking))

    def parse_priority_force(self, **parameters):
        """
        parse the priority_force mapping param.
        Args:
            parameters contains:
                priority_force(integer): set priority_forcer.
                    Allowed value is <0-7>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority_force' not in parameters:
            return None

        priority_force = parameters['priority_force']
        if not priority_force:
            return None

        if priority_force >= 0 and priority_force <= 7:
            return 'priority-force ' + str(priority_force)

        raise ValueError("Invalid priority_force {}. "
                         "Allowed value in decimal <0-7>."
                         .format(priority_force))

    def parse_priority_mapping(self, **parameters):
        """
        parse the priority_mapping mapping param.
        Args:
            parameters contains:
                priority_mapping(integer): set priority_mappingr.
                    Allowed value is <0-7>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority_mapping' not in parameters:
            return None

        priority_mapping = parameters['priority_mapping']
        if not priority_mapping:
            return None

        if priority_mapping >= 0 and priority_mapping <= 7:
            return 'priority-mapping ' + str(priority_mapping)

        raise ValueError("Invalid priority_mapping {}. "
                         "Allowed value in decimal <0-7>."
                         .format(priority_mapping))

    def parse_suppress_rpf_drop(self, **parameters):
        """
        parse the suppress_rpf_drop mapping param.
        Args:
            parameters contains:
                suppress_rpf_drop (boolean):Permit packets that fail RPF check
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'suppress_rpf_drop' not in parameters:
            return None
        suppress_rpf_drop = parameters['suppress_rpf_drop']
        if not suppress_rpf_drop:
            return None

        return 'suppress-rpf-drop'

    def parse_icmp_filter(self, **parameters):
        """
        parse the icmp_type and icmp_code param
        Args:
            parameters contains:
                icmp_filter(string): The string contains vlaues in below format
                [ [icmp-type <vlaue>] [icmp-code <value> ] ] |
                [ icmp-message <value> ]
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        if 'icmp_filter' not in parameters or not parameters['icmp_filter']:
            return None

        if 'protocol_type' not in parameters or \
                not parameters['protocol_type'] or \
                parameters['protocol_type'] != 'icmp':

            raise ValueError("icmp filter is supported only for."
                             "protocol_type = icmp")

        icmp_filter = parameters['icmp_filter']
        icmp_filter = ' '.join(icmp_filter.split()).split()

        if icmp_filter[0].isdigit():
            return self._parse_icmp_type_and_code(*icmp_filter)
        else:
            return self._parse_icmp_message(*icmp_filter)

    def _parse_icmp_type_and_code(self, icmp_type, icmp_code=None):
        """
        parse the icmp_type and icmp_code param
        Args:
            icmp_type(integer): Validate an ICMP type.
            icmp_code(integer): Validate an ICMP code.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        ret = None

        if int(icmp_type) >= 0 and int(icmp_type) <= 255:
            ret = icmp_type

            if icmp_code:
                if int(icmp_code) >= 0 and int(icmp_code) <= 255:
                    ret = ret + ' ' + icmp_code

        return ret

    def _parse_icmp_message(self, icmp_message):
        """
        parse the icmp_message param
        Args:
            icmp_message(string): Validate an ICMP message.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        if icmp_message in ['beyond-scope', 'destination-unreachable',
                            'dscp', 'echo-reply', 'echo-request',
                            'flow-label', 'fragments', 'header',
                            'hop-limit', 'mld-query', 'mld-reduction',
                            'mld-report', 'nd-na', 'nd-ns',
                            'next-header', 'no-admin', 'no-route',
                            'packet-too-big', 'parameter-option',
                            'parameter-problem', 'port-unreachable',
                            'reassembly-timeout', 'renum-command',
                            'renum-result', 'renum-seq-number',
                            'router-advertisement',
                            'router-renumbering',
                            'router-solicitation', 'routing',
                            'sequence', 'time-exceeded',
                            'unreachable']:
            return icmp_message
        raise ValueError("{} icmp message not supported."
                         "Refer config guide for supported messages"
                         .format(icmp_message))

    def parse_tcp_operator(self, **parameters):
        """
        parse the icmp_message param
        Args:
            parameters contains:
                tcp_operator(string): Validate comparison operator for TCP port
                    This parameter works only for tcp protocol.
                    Allowed values are : established or syn
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'tcp_operator' in parameters and parameters['tcp_operator']:
            tcp_operator = parameters['tcp_operator']

            if 'protocol_type' not in parameters or \
                    not parameters['protocol_type'] or \
                    parameters['protocol_type'] != 'tcp':

                raise ValueError("{} tcp operator is supported only for."
                                 "protocol_type = tcp"
                                 .format(tcp_operator))

            if tcp_operator in ['established', 'syn', 'established syn',
                                'syn established']:
                return tcp_operator

            raise ValueError("Only supported tcp operator are: "
                             "established and/or syn")
        return None
