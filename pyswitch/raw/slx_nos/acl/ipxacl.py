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

import pyswitch.utilities as utilities
from pyswitch.raw.slx_nos.acl.aclparam_parser import AclParamParser


class IpAcl(AclParamParser):
    """
    The IpAcl class holds all the functions assocaiated with
    Ip Access Control list.
    Attributes:
        None
    """

    def _parse_xport_val(self, xport_val):
        if xport_val.isdigit():
            return xport_val

        xport_val = xport_val.lower()
        if xport_val == 'bgp':
            return 179  # Border Gateway Protocol (179)
        elif xport_val == 'daytime':
            return 13  # Daytime (13)
        elif xport_val == 'domain':
            return 53  # Domain Name Service (53)
        elif xport_val == 'echo':
            return 7  # Echo (7)
        elif xport_val == 'ftp':
            return 21  # File Transfer Protocol (21)
        elif xport_val == 'ftp-data':
            return 20  # FTP data connections (20)
        elif xport_val == 'hostname':
            return 101  # NIC hostname server (101)
        elif xport_val == 'login':
            return 513  # Login (rlogin, 513)
        elif xport_val == 'pim-auto-rp':
            return 496  # PIM Auto-RP (496)
        elif xport_val == 'smtp':
            return 25  # Simple Mail Transport Protocol (25)
        elif xport_val == 'syslog':
            return 514  # System Logger (514)
        elif xport_val == 'tacacs':
            return 49  # TAC Access Control System (49)
        elif xport_val == 'talk':
            return 517  # Talk (517)
        elif xport_val == 'telnet':
            return 23  # Telnet (23)
        elif xport_val == 'time':
            return 37  # Time (37)
        elif xport_val == 'www':
            return 80  # World Wide Web (HTTP, 80)
        elif xport_val == 'bootpc':
            return 68  # Bootstrap Protocol (BOOTP) clien (68)
        elif xport_val == 'bootps':
            return 67  # Bootstrap Protocol (BOOTP) server (67)
        elif xport_val == 'ntp':
            return 123  # Network Time Protocol (123)
        elif xport_val == 'rip':
            return 520  # Routing Information Protocol (router, in.routed, 520)
        elif xport_val == 'snmp':
            return 161  # Simple Network Management Protocol (161)
        elif xport_val == 'tftp':
            return 69  # Trivial File Transfer Protocol (69)

        raise ValueError('{} operator not supported')

    def _parse_op_str(self, op_str, ret):
        xport = {}

        op_str = ' '.join(op_str.split()).split()

        if len(op_str) == 2:
            if op_str[0] in ['neq', 'lt', 'gt', 'eq']:
                xport['op'] = op_str[0]
                xport['val'] = [self._parse_xport_val(op_str[1])]
                ret['xport'] = xport
                return True
        elif len(op_str) == 3 and op_str[0] == 'range':
            xport['op'] = op_str[0]
            xport['val'] = [self._parse_xport_val(op_str[1]),
                            self._parse_xport_val(op_str[2])]
            ret['xport'] = xport
            return True

        raise ValueError("Unsupported operator {}".format(op_str))

    def _parse_source_destination(self, protocol_type, input_param,
                                  address_type):

        ret = {"host_any": None, "host_ip": None, "mask": None, 'xport': None}

        v4_str = input_param
        op_str = ''
        op_index = -1
        for tcp_udp_op in ['range', 'neq', 'lt', 'gt', 'eq']:
            op_index = input_param.find(tcp_udp_op)
            if op_index >= 0:
                op_str = input_param[op_index:]
                v4_str = input_param[0:op_index]
                break

        if protocol_type and op_str:
            if protocol_type not in ['tcp', 'udp']:
                raise ValueError("tcp udp operator is supported only for."
                                 "protocol_type = tcp or udp")
            self._parse_op_str(op_str, ret)

        if v4_str[0:3] == "any":
            ret['host_any'] = "any"
            return ret

        if v4_str[0:4] == "host":
            utilities.validate_ip_address(v4_str[5:], address_type)
            ret['host_any'] = "host"
            ret['host_ip'] = v4_str[5:]
            return ret

        v4_str = ' '.join(v4_str.split())
        if '/' in v4_str:
            ip, mask = v4_str.split('/')

            utilities.validate_ip_address(ip, address_type)

            if address_type == 'ipv6':
                ret['host_any'] = v4_str
                return ret

            if address_type == 'ip':
                if mask.isdigit():
                    if int(mask) < 0 or int(mask) > 32:
                        raise ValueError("Invalid Prefix: {}. Valid Range "
                                         "0 to 32".format(mask))
                    ret['host_any'] = v4_str
                else:
                    utilities.validate_ip_address(mask, address_type)
                    ret['host_any'] = ip
                    ret['mask'] = mask
                return ret

        raise ValueError("Invalid input param {}".format(input_param))

    def parse_source(self, **kwargs):
        """
        parse the source param.
        Args:
            kwargs contains:
                source (string): Destination address filters
                    { any | S_IPaddress/mask(0.0.0.255) |
                    host,S_IPaddress } [ source-operator [ S_port-numbers ] ]
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'source' not in kwargs or not kwargs['source']:
            raise ValueError("Missing \'source\' in kwargs")

        protocol_type = None
        if 'protocol_type' in kwargs and kwargs['protocol_type']:
            protocol_type = kwargs['protocol_type']

        src = kwargs['source']
        src = ' '.join(src.split())

        return self._parse_source_destination(protocol_type, src,
                                              kwargs['address_type'])

    def parse_destination(self, **kwargs):
        """
        parse the source param.
        Args:
            kwargs contains:
                destination (string): Destination address filters
                    { any | S_IPaddress/mask(0.0.0.255) |
                    host,S_IPaddress } [ source-operator [ S_port-numbers ] ]


        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'destination' not in kwargs or not kwargs['destination']:
            raise ValueError("Missing \'destination\' in kwargs")

        dst = kwargs['destination']
        dst = ' '.join(dst.split())

        return self._parse_source_destination(kwargs['protocol_type'], dst,
                                              kwargs['address_type'])

    def parse_protocol_type(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                protocol_type(string): Type of IP packets to be filtered based
                    on protocol. Valid values are <0-255> or key words tcp,
                    udp, icmp or ip
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'protocol_type' not in kwargs or not kwargs['protocol_type']:
            raise ValueError("Missing \'protocol_type\' in kwargs")

        protocol_type = kwargs['protocol_type']
        protocol_type = ' '.join(protocol_type.split())

        if protocol_type in ['tcp', 'udp', 'icmp', 'ip', 'ipv6', 'ipv6-icmp']:
            return protocol_type

        if protocol_type.isdigit():
            if int(protocol_type) >= 0 and int(protocol_type) <= 255:
                return protocol_type

        raise ValueError("Invalid \'protocol_type\' {} in kwargs"
                         .format(protocol_type))

    def parse_dscp(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                dscp(string): Matches the specified value against the DSCP
                    value of the packet to filter. Allowed 0 to 63.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'dscp' not in kwargs or not kwargs['dscp']:
            return None

        dscp = kwargs['dscp']
        dscp = ' '.join(dscp.split())

        dscp = dscp.split(',')[0]

        if dscp.isdigit():
            if int(dscp) >= 0 and int(dscp) <= 63:
                return dscp
        elif dscp.lower() == 'af11':
            return 10  # AF11 dscp (001010)
        elif dscp.lower() == 'af12':
            return 12  # AF12 dscp (001100)
        elif dscp.lower() == 'af13':
            return 14  # AF13 dscp (001110)
        elif dscp.lower() == 'af21':
            return 18  # AF13 dscp (010010)
        elif dscp.lower() == 'af22':
            return 20  # AF13 dscp (010100)
        elif dscp.lower() == 'af23':
            return 22  # AF13 dscp (010110)
        elif dscp.lower() == 'af31':
            return 26  # AF13 dscp (011010)
        elif dscp.lower() == 'af32':
            return 28  # AF13 dscp (011100)
        elif dscp.lower() == 'af33':
            return 30  # AF13 dscp (011110)
        elif dscp.lower() == 'af41':
            return 34  # AF13 dscp (100010)
        elif dscp.lower() == 'af42':
            return 36  # AF13 dscp (100100)
        elif dscp.lower() == 'af43':
            return 38  # AF13 dscp (100110)
        elif dscp.lower() == 'cs1':
            return 8   # AF13 dscp (001000)
        elif dscp.lower() == 'cs2':
            return 16  # AF13 dscp (010000)
        elif dscp.lower() == 'cs3':
            return 24  # AF13 dscp (011000)
        elif dscp.lower() == 'cs4':
            return 32  # AF13 dscp (100000)
        elif dscp.lower() == 'cs5':
            return 40  # AF13 dscp (101000)
        elif dscp.lower() == 'cs6':
            return 48  # AF13 dscp (110000)
        elif dscp.lower() == 'cs7':
            return 56  # AF13 dscp (111000)
        elif dscp.lower() == 'default':
            return 0   # AF13 dscp (000000)
        elif dscp.lower() == 'ef':
            return 46  # AF13 dscp (101110)

        raise ValueError("Invalid \'dscp\' {} in kwargs"
                         .format(dscp))

    def parse_dscp_force(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                dscp(string): Matches the specified value against the DSCP
                    value of the packet to filter. Allowed 0 to 63.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'dscp' not in kwargs or not kwargs['dscp']:
            return None

        dscp = kwargs['dscp']
        dscp = ' '.join(dscp.split())

        dscp = dscp.split(',')
        if len(dscp) == 2:
            dscp = dscp[1]
        else:
            return None

        if dscp.isdigit():
            if int(dscp) >= 0 and int(dscp) <= 63:
                return dscp

        raise ValueError("Invalid \'dscp\' {} in kwargs"
                         .format(dscp))

    def parse_vlan_id(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                vlan_id(integer): VLAN interface to which the ACL is bound
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'vlan_id' not in kwargs or not kwargs['vlan_id']:
            return None

        vlan_id = kwargs['vlan_id']

        if vlan_id >= 1 and vlan_id <= 4095:
            return str(vlan_id)

        raise ValueError("Invalid \'vlan_id\' {} in kwargs"
                         .format(vlan_id))

    def parse_nos_vlan_id(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                vlan_id(integer): VLAN interface to which the ACL is bound
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'vlan_id' not in kwargs or not kwargs['vlan_id']:
            return None

        vlan_id = kwargs['vlan_id']

        if vlan_id >= 1 and vlan_id <= 8191:
            return str(vlan_id)

        raise ValueError("Invalid \'vlan_id\' {} in kwargs"
                         .format(vlan_id))

    def parse_tcp_specific_params(self, user_data, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                urg(string): Enables urg for the rule
                ack(string): Enables ack for the rule
                push(string): Enables push for the rule
                fin(string): Enables fin for the rule
                rst(string): Enables rst for the rule
                sync(string): Enables sync for the rule
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        is_tcp = False
        tcp_params = ['sync', 'rst', 'fin', 'push', 'ack', 'urg']

        if 'protocol_type' in kwargs and kwargs['protocol_type']:
            protocol_type = kwargs['protocol_type'].lower()
            if protocol_type == 'tcp' or protocol_type == 6:
                is_tcp = True

        for key in tcp_params:
            if key in kwargs and kwargs[key]:
                val = kwargs[key]
                val = ' '.join(val.split())
                if val.lower() == 'true':
                    if is_tcp:
                        user_data[key] = True
                    else:
                        raise ValueError("Config {} is only allowed for"
                                         " protocol_type tcp".format(key))
            else:
                user_data[key] = None

        return True
