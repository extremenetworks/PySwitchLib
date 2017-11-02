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

import re
from pyswitch.raw.nos.base.acl import Acl as NosBaseAcl


class Acl(NosBaseAcl):
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

    def add_mac_acl_rule(self, **kwargs):
        """
        Add ACL rule to an existing L2 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (array): List of ACL sequence rules.
            seq_id (int): Sequence number of the rule.
            action (str): Action to apply on the traffic (deny/permit/hard-drop).
            source (str): Source filter, can be 'any' or 'host', or the actual MAC address.
            srchost (str): Source MAC in HHHH.HHHH.HHHH format.
            src_mac_addr_mask (str): Mask for the source MAC address.
            dst (str): Destination filter, can be 'any' or 'host', or the actual MAC address.
            dsthost (str): Destination MAC in HHHH.HHHH.HHHH format.
            dst_mac_addr_mask (str): Mask for the destination MAC address.
            vlan_tag_format (str): VLAN tag fromat, (untagged/single-tagged/double-tagged).
            vlan (str): VLAN IDs (Vlan, OuterVlan, InnerVlan) - 'any' or 1-4096, Mask 0xHHH.
            ethertype (str): EtherType, can be 'arp', 'fcoe', 'ipv4' or 1536-65535.
            arp_guard (str): Enables arp-guard for the rule.
            pcp (str): PCP values (pcp,pcp-force) between 0 and 7.
            drop_precedence_force (str): Drop_precedence value of the packet to filter.
            count (str): Enables the packet count.
            log (str): Enables the logging.
            mirror (str): Enables mirror for the rule.
            copy_sflow (str): Enables copy-sflow for the rule.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
                                             address_type='mac')
            True
            >>>     print dev.acl.add_mac_acl_rule(acl_name='Acl_1', seq_id=20,
                                                   action='permit', source='host',
                                                   srchost='2222.2222.2222')
            True
        """
        acl_name = kwargs.pop('acl_name', '')
        acl_rules = kwargs.pop('acl_rules', [])
        callback = kwargs.pop('callback', self._callback)
        seqs_list = []
        seq_id_next = 10
        seq_id_fetched = False

        acl = self.get_acl_type(acl_name)
        address_type = acl['protocol']
        acl_type = acl['type']
        self.logger.info('Successfully identified the acl_type as (%s:%s)',
                         acl['protocol'], acl_type)
        if acl_type == 'standard':
            seq_variables = self.seq_variables_mac_std
        elif acl_type == 'extended':
            seq_variables = self.seq_variables_mac_ext

        if address_type is not 'mac':
            raise ValueError('ACL %s is not compatible for adding L2 acl rule', acl_name)

        if 'source' in kwargs and kwargs['source'] is not None:
            acl_rules.append(kwargs)
        for rule in acl_rules:
            seq_id = rule.pop('seq_id', None)
            action = rule.pop('action', 'deny')
            source = rule.pop('source', 'any')
            srchost = rule.pop('srchost', None)
            src_mac_addr_mask = rule.pop('src_mac_addr_mask', None)
            dst = rule.pop('dst', 'any')
            dsthost = rule.pop('dsthost', None)
            dst_mac_addr_mask = rule.pop('dst_mac_addr_mask', None)
            vlan_tag_format = rule.pop('vlan_tag_format', None)
            vlan = rule.pop('vlan', None)
            ethertype = rule.pop('ethertype', None)
            arp_guard = rule.pop('arp_guard', False)
            pcp = rule.pop('pcp', None)
            drop_precedence_force = rule.pop('drop_precedence_force', None)
            count = rule.pop('count', False)
            log = rule.pop('log', False)
            mirror = rule.pop('mirror', False)
            copy_sflow = rule.pop('copy_sflow', False)

            # Check is the user input for ACL rule is correct
            if acl_type == 'extended' and not any([dst, dsthost, dst_mac_addr_mask]):
                raise ValueError('Destination required in extended access list')
            elif acl_type == 'standard' and any([dsthost, dst_mac_addr_mask]):
                raise ValueError('Destination cannot be given for standard access list')
            any([action, count, log, mirror])   # to keep lint happy.

            # Creating sequence dict for ACL rules
            try:
                seq_dict = {key: None for key in seq_variables}
            except:
                raise ValueError('Cannot get seq_variables')

            seq_dict['user_seq_id'] = seq_id
            if seq_id is None:
                if not seq_id_fetched:
                    seq_id = self.get_seq_id(acl_name, acl_type, address_type)
                    seq_id_fetched = True
                if seq_id is None or seq_id < seq_id_next:
                    seq_id = seq_id_next
            if seq_id >= seq_id_next:
                seq_id_next = (seq_id + 10) // 10 * 10
            self.logger.info('seq_id for the rule is %s', seq_id)

            valid_src = self.__validate_mac_address(source, srchost, src_mac_addr_mask, key='src')
            if not valid_src:
                raise ValueError("Invalid source parameters")

            valid_dst = self.__validate_mac_address(dst, dsthost, dst_mac_addr_mask, key='dst')
            if not valid_dst:
                raise ValueError("Invalid dst parameters")

            if ethertype and ethertype not in ["arp", "fcoe", "ipv4"]:
                try:
                    ethertype_id = (int(ethertype))
                except ValueError as verr:
                    raise ValueError("The ethertype value %s is invalid, could not convert to"
                                     " integer due to %s" % (ethertype, verr.message))
                if ethertype_id < 1536 or ethertype_id > 65535:
                    raise ValueError("The ethertype value %s is invalid, "
                                     "valid value is 1536-65535" % ethertype)
            seq_dict['vlan'] = seq_dict['vlan-id-mask'] = None
            seq_dict['outer-vlan'] = seq_dict['outer-vlan-id-mask'] = None
            seq_dict['inner-vlan'] = seq_dict['inner-vlan-id-mask'] = None
            seq_dict['pcp'] = seq_dict['pcp-force'] = None
            for variable in seq_dict:
                try:
                    seq_dict[variable] = eval(variable)
                except:
                    pass
            if vlan is not None and (' ' in vlan or ',' in vlan):
                vlan_vals = re.split(' |,', vlan)
                vlan_vals = map(lambda x: x.strip(",. \n-"), vlan_vals)
                if vlan_tag_format == 'double-tagged':
                    seq_dict['vlan'] = None
                    seq_dict['outer-vlan'] = vlan_vals[0]
                    seq_dict['outer-vlan-id-mask'] = \
                        vlan_vals[1] if '0x' in vlan_vals[1].lower() else None
                    seq_dict['inner-vlan'] = \
                        vlan_vals[2] if len(vlan_vals) > 2 and \
                        '0x' in vlan_vals[1].lower() else vlan_vals[1]
                    if len(vlan_vals) > 2:
                        seq_dict['inner-vlan-id-mask'] = \
                            vlan_vals[3] if len(vlan_vals) > 3 else vlan_vals[2]
                    if seq_dict['inner-vlan'] == seq_dict['inner-vlan-id-mask']:
                        seq_dict['inner-vlan-id-mask'] = None
                else:
                    seq_dict['vlan'] = vlan_vals[0]
                    seq_dict['vlan-id-mask'] = vlan_vals[1]

            if pcp is not None and (' ' in pcp or ',' in pcp):
                pcp_vals = re.split(' |,', pcp)
                seq_dict['pcp'] = pcp_vals[0].strip()
                seq_dict['pcp-force'] = pcp_vals[1].strip()
            seq_dict['vlan-tag-format'] = vlan_tag_format
            seq_dict['arp-guard'] = arp_guard
            seq_dict['drop-precedence-force'] = drop_precedence_force
            seq_dict['copy-sflow'] = copy_sflow
            if seq_dict['vlan'] is not None and \
                not re.match("^(any)|(([1-9][0-9]{0,2})|([1-3][0-9]{3})|" +
                             "(40[0-8][0-9])|(409[0-4]))$", seq_dict['vlan']):
                    raise ValueError("Invalid \'vlan\' value,"
                                     " any or 1-4096 only supported")
            if seq_dict['vlan-id-mask'] is not None and \
               not re.match("^0x([0-9a-fA-F]{3})$", seq_dict['vlan-id-mask']):
                    raise ValueError("Invalid \'vlan-id-mask\' value,"
                                     " 0xHHH (3 digit hex value) only supported")
            if seq_dict['outer-vlan'] is not None and \
                not re.match("^(any)|(([1-9][0-9]{0,2})|([1-3][0-9]{3})|"
                             "(40[0-8][0-9])|(409[0-4]))$", seq_dict['outer-vlan']):
                    raise ValueError("Invalid \'outer-vlan\' value,"
                                     " any or 1-4096 only supported")
            if seq_dict['outer-vlan-id-mask'] is not None and \
               not re.match("^0x([0-9a-fA-F]{3})$", seq_dict['outer-vlan-id-mask']):
                    raise ValueError("Invalid \'outer-vlan-id-mask\' value,"
                                     " 0xHHH (3 digit hex value) only supported")
            if seq_dict['inner-vlan'] is not None and \
                not re.match("^(any)|(([1-9][0-9]{0,2})|([1-3][0-9]{3})|"
                             "(40[0-8][0-9])|(409[0-4]))$", seq_dict['inner-vlan']):
                    raise ValueError("Invalid \'inner-vlan\' value,"
                                     " any or 1-4096 only supported")
            if seq_dict['inner-vlan-id-mask'] is not None and \
               not re.match("^0x([0-9a-fA-F]{3})$", seq_dict['inner-vlan-id-mask']):
                    raise ValueError("Invalid \'inner-vlan-id-mask\' value,"
                                     " 0xHHH (3 digit hex value) only supported")
            if seq_dict['pcp'] is not None and not re.match("^[0-7]$", seq_dict['pcp']):
                    raise ValueError("Invalid \'pcp\' value, 0-7 only supported")
            if seq_dict['pcp-force'] is not None and \
               not re.match("^[0-7]$", seq_dict['pcp-force']):
                    raise ValueError("Invalid \'pcp-force\' value, 0-7 only supported")
            if seq_dict['drop-precedence-force'] is not None and \
               not re.match("^[0-2]$", seq_dict['drop-precedence-force']):
                    raise ValueError("Invalid \'drop-precedence-force\' value,"
                                     " 0-2 only supported")
            seqs_list.append(seq_dict)

        result = {}
        for seq_dict in seqs_list:
            self.logger.info('Adding rule on ACL %s at seq_id %s', acl_name,
                             str(seq_dict['seq_id']))
            config = self.__generate_acl_rule_xml(address_type, acl_type, acl_name, [seq_dict])
            try:
                callback(config)
                self.logger.info('Successfully added rule on ACL %s', acl_name)
                result['Seq-%s' % str(seq_dict['seq_id'])] = True
            except Exception as e:
                if 'Access-list entry already exists' in str(e) and \
                        seq_dict['user_seq_id'] is None:
                    self.logger.warning(str(e).split('%Error: ')[1])
                    result['Seq-%s' % str(seq_dict['seq_id'])] = None
                else:
                    raise
        return result

    def add_ip_acl_rule(self, **kwargs):
        """
        Add ACL rule to an existing ACL.
        Args:
            acl_name (str): Name of the access list.
            address_type (str): ACL address type, ip or ipv6.
            acl_rules (array): List of ACL sequence rules.
            seq_id (int): Sequence number of the rule.
            action (str): Action to apply on the traffic (deny/permit/hard-drop).
            protocol_type (str): Type of IP packets to be filtered (<0-255>, tcp, udp, icmp or ip).
            source (str): Source filter, can be 'any' or 'host', or the actual MAC address.
            destination (str): Destination filter, can be 'any' or 'host', or the actual MAC.
            dscp (str): DSCP and DSCP-Force values of the packet to filter.
            drop_precedence_force (str): Drop_precedence value of the packet to filter.
            urg (str): Enables urg for the rule.
            ack (str): Enables ack for the rule.
            push (str):Enables push for the rule.
            fin (str): Enables fin for the rule.
            rst (str): Enables rst for the rule.
            sync (str): Enables sync for the rule.
            vlan_id (str): VLAN ID for the rule.
            count (str): Enables the packet count.
            log (str): Enables the logging.
            mirror (str): Enables mirror for the rule.
            copy_sflow (str): Enables copy-sflow for the rule.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
                                             address_type='ip')
            True
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10,
                                                  action='permit',
                                                  source='host 192.168.0.3')
            True
        """
        acl_name = kwargs.pop('acl_name', '')
        address_type = kwargs.pop('address_type', '')
        acl_rules = kwargs.pop('acl_rules', [])
        callback = kwargs.pop('callback', self._callback)
        seqs_list = []
        seq_id_next = 10
        seq_id_fetched = False

        acl = self.get_acl_type(acl_name)
        acl_type = acl['type']
        self.logger.info('Successfully identified the acl_type as (%s:%s)',
                         acl['protocol'], acl_type)
        if acl_type == 'standard':
            seq_variables = self.seq_variables_ip_std
        elif acl_type == 'extended':
            seq_variables = self.seq_variables_ip_ext

        if address_type is 'ip' and acl['protocol'] is not 'ip':
            raise ValueError('ACL %s is not compatible for adding IPV4 acl rule', acl_name)
        elif address_type is 'ipv6' and acl['protocol'] is not 'ipv6':
            raise ValueError('ACL %s is not compatible for adding IPV6 acl rule', acl_name)
        elif acl['protocol'] is 'mac':
            raise ValueError('Use L3 ACLs with this action')

        if 'source' in kwargs and kwargs['source'] is not None:
            acl_rules.append(kwargs)
        for rule in acl_rules:
            seq_id = rule.pop('seq_id', None)
            action = rule.pop('action', 'permit')
            protocol_type = rule.pop('protocol_type', None)
            source = rule.pop('source', 'any')
            destination = rule.pop('destination', None)
            dscp = rule.pop('dscp', None)
            drop_precedence_force = rule.pop('drop_precedence_force', None)
            urg = rule.pop('urg', False)
            ack = rule.pop('ack', False)
            push = rule.pop('push', False)
            fin = rule.pop('fin', False)
            rst = rule.pop('rst', False)
            sync = rule.pop('sync', False)
            vlan = rule.pop('vlan_id', None)
            count = rule.pop('count', False)
            log = rule.pop('log', False)
            mirror = rule.pop('mirror', False)
            copy_sflow = rule.pop('copy_sflow', False)

            # Check is the user input for ACL rule is correct
            if acl_type == 'extended' and destination is None:
                raise ValueError('Destination required in extended access list')
            elif acl_type == 'extended' and protocol_type is None:
                raise ValueError('protocol_type is required for extended access list')
            elif acl_type == 'standard' and destination:
                raise ValueError('Destination cannot be given for standard access list')
            elif acl_type == 'standard' and protocol_type:
                raise ValueError('protocol_type cannot be given for standard access list')
            elif acl_type == 'standard' and vlan:
                raise ValueError('vlan_id cannot be given for standard access list')
            elif acl_type == 'standard' and dscp:
                raise ValueError('dscp cannot be given for standard access list')
            elif acl_type == 'standard' and drop_precedence_force:
                raise ValueError('drop_precedence_force cannot be given for standard access list')
            elif acl_type == 'standard' and any([urg, ack, push, fin, rst, sync, mirror]):
                raise ValueError('Any of (urg, ack, push, fin, rst, sync, mirror) '
                                 'cannot be given for standard access list')
            any([action, count, log])   # to keep lint happy.

            # Creating sequence dict for ACL rules
            try:
                seq_dict = {key: None for key in seq_variables}
            except:
                raise ValueError('Cannot get seq_variables')
            seq_dict['user_seq_id'] = seq_id
            if seq_id is None:
                if not seq_id_fetched:
                    seq_id = self.get_seq_id(acl_name, acl_type, address_type)
                    seq_id_fetched = True
                if seq_id is None or seq_id < seq_id_next:
                    seq_id = seq_id_next
            if seq_id >= seq_id_next:
                seq_id_next = (seq_id + 10) // 10 * 10
            self.logger.info('seq_id for the rule is %s', seq_id)
            src_dict = self.__parse_ip_address(address_type, protocol_type, source, 'src')
            if acl_type == 'extended':
                dst_dict = self.__parse_ip_address(address_type, protocol_type, destination, 'dst')
            for variable in seq_dict:
                if 'src' in variable or 'sport' in variable:
                    try:
                        seq_dict[variable] = src_dict[variable]
                    except:
                        pass
                elif 'dst' in variable or 'dport' in variable:
                    try:
                        seq_dict[variable] = dst_dict[variable]
                    except:
                        pass
                else:
                    try:
                        seq_dict[variable] = eval(variable)
                    except:
                        pass
            if dscp is not None and (' ' in dscp or ',' in dscp):
                dscp_vals = re.split(' |,', dscp)
                seq_dict['dscp'] = dscp_vals[0].strip()
                seq_dict['dscp-force'] = dscp_vals[1].strip()
            seq_dict['drop-precedence-force'] = drop_precedence_force
            seq_dict['copy-sflow'] = copy_sflow
            if seq_dict['drop-precedence-force'] is not None and \
               not re.match("^[0-2]$", seq_dict['drop-precedence-force']):
                        raise ValueError("Invalid \'drop-precedence-force\' value,"
                                         " 0-2 only supported")
            seqs_list.append(seq_dict)

        result = {}
        for seq_dict in seqs_list:
            self.logger.info('Adding rule on ACL %s at seq_id %s', acl_name,
                             str(seq_dict['seq_id']))
            config = self.__generate_acl_rule_xml(address_type, acl_type, acl_name, [seq_dict])
            try:
                callback(config)
                self.logger.info('Successfully added rule on ACL %s', acl_name)
                result['Seq-%s' % str(seq_dict['seq_id'])] = True
            except Exception as e:
                if 'Access-list entry already exists' in str(e) and \
                        seq_dict['user_seq_id'] is None:
                    self.logger.warning(str(e).split('%Error: ')[1])
                    result['Seq-%s' % str(seq_dict['seq_id'])] = None
                else:
                    raise
        return result
