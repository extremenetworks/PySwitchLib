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

import jinja2
import pyswitch.raw.slx_nos.acl.params_validator as params_validator
import pyswitch.utilities as utilities
from pyswitch.raw.nos.base.acl import acl_template
from pyswitch.raw.slx_nos.acl.acl import SlxNosAcl
from pyswitch.raw.slx_nos.acl.macacl import MacAcl
from pyswitch.raw.slx_nos.acl.ipv46acl import IpAcl


class Acl(SlxNosAcl):
    """
    The Acl class holds all the functions assocaiated with the Access Control
    list of a NOS device.

    Attributes:
        None
    """

    os_type = "nos"

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

    @property
    def mac(self):
        return self._mac

    @property
    def ip(self):
        return self._ip

    def add_ipv46_rule_acl(self, **kwargs):
        """
        Add ACL rule to an existing IPv4 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (array): List of ACL sequence rules.
            seq_id (int): Sequence number of the rule.
            action (str): Action to apply on the traffic
                (deny/permit/hard-drop).
            protocol_type (str): Type of IP packets to be filtered (<0-255>,
                tcp, udp, icmp or ip).
            source (str): Source filter, can be 'any' or 'host', or the actual
                 MAC address.
            destination (str): Destination filter, can be 'any' or 'host', or
                the actual MAC.
            dscp (str): DSCP values of the packet to filter.
            urg (str): Enables urg for the rule.
            ack (str): Enables ack for the rule.
            push (str):Enables push for the rule.
            fin (str): Enables fin for the rule.
            rst (str): Enables rst for the rule.
            sync (str): Enables sync for the rule.
            vlan (str): VLAN ID for the rule.
            count (str): Enables the packet count.
            log (str): Enables the logging.
            callback (function): A function executed upon completion of the
                method. The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
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
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10,
                                                  action='permit',
                                                  source='host 192.168.0.3')
        """
        # Parse params
        acl_name = self.ip.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)
        acl = self._get_acl_info(acl_name, get_seqs=True)

        acl_type = acl['type']
        address_type = acl['protocol']

        self.logger.info('Successfully identified the acl_type as ({}:{})'
                         .format(address_type, acl_type))

        # This is required to distinguish between ipv4 or v6
        kwargs['address_type'] = address_type

        if acl_type == 'standard':
            user_data = self._parse_params_for_add_standard(**kwargs)
        elif acl_type == 'extended':
            user_data = self._parse_params_for_add_extended(**kwargs)
        else:
            raise ValueError('{} not supported'.format(acl_type))

        # Validate seq_id if user has specified 
        next_seq = self._get_next_seq_id(acl['seq_ids'], user_data['seq_id'])

        user_data['seq_id'] = next_seq
        user_data['acl_type'] = acl_type
        user_data['address_type'] = address_type

        t = jinja2.Template(acl_template.acl_rule_ip)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.info(config)

        callback(config)

        self.logger.info('Successfully added rule ACL {}'.format(acl_name))
        return True

    def _parse_params_for_add_standard(self, **kwargs):
        """
        Parses params for l2 Rule to be added to standard Access Control List.
        Args:
            Parse below params if contained in kwargs.
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
                count(string): Enables the packet count.
                log: (string) Enables logging for the rule
                    (Available for permit or deny only)
        Returns:
            Return a dict cotaining the kwargs in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        Examples:
        """
        user_data = {}
        user_data['acl_name'] = kwargs['acl_name']
        user_data['seq_id'] = self.ip.parse_seq_id(**kwargs)
        user_data['action'] = self.ip.parse_action(**kwargs)
        user_data['source'] = self.ip.parse_source(**kwargs)
        bool_params = ['log', 'count']
        self.ip.parse_boolean_params(user_data, bool_params, **kwargs)
        return user_data

    def _parse_params_for_add_extended(self, **kwargs):
        """
        Parses params for l2 Rule to be added to standard Access Control List.
        Args:
            Parse below params if contained in kwargs.
                acl_name: (string) Name of the access list
                seq_id: (integer) Sequence number of the rule,
                    if not specified, the rule is added at the end of the list.
                    Valid range is 0 to 4294967290
                action: (string) Action performed by ACL rule
                    - permit
                    - deny
                protocol_type(string): Type of IP packets to be filtered based
                    on protocol. Valid values are <0-255> or key words tcp,
                    udp, icmp or ip
                source: (string) Source address filters
                    { any | S_IPaddress/mask(0.0.0.255) |
                    host,S_IPaddress } [ source-operator [ S_port-numbers ] ]
                destination: (string) Destination address filters
                    { any | S_IPaddress/mask(0.0.0.255) |
                    host,S_IPaddress } [ source-operator [ S_port-numbers ] ]
                dscp(string): Matches the specified value against the DSCP
                    value of the packet to filter.  Allowed values 0 to 63.
                urg(string): Enables urg for the rule
                ack(string): Enables ack for the rule
                push(string): Enables push for the rule
                fin(string): Enables fin for the rule
                rst(string): Enables rst for the rule
                sync(string): Enables sync for the rule
                vlan_id(integer): VLAN interface to which the ACL is bound
                count(string): Enables the packet count.
                log: (string) Enables logging for the rule
                    (Available for permit or deny only)
        Returns:
            Return a dict cotaining the kwargs in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        Examples:
        """

        # Check for supported and mandatory kwargs
        mandatory_params = ['acl_name', 'action', 'protocol_type',
                            'source', 'destination']
        supported_params = ['acl_name', 'seq_id', 'action', 'protocol_type',
                            'source', 'destination', 'dscp', 'urg', 'ack',
                            'push', 'fin', 'rst', 'sync', 'vlan_id','count',
                            'log', 'address_type']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

        user_data = {}

        user_data['acl_name'] = kwargs['acl_name']
        user_data['seq_id'] = self.ip.parse_seq_id(**kwargs)
        user_data['action'] = self.ip.parse_action(**kwargs)
        user_data['protocol_type'] = self.ip.parse_protocol_type(**kwargs)
        user_data['source'] = self.ip.parse_source(**kwargs)
        user_data['destination'] = self.ip.parse_destination(**kwargs)
        user_data['dscp'] = self.ip.parse_dscp(**kwargs)
        user_data['vlan_id'] = self.ip.parse_vlan_id(**kwargs)

        # All these params of same type. Parsing them together
        bool_params = ['urg', 'ack', 'push', 'fin', 'rst', 'sync',
                       'log', 'count']
        self.ip.parse_boolean_params(user_data, bool_params, **kwargs)

        return user_data

    def add_ipv4_rule_acl(self, **kwargs):
        return self.add_ipv46_rule_acl(**kwargs)

    def add_ipv6_rule_acl(self, **kwargs):
        return self.add_ipv46_rule_acl(**kwargs)

    def add_l2_acl_rule(self, **kwargs):
        """
        Add ACL rule to an existing IPv4 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (array): List of ACL sequence rules.
            seq_id (int): Sequence number of the rule.
            action (str): Action to apply on the traffic
                (deny/permit/hard-drop).
            protocol_type (str): Type of IP packets to be filtered (<0-255>,
                tcp, udp, icmp or ip).
            source (str): Source filter, can be 'any' or 'host', or the actual
                 MAC address.
            destination (str): Destination filter, can be 'any' or 'host', or
                the actual MAC.
            dscp (str): DSCP values of the packet to filter.
            urg (str): Enables urg for the rule.
            ack (str): Enables ack for the rule.
            push (str):Enables push for the rule.
            fin (str): Enables fin for the rule.
            rst (str): Enables rst for the rule.
            sync (str): Enables sync for the rule.
            vlan (str): VLAN ID for the rule.
            count (str): Enables the packet count.
            log (str): Enables the logging.
            callback (function): A function executed upon completion of the
                method. The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
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
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10,
                                                  action='permit',
                                                  source='host 192.168.0.3')
        """
        params_validator.validate_params_nos_add_or_remove_l2_acl_rule(
            **kwargs)

        # Parse params
        acl_name = self.ip.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)
        acl = self._get_acl_info(acl_name, get_seqs=True)

        acl_type = acl['type']
        address_type = acl['protocol']

        self.logger.info('Successfully identified the acl_type as ({}:{})'
                         .format(address_type, acl_type))

        # This is required to distinguish between ipv4 or v6
        kwargs['address_type'] = address_type

        if acl_type == 'standard':
            user_data = self._parse_params_for_add_mac_standard(**kwargs)
        elif acl_type == 'extended':
            user_data = self._parse_params_for_add_mac_extended(**kwargs)
        else:
            raise ValueError('{} not supported'.format(acl_type))

        # Validate seq_id if user has specified 
        next_seq = self._get_next_seq_id(acl['seq_ids'], user_data['seq_id'])

        user_data['seq_id'] = next_seq
        user_data['acl_name'] = acl_name
        user_data['acl_type'] = acl_type
        user_data['address_type'] = address_type

        t = jinja2.Template(acl_template.acl_rule_mac)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.info(config)

        callback(config)

        self.logger.info('Successfully added rule ACL {}'.format(acl_name))
        return True

    def _parse_params_for_add_mac_standard(self, **kwargs):
        """
        Parses params for l2 Rule to be added to standard Access Control List.
        Args:
            Parse below params if contained in kwargs.
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
                count(string): Enables the packet count.
                log: (string) Enables logging for the rule
                    (Available for permit or deny only)
        Returns:
            Return a dict cotaining the kwargs in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        Examples:
        """

        # Check for supported and mandatory kwargs
        if 'arp_guard' in kwargs['arp_guard'] and \
            kwargs['arp_guard'] != 'False':
            raise ValueError("\'arp_guard\' not supported")

        if 'dst' in kwargs['dst'] and kwargs['dst'] != 'any':
            raise ValueError("\'dst\' not supported")

        if 'copy_sflow' in kwargs['copy_sflow'] and \
            kwargs['copy_sflow'] != 'False':
            raise ValueError("\'copy_sflow\' not supported")

        if 'mirror' in kwargs['mirror'] and kwargs['mirror'] != 'False':
            raise ValueError("\'mirror\' not supported")

        mandatory_params = ['acl_name', 'action', 'source']
        supported_params = ['acl_name', 'seq_id', 'action', 'source',
                            'srchost', 'src_mac_addr_mask',
                            'count', 'log', 'address_type',
                            'arp_guard', 'dst', 'copy_sflow', 'mirror']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

        user_data = {}

        user_data['acl_name'] = kwargs['acl_name']
        user_data['seq_id'] = self.mac.parse_seq_id(**kwargs)
        user_data['action'] = self.mac.parse_action(**kwargs)
        user_data['source'] = self.mac.parse_source(**kwargs)
        bool_params = ['log', 'count']
        self.mac.parse_boolean_params(user_data, bool_params, **kwargs)
        return user_data

    def _parse_params_for_add_mac_extended(self, **kwargs):
        """
        Parses params for l2 Rule to be added to standard Access Control List.
        Args:
            Parse below params if contained in kwargs.
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
                count(string): Enables the packet count.
                log: (string) Enables logging for the rule
                    (Available for permit or deny only)
        Returns:
            Return a dict cotaining the kwargs in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        Examples:
        """
        user_data = {}

        user_data['acl_name'] = kwargs['acl_name']
        user_data['seq_id'] = self.mac.parse_seq_id(**kwargs)
        user_data['action'] = self.mac.parse_action(**kwargs)
        user_data['source'] = self.mac.parse_source(**kwargs)
        user_data['dst'] = self.mac.parse_dst(**kwargs)
        user_data['ethertype'] = self.mac.parse_ethertype(**kwargs)
        user_data['vlan'] = self.mac.parse_vlan(**kwargs)
        bool_params = ['log', 'count']
        self.mac.parse_boolean_params(user_data, bool_params, **kwargs)

        return user_data

    def apply_acl(self, **kwargs):
        """
        Apply an ACL to a physical port, port channel, VE or management
        interface.
        Args:
            rbridge_id (str): RBridge ID of the VDX switch under which VE will
                be configured
            intf_type (str): Interface type, (physical, port channel, VE or
                management interface).
            intf_names (str[]): Array of the Interface Names.
            acl_name (str): Name of the access list.
            acl_direction (str): Direction of ACL binding on the specified
                interface [in/out].
            traffic_type (str): Traffic type for the ACL being applied
                [switched/routed].
            callback (function): A function executed upon completion of method.
                The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each interfaces.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                    connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.apply_acl(intf_type='ethernet',
                                            intf_name='0/1,0/2',
                                            acl_name='Acl_1',
                                            acl_direction='in',
                                            traffic_type='switched')
        """
        pass
        '''
        mandatory_params = ['acl_name', 'intf_name', 'intf_type',
                            'acl_direction']
        supported_params = ['acl_name', 'intf_name', 'intf_type', 'source',
                            'acl_direction', 'rbridge_id', 'traffic_type']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

        intf_type = kwargs['intf_type'].lower()
        intf_name = kwargs['intf_name']
        acl_name =  kwargs['acl_name']
        acl_direction = kwargs['acl_direction']

        rbridge_id = kwargs.pop('rbridge_id', '')
        traffic_type = kwargs.pop('traffic_type', '')
        callback = kwargs.pop('callback', self._callback)

        def self._get_acl_info(acl_name)
        acl_type = acl['type']
        address_type = acl['protocol']

        result = {}

        # Check is the user input for Interface Name is correct
        for intf in intf_name:
            if not utilities.validate_interface(intf_type, str(intf),
                                                rbridge_id=rbridge_id,
                                                os_type=self.os_type,
                                                logger=self.logger):
                raise ValueError("{} is not a valid Interface".format(intf))

        if address_type == 'mac':
            acl_apply = template.acl_apply_mac
        elif address_type == 'ip':
            acl_apply = template.acl_apply_ipv4
        else:
            acl_apply = template.acl_apply_ipv6

        for intf in intf_name:

            self.logger.info('Applying ACL {} on interface ({}-{})',
                             .format(acl_name, intf_type, intf))

            acl_apply = acl_apply.format(address_type=address_type,
                                         intf_type=intf_type.replace('_', '-'),
                                         intf=intf, acl_name=acl_name,
                                         acl_direction=acl_direction,
                                         traffic_type='' if not traffic_type else
                                         '<traffic-type>' + traffic_type + '</traffic-type>',
                                         delete='')
            if rbridge_id:
                config = template.rbridge_acl_apply
            else:
                config = '<config> {acl_apply} </config>'

            config = config.format(rbridge_id=rbridge_id, acl_apply=acl_apply)
            callback(config)
            self.logger.info('Successfully applied ACL %s on interface %s %s (%s)',
                             acl_name, intf_type, intf, acl_direction)
            result[intf] = True
        return result
        '''

    def remove_acl(self, **kwargs):
        pass

