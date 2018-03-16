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


class IpAcl(AclParamParser):
    """
    The IpAcl class holds all the functions assocaiated with
    IP Access Control list.
    Attributes:
        None
    """

    def _validate_op_str(self, op_str):
        op_str = ' '.join(op_str.split()).split()

        if len(op_str) == 2:
            if (op_str[0] == 'neq' or op_str[0] == 'lt' or
                    op_str[0] == 'gt' or op_str[0] == 'eq'):
                return True
        elif len(op_str) == 3 and op_str[0] == 'range':
            return True

        raise ValueError('Invalid tcp-udp-operator: ' + ' '.join(op_str))

    def _validate_ipv4(self, addr):
        addr = ' '.join(addr.split())
        try:
            socket.inet_aton(addr)
        except socket.error:
            raise ValueError('Invalid address: ' + addr)

    def _parse_source_destination(self, protocol_type, input_param):

        v4_str = input_param
        op_str = ''
        op_index = -1
        for tcp_udp_op in ['range', 'neq', 'lt', 'gt', 'eq']:
            op_index = input_param.find(tcp_udp_op)
            if op_index >= 0:
                op_str = input_param[op_index:]
                v4_str = input_param[0:op_index]
                break

        if protocol_type not in ['tcp', 'udp'] and op_str:
            raise ValueError("tcp udp operator is supported only for."
                             "protocol_type = tcp or udp")

        if op_str:
            self._validate_op_str(op_str)

        if v4_str[0:3] == "any":
            return v4_str + ' ' + op_str

        if v4_str[0:4] == "host":
            return v4_str[0:4] + ' ' + v4_str[5:] + ' ' + op_str

        v4_str = ' '.join(v4_str.split())
        if '/' in v4_str:
            ip, prefix_len = v4_str.split('/')
            self._validate_ipv4(ip)

            if prefix_len.isdigit():
                if int(prefix_len) < 0 or int(prefix_len) > 32:
                    raise ValueError('Invalid address: ' + v4_str)
                return v4_str + ' ' + op_str
            else:
                self._validate_ipv4(prefix_len)
                return ip + ' ' + prefix_len + ' ' + op_str

        ip, mask = v4_str.split()
        self._validate_ipv4(ip)
        self._validate_ipv4(mask)
        return v4_str + ' ' + op_str

    def parse_source(self, **parameters):
        """
        parse the source param.
        Args:
            parameters contains:
                source (string): Source filter, can be 'any' or
                    the MAC/Mask in HHHH.HHHH.HHHH/mask or
                    the host Mask in HHHH.HHHH.HHHH or
                    host <name | ip >
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'source' not in parameters or not parameters['source']:
            raise ValueError("Missing \'source\' in parameters")

        protocol_type = None
        if 'protocol_type' in parameters and parameters['protocol_type']:
            protocol_type = parameters['protocol_type']

        src = parameters['source']
        src = ' '.join(src.split())

        return self._parse_source_destination(protocol_type, src)

    def parse_destination(self, **parameters):
        """
        parse the destination param.
        Args:
            parameters contains:
                destination (string): destination filter, can be 'any' or
                    the MAC/Mask in HHHH.HHHH.HHHH/mask or
                    the host Mask in HHHH.HHHH.HHHH or
                    host <name | ip >
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
            return str(vlan)

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
        if 'protocol_type' not in parameters:
            return None

        protocol_type = parameters['protocol_type']

        if not protocol_type:
            return None

        if protocol_type.isdigit():
            if int(protocol_type) < 0 or int(protocol_type) > 255:
                raise ValueError("The \'protocol\' value {} is invalid."
                                 " Specify \'0-255\' supported values"
                                 .format(protocol_type))
        elif protocol_type not in ['a_n', 'ahp', 'argus', 'aris', 'ax25',
                                   'bbn-rcc', 'bna', 'br-sat-mon', 'cbt',
                                   'cftp', 'chaos', 'compaq-peer', 'cphb',
                                   'cpnx', 'crdup', 'crtp', 'dcn', 'ddp',
                                   'ddx', 'dgp', 'divert', 'egp', 'emcon',
                                   'encap', 'esp', 'etherip', 'fc', 'fire',
                                   'ggp', 'gmtp', 'gre', 'hip', 'hmp',
                                   'i-nlsp', 'iatp', 'icmp', 'idpr',
                                   'idpr-cmtp', 'idrp', 'ifmp', 'igmp', 'igp',
                                   'igrp', 'il', 'ip', 'ipcomp', 'ipcv',
                                   'ipencap', 'ipip', 'iplt', 'ippc', 'ipv6',
                                   'ipv6-frag', 'ipv6-icmp', 'ipv6-nonxt',
                                   'ipv6-opts', 'ipv6-route', 'ipx-in-ip',
                                   'irtp', 'isis', 'iso-ip', 'iso-tp4',
                                   'kryptolan', 'l2tp', 'larp', 'leaf-1',
                                   'leaf-2', 'manet', 'merit-inp', 'mfe-nsp',
                                   'mhrp', 'micp', 'mobile', 'mobility-header',
                                   'mpls-in-ip', 'mtp', 'mux', 'narp',
                                   'netblt', 'nsfnet-igp', 'nvp', 'ospf',
                                   'pgm', 'pim', 'pipe', 'pnni', 'prm', 'ptp',
                                   'pup', 'pvp', 'qnx', 'rdp', 'rsvp',
                                   'rsvp-e2e-ignore', 'rvd', 'sat-expak',
                                   'sat-mon', 'scc-sp', 'scps', 'sctp', 'sdrp',
                                   'secure-vmtp', 'sep', 'shim6', 'skip', 'sm',
                                   'smp', 'snp', 'sprite-rpc', 'sps', 'srp',
                                   'sscopmce', 'st', 'st2', 'sun-nd', 'swipe',
                                   'tcf', 'tcp', 'third-pc', 'tlsp', 'tp++',
                                   'trunk-1', 'trunk-2', 'ttp', 'udp',
                                   'udplite', 'uti', 'vines', 'visa', 'vlan',
                                   'vmtp', 'vrrp', 'wb-expak', 'wb-mon', 'wsn',
                                   'xnet', 'xns-idp', 'xtp']:
            raise ValueError("invalid \'protocol_type\' value {}."
                             .format(protocol_type))

        return str(protocol_type)

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
        if 'dscp' not in parameters or not parameters['dscp']:
            return None

        dscp_mapping = parameters['dscp']
        dscp_mapping = ' '.join(dscp_mapping.split())

        if dscp_mapping.isdigit():
            if int(dscp_mapping) >= 0 and int(dscp_mapping) <= 63:
                return 'dscp-mapping ' + dscp_mapping

        raise ValueError("Invalid dscp_mapping {}. Supported range is "
                         "<0-63>".format(dscp_mapping))

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
        if 'dscp_marking' not in parameters or not parameters['dscp_marking']:
            return None

        dscp_marking = parameters['dscp_marking']
        dscp_marking = ' '.join(dscp_marking.split())

        if dscp_marking.isdigit():
            if int(dscp_marking) >= 0 and int(dscp_marking) <= 63:
                return 'dscp-marking ' + dscp_marking

        raise ValueError("Invalid dscp_marking {}. Supported range is "
                         "<0-63>".format(dscp_marking))

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
        if 'fragment' not in parameters or not parameters['fragment']:
            return None

        fragment = parameters['fragment']
        fragment = ' '.join(fragment.split())

        if fragment in ['fragment', 'non-fragment']:
            return fragment

        raise ValueError("Invalid fragment {}. Supported values are "
                         "fragment or non-fragment".format(fragment))

    def parse_precedence(self, **parameters):
        """
        parse the precedence mapping param.
        Args:
            parameters contains:
                precedence:
                  type: string
                  description: Match packets with given precedence value.
                      Allowed value { <0 to 7> | critical | flash |
                      flash-override | immediate | internet | network |
                      priority | routine  }
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'precedence' not in parameters or not parameters['precedence']:
            return None

        precedence = parameters['precedence']
        precedence = ' '.join(precedence.split())

        if precedence.isdigit():
            if int(precedence) >= 0 and int(precedence) <= 7:
                return 'precedence ' + precedence
        if precedence in ['critical', 'flash', 'flash-override',
                          'immediate', 'internet', 'network',
                          'priority', 'routine']:
                return 'precedence ' + precedence

        raise ValueError("Invalid precedence {}. Supported values are "
                         "<0 to 7> | critical | flash |"
                         "flash-override | immediate | internet | network |"
                         "priority | routine ".format(precedence))

    def _is_tcp_udp_opstr_set(self, protocol_type, input_param):
        for tcp_udp_op in ['range', 'neq', 'lt', 'gt', 'eq']:
            op_index = input_param.find(tcp_udp_op)
            if op_index >= 0:
                raise ValueError('option keyword cannot be used along with TCP'
                                 ' destination port matching')
        return True

    def parse_option(self, **parameters):
        """
        parse the option mapping param.
        Args:
            parameters contains:
                option (string): Match match IP option packets.
                    supported values are -
                        any, eol, extended-security, ignore, loose-source-route
                        no-op, record-route, router-alert, security, streamid,
                        strict-source-route, timestamp
                        Allowed value in decimal <0-255>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'option' not in parameters or not parameters['option']:
            return None

        if 'protocol_type' in parameters and parameters['protocol_type'] and \
                parameters['protocol_type'] in ['tcp', 'udp']:

            if 'source' in parameters and parameters['source']:
                src = parameters['source']
                src = ' '.join(src.split())
                self._is_tcp_udp_opstr_set(parameters['protocol_type'], src)

            if 'destination' in parameters and parameters['destination']:
                dst = parameters['destination']
                dst = ' '.join(src.split())
                self._is_tcp_udp_opstr_set(parameters['protocol_type'], dst)

        option = parameters['option']
        option = ' '.join(option.split())

        if option.isdigit():
            if int(option) >= 0 and int(option) <= 255:
                return 'option ' + option
        if option in ['any', 'eol', 'extended-security',
                      'ignore', 'loose-source-route',
                      'no-op', 'record-route', 'router-alert',
                      'security', 'streamid',
                      'strict-source-route', 'timestamp']:
                return 'option ' + option

        raise ValueError("Invalid option {}. Supported values are "
                         "any, eol, extended-security, ignore, "
                         "loose-source-route no-op, record-route, "
                         "router-alert, security, streamid, "
                         "strict-source-route, timestamp "
                         "Allowed value in decimal <0-255>."
                         .format(option))

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
        if 'suppress_rpf_drop' not in parameters or \
                not parameters['suppress_rpf_drop']:
            return None

        return 'suppress-rpf-drop'

    def parse_priority(self, **parameters):
        """
        parse the priority param.
        Args:
            parameters contains:
                priority(integer): set priorityr. Allowed value is <0-7>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority' not in parameters or not parameters['priority']:
            return None

        if 'priority_force' in parameters and parameters['priority_force']:
            raise ValueError('priority and priority-force can not be'
                             ' enabled at the same time!')

        priority = parameters['priority']

        if priority >= 0 and priority <= 7:
            return 'priority ' + str(priority)

        raise ValueError("Invalid priority {}. "
                         "Allowed value in decimal <0-7>."
                         .format(priority))

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
        if 'priority_force' not in parameters or \
                not parameters['priority_force']:
            return None

        if 'priority' in parameters and parameters['priority']:
            raise ValueError('priority and priority-force can not be'
                             ' enabled at the same time!')

        priority_force = parameters['priority_force']

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
        if 'priority_mapping' not in parameters or \
                not parameters['priority_mapping']:
            return None

        priority_mapping = parameters['priority_mapping']

        if priority_mapping >= 0 and priority_mapping <= 7:
            return 'priority-mapping ' + str(priority_mapping)

        raise ValueError("Invalid priority_mapping {}. "
                         "Allowed value in decimal <0-7>."
                         .format(priority_mapping))

    def parse_tos(self, **parameters):
        """
        parse the tos mapping param.
        Args:
            parameters contains:
                tos(integer): set tosr. Allowed value is <0-15>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'tos' not in parameters or not parameters['tos']:
            return None

        tos = parameters['tos']

        if tos.isdigit():
            if int(tos) >= 0 and int(tos) <= 15:
                return 'tos ' + tos
        elif tos in ['max-reliability', 'max-throughput', 'min-delay',
                     'normal']:
            return 'tos ' + tos

        raise ValueError("Invalid tos {}. "
                         "Allowed value in decimal <0-15>."
                         .format(tos))

    def parse_drop_precedence(self, **parameters):
        """
        parse the drop_precedence mapping param.
        Args:
            parameters contains:
                drop_precedence(string): drop_precedence value of the packet
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence' not in parameters or \
                not parameters['drop_precedence']:
            return None

        if 'drop_precedence_force' in parameters and \
                parameters['drop_precedence_force']:
            raise ValueError('drop-precedence and drop-precedence-force can '
                             'not be enabled at the same time!')

        drop_precedence = parameters['drop_precedence']
        drop_precedence = ' '.join(drop_precedence.split())

        if drop_precedence.isdigit():
            if int(drop_precedence) >= 0 and int(drop_precedence) <= 3:
                return 'drop-precedence ' + drop_precedence

        raise ValueError("drop-precedence value should be 0 - 3")

    def parse_drop_precedence_force(self, **parameters):
        """
        parse the drop_precedence_force mapping param.
        Args:
            parameters contains:
                drop_precedence_force(string):
                    drop_precedence_force value of the packet
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence_force' not in parameters or \
                not parameters['drop_precedence_force']:
            return None

        if 'drop_precedence' in parameters and \
                parameters['drop_precedence']:
            raise ValueError('drop-precedence and drop-precedence-force can '
                             'not be enabled at the same time!')

        drop_precedence_force = parameters['drop_precedence_force']
        drop_precedence_force = ' '.join(drop_precedence_force.split())

        if drop_precedence_force.isdigit():
            if int(drop_precedence_force) >= 0 and \
                    int(drop_precedence_force) <= 3:
                return 'drop-precedence-force ' + drop_precedence_force

        raise ValueError("drop-precedence-force value should be 0 - 3")

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

        if icmp_message in ['administratively-prohibited', 'any-icmp-type',
                            'destination-host-prohibited',
                            'destination-host-unknown',
                            'destination-net-prohibited',
                            'destination-network-unknown', 'echo',
                            'echo-reply', 'general-parameter-problem',
                            'host-precedence-violation', 'host-redirect',
                            'host-tos-redirect', 'host-tos-unreachable',
                            'host-unreachable', 'information-reply',
                            'information-request', 'mask-reply',
                            'mask-request', 'net-redirect', 'net-tos-redirect',
                            'net-tos-unreachable', 'net-unreachable',
                            'packet-too-big', 'parameter-problem',
                            'port-unreachable', 'precedence-cutoff',
                            'protocol-unreachable', 'reassembly-timeout',
                            'redirect', 'router-advertisement',
                            'router-solicitation', 'source-host-isolated',
                            'source-quench', 'source-route-failed',
                            'time-exceeded', 'timestamp-reply',
                            'timestamp-request', 'ttl-exceeded',
                            'unreachable']:
            return icmp_message
        raise ValueError("{} icmp message not supported."
                         "Refer config guide for supported messages"
                         .format(icmp_message))

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
        elif len(icmp_filter) == 1:
            return self._parse_icmp_message(icmp_filter[0])

        raise ValueError("invalid icmp filter string")

    def parse_tcp_operator(self, **parameters):
        """
        parse the icmp_message param
        Args:
            parameters contains:
                tcp_operator(string): Validate comparison operator for TCP port
                    This parameter works only for tcp protocol.
                    Allowed values are : established and/or syn
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
