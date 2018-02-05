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
from pyswitch.raw.slxos.ver_17s import aclparam_parser as app
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
        self._app = app.AclParamParser()

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

        if acl_type == 'standard':
            params_validator.validate_params_slx_std_add_or_remove_l2_acl_rule(
                **kwargs)

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

        callback(config)

        return True

    def validate_interfaces(self, callback, user_data):

        for intf in user_data['interface_list']:
            invalid_intf = True

            user_data['intf'] = intf
            cmd = acl_template.get_interface_by_name
            t = jinja2.Template(cmd)
            config = t.render(**user_data)
            config = ' '.join(config.split())
            rpc_response = callback(config, handler='get')
            # xml.etree.ElementTree.dump(rpc_response)
            for elem in rpc_response.iter():
                if elem.text == str(intf):
                    invalid_intf = False
                    break
            if invalid_intf:
                raise ValueError("{} interface {} does not exist."
                                 .format(user_data['intf_type'], intf))

    def apply_acl(self, **kwargs):
        """
        Apply an ACL to a physical port, port channel, VE or mgmt interface.
        Args:
            rbridge_id (str): RBridge ID of the VDX switch under which VE
                will be configured
            intf_type (str): Interface type, (physical, port channel, VE
                or management interface).
            intf_names (str[]): Array of the Interface Names.
            acl_name (str): Name of the access list.
            acl_direction (str): Direction of ACL binding on the specified
                interface [in/out].
            traffic_type (str): Traffic type for the ACL being applied
                [switched/routed].
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be
                the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each interfaces.
        Raises:
            Exception, ValueError for invalid seq_id.
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

        # Validate required and accepted parameters
        params_validator.validate_params_slx_ver17s_apply_acl(**kwargs)

        # Parse params
        acl_name = self.ip.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)
        acl = self._get_acl_info(acl_name, get_seqs=False)
        address_type = acl['protocol']

        kwargs['address_type'] = address_type
        # Parse params
        user_data = self._parse_params_for_apply_or_remove_acl(**kwargs)

        self.validate_interfaces(callback, user_data)

        result = {}
        for intf in user_data['interface_list']:
            user_data['intf'] = intf
            t = jinja2.Template(acl_template.acl_apply)
            config = t.render(**user_data)
            config = ' '.join(config.split())
            callback(config)

            result[intf] = True
        return result

    def remove_acl(self, **kwargs):
        """
        Remove ACL from a physical port, port channel, VE or mgmt interface.
        Args:
            rbridge_id (str): RBridge ID of the VDX switch under which VE
                will be configured
            intf_type (str): Interface type, (physical, port channel, VE or
                management interface).
            intf_name (str[]): Array of the Interface Names.
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
        Raises:
            Exception, ValueError for invalid seq_id.
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
            >>>     print dev.acl.remove_acl(intf_type='ethernet',
                                            intf_name='0/1,0/2',
                                            acl_name='Acl_1',
                                            acl_direction='in',
                                            traffic_type='switched')
        """
        # Validate required and accepted parameters
        params_validator.validate_params_slx_ver17s_apply_acl(**kwargs)

        # Parse params
        acl_name = self.ip.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)
        acl = self._get_acl_info(acl_name, get_seqs=False)
        address_type = acl['protocol']

        kwargs['address_type'] = address_type
        # Parse params
        user_data = self._parse_params_for_apply_or_remove_acl(**kwargs)

        self.validate_interfaces(callback, user_data)

        result = {}
        for intf in user_data['interface_list']:
            user_data['intf'] = intf
            t = jinja2.Template(acl_template.acl_remove)
            config = t.render(**user_data)
            config = ' '.join(config.split())
            try:
                callback(config)
                result[intf] = True
            except Exception as e:
                if '<bad-element>access-group</bad-element>' in str(e):
                    result[intf] = None
                else:
                    raise
        return result

    def _parse_params_for_apply_or_remove_acl(self, **kwargs):
        """
        Parses params for Apply or Remove ACL on Interfaces.
        Args:
            Parse below params if contained in kwargs.

                rbridge_id: (string) rbridge_id of the interface,
                    Valid range is 1 to 239
                intf_type: (string) Allowed intf_type are,
                          - gigabitethernet
                          - tengigabitethernet
                          - fortygigabitethernet
                          - hundredgigabitethernet
                          - port_channel
                          - ve
                          - loopback
                          - ethernet
                intf_name: (string array) Array of interface names
                acl_name: (string) Name of the access list
                acl_direction: (string) Action performed by ACL rule
                    - in
                    - out
                traffic_type: (string) Action performed by ACL rule
                    - switched
                    - routed
        Returns:
            Return a dict cotaining the kwargs in string format
            key name will be key name in the parameter followed by _str.
        Raise:
            Raises ValueError, Exception
        Examples:
        """
        user_data = {}

        user_data['address_type'] = kwargs['address_type']
        user_data['acl_name'] = self.ap.parse_acl_name(**kwargs)
        user_data['interface_list'] = self.ap.parse_intf_names(**kwargs)
        user_data['intf_type'] = self._app.parse_intf_type(**kwargs)
        user_data['acl_direction'] = self._app.parse_acl_direction(**kwargs)
        user_data['traffic_type'] = self._app.parse_traffic_type(**kwargs)

        return user_data

    def validate_mac_std_rules(self, acl_name, acl_rules):
        user_data_list = []
        for rule in acl_rules:
            rule['acl_name'] = acl_name
            params_validator.validate_params_slx_std_add_or_remove_l2_acl_rule(
                **rule)
            rule['address_type'] = 'mac'
            user_data = self._parse_params_for_add_mac_standard(**rule)
            user_data_list.append(user_data)
        return user_data_list

    def validate_mac_ext_rules(self, acl_name, acl_rules):
        user_data_list = []
        for rule in acl_rules:
            rule['acl_name'] = acl_name
            params_validator. \
                validate_params_slxos_17s_add_or_remove_l2_acl_rule(**rule)
            rule['address_type'] = 'mac'
            user_data = self._parse_params_for_add_mac_extended(**rule)
            user_data_list.append(user_data)
        return user_data_list

    def process_response_mac_rule_bulk_req(self, rpc_err, acl_rules,
                                           failed_seq_id):
        rpc_err = str(rpc_err)
        if "Error: Access-list entry already exists" in rpc_err:

            configured_count = 0
            unconfigured_count = 0

            for rule in acl_rules:
                if rule['seq_id'] < int(failed_seq_id):
                    configured_count = configured_count + 1
                else:
                    unconfigured_count = unconfigured_count + 1
        raise ValueError(rpc_err)

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

        # Parse params
        acl_name = self.mac.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)
        acl = self._get_acl_info(acl_name, get_seqs=True)
        acl_type = acl['type']
        address_type = acl['protocol']

        if address_type != 'mac':
            raise ValueError("mac Rule can not be added to non-mac ACL."
                             "ACL {} is of type {}"
                             .format(acl_name, address_type))

        # if there are already configured rules. Make sure that they are
        # not overlapping with new rules to be configured
        self.set_seq_id_for_bulk_rules(acl['seq_ids'], acl_rules)

        # Parse parameters
        if acl_type == 'standard':
            user_data_list = self.validate_mac_std_rules(acl_name, acl_rules)
        elif acl_type == 'extended':
            user_data_list = self.validate_mac_ext_rules(acl_name, acl_rules)
        else:
            raise ValueError('{} not supported'.format(acl_type))

        # send the rules in a chunk of Acl.MAC_RULE_CHUNK_SIZE
        chunks = [user_data_list[i:i + Acl.MAC_RULE_CHUNK_SIZE]
                  for i in
                  xrange(0, len(user_data_list), Acl.MAC_RULE_CHUNK_SIZE)]

        for chunk in chunks:
            t = jinja2.Template(acl_template.acl_rule_mac_bulk)
            config = t.render(address_type=address_type,
                              acl_type=acl_type,
                              acl_name=acl_name,
                              user_data_list=chunk)

            config = ' '.join(config.split())
            try:
                callback(config)
            except Exception as err:
                self.process_response_mac_rule_bulk_req(err, acl_rules,
                                                        chunk[0]['seq_id'])

        return True
