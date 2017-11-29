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


import xml.etree.ElementTree
import jinja2
import math
import pyswitch.utilities as utilities
from pyswitch.raw.base.acl import Acl as BaseAcl
from pyswitch.raw.slxnos_common.acl import acl_template
from pyswitch.raw.slxnos_common.acl.macacl import MacAcl
from pyswitch.raw.slxnos_common.acl.ipacl import IpAcl


class SlxNosAcl(BaseAcl):
    """
    The Acl class holds all the functions assocaiated
    with the Access Control list of a SLXOS or NOS device.

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
        super(SlxNosAcl, self).__init__(callback)

        self._mac = MacAcl()
        self._ip = IpAcl()

    @property
    def mac(self):
        return self._mac

    @property
    def ip(self):
        return self._ip

    def create_acl(self, **kwargs):
        """
        Create an Access Control List.
        Args:
            address_type (str): ACL address type, ip or ipv6 or mac.
            acl_type (str): ACL type, extended or standard.
            acl_name (str): Unique name for ACL.
            callback (function): A function executed upon completion
                of the method. The only parameter passed to `callback` will be
                the ``ElementTree`` `config`.
        Returns:
            True,False or None for Success, failure and no-change respectively.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.create_acl(acl_name='Acl_2',
                                             acl_type='extended',
                                             address_type='ip')
            >>>     print dev.acl.create_acl(acl_name='Acl_3',
                                             acl_type='extended',
                                             address_type='ipv6')
        """

        # Parse params
        user_data = self._parse_params_for_create_acl(**kwargs)

        callback = kwargs.pop('callback', self._callback)

        self.logger.info('Creating ACL {} ({}:{})'.format(
                          kwargs['acl_name'], kwargs['address_type'],
                          kwargs['acl_type']))

        cmd = acl_template.acl_create

        t = jinja2.Template(cmd)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.info(config)
        callback(config)

        self.logger.info('Successfully created ACL {}'
                         .format(kwargs['acl_name']))
        return True

    def _parse_params_for_create_acl(self, **kwargs):
        # Check for supported and mandatory kwargs
        supported_params = ['address_type', 'acl_name', 'acl_type']
        mandatory_params = ['address_type', 'acl_name', 'acl_type']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

        user_data = {}
        user_data['acl_name'] = self.mac.parse_acl_name(**kwargs)
        user_data['address_type'] = self.mac.parse_address_type(**kwargs)
        user_data['acl_type'] = self.mac.parse_acl_type(**kwargs)

        return user_data

    def delete_acl(self, **kwargs):
        """
        Delete Access Control List.
        Args:
            acl_name (str): Name of the access list.
            callback (function): A function executed upon completion
                of the method.  The only parameter passed to `callback`
                will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.delete_acl(acl_name='Acl_2')
            >>>     print dev.acl.delete_acl(acl_name='Acl_1')
        """
        # Check for supported and mandatory kwargs
        supported_params = ['acl_name']
        mandatory_params = ['acl_name']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

        # Parse params
        acl_name = self.mac.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)
        acl = self._get_acl_info(acl_name)

        user_data = {'acl_name': acl_name,
                     'address_type': acl['protocol'],
                     'acl_type': acl['type']}

        self.logger.info('Deleting ACL {}'
                         .format(user_data))

        t = jinja2.Template(acl_template.acl_delete)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.info(config)
        callback(config)

        self.logger.info('Successfully deleted ACL {}'
                         .format(kwargs['acl_name']))
        return True

    def add_ipv4_rule_acl(self, **kwargs):
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

        if acl_type == 'standard':
            user_data = self._parse_params_for_add_ipv4_standard(**kwargs)
        elif acl_type == 'extended':
            user_data = self._parse_params_for_add_ipv4_extended(**kwargs)
        else:
            raise ValueError('{} not supported'.format(acl_type))

        # Validate seq_id if user has specified 
        if user_data['seq_id']:
            if int(user_data['seq_id']) in acl['seq_ids']:
                raise ValueError("Access-list entry with sequence number {} "
                                 "already exists.".format(user_data['seq_id']))
        else: # Generate a valid seq_id if user has not specified 
            if acl['seq_ids']:
                last_seq_id = max(acl['seq_ids'])
                user_data['seq_id'] = (last_seq_id + 10) // 10 * 10
            else:
                user_data['seq_id'] = 10

        user_data['acl_type'] = acl_type
        user_data['address_type'] = address_type

        t = jinja2.Template(acl_template.acl_rule_ip)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.info(config)

        callback(config)

        self.logger.info('Successfully added rule ACL {}'.format(acl_name))
        return True

    def _parse_params_for_add_ipv4_standard(self, **kwargs):
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
        mandatory_params = ['acl_name', 'action', 'source']
        supported_params = ['acl_name', 'seq_id', 'action', 'source',
                            'count', 'log']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

        user_data = {}

        user_data['acl_name'] = kwargs['acl_name']
        user_data['seq_id'] = self.ip.parse_seq_id(**kwargs)
        user_data['action'] = self.ip.parse_action(**kwargs)
        user_data['source'] = self.ip.parse_source(**kwargs)
        bool_params = ['log', 'count']
        self.ip.parse_boolean_params(user_data, bool_params, **kwargs)
        return user_data

    def _parse_params_for_add_ipv4_extended(self, **kwargs):
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
                            'log']
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

    def delete_ipv4_acl_rule(self, **kwargs):
        # Parse params
        acl_name = self.ip.parse_acl_name(**kwargs)
        seq_id = self.ip.parse_seq_id(**kwargs)
        callback = kwargs.pop('callback', self._callback)

        acl = self._get_acl_info(acl_name, get_seqs=True)
        acl_type = acl['type']
        address_type = acl['protocol']

        self.logger.info('Successfully identified the acl_type as ({}:{})'
                         .format(address_type, acl_type))

        # Validate seq_id if user has specified 
        if not seq_id:
            raise ValueError('seq_id is required to delete rule for {}'
                             .format(acl_name))

        if int(seq_id) not in acl['seq_ids']:
            raise ValueError("seq_id {} does not exists."
                              .format(seq_id))

        user_data = {}
        user_data['acl_type'] = acl_type
        user_data['address_type'] = address_type
        user_data['seq_id'] = seq_id
        user_data['acl_name'] = acl_name

        t = jinja2.Template(acl_template.acl_rule_ip_delete)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.info(config)

        callback(config)

        self.logger.info('Successfully deleted rule ACL {}'.format(acl_name))
        return True

    def add_ipv6_rule_acl(self, **kwargs):
        pass
    def delete_ipv6_acl_rule(self, **kwargs):
        pass

    def add_l2_acl_rule(self, **kwargs):
        pass
    def delete_l2_acl_rule(self, **kwargs):
        pass

    def apply_acl(self, **kwargs):
        pass
    def remove_acl(self, **kwargs):
        pass


    def _get_seq_ids(self, acl_elem, ret):

        # xml.etree.ElementTree.dump(acl_elem)
        seq_ids = []
        for elem in acl_elem.iter():
            if 'seq-id' in elem.tag:
                seq_ids.append(int(elem.text))

        ret['seq_ids'] = seq_ids
        return True

    def _get_acl_info(self, acl_name, get_seqs=False):
        """
        Return acl-type as dict 
            {'type':'standard'/'extended;, 'protocol':'mac'/'ip'/'ipv6'}.
        """
        seq_element = None

        for address_type in ['mac', 'ip', 'ipv6']:
            for acl_type in ['standard', 'extended']:
                cmd = acl_template.acl_get_config

                t = jinja2.Template(cmd)
                config = t.render(acl_type=acl_type,
                                  address_type=address_type,
                                  acl_name=acl_name)
                config = ' '.join(config.split())

                rpc_response = self._callback(config, handler='get')

                parent = None
                for elem in rpc_response.iter():

                    if elem.text == acl_name:
                        ret = {'type': acl_type,
                               'protocol': address_type,
                               'seq_ids': None}
                        if get_seqs:
                            self._get_seq_ids(parent, ret)

                        return ret
                    parent = elem

        raise ValueError('Failed to identify acl_type. '
                         'Check if the ACL {} exists'.format(acl_name))
