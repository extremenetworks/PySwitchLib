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


# import xml.etree.ElementTree
import jinja2
import pyswitch.raw.slx_nos.acl.params_validator as params_validator
from pyswitch.raw.slxos.ver_17s import acl_template
from pyswitch.raw.nos.base.acl.acl import Acl as NosBaseAcl


class Acl(NosBaseAcl):
    """
    The Acl class holds all the actions assocaiated with the Access Control
    list of a SLX device.

    Attributes:
        None
    """

    os_type = "slxos"

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
        user_data['pcp'] = self.mac.parse_pcp(**kwargs)
        bool_params = ['log', 'count']
        self.mac.parse_boolean_params(user_data, bool_params, **kwargs)

        return user_data

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
        params_validator.validate_params_slxos_17s_add_or_remove_l2_acl_rule(
            **kwargs)

        # Parse params
        acl_name = self.ip.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)
        acl = self._get_acl_info(acl_name, get_seqs=True)

        acl_type = acl['type']
        address_type = acl['protocol']

        if address_type != 'mac':
            raise ValueError('Rule can not be configured as {} type is {}'
                             .format(acl_name, address_type))

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

        self.logger.debug(config)

        callback(config)

        self.logger.info('Successfully added rule ACL {}'.format(acl_name))
        return True
