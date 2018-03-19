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
import json
import inspect
import jinja2
import re
import acl_template

from pyswitch.snmp.base.acl.acl import Acl as BaseAcl
from pyswitch.snmp.base.acl.macacl import MacAcl
from pyswitch.snmp.base.acl.ipacl import IpAcl
from pyswitch.snmp.base.acl.ipv6acl import Ipv6Acl
import pyswitch.snmp.base.acl.params_validator as params_validator


class Acl(BaseAcl):
    """
    The Acl class holds all the functions assocaiated with the
    Access Control list of a MLX device.
    Attributes:
        None
    """

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
        super(Acl, self).__init__(callback)

        self._mac = MacAcl()
        self._ip = IpAcl()
        self._ipv6 = Ipv6Acl()

    @property
    def mac(self):
        return self._mac

    @property
    def ip(self):
        return self._ip

    @property
    def ipv6(self):
        return self._ipv6

    def create_acl(self, **parameters):
        """
        Create an Access Control List.
        Args:
            address_type (str): ACL address type, ip or ipv6 or mac.
            acl_type (str): ACL type, extended or standard.
            acl_name (str): Unique name for ACL.
            callback (function): A function executed upon completion of the
                method. The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `string` message.
        Raise:
            Raises ValueError, Exception
        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
            ...             connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1',
            ...                              acl_type='standard',
            ...                              address_type='mac')
            ...     print dev.acl.create_acl(acl_name='Acl_2',
            ...                              acl_type='extended',
            ...                              address_type='ip')
        """
        params_validator.validate_params_mlx_create_acl(**parameters)

        address_type = parameters['address_type']
        acl_type = parameters.get('acl_type', None)
        acl_name = self.mac.parse_acl_name(**parameters)

        if address_type == 'mac':
            config = 'mac access-list ' + acl_name
        elif address_type == 'ip':
            if not acl_type:
                raise ValueError("acl_type is required param for ip ACL")
            config = 'ip access-list ' + acl_type + ' ' + acl_name
        elif address_type == 'ipv6':
            config = 'ipv6 access-list ' + acl_name
        else:
            raise ValueError("Address Type: {} not supported".format(
                             address_type))

        output = self._callback([config], handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3], config, output)

    def delete_acl(self, **parameters):
        """
        Delete Access Control List.
        Args:
            parameters contains:
                acl_name (str): Name of the access list.
        Returns:
            Return value of `string` message.
        Raise:
            Raises ValueError, Exception
            >>> from pyswitch.device import Device
            >>> conn=('10.37.73.148', 22)
            >>> auth=('admin', 'admin')
            >>> with Device(conn=conn, auth=auth,
            ...             connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1',
            ...                              acl_type='standard',
            ...                              address_type='mac')
            ...     print dev.acl.delete_acl(acl_name='Acl_1')
        """
        params_validator.validate_params_mlx_delete_acl(**parameters)

        acl_name = parameters['acl_name']

        ret = self.get_acl_address_and_acl_type(acl_name)
        acl_type = ret['type']
        address_type = ret['protocol']

        if address_type == 'mac':
            cmd = acl_template.delete_acl_template
            t = jinja2.Template(cmd)
            config = t.render(acl_name_str=acl_name)
        elif address_type == 'ip':
            config = 'no ip access-list ' + acl_type + ' ' + acl_name
        elif address_type == 'ipv6':
            config = 'no ipv6 access-list ' + acl_name
        else:
            raise ValueError("Address Type: {} not supported".format(
                             address_type))

        output = self._callback([config], handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3], config, output)

    def add_l2_acl_rule(self, **parameters):
        """
        Delete Access Control List.
        Args:
            parameters contains:
                acl_name: Name of the access list.
                seq_id: Sequence number of the rule. For add operation,
                    if not specified, the rule is added at the end of the list.
                action: Action apply on the traffic, either to deny or permit.
                source: Source filter, can be 'any' or the actual MAC in
                    HHHH.HHHH.HHHH format.
                src_mac_addr_mask: Mask for the source HHHH.HHHH.HHHH format.
                dst: Destination filter, can be 'any' or the actual MAC in
                        HHHH.HHHH.HHHH format.
                dst_mac_addr_mask: Mask for the dst in HHHH.HHHH.HHHH format.
                vlan: VLAN IDs - 'any' or 1-4096
                ethertype: EtherType, can be 'arp', 'fcoe', 'ipv4-15', 'ipv6'
                    or custom value between 1536 and 65535.
                arp_guard: Enables arp-guard for the rule
                drop_precedence_force: Matches the specified value against the
                    drop_precedence_force value of the packet to filter.
                    Allowed values are 0 through 3.
                log: Enables the logging
                mirror: Enables mirror for the rule
                drop_precedence: Matches the specified value against the
                    drop_precedence value of the packet to filter.
                    Allowed values are 0 through 3.
                priority: Matches the specified value against the priority
                    value of the packet to filter.
                    Allowed values are 0 through 7.
                priority_force: Matches the specified value against the
                    priority_force value of the packet to filter.
                    Allowed values are 0 through 7.
               priority_mapping: Matches the specified value against the
                    priority_mapping value of the packet to filter.
                    Allowed values are 0 through 7.
        Returns:
            Return value of `string` message.
        Raise:
            Raises ValueError, Exception
        Examples:
            >>> from pyswitch.device import Device
            >>> conn=('10.37.73.148', 22)
            >>> auth=('admin', 'admin')
            >>> with Device(conn=conn, auth=auth,
            ...             connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1',
            ...                              acl_type='extended',
            ...                              address_type='mac')
            ...     print dev.acl.add_l2_acl_rule(acl_name='Acl_1',
            ...                                   action='permit',
            ...                                   source='any',
            ...                                   dst='any',
            ...                                   vlan=10)
        """
        params_validator.\
            validate_params_mlx_add_or_remove_l2_acl_rule(**parameters)

        cli_arr = []
        user_data = self.parse_params_for_add_l2_acl_rule(**parameters)

        cmd = acl_template.create_acl_template
        t = jinja2.Template(cmd)
        config = t.render(acl_name_str=user_data['acl_name_str'])
        cli_arr.append(config)

        cmd = acl_template.add_l2_acl_rule_template
        t = jinja2.Template(cmd)
        config = t.render(**user_data)

        config = re.sub(r'[^a-zA-Z0-9 .-]', r'', config)
        config = ' '.join(config.split())

        cli_arr.append(config)
        output = self._callback(cli_arr, handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3], config, output)

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
        Raise:
            Raises ValueError, Exception
        Examples:
            >>> from pyswitch.device import Device
            >>> conn=('10.37.73.148', 22)
            >>> auth=('admin', 'admin')
            >>> with Device(conn=conn, auth=auth,
            ...             connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1',
            ...                              acl_type='extended',
            ...                              address_type='mac')
            ...     print dev.acl.add_l2_acl_rule(acl_name='Acl_1',
            ...                                   action='permit',
            ...                                   source='any',
            ...                                   dst='any',
            ...                                   vlan=10)
            ...     print dev.acl.delete_l2_acl_rule(acl_name='Acl_1',
            ...                                   vlan=10)
        """

        if 'seq_id' not in parameters or not parameters['seq_id']:
            raise ValueError("missing required parameters: ['seq_id']")

        if 'acl_name' not in parameters or not parameters['acl_name']:
            raise ValueError("missing required parameters: ['acl_name']")

        acl_name = self.mac.parse_acl_name(**parameters)
        seq_id = parameters['seq_id']

        self.is_valid_seq_id(seq_id, acl_name)

        cli_arr = []

        cmd = acl_template.create_acl_template
        t = jinja2.Template(cmd)
        config = t.render(acl_name_str=acl_name)
        config = ' '.join(config.split())
        cli_arr.append(config)

        cmd = acl_template.delete_rule_by_seq_id
        t = jinja2.Template(cmd)
        config = t.render(seq_id_str=parameters['seq_id'])
        config = re.sub(r'[^a-zA-Z0-9 .-]', r'', config)
        config = ' '.join(config.split())
        cli_arr.append(config)

        output = self._callback(cli_arr, handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3], config, output)

    def parse_params_for_add_l2_acl_rule(self, **parameters):
        """
        Parses params for l2 Rule to be added to Access Control List.
        Args:
            Parse below params if contained in parameters.
                action:
                source:
                dst:
                vlan:
                ethertype:
                arp_guard:
                drop_precedence:
                drop_precedence_force:
                log:
                mirror:
                priority:
                priority_force:
                priority_mapping:

        Returns:
            Return a dict cotaining the parameters in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        Examples:
        """
        user_data = {}
        user_data['acl_name_str'] = self.mac.parse_acl_name(**parameters)
        user_data['seq_id_str'] = self.mac.parse_seq_id(**parameters)
        user_data['action_str'] = self.mac.parse_action(**parameters)
        user_data['source_str'] = self.mac.parse_source(**parameters)
        user_data['dst_str'] = self.mac.parse_dst(**parameters)
        user_data['vlan_str'] = self.mac.parse_vlan(**parameters)
        user_data['ethertype_str'] = self.mac.parse_ethertype(**parameters)
        user_data['arp_guard_str'] = self.mac.parse_arp_guard(**parameters)
        user_data['drop_precedence_str'] = \
            self.mac.parse_drop_precedence(**parameters)
        user_data['drop_precedence_force_str'] = \
            self.mac.parse_drop_precedence_force(**parameters)
        user_data['log_str'] = self.mac.parse_log(**parameters)
        user_data['mirror_str'] = self.mac.parse_mirror(**parameters)
        user_data['priority_str'] = self.mac.parse_priority(**parameters)
        user_data['priority_force_str'] = \
            self.mac.parse_priority_force(**parameters)
        user_data['priority_mapping_str'] = \
            self.mac.parse_priority_mapping(**parameters)

        parameters['user_data'] = user_data
        return user_data

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
        if not acl_name:
            raise ValueError('Acl Name is manadatory parameter')

        if not seq_id:
            raise ValueError('Sequence Id is manadatory parameter')

        address_type = self.get_address_type(acl_name)
        cmd = ''

        if address_type == 'mac':
            cmd = acl_template.show_l2_access_list
        elif address_type == 'ip':
            cmd = acl_template.show_ip_access_list
        elif address_type == 'ipv6':
            cmd = acl_template.show_ipv6_access_list
        else:
            raise ValueError('{} not supported'.format(address_type))

        t = jinja2.Template(cmd)
        config = t.render(acl_name_str=acl_name)
        config = ' '.join(config.split())

        output = self._callback(config, handler='cli-get')

        # Check if there is any error
        self._process_cli_output(inspect.stack()[0][3], config, output)

        # Now check if seq id exists
        for line in output.split('\n'):
            if not line:
                continue

            line_seq_id = line.split(':')[0]
            line_seq_id = ' '.join(line_seq_id.split())
            if not line_seq_id.isdigit():
                continue

            if int(line_seq_id) == seq_id:
                return True

        raise ValueError('{} not exists for acl {}'.format(seq_id, acl_name))

    def apply_acl(self, **parameters):
        """
        Apply Access Control List on interface.
        Args:
            parameters contains:
                acl_name: Name of the access list.
                intf_type: - ethernet, ve
                intf_name: array of interfaces
                acl_direction: Direction of ACL binding on the specified
                    interface
        Returns:
            Return True
        Raises:
            Exception, ValueError for invalid seq_id.
        """
        params_validator.validate_params_mlx_apply_acl(**parameters)

        acl_name = parameters['acl_name']
        intf_type = parameters['intf_type']
        intf_name = parameters.pop('intf_name', None)

        if not intf_name:
            raise ValueError('No Interface specified')

        address_type = self.get_address_type(acl_name)

        if address_type not in ['mac', 'ip', 'ipv6']:
            raise ValueError('{} not supported'.format(address_type))

        if address_type == 'mac':
            if intf_type != 'ethernet':
                raise ValueError('intf type:{} not supported'
                                 .format(intf_type))

        if intf_type == 'port_channel':
            raise ValueError("MLX does not allow ACL configuration on "
                             " port channel interface. Configure ACL on "
                             " ports part of port channel")

        # This iteration will validate that interface exists
        # It will also validate for interfaces part of lag
        for intf in intf_name:
            cmd = acl_template.interface_submode_template
            t = jinja2.Template(cmd)
            config = t.render(intf_name=intf, **parameters)
            config = ' '.join(config.split())
            output = self._callback([config], handler='cli-set')
            self._process_cli_output(inspect.stack()[0][3], config, output)

        for intf in intf_name:
            cli_arr = []

            cmd = acl_template.interface_submode_template
            t = jinja2.Template(cmd)
            config = t.render(intf_name=intf, **parameters)
            config = ' '.join(config.split())
            cli_arr.append(config)

            cmd = acl_template.apply_acl_template
            t = jinja2.Template(cmd)
            config = t.render(address_type=address_type, **parameters)
            config = ' '.join(config.split())
            cli_arr.append(config)

            cli_arr.append('exit')

            output = self._callback(cli_arr, handler='cli-set')
            self._process_cli_output(inspect.stack()[0][3], config, output)

        return 'apply_acl: Successful'

    def remove_acl(self, **parameters):
        """
        Remove Access Control List from interface.
        Args:
            parameters contains:
                acl_name: Name of the access list.
                intf_type: - ethernet, ve
                intf_name: array of interfaces
                acl_direction: Direction of ACL binding on the specified
                    interface
        Returns:
            Return True
        Raises:
            Exception, ValueError for invalid seq_id.
        """
        params_validator.validate_params_mlx_remove_acl(**parameters)

        acl_name = parameters['acl_name']
        intf_type = parameters['intf_type']
        intf_name = parameters.pop('intf_name', None)

        if not intf_name:
            raise ValueError('No Interface specified')

        address_type = self.get_address_type(acl_name)

        if address_type not in ['mac', 'ip', 'ipv6']:
            raise ValueError('{} not supported'.format(address_type))

        if address_type == 'mac':
            if intf_type != 'ethernet':
                raise ValueError('intf type:{} not supported'
                                 .format(intf_type))

        if intf_type == 'port_channel':
            raise ValueError("MLX does not allow ACL configuration on "
                             " port channel interface. Configure ACL on "
                             " ports part of port channel")

        # This iteration will validate that interface exists
        # It will also validate for interfaces part of lag
        for intf in intf_name:
            cmd = acl_template.interface_submode_template
            t = jinja2.Template(cmd)
            config = t.render(intf_name=intf, **parameters)
            config = ' '.join(config.split())
            output = self._callback([config], handler='cli-set')
            self._process_cli_output(inspect.stack()[0][3], config, output)

        processed_interfaces = []
        for intf in intf_name:
            cli_arr = []
            cmd = acl_template.interface_submode_template
            t = jinja2.Template(cmd)
            config = t.render(intf_name=intf, **parameters)
            config = ' '.join(config.split())
            cli_arr.append(config)

            cmd = acl_template.remove_acl_template
            t = jinja2.Template(cmd)
            config = t.render(address_type=address_type, **parameters)
            config = ' '.join(config.split())
            cli_arr.append(config)

            cli_arr.append('exit')

            output = self._callback(cli_arr, handler='cli-set')
            regex = re.compile('no.*bound acl', re.IGNORECASE)
            m = regex.search(output)
            if m:
                raise ValueError("Acl removed from interfaces {}, "
                                 "but failed remove_acl for interface {}"
                                 .format(str(processed_interfaces), intf))
            self._process_cli_output(inspect.stack()[0][3], config, output)
            processed_interfaces.append(intf)

        return 'remove_acl : Successful'

    def add_ipv4_rule_acl(self, **parameters):
        """
        Add rules to Access Control List of ipv4.
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

                dscp-marking: (string) dscp-marking number is used to mark the
                    DSCP value in the incoming packet with the value you
                    specify to filter.  Allowed values are 0 through 63.
                fragment: (string) Use fragment keyword to allow the ACL to
                    filter fragmented packets. Use the non-fragment keyword to
                    filter non-fragmented packets.
                    Allowed values are- fragment, non-fragment
                precedence: (integer) Match packets with given precedence value
                    Allowed value in range 0 to 7.
                option: (string) Match match IP option packets.
                    supported values are:
                        any, eol, extended-security, ignore, loose-source-route
                        no-op, record-route, router-alert, security, streamid,
                        strict-source-route, timestamp
                        Allowed value in decimal <0-255>.
                suppress-rpf-drop: (boolean) Permit packets that fail RPF check
                priority: (integer) set priority
                priority-force: (integer) force packet outgoing priority.
                priority-mapping: (integer) map incoming packet priority.
                tos: (integer) Match packets with given TOS value.
                    Allowed value in decimal <0-15>.
        Returns:
            Return True
        Raises:
            Exception, ValueError for invalid seq_id.
            >>> from pyswitch.device import Device
            >>> conn=('10.37.73.148', 22)
            >>> auth=('admin', 'admin')
            >>> with Device(conn=conn, auth=auth,
            ...             connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1',
            ...                              acl_type='standard',
            ...                              address_type='ip')
            ...     print dev.acl.add_ipv4_rule_acl(acl_name='Acl_1',
            ...                                   action='permit',
            ...                                   source='any',
            ...                                   dst='any',
            ...                                   vlan=10)
        """
        params_validator.validate_params_mlx_add_ipv4_rule_acl(**parameters)

        acl_name = parameters['acl_name']
        ret = self.get_acl_address_and_acl_type(acl_name)
        acl_type = ret['type']
        address_type = ret['protocol']

        if address_type != 'ip':
            raise ValueError('{} not supported'.format(address_type))

        cli_arr = ['ip access-list ' + ' ' + acl_type + ' ' + acl_name]

        if acl_type == 'standard':
            user_data = self.parse_params_for_add_ipv4_standard(**parameters)
            cmd = acl_template.add_ip_standard_acl_rule_template
        elif acl_type == 'extended':
            user_data = self.parse_params_for_add_ipv4_extended(**parameters)
            cmd = acl_template.add_ip_extended_acl_rule_template
        else:
            raise ValueError('{} not supported'.format(acl_type))

        t = jinja2.Template(cmd)
        config = t.render(**user_data)
        config = ' '.join(config.split())
        cli_arr.append(config)

        output = self._callback(cli_arr, handler='cli-set')
        if 'Failed to initialize dns request' in output:
            raise ValueError('ACL DNS: Errno(5) Failed '
                             'to initialize dns request')
        if 'are undefined' in output:
            raise ValueError('Invlaid icmp filter: {}'
                             .format(parameters['icmp_filter']))
        return self._process_cli_output(inspect.stack()[0][3], config, output)

    def parse_params_for_add_ipv4_standard(self, **parameters):
        """
        Parses params for l2 Rule to be added to standard Access Control List.
        Args:
            Parse below params if contained in parameters.
                acl_name: (string) Name of the access list
                seq_id: (integer) Sequence number of the rule,
                    if not specified, the rule is added at the end of the list.
                    Valid range is 0 to 4294967290
                action: (string) Action performed by ACL rule
                    - permit
                    - deny
                source: (string) Source address filters
                    { any | S_IPaddress/mask(0.0.0.255) |
                    host,S_IPaddress } [ source-operator [ S_port-numbers ] ]
                vlan_id: (integer) VLAN interface to which the ACL is bound
                log: (string) Enables logging for the rule
                    (Available for permit or deny only)
        Returns:
            Return a dict cotaining the parameters in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        Examples:
        """
        supported_params = ['acl_name', 'seq_id', 'action', 'source',
                            'vlan_id', 'log']
        self._is_parameter_supported(supported_params, parameters)

        user_data = {}

        user_data['acl_name_str'] = parameters['acl_name']
        user_data['seq_id_str'] = self.ip.parse_seq_id(**parameters)
        user_data['action_str'] = self.ip.parse_action(**parameters)
        user_data['source_str'] = self.ip.parse_source(**parameters)
        user_data['vlan_str'] = self.ip.parse_vlan(**parameters)
        user_data['log_str'] = self.ip.parse_log(**parameters)
        parameters['user_data'] = user_data
        return user_data

    def parse_params_for_add_ipv4_extended(self, **parameters):
        """
        Parses params for l2 Rule to be added to Access Control List.
        Args:
            Parse below params if contained in parameters.
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

                dscp-marking: (string) dscp-marking number is used to mark the
                    DSCP value in the incoming packet with the value you
                    specify to filter.  Allowed values are 0 through 63.
                fragment: (string) Use fragment keyword to allow the ACL to
                    filter fragmented packets. Use the non-fragment keyword to
                    filter non-fragmented packets.
                    Allowed values are- fragment, non-fragment
                precedence: (integer) Match packets with given precedence value
                    Allowed value in range 0 to 7.
                option: (string) Match match IP option packets.
                    supported values are:
                        any, eol, extended-security, ignore, loose-source-route
                        no-op, record-route, router-alert, security, streamid,
                        strict-source-route, timestamp
                        Allowed value in decimal <0-255>.
                suppress-rpf-drop: (boolean) Permit packets that fail RPF check
                priority: (integer) set priority
                priority-force: (integer) force packet outgoing priority.
                priority-mapping: (integer) map incoming packet priority.
                tos: (integer) Match packets with given TOS value.
                    Allowed value in decimal <0-15>.


        Returns:
            Return a dict cotaining the parameters in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        Examples:
        """
        user_data = {}
        user_data['acl_name_str'] = parameters['acl_name']
        user_data['seq_id_str'] = self.ip.parse_seq_id(**parameters)
        user_data['action_str'] = self.ip.parse_action(**parameters)
        user_data['vlan_str'] = self.ip.parse_vlan(**parameters)
        user_data['protocol_str'] = self.ip.parse_protocol(**parameters)
        user_data['source_str'] = self.ip.parse_source(**parameters)
        user_data['dst_str'] = self.ip.parse_destination(**parameters)
        user_data['copy_sflow'] = self.ip.parse_copy_sflow(**parameters)
        user_data['tcp_operator_str'] = \
            self.ip.parse_tcp_operator(**parameters)
        user_data['icmp_filter_str'] = \
            self.ip.parse_icmp_filter(**parameters)
        user_data['dscp_mapping_str'] = \
            self.ip.parse_dscp_mapping(**parameters)
        user_data['dscp_marking_str'] = \
            self.ip.parse_dscp_marking(**parameters)
        user_data['fragment_str'] = self.ip.parse_fragment(**parameters)
        user_data['precedence_str'] = self.ip.parse_precedence(**parameters)
        user_data['option_str'] = self.ip.parse_option(**parameters)
        user_data['suppress_rpf_drop_str'] = \
            self.ip.parse_suppress_rpf_drop(**parameters)
        user_data['priority_str'] = self.ip.parse_priority(**parameters)
        user_data['priority_force_str'] = \
            self.ip.parse_priority_force(**parameters)
        user_data['priority_mapping_str'] = \
            self.ip.parse_priority_mapping(**parameters)
        user_data['tos_str'] = self.ip.parse_tos(**parameters)
        user_data['drop_precedence_str'] = \
            self.ip.parse_drop_precedence(**parameters)
        user_data['drop_precedence_force_str'] = \
            self.ip.parse_drop_precedence_force(**parameters)
        user_data['log_str'] = self.ip.parse_log(**parameters)
        user_data['mirror_str'] = self.ip.parse_mirror(**parameters)

        return user_data

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
            >>> from pyswitch.device import Device
            >>> conn=('10.37.73.148', 22)
            >>> auth=('admin', 'admin')
            >>> with Device(conn=conn, auth=auth,
            ...             connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1',
            ...                              acl_type='extended',
            ...                              address_type='mac')
            ...     print dev.acl.add_ipv4_rule_acl(acl_name='Acl_1',
            ...                                   action='permit',
            ...                                   source='any',
            ...                                   dst='any',
            ...                                   vlan=10)
            ...     print dev.acl.delete_ipv4_acl_rule(acl_name='Acl_1',
            ...                                   seq_id=10)
        """
        params_validator.validate_params_mlx_delete_ipv4_rule_acl(**parameters)

        acl_name = parameters['acl_name']
        seq_id = parameters['seq_id']
        acl_type = self.get_acl_type(acl_name)
        self.is_valid_seq_id(seq_id, acl_name)

        cli_arr = ['ip access-list ' + ' ' + acl_type + ' ' + acl_name]

        cmd = acl_template.delete_rule_by_seq_id
        t = jinja2.Template(cmd)
        config = t.render(seq_id_str=parameters['seq_id'])
        config = re.sub(r'[^a-zA-Z0-9 .-]', r'', config)
        config = ' '.join(config.split())
        cli_arr.append(config)

        output = self._callback(cli_arr, handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3], config, output)

    def add_ipv6_rule_acl(self, **parameters):
        """
        Add rules to Access Control List of ipv6.
        Args:
            parameters contains:
                acl_name(string): Name of the access list
                seq_id(integer): Sequence number of the rule,
                    if not specified, the rule is added
                    at the end of the list. Valid range is 0 to 4294967290
                action(string): Action performed by ACL rule
                    - permit (default)
                    - deny
                protocol_type(string): Type of IP packets to be filtered based
                    on protocol. Valid values are 0 through 255 or key words
                    ahp, esp, icmp, ipv6, sctp, tcp, udp
                source(string): Source address filters
                    { any | S_IPaddress mask | host S_IPaddress }
                        [ source-operator [ S_port-numbers ] ]
                destination(string):Destination address filters
                    { any | S_IPaddress mask | host S_IPaddress }
                        [ source-operator [ S_port-numbers ] ]
                dscp(string): Matches the specified value against the DSCP
                    value of the packet to filter.
                    Can be either a numerical value or DSCP name
                drop_precedence_force(string): Matches the drop_precedence
                    value of the packet.  Allowed values are 0 through 2.
                urg(string): Enables urg for the rule
                ack(string): Enables ack for the rule
                push(string): Enables push for the rule
                fin(string): Enables fin for the rule
                rst(string): Enables rst for the rule
                sync(string): Enables sync for the rule
                vlan_id:(integer): VLAN interface to which the ACL is bound
                count(string): Enables statistics for the rule
                log(string): Enables logging for the rule
                mirror(string): Enables mirror for the rule
                copy_sflow(string): Enables copy-sflow for the rule
        Returns:
            Return True
        Raises:
            Exception, ValueError for invalid seq_id.
        """
        params_validator.validate_params_mlx_add_ipv6_rule_acl(**parameters)

        acl_name = parameters['acl_name']
        ret = self.get_acl_address_and_acl_type(acl_name)
        address_type = ret['protocol']

        if address_type != 'ipv6':
            raise ValueError('{} not supported'.format(address_type))

        cli_arr = ['ipv6 access-list ' + ' ' + acl_name]

        user_data = self.parse_params_for_add_ipv6_extended(**parameters)
        cmd = acl_template.add_ipv6_standard_acl_rule_template

        t = jinja2.Template(cmd)
        config = t.render(**user_data)
        config = ' '.join(config.split())
        cli_arr.append(config)

        output = self._callback(cli_arr, handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3], config, output)

    def parse_params_for_add_ipv6_extended(self, **parameters):
        """
        Parase parameters passed to add_ipv6_rule_acl method.
        Args:
            parameters contains:
                all parameters passed to add_ipv6_rule_acl
        Returns:
            Return a dict cotaining the parameters in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        """
        user_data = {}
        user_data['acl_name_str'] = parameters['acl_name']
        user_data['seq_id_str'] = self.ipv6.parse_seq_id(**parameters)
        user_data['action_str'] = self.ipv6.parse_action(**parameters)
        user_data['vlan_str'] = self.ipv6.parse_vlan(**parameters)
        user_data['protocol_str'] = self.ipv6.parse_protocol(**parameters)
        user_data['source_str'] = self.ipv6.parse_source(**parameters)
        user_data['dst_str'] = self.ipv6.parse_destination(**parameters)
        user_data['dscp_mapping_str'] = \
            self.ipv6.parse_dscp_mapping(**parameters)
        user_data['fragment_str'] = self.ipv6.parse_fragment(**parameters)
        user_data['tcp_operator_str'] = \
            self.ipv6.parse_tcp_operator(**parameters)
        user_data['icmp_filter_str'] = \
            self.ipv6.parse_icmp_filter(**parameters)
        user_data['copy_sflow_str'] = self.ipv6.parse_copy_sflow(**parameters)
        user_data['drop_precedence_str'] = \
            self.ipv6.parse_drop_precedence(**parameters)
        user_data['drop_precedence_force_str'] = \
            self.ipv6.parse_drop_precedence_force(**parameters)
        user_data['dscp_marking_str'] = \
            self.ipv6.parse_dscp_marking(**parameters)
        user_data['priority_force_str'] = \
            self.ipv6.parse_priority_force(**parameters)
        user_data['priority_mapping_str'] = \
            self.ipv6.parse_priority_mapping(**parameters)
        user_data['suppress_rpf_drop_str'] = \
            self.ipv6.parse_suppress_rpf_drop(**parameters)
        user_data['mirror_str'] = self.ipv6.parse_mirror(**parameters)
        user_data['log_str'] = self.ipv6.parse_log(**parameters)
        return user_data

    def delete_ipv6_acl_rule(self, **parameters):
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
            >>> from pyswitch.device import Device
            >>> conn=('10.37.73.148', 22)
            >>> auth=('admin', 'admin')
            >>> with Device(conn=conn, auth=auth,
            ...             connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1',
            ...                              acl_type='extended',
            ...                              address_type='ipv6')
            ...     print dev.acl.add_ipv6_rule_acl(acl_name='Acl_1',
            ...                                   action='permit',
            ...                                   source='any',
            ...                                   dst='any',
            ...                                   vlan=10)
            ...     print dev.acl.delete_ipv6_acl_rule(acl_name='Acl_1',
            ...                                   seq_id=10)
        """
        params_validator.validate_params_mlx_delete_ipv6_rule_acl(**parameters)

        acl_name = parameters['acl_name']
        seq_id = parameters['seq_id']
        self.is_valid_seq_id(seq_id, acl_name)

        cli_arr = ['ipv6 access-list ' + ' ' + acl_name]

        cmd = acl_template.delete_rule_by_seq_id
        t = jinja2.Template(cmd)
        config = t.render(seq_id_str=parameters['seq_id'])
        config = re.sub(r'[^a-zA-Z0-9 .-]', r'', config)
        config = ' '.join(config.split())
        cli_arr.append(config)

        output = self._callback(cli_arr, handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3], config, output)

    def get_address_type(self, acl_name):
        """
        get_address_type determines address type for the provided acl_name

        Args:
            acl_name (str): Name of the access list.
        Returns:
            Returns a string containing address type.
        Raises:
            Exception, ValueError
        Examples:
        """
        ret = self.get_acl_address_and_acl_type(acl_name)
        return ret['protocol']

    def get_acl_type(self, acl_name):
        """
        get_acl_type determines acl type for the provided acl_name

        Args:
            acl_name (str): Name of the access list.
        Returns:
            Returns a string containing acl type.
        Raises:
            Exception, ValueError
        Examples:
        """

        ret = self.get_acl_address_and_acl_type(acl_name)
        return ret['type']

    def get_acl_address_and_acl_type(self, acl_name):
        """
        get_acl_address_and_acl_type determines acl type and address
        type for the provided acl_name

        Args:
            acl_name (str): Name of the access list.
        Returns:
            Return a dict
            {'type':'standard'/'extended;, 'protocol':'mac'/'ip'/'ipv6'}.
        Raises:
            Exception, ValueError
        Examples:
        """

        ret = {'type': '', 'protocol': ''}
        res = self._callback('show access-list all',
                             handler='cli-get').split('\n')
        res += self._callback('show ipv6 access-list',
                              handler='cli-get').split('\n')

        for line in res:
            if acl_name in line:
                if line[0:4] == 'mac ':
                    ret['protocol'] = 'mac'
                    ret['type'] = 'extended'
                elif line[0:3] == 'ip ':
                    ret['protocol'] = 'ip'
                    if 'extended' in line:
                        ret['type'] = 'extended'
                    else:
                        ret['type'] = 'standard'
                elif line[0:5] == 'ipv6 ':
                    ret['protocol'] = 'ipv6'
                    ret['type'] = 'standard'
                break

        if ret['protocol'] != '':
            return ret

        raise ValueError("Failed to identify acl_type."
                         " Check if the ACL {} exists".format(acl_name))

    def get_configured_seq_ids(self, acl_name, address_type):
        """
        get_configured_seq_ids get existing seq_ids.
        Args:
            acl_name (str): Name of the access list.
        Returns:
            Return True
        Raises:
            Exception
        Examples:
        """
        if not acl_name:
            raise ValueError('Acl Name is manadatory parameter')

        if not address_type:
            raise ValueError('Address type is manadatory parameter')

        if address_type == 'mac':
            cmd = acl_template.show_l2_access_list
        elif address_type == 'ip':
            cmd = acl_template.show_ip_access_list
        elif address_type == 'ipv6':
            cmd = acl_template.show_ipv6_access_list
        else:
            raise ValueError('{} not supported'.format(address_type))

        t = jinja2.Template(cmd)
        config = t.render(acl_name_str=acl_name)
        config = ' '.join(config.split())

        output = self._callback(config, handler='cli-get')

        # Check if there is any error
        self._process_cli_output(inspect.stack()[0][3], config, output)

        re_cmp = re.compile(r'\d+: ')
        configured_seq_ids = re_cmp.findall(output)
        configured_seq_ids = [int(x[:-2]) for x in configured_seq_ids]
        return configured_seq_ids

    def set_seq_id_for_bulk_rules(self, existing_seq_ids, acl_rules):

        user_seq_ids = [rule['seq_id'] for rule in acl_rules
                        if 'seq_id' in rule and rule['seq_id']]

        # There are configured rules and user has requested rules with seq_ids
        if existing_seq_ids and user_seq_ids:

            # Validate if user has provided all or none seq_id
            if len(user_seq_ids) != len(acl_rules):
                raise ValueError("User should provide seq_id for all or none "
                                 "of the rules")

            # Validate if user provided ids are not overlapping
            overlapping_ids = set(user_seq_ids).intersection(existing_seq_ids)
            if overlapping_ids:
                    raise ValueError("These sequence ids are already "
                                     "configured: {}".format(overlapping_ids))

            acl_rules = sorted(acl_rules, key=lambda k: k['seq_id'])

        elif user_seq_ids:
            # Validate if user has provided all or none seq_id
            if len(user_seq_ids) != len(acl_rules):
                raise ValueError("User should provide seq_id for all or none "
                                 "of the rules")

            acl_rules = sorted(acl_rules, key=lambda k: k['seq_id'])

        elif existing_seq_ids:
            next_seq_id = (max(existing_seq_ids) + 10) // 10 * 10

            # Assign seq_id to all the rules.
            for rule in acl_rules:
                rule['seq_id'] = next_seq_id
                next_seq_id = next_seq_id + 10
        else:
            next_seq_id = 10

            # Assign seq_id to all the rules.
            for rule in acl_rules:
                rule['seq_id'] = next_seq_id
                next_seq_id = next_seq_id + 10

        return True

    def validate_std_rules(self, acl_name, acl_rules):
        user_data_list = []
        for rule in acl_rules:
            rule['acl_name'] = acl_name
            params_validator.validate_params_mlx_add_std_ipv4_rule_acl(**rule)
            user_data = self.parse_params_for_add_ipv4_standard(**rule)
            rule['address_type'] = 'ip'
            user_data_list.append(user_data)
        return user_data_list

    def validate_ext_rules(self, acl_name, acl_rules):
        user_data_list = []
        for rule in acl_rules:
            rule['acl_name'] = acl_name
            params_validator.validate_params_mlx_add_ipv4_rule_acl(**rule)
            rule['address_type'] = 'ip'
            user_data = self.parse_params_for_add_ipv4_extended(**rule)
            user_data_list.append(user_data)
        return user_data_list

    def add_ipv4_rule_acl_bulk(self, **kwargs):
        """
        Add ACL rule to an existing IPv4 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (array): List of ACL sequence rules.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='ip')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1',
                        acl_rules = [{"seq_id": 10, "action": "permit",
                                      "source": "host 192.168.0.3")
        """
        if 'acl_rules' not in kwargs or not kwargs['acl_rules']:
            return True

        acl_rules = kwargs['acl_rules']

        if len(acl_rules) > 64:
            raise ValueError("On MLX device maximum 64 rules can be bulked "
                             "while rule creation")

        # Parse params
        acl_name = self.ip.parse_acl_name(**kwargs)
        ret = self.get_acl_address_and_acl_type(acl_name)
        acl_type = ret['type']
        address_type = ret['protocol']

        if address_type != 'ip':
            raise ValueError("IPv4 Rule can not be added to non-ip ACL."
                             "ACL {} is of type {}"
                             .format(acl_name, address_type))

        # Get already configured seq_ids
        configured_seq_ids = self.get_configured_seq_ids(acl_name,
                                                         address_type)

        # if there are already configured rules. Make sure that they are
        # not overlapping with new rules to be configured
        self.set_seq_id_for_bulk_rules(configured_seq_ids, acl_rules)

        # Parse parameters
        if acl_type == 'standard':
            user_data_list = self.validate_std_rules(acl_name, acl_rules)
            cmd = acl_template.add_ip_standard_acl_rule_template
        elif acl_type == 'extended':
            user_data_list = self.validate_ext_rules(acl_name, acl_rules)
            cmd = acl_template.add_ip_extended_acl_rule_template
        else:
            raise ValueError('{} not supported'.format(acl_type))

        configured_count = 0

        cli_arr = ['ip access-list ' + ' ' + acl_type + ' ' + acl_name]
        for user_data in user_data_list:
            t = jinja2.Template(cmd)
            config = t.render(**user_data)
            config = ' '.join(config.split())
            cli_arr.append(config)
            try:
                output = self._callback(cli_arr, handler='cli-set')
                if 'Failed to initialize dns request' in output:
                    raise ValueError('ACL DNS: Errno(5) Failed '
                                     'to initialize dns request')
                if 'are undefined' in output:
                    raise ValueError('Invlaid icmp filter: {}'
                                     .format(user_data['icmp_filter']))
                self._process_cli_output(inspect.stack()[0][3], config, output)
                configured_count = configured_count + 1
                cli_arr.pop()
            except Exception as err:
                raise ValueError(err)
        return True

    def delete_ipv4_acl_rule_bulk(self, **kwargs):
        """
        Delete ACL rules from IPv4 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (string): Range of ACL sequence rules.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='ip')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1',
                        acl_rules = [{"seq_id": 10, "action": "permit",
                                      "source": "host 192.168.0.3")
        """
        # Validate required and accepted kwargs
        params_validator.validate_params_mlx_delete_ipv4_rule_acl(**kwargs)

        acl_name = self.mac.parse_acl_name(**kwargs)

        ret = self.get_acl_address_and_acl_type(acl_name)
        acl_type = ret['type']
        address_type = ret['protocol']

        if address_type != 'ip':
            raise ValueError("IPv4 Rule can not be added to non-ip ACL."
                             "ACL {} is of type {}"
                             .format(acl_name, address_type))

        # Get already configured seq_ids
        configured_seq_ids = self.get_configured_seq_ids(acl_name,
                                                         address_type)
        seq_range = self.mac.parse_seq_id_by_range(configured_seq_ids,
                                                   **kwargs)

        cli_arr = ['ip access-list ' + ' ' + acl_type + ' ' + acl_name]

        for seq_id in seq_range:
            cli_arr.append('no sequence ' + str(seq_id))

        output = self._callback(cli_arr, handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3],
                                        str(cli_arr), output)

    def validate_l2_acl_rules(self, acl_name, acl_rules):
        user_data_list = []
        for rule in acl_rules:
            rule['acl_name'] = acl_name
            params_validator.\
                validate_params_mlx_add_or_remove_l2_acl_rule(**rule)
            user_data = self.parse_params_for_add_l2_acl_rule(**rule)
            rule['address_type'] = 'mac'
            user_data_list.append(user_data)
        return user_data_list

    def add_l2_acl_rule_bulk(self, **kwargs):
        """
        Add ACL rule to an existing L2 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (array): List of ACL sequence rules.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.add_mac_acl_rule(acl_name='Acl_1', seq_id=20,
                                                   action='permit',
                                                   source='host',
                                                   srchost='2222.2222.2222')
        """
        if 'acl_rules' not in kwargs or not kwargs['acl_rules']:
            return True

        acl_rules = kwargs['acl_rules']

        if len(acl_rules) > 64:
            raise ValueError("On MLX device maximum 64 rules can be bulked "
                             "while rule creation")

        # Parse params
        acl_name = self.mac.parse_acl_name(**kwargs)

        try:
            ret = self.get_acl_address_and_acl_type(acl_name)
            address_type = ret['protocol']

            if address_type != 'mac':
                raise ValueError("l2 Rule can not be added to non-l2 ACL."
                                 "ACL {} is of type {}"
                                 .format(acl_name, address_type))
        except Exception:
            address_type = 'mac'

        # Get already configured seq_ids
        configured_seq_ids = self.get_configured_seq_ids(acl_name,
                                                         address_type)

        # if there are already configured rules. Make sure that they are
        # not overlapping with new rules to be configured
        self.set_seq_id_for_bulk_rules(configured_seq_ids, acl_rules)

        # Parse parameters
        user_data_list = self.validate_l2_acl_rules(acl_name, acl_rules)
        cmd = acl_template.add_l2_acl_rule_template

        configured_count = 0

        cli_arr = ['mac access-list ' + acl_name]
        for user_data in user_data_list:

            t = jinja2.Template(cmd)
            config = t.render(**user_data)
            config = ' '.join(config.split())
            cli_arr.append(config)
            try:
                output = self._callback(cli_arr, handler='cli-set')
                self._process_cli_output(inspect.stack()[0][3], config, output)
                configured_count = configured_count + 1
                cli_arr.pop()
            except Exception as err:
                raise ValueError(err)
        return True

    def delete_l2_acl_rule_bulk(self, **parameters):
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
            >>> from pyswitch.device import Device
            >>> conn=('10.37.73.148', 22)
            >>> auth=('admin', 'admin')
            >>> with Device(conn=conn, auth=auth,
            ...             connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1',
            ...                              acl_type='extended',
            ...                              address_type='mac')
            ...     print dev.acl.add_l2_acl_rule(acl_name='Acl_1',
            ...                                   action='permit',
            ...                                   source='any',
            ...                                   dst='any',
            ...                                   vlan=10)
            ...     print dev.acl.delete_l2_acl_rule(acl_name='Acl_1',
            ...                                   vlan=10)
        """
        # Validate required and accepted kwargs
        params_validator.validate_params_mlx_delete_l2_acl_rule(**parameters)
        acl_name = self.mac.parse_acl_name(**parameters)

        ret = self.get_acl_address_and_acl_type(acl_name)
        address_type = ret['protocol']

        if address_type != 'mac':
            raise ValueError("L2 Rule can not be added to non-l2 ACL."
                             "ACL {} is of type {}"
                             .format(acl_name, address_type))

        # Get already configured seq_ids
        configured_seq_ids = self.get_configured_seq_ids(acl_name, 'mac')
        seq_range = self.mac.parse_seq_id_by_range(configured_seq_ids,
                                                   **parameters)

        cli_arr = ['mac access-list ' + acl_name]

        for seq_id in seq_range:
            cli_arr.append('no sequence ' + str(seq_id))

        output = self._callback(cli_arr, handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3],
                                        str(cli_arr), output)

    def validate_ipv6_rules(self, acl_name, acl_rules):
        user_data_list = []
        for rule in acl_rules:
            rule['acl_name'] = acl_name
            params_validator.validate_params_mlx_add_ipv6_rule_acl(**rule)
            user_data = self.parse_params_for_add_ipv6_extended(**rule)
            rule['address_type'] = 'ipv6'
            user_data_list.append(user_data)
        return user_data_list

    def add_ipv6_rule_acl_bulk(self, **kwargs):
        """
        Add ACL rule to an existing IPv6 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (array): List of ACL sequence rules.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='ip')
            >>>     print dev.acl.add_ipv6_acl_rule(acl_name='Acl_1',
                        acl_rules = [{"seq_id": 10, "action": "permit",
                                      "source": "host 192.168.0.3")
        """
        if 'acl_rules' not in kwargs or not kwargs['acl_rules']:
            return True

        acl_rules = kwargs['acl_rules']

        if len(acl_rules) > 64:
            raise ValueError("On MLX device maximum 64 rules can be bulked "
                             "while rule creation")

        # Parse params
        acl_name = self.ip.parse_acl_name(**kwargs)
        ret = self.get_acl_address_and_acl_type(acl_name)
        address_type = ret['protocol']

        if address_type != 'ipv6':
            raise ValueError("IPv6 Rule can not be added to non-ip ACL."
                             "ACL {} is of type {}"
                             .format(acl_name, address_type))

        # Get already configured seq_ids
        configured_seq_ids = self.get_configured_seq_ids(acl_name,
                                                         address_type)

        # if there are already configured rules. Make sure that they are
        # not overlapping with new rules to be configured
        self.set_seq_id_for_bulk_rules(configured_seq_ids, acl_rules)

        # Parse parameters
        user_data_list = self.validate_ipv6_rules(acl_name, acl_rules)

        configured_count = 0
        cli_arr = ['ipv6 access-list ' + acl_name]

        for user_data in user_data_list:

            cmd = acl_template.add_ipv6_standard_acl_rule_template
            t = jinja2.Template(cmd)
            config = t.render(**user_data)
            config = ' '.join(config.split())
            cli_arr.append(config)
            try:
                output = self._callback(cli_arr, handler='cli-set')
                self._process_cli_output(inspect.stack()[0][3], config, output)
                configured_count = configured_count + 1
                cli_arr.pop()
            except Exception as err:
                raise ValueError(err)
        return True

    def delete_ipv6_acl_rule_bulk(self, **kwargs):
        """
        Delete ACL rules from IPv6 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (string): Range of ACL sequence rules.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='ip')
            >>>     print dev.acl.add_ipv6_acl_rule(acl_name='Acl_1',
                        acl_rules = [{"seq_id": 10, "action": "permit",
                                      "source": "host 192.168.0.3")
        """
        # Validate required and accepted kwargs
        params_validator.validate_params_mlx_delete_ipv6_rule_acl(**kwargs)

        acl_name = self.mac.parse_acl_name(**kwargs)

        ret = self.get_acl_address_and_acl_type(acl_name)
        address_type = ret['protocol']

        if address_type != 'ipv6':
            raise ValueError("IPv6 Rule can not be deleted from non-ipv6 ACL."
                             "ACL {} is of type {}"
                             .format(acl_name, address_type))

        # Get already configured seq_ids
        configured_seq_ids = self.get_configured_seq_ids(acl_name,
                                                         address_type)
        seq_range = self.mac.parse_seq_id_by_range(configured_seq_ids,
                                                   **kwargs)

        cli_arr = ['ipv6 access-list ' + acl_name]

        for seq_id in seq_range:
            cli_arr.append('no sequence ' + str(seq_id))

        output = self._callback(cli_arr, handler='cli-set')
        return self._process_cli_output(inspect.stack()[0][3],
                                        str(cli_arr), output)

    def _get_acl_rules(self, address_type, acl_type, acl_name, seq_range):
        """
        Return list of rules configured for acl_name
        """
        rules_list = []

        if address_type == 'mac':
            cmd = acl_template.show_l2_access_list
        elif address_type == 'ip':
            cmd = acl_template.show_ip_access_list
        elif address_type == 'ipv6':
            cmd = acl_template.show_ipv6_access_list
        else:
            raise ValueError('{} not supported'.format(address_type))

        t = jinja2.Template(cmd)
        config = t.render(acl_name_str=acl_name)
        config = ' '.join(config.split())

        output = self._callback(config, handler='cli-get')

        # Check if there is any error
        self._process_cli_output(inspect.stack()[0][3], config, output)

        if address_type == 'mac':
            rules_list = self._parse_l2_rule(output, seq_range)
        elif address_type == 'ip':
            if acl_type == 'standard':
                rules_list = self._parse_std_ip_rule(output, seq_range)
            elif acl_type == 'extended':
                rules_list = self._parse_ext_ip_rule(output, seq_range)
        elif address_type == 'ipv6':
            pass

        return rules_list

    def _parse_l2_rule(self, output, seq_range):

        rules_list = []
        for line in output.split('\n'):
            if line:
                rule = line.split()

                index = 0
                if rule[index][:-1].isdigit():

                    if int(rule[index][:-1]) in seq_range:
                        config = {}

                        config['seq_id'] = rule[index][:-1]
                        index += 1

                        config['action'] = rule[index]
                        index += 1

                        config['source'] = rule[index]
                        index += 1

                        if config['source'] != 'any':
                            config['src_mac_addr_mask'] = rule[index]
                            index += 1

                        config['dst'] = rule[index]
                        index += 1

                        if config['dst'] != 'any':
                            config['dst_mac_addr_mask'] = rule[index]
                            index += 1

                        config['vlan'] = rule[index]
                        index += 1

                        for j, val in enumerate(rule[index:]):
                            i = index + j
                            if val == 'etype':
                                config['ethertype'] = rule[i + 1]
                            elif val == 'priority':
                                config['priority'] = rule[i + 1]
                            elif val == 'priority-force':
                                config['priority_force'] = rule[i + 1]
                            elif val == 'priority-mapping':
                                config['priority_mapping'] = rule[i + 1]
                            elif val == 'drop-precedence-force':
                                config['drop_precedence_force'] = rule[i + 1]
                            elif val == 'drop-precedence':
                                config['drop_precedence'] = rule[i + 1]
                            elif val == 'mirror':
                                config['mirror'] = "True"
                            elif val == 'log':
                                config['log'] = "True"
                            elif val == 'arp-guard':
                                config['arp_guard'] = "True"

                        rules_list.append(config)

        return rules_list

    def _parse_std_ip_rule(self, output, seq_range):

        rules_list = []
        for line in output.split('\n'):
            if line:
                rule = line.split()

                index = 0
                if rule[index][:-1].isdigit():

                    if int(rule[index][:-1]) in seq_range:
                        config = {}

                        config['seq_id'] = rule[index][:-1]
                        index += 1

                        config['action'] = rule[index]
                        index += 1

                        config['source'] = rule[index]
                        index += 1

                        if config['source'] != 'any':
                            config['source'] += '/' + rule[index]
                            index += 1

                        if 'log' in rule:
                            config['log'] = "True"

                        rules_list.append(config)
        return rules_list

    def _parse_ext_ip_rule(self, output, seq_range):

        rules_list = []
        for line in output.split('\n'):
            if line:
                rule = line.split()

                index = 0
                if rule[index][:-1].isdigit():

                    if int(rule[index][:-1]) in seq_range:
                        config = {}

                        config['seq_id'] = rule[index][:-1]
                        index += 1

                        config['action'] = rule[index]
                        index += 1

                        if rule[index] == 'vlan':
                            config['vlan_id'] = rule[index + 1]
                            index += 2

                        config['protocol_type'] = rule[index]
                        index += 1

                        config['source'] = rule[index]
                        index += 1

                        if config['source'] == 'host':
                            config['source'] += ',' + rule[index]
                            index += 1
                        elif config['source'] != 'any':
                            config['source'] += '/' + rule[index]
                            index += 1

                        if rule[index] in ['eq', 'lt', 'gt', 'neq']:
                            config['source'] += ' ' + rule[index] + \
                                ' ' + rule[index + 1]
                            index += 2

                        elif rule[index] == 'range':
                            config['source'] += ' ' + rule[index] + \
                                ' ' + rule[index + 1] + ' ' + rule[index + 2]
                            index += 3

                        config['destination'] = rule[index]
                        index += 1

                        if config['destination'] == 'host':
                            config['destination'] += ',' + rule[index]
                            index += 1
                        elif config['destination'] != 'any':
                            config['destination'] += '/' + rule[index]
                            index += 1

                        if len(rule) == index:
                            rules_list.append(config)
                            continue

                        if rule[index] in ['eq', 'lt', 'gt', 'neq']:
                            config['destination'] += ' ' + rule[index] + \
                                ' ' + rule[index + 1]
                            index += 2
                        elif rule[index] == 'range':
                            config['destination'] += ' ' + rule[index] + \
                                ' ' + rule[index + 1] + ' ' + rule[index + 2]
                            index += 3

                        if len(rule) == index:
                            rules_list.append(config)
                            continue

                        for j, val in enumerate(rule[index:]):
                            i = index + j
                            if val == 'priority':
                                config['priority'] = rule[i + 1]
                            elif val == 'priority-force':
                                config['priority_force'] = rule[i + 1]
                            elif val == 'priority-mapping':
                                config['priority_mapping'] = rule[i + 1]
                            elif val == 'drop-precedence-force':
                                config['drop_precedence_force'] = rule[i + 1]
                            elif val == 'drop-precedence':
                                config['drop_precedence'] = rule[i + 1]
                            elif val == 'precedence':
                                config['precedence'] = rule[i + 1]
                            elif val == 'dscp-marking':
                                config['dscp_marking'] = rule[i + 1]
                            elif val == 'dscp-mapping':
                                config['dscp'] = rule[i + 1]
                            elif val == 'option':
                                config['option'] = rule[i + 1]
                            elif val == 'tos':
                                config['tos'] = rule[i + 1]
                            elif val == 'mirror':
                                config['mirror'] = "True"
                            elif val == 'log':
                                config['log'] = "True"
                            elif val == 'suppress-rpf-drop':
                                config['suppress_rpf_drop'] = "true"
                            elif val == 'fragment':
                                config['fragment'] = "True"
                            elif val == 'copy-sflow':
                                config['copy_sflow'] = "True"
                            elif val == 'established':
                                if 'tcp_operator' in config:
                                    config['tcp_operator'] = 'established syn'
                                else:
                                    config['tcp_operator'] = 'established'
                            elif val == 'syn':
                                if 'tcp_operator' in config:
                                    config['tcp_operator'] = 'established syn'
                                else:
                                    config['tcp_operator'] = 'syn'
                            elif val in ['administratively-prohibited',
                                         'any-icmp-type',
                                         'destination-host-prohibited',
                                         'destination-host-unknown',
                                         'destination-net-prohibited',
                                         'destination-network-unknown',
                                         'echo',
                                         'echo-reply',
                                         'general-parameter-problem',
                                         'host-precedence-violation',
                                         'host-redirect',
                                         'host-tos-redirect',
                                         'host-tos-unreachable',
                                         'host-unreachable',
                                         'information-reply',
                                         'information-request',
                                         'mask-reply',
                                         'mask-request',
                                         'net-redirect',
                                         'net-tos-redirect',
                                         'net-tos-unreachable',
                                         'net-unreachable',
                                         'packet-too-big',
                                         'parameter-problem',
                                         'port-unreachable',
                                         'precedence-cutoff',
                                         'protocol-unreachable',
                                         'reassembly-timeout',
                                         'redirect',
                                         'router-advertisement',
                                         'router-solicitation',
                                         'source-host-isolated',
                                         'source-quench',
                                         'source-route-failed',
                                         'time-exceeded',
                                         'timestamp-reply',
                                         'timestamp-request',
                                         'ttl-exceeded',
                                         'unreachable']:
                                config['icmp_filter'] = val
                        rules_list.append(config)
        return rules_list

    def get_acl_rules(self, **kwargs):
        """
        Returns the number of congiured rules
        Args:
            acl_name (str): Name of the access list.
        Returns:
            Number of rules configured,
        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.get_acl_rules(acl_name='Acl_1',
                                                seq_id='all')
        """

        # Validate required and accepted parameters
        params_validator.validate_params_mlx_get_acl_rules(**kwargs)

        # Parse params
        acl_name = self.mac.parse_acl_name(**kwargs)

        acl = self.get_acl_address_and_acl_type(acl_name)
        acl_type = acl['type']
        address_type = acl['protocol']

        seq_range = self.mac.parse_seq_id_by_range(range(20480), **kwargs)

        rules_list = self._get_acl_rules(address_type, acl_type, acl_name,
                                         seq_range)

        resp_body = json.dumps(rules_list)
        return resp_body
