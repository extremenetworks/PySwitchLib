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
import template
import pyswitch.NetConfDevice
import pyswitch.utilities as utilities
from pyswitch.raw.base.acl import Acl as BaseAcl


class Acl(BaseAcl):
    """
    The Acl class holds all the functions assocaiated with the Access Control list
    of a NOS device.

    Attributes:
        None
    """

    os_type = "nos"

    __seq_variables_ip_std = ('seq_id', 'action', 'src_host_any_sip', 'src_host_ip',
                              'src_mask', 'count', 'log')

    __seq_variables_ip_ext = ('seq_id', 'action', 'protocol_type', 'src_host_any_sip',
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
                              'dport_number_range_higher_udp', 'dscp', 'urg', 'ack', 'push',
                              'fin', 'rst', 'sync', 'vlan', 'count', 'log')

    __seq_variables_mac_std = ('seq_id', 'action', 'source', 'srchost',
                               'src_mac_addr_mask', 'count', 'log')

    __seq_variables_mac_ext = ('seq_id', 'action', 'source', 'srchost',
                               'src_mac_addr_mask', 'dst', 'dsthost',
                               'dst_mac_addr_mask', 'ethertype', 'count', 'log')

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

    def get_acl_type(self, acl_name):
        """
        Return acl-type as dict {'type':'standard'/'ectended;, 'protocol':'mac'/'ip'/'ipv6'}.
        """

        try:
            # Check 'acl_name' in the 'mac' 'standard' ACLs
            fltr = template.mac_fltr.format(acl_type='standard', acl_name=acl_name)
            config = template.acl_get_config.format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0].text == acl_name:
                return {'type': 'standard', 'protocol': 'mac'}
        except IndexError:
            pass        # acl_name not present in mac standard ACLs, pass for next checks.

        try:
            # Check 'acl_name' in the 'mac' 'extended' ACLs
            fltr = template.mac_fltr.format(acl_type='extended', acl_name=acl_name)
            config = template.acl_get_config.format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0].text == acl_name:
                return {'type': 'extended', 'protocol': 'mac'}
        except IndexError:
            pass        # acl_name not present in mac extended ACLs, pass for next checks.

        try:
            # Check 'acl_name' in the 'ip' 'standard' ACLs
            fltr = template.ipv4_fltr.format(acl_type='standard', acl_name=acl_name)
            config = template.acl_get_config.format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0][0].text == acl_name:
                return {'type': 'standard', 'protocol': 'ip'}
        except IndexError:
            pass        # acl_name not present in ip standard ACLs, pass for next checks.

        try:
            # Check 'acl_name' in the 'ip' 'extended' ACLs
            fltr = template.ipv4_fltr.format(acl_type='extended', acl_name=acl_name)
            config = template.acl_get_config.format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0][0].text == acl_name:
                return {'type': 'extended', 'protocol': 'ip'}
        except IndexError:
            pass        # acl_name not present in ip extended ACLs, pass for next checks.

        try:
            # Check 'acl_name' in the 'ipv6' 'standard' ACLs
            fltr = template.ipv6_fltr.format(acl_type='standard', acl_name=acl_name)
            config = template.acl_get_config.format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0][0].text == acl_name:
                return {'type': 'standard', 'protocol': 'ipv6'}
        except IndexError:
            pass        # acl_name not present in ipv6 standard ACLs, pass for next checks.

        try:
            # Check 'acl_name' in the 'ipv6' 'extended' ACLs
            fltr = template.ipv6_fltr.format(acl_type='extended', acl_name=acl_name)
            config = template.acl_get_config.format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0][0].text == acl_name:
                return {'type': 'extended', 'protocol': 'ipv6'}
        except IndexError:
            pass        # acl_name not present in ipv6 extended ACLs also.

        raise ValueError('Failed to identify acl_type. Check if the ACL %s exists' % acl_name)

    def get_seq(self, acl_name, seq_id, acl_type, address_type):
        """
        Return ACL rule sequence as dict() with given 'seq_id'
        or last sequence if 'seq_id' not given.
        """
        fltr = ""
        seqIdx = ""

        if address_type == 'mac':
            fltr = template.mac_fltr.format(acl_type=acl_type, acl_name=acl_name)
            seqIdx = "res[0][0][0][0][1]"
        elif address_type == 'ip':
            fltr = template.ipv4_fltr.format(acl_type=acl_type, acl_name=acl_name)
            seqIdx = "res[0][0][0][0][0][1]"
        elif address_type == 'ipv6':
            fltr = template.ipv6_fltr.format(acl_type=acl_type, acl_name=acl_name)
            seqIdx = "res[0][0][0][0][0]"

        config = template.acl_get_config.format(filter=fltr)
        try:
            res = self._callback(config, handler='get')
        except pyswitch.NetConfDevice.DeviceCommError:
            raise
        except:
            raise ValueError('Failed to get sequence details')
        seqElements = []
        try:
            res[0][0][0][0][0]      # to keep lint happy.
            seqElements = list(eval(seqIdx))
        except:
            return None             # No sequences found
        seqElem = seqElements[-1] if not seq_id and len(seqElements) > 0 else None
        if seqElem is None:
            for elem in seqElements:
                if 'seq' in elem.tag:
                    for tag in elem:
                        if 'seq-id' in tag.tag:
                            if tag.text == str(seq_id):
                                seqElem = elem
                            break
                    if seqElem is not None:
                        break
        if seqElem is not None and 'seq' in seqElem.tag:
            seq_dict = dict()
            for tag in seqElem:
                key = tag.tag.split('}')[1]
                seq_dict[key.replace('-', '_')] = 'True' if not tag.text else tag.text
            return seq_dict
        else:
            return None

    def get_seq_id(self, acl_name, acl_type, address_type=None):
        """
        Return new sequence id for the given ACL.
        """
        try:
            last_id = 0
            seq_itm = self.get_seq(acl_name, None, acl_type, address_type)
            if seq_itm is not None:
                last_id = int(seq_itm['seq_id'])
            return (last_id + 10) // 10 * 10
        except:
            raise

    def __validate_mac_address(self, src_dst, src_dst_host, mac_addr_mask, key):
        """
        Validates source and destination address related parameters for L2 ACL rules.
        """
        if src_dst != "any" and src_dst != "host":
            self.logger.debug("%s is a MAC address", key)
            if not utilities.is_valid_mac_address(src_dst):
                self.logger.error("The format of %s MAC address %s is invalid. "
                                  "Valid format is HHHH.HHHH.HHHH", key, src_dst)
                return False

            if mac_addr_mask is None:
                self.logger.error("The %s_mac_addr_mask is required when %s "
                                  "is a MAC address value", key, key)
                return False
            elif src_dst_host:
                self.logger.error("The %shost can't be entered when %s "
                                  "is a MAC address value", key, key)
                return False
            elif not utilities.is_valid_mac_address(mac_addr_mask):
                self.logger.error("The format of %s_mac_addr_mask %s is invalid. "
                                  "Valid format is HHHH.HHHH.HHHH", key, mac_addr_mask)
                return False
        elif src_dst == "host":
            if mac_addr_mask:
                self.logger.error("Can't enter %s_mac_addr_mask when %s is host",
                                  key, key)
                return False
            elif not src_dst_host:
                self.logger.error("Need a valid mac address in %shost when %s is host",
                                  key, key)
                return False
        return True

    def __parse_ip_address(self, address_type, protocol_type, statement, key):
        """
        Parses source and destination address and related parameters for IPv4 and IPv6 ACL rules.
        """
        output = {}
        msg = None
        statement_list = statement.split(' ') if address_type == 'ipv6' else \
            re.split(' |,|/', statement)
        map(lambda x: x.strip(",. \n-"), statement_list)
        if statement_list[0] == 'any':
            output[key + '_host_any_' + key[:1] + 'ip'] = statement_list.pop(0)
        elif 'host' in statement_list[0]:
            try:
                output[key + '_host_any_' + key[:1] + 'ip'] = statement_list.pop(0)
                host_ip = statement_list.pop(0)
                if utilities.is_valid_ip_address(host_ip, address_type):
                    output[key + '_host_ip'] = host_ip
                else:
                    msg = 'host ip in {} statement is invalid'.format(key)
            except:
                msg = 'host ip missing in {} statement'.format(key)
        elif utilities.is_valid_ip_address(statement_list[0], address_type):
            output[key + '_host_any_' + key[:1] + 'ip'] = statement_list.pop(0)
            try:
                output[key + '_mask'] = statement_list.pop(0)
            except:
                msg = 'IP address mask missing in {} statement'.format(key)
        elif address_type == 'ipv6' and utilities.is_valid_ip_network(statement_list[0]):
            output[key + '_host_any_' + key[:1] + 'ip'] = statement_list.pop(0)
        else:
            msg = 'Incorrect {} statement'.format(key)
        if msg is not None:
            self.logger.error(msg)
            raise ValueError(msg)
        try:
            port = statement_list[0]
        except:
            return output
        if statement_list[0] in ['lt', 'gt', 'eq', 'range', 'neq']:
            output[key[:1] + 'port'] = port
            statement_list.pop(0)
            if port in ['eq', 'neq']:
                port = 'eq_neq'
            if port != 'range':
                try:
                    output[key[:1] + 'port_number_' + port +
                           '_' + protocol_type] = statement_list.pop(0)
                except:
                    msg = '{} port number {} missing'.format(key, port)
            else:
                try:
                    output[key[:1] + 'port_number_' + port + '_lower_' +
                           protocol_type] = statement_list.pop(0)
                    output[key[:1] + 'port_number_' + port + '_higher_' +
                           protocol_type] = statement_list.pop(0)
                except:
                    msg = '{} port numbers range missing'.format(key)
        else:
            msg = 'Incorrect {} statement'.format(key)

        if msg is not None:
            self.logger.error(msg)
            raise ValueError(msg)
        return output

    def __generate_acl_rule_xml(self, address_type, acl_type, acl_name, seqs_list, delete=False):
        """
        Generate XML payload for ACL rules configuration.
        """
        sequences = ''
        if address_type == 'mac':
            if acl_type == 'standard':
                seq_vars = self.__seq_variables_mac_std
            else:
                seq_vars = self.__seq_variables_mac_ext
        else:
            if acl_type == 'standard':
                seq_vars = self.__seq_variables_ip_std
            else:
                seq_vars = self.__seq_variables_ip_ext
        for seq in seqs_list:
            if delete:
                if 'seq_id' in seq and seq['seq_id'] is not None:
                    seqxml = '<seq-id>%s</seq-id>' % str(seq['seq_id'])
                sequences += "<seq operation=\'delete\'>\n{}</seq>\n".format(seqxml)
            else:
                seqxml = ''
                for key in seq_vars:
                    if seq[key]:
                        if str(seq[key]).lower() == 'true':
                            seqxml += "<{0}></{0}> \n".format(key.replace('_', '-'))
                        elif str(seq[key]).lower() != 'false':
                            seqxml += "<{0}>{1}</{0}> \n".format(key.replace('_', '-'), seq[key])
                sequences += "<seq>\n{}</seq>\n".format(seqxml)

        if sequences and address_type == 'ip':
            if acl_type == 'standard':
                sequences = "<hide-ip-acl-std>\n{}</hide-ip-acl-std>\n".format(sequences)
            else:
                sequences = "<hide-ip-acl-ext>\n{}</hide-ip-acl-ext>\n".format(sequences)
        elif sequences and address_type == 'mac':
            if acl_type == 'standard':
                sequences = "<hide-mac-acl-std>\n{}</hide-mac-acl-std>\n".format(sequences)
            else:
                sequences = "<hide-mac-acl-ext>\n{}</hide-mac-acl-ext>\n".format(sequences)

        if address_type == 'mac':
            config = template.acl_rule_mac
        else:
            config = template.acl_rule_ip

        config = config.format(address_type=address_type,
                               acl_name=acl_name,
                               acl_type=acl_type,
                               sequences=sequences)
        return config

    def create_acl(self, **kwargs):
        """
        Create an Access Control List.
        Args:
            address_type (str): ACL address type, ip or ipv6 or mac.
            acl_type (str): ACL type, extended or standard.
            acl_name (str): Unique name for ACL.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.create_acl(acl_name='Acl_2', acl_type='extended',
                                             address_type='ip')
            >>>     print dev.acl.create_acl(acl_name='Acl_3', acl_type='extended',
                                             address_type='ipv6')
        """

        address_type = kwargs.pop('address_type', '')
        acl_type = kwargs.pop('acl_type', '')
        acl_name = kwargs.pop('acl_name', '')
        callback = kwargs.pop('callback', self._callback)
        self.logger.info('Creating ACL %s (%s:%s)', acl_name, address_type, acl_type)

        if address_type == 'mac':
            config = template.acl_create_mac
        else:
            config = template.acl_create_ip

        config = config.format(address_type=address_type,
                               acl_name=acl_name,
                               acl_type=acl_type,
                               delete='')
        callback(config)
        self.logger.info('Successfully created ACL %s' % acl_name)
        return True

    def delete_acl(self, **kwargs):
        """
        Delete Access Control List.
        Args:
            acl_name (str): Name of the access list.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.delete_acl(acl_name='Acl_2')
            >>>     print dev.acl.delete_acl(acl_name='Acl_1')
        """

        acl_name = kwargs.pop('acl_name', '')
        callback = kwargs.pop('callback', self._callback)
        try:
            acl = self.get_acl_type(acl_name)
            address_type = acl['protocol']
            acl_type = acl['type']
            self.logger.info('Deleting ACL %s (%s:%s)', acl_name, address_type, acl_type)

            if address_type == 'mac':
                config = template.acl_create_mac
            else:
                config = template.acl_create_ip

            config = config.format(address_type=address_type,
                                   acl_name=acl_name,
                                   acl_type=acl_type,
                                   delete='operation=\'delete\'')
            callback(config)
            self.logger.info('Successfully deleted ACL %s' % acl_name)
            return True
        except ValueError as e:
            if 'Failed to identify acl_type' in e.message:
                self.logger.warning("ACL %s does not exist", acl_name)
                return None
            else:
                raise
        return False

    def apply_acl(self, **kwargs):
        """
        Apply an ACL to a physical port, port channel, VE or management interface.
        Args:
            rbridge_id (str): RBridge ID of the VDX switch under which VE will be configured
            intf_type (str): Interface type, (physical, port channel, VE or management interface).
            intf_names (str[]): Array of the Interface Names.
            acl_name (str): Name of the access list.
            acl_direction (str): Direction of ACL binding on the specified interface [in/out].
            traffic_type (str): Traffic type for the ACL being applied [switched/routed].
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each interfaces.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.apply_acl(intf_type='ethernet', intf_name='0/1,0/2',
                                            acl_name='Acl_1', acl_direction='in',
                                            traffic_type='switched')
        """
        rbridge_id = kwargs.pop('rbridge_id', '')
        intf_type = kwargs.pop('intf_type', '').lower()
        intf_name = kwargs.pop('intf_name', '')
        acl_name = kwargs.pop('acl_name', '')
        acl_direction = kwargs.pop('acl_direction', '')
        traffic_type = kwargs.pop('traffic_type', '')
        callback = kwargs.pop('callback', self._callback)
        address_type = self.get_acl_type(acl_name)['protocol']
        interface_list = []
        result = {}

        # Check is the user input for Interface Name is correct
        for intf in intf_name:
            if "-" not in str(intf):
                interface_list.append(intf)
            else:
                ex_intflist = utilities.extend_interface_range(intf_type=intf_type, intf_name=intf,
                                                               logger=self.logger)
                for ex_intf in ex_intflist:
                    interface_list.append(ex_intf)
        for intf in interface_list:
                if not utilities.validate_interface(intf_type, str(intf), rbridge_id=rbridge_id,
                                                    os_type=self.os_type, logger=self.logger):
                    raise ValueError("Input is not a valid Interface")
        for intf in interface_list:
            if address_type == 'mac':
                acl_apply = template.acl_apply_mac
            elif address_type == 'ip':
                acl_apply = template.acl_apply_ipv4
            else:
                acl_apply = template.acl_apply_ipv6

            self.logger.info('Applying ACL %s on interface (%s-%s)', acl_name, intf_type, intf)
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

    def remove_acl(self, **kwargs):
        """
        Remove ACL from a physical port, port channel, VE or management interface.
        Args:
            rbridge_id (str): RBridge ID of the VDX switch under which VE will be configured
            intf_type (str): Interface type, (physical, port channel, VE or management interface).
            intf_name (str[]): Array of the Interface Names.
            acl_name (str): Name of the access list.
            acl_direction (str): Direction of ACL binding on the specified interface [in/out].
            traffic_type (str): Traffic type for the ACL being applied [switched/routed].
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each interfaces.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.apply_acl(intf_type='ethernet', intf_name='0/1,0/2',
                                            acl_name='Acl_1', acl_direction='in',
                                            traffic_type='switched')
            >>>     print dev.acl.remove_acl(intf_type='ethernet', intf_name='0/1,0/2',
                                            acl_name='Acl_1', acl_direction='in',
                                            traffic_type='switched')
        """
        rbridge_id = kwargs.pop('rbridge_id', '')
        intf_type = kwargs.pop('intf_type', '').lower()
        intf_name = kwargs.pop('intf_name', '')
        acl_name = kwargs.pop('acl_name', '')
        acl_direction = kwargs.pop('acl_direction', '')
        traffic_type = kwargs.pop('traffic_type', '')
        callback = kwargs.pop('callback', self._callback)
        address_type = self.get_acl_type(acl_name)['protocol']
        interface_list = []
        result = {}

        # Check is the user input for Interface Name is correct
        for intf in intf_name:
            if "-" not in str(intf):
                interface_list.append(intf)
            else:
                ex_intflist = utilities.extend_interface_range(intf_type=intf_type, intf_name=intf,
                                                               logger=self.logger)
                for ex_intf in ex_intflist:
                    interface_list.append(ex_intf)
        for intf in interface_list:
                if not utilities.validate_interface(intf_type, str(intf), rbridge_id=rbridge_id,
                                                    os_type=self.os_type, logger=self.logger):
                    raise ValueError("Input is not a valid Interface")
        for intf in interface_list:
            if address_type == 'mac':
                acl_apply = template.acl_apply_mac
            elif address_type == 'ip':
                acl_apply = template.acl_apply_ipv4
            else:
                acl_apply = template.acl_apply_ipv6

            self.logger.info('Removing ACL %s from interface (%s-%s)', acl_name, intf_type, intf)
            acl_apply = acl_apply.format(address_type=address_type,
                                         intf_type=intf_type.replace('_', '-'),
                                         intf=intf, acl_name=acl_name,
                                         acl_direction=acl_direction,
                                         traffic_type='' if not traffic_type else
                                         '<traffic-type>' + traffic_type + '</traffic-type>',
                                         delete='operation=\'delete\'')
            if rbridge_id:
                config = template.rbridge_acl_apply
            else:
                config = '<config> {acl_apply} </config>'

            config = config.format(rbridge_id=rbridge_id, acl_apply=acl_apply)
            try:
                callback(config)
                self.logger.info('Successfully removed ACL %s from interface %s %s (%s)',
                                 acl_name, intf_type, intf, acl_direction)
                result[intf] = True
            except Exception as e:
                if '<bad-element>access-group</bad-element>' in str(e):
                    self.logger.warning('ACL %s not present in the interface %s %s (%s)',
                                        acl_name, intf_type, intf, acl_direction)
                    result[intf] = None
                else:
                    raise
        return result

    def add_l2_acl_rule(self, **kwargs):
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
            ethertype (str): EtherType, can be 'arp', 'fcoe', 'ipv4' or 1536-65535.
            count (str): Enables the packet count.
            log (str): Enables the logging.
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
            >>>     print dev.acl.add_mac_acl_rule(acl_name='Acl_1', seq_id=20,
                                                   action='permit', source='host',
                                                   srchost='2222.2222.2222')
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
            seq_variables = self.__seq_variables_mac_std
        elif acl_type == 'extended':
            seq_variables = self.__seq_variables_mac_ext

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
            ethertype = rule.pop('ethertype', None)
            count = rule.pop('count', False)
            log = rule.pop('log', False)

            # Check is the user input for ACL rule is correct
            if acl_type == 'extended' and not any([dst, dsthost, dst_mac_addr_mask]):
                raise ValueError('Destination required in extended access list')
            elif acl_type == 'standard' and any([dsthost, dst_mac_addr_mask]):
                raise ValueError('Destination cannot be given for standard access list')
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
            for variable in seq_dict:
                try:
                    seq_dict[variable] = eval(variable)
                except:
                    pass
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

    def __add_ip_acl_rules(self, **kwargs):
        """
        Add ACL rule to an existing IPv4 or IPv6 ACL.
        Args:
            acl_name (str): Name of the access list.
            address_type (str): ACL address type, ip or ipv6.
            acl_rules (array): List of ACL sequence rules.
            seq_id (int): Sequence number of the rule.
            action (str): Action to apply on the traffic (deny/permit/hard-drop).
            protocol_type (str): Type of IP packets to be filtered (<0-255>, tcp, udp, icmp or ip).
            source (str): Source filter, can be 'any' or 'host', or the actual MAC address.
            destination (str): Destination filter, can be 'any' or 'host', or the actual MAC.
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
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.
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
            seq_variables = self.__seq_variables_ip_std
        elif acl_type == 'extended':
            seq_variables = self.__seq_variables_ip_ext

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
            urg = rule.pop('urg', False)
            ack = rule.pop('ack', False)
            push = rule.pop('push', False)
            fin = rule.pop('fin', False)
            rst = rule.pop('rst', False)
            sync = rule.pop('sync', False)
            vlan = rule.pop('vlan_id', None)
            count = rule.pop('count', False)
            log = rule.pop('log', False)

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
            elif acl_type == 'standard' and any([urg, ack, push, fin, rst, sync]):
                raise ValueError('Any of (urg, ack, push, fin, rst, sync) '
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

    def add_ipv4_rule_acl(self, **kwargs):
        """
        Add ACL rule to an existing IPv4 ACL.
        Args:
            acl_name (str): Name of the access list.
            acl_rules (array): List of ACL sequence rules.
            seq_id (int): Sequence number of the rule.
            action (str): Action to apply on the traffic (deny/permit/hard-drop).
            protocol_type (str): Type of IP packets to be filtered (<0-255>, tcp, udp, icmp or ip).
            source (str): Source filter, can be 'any' or 'host', or the actual MAC address.
            destination (str): Destination filter, can be 'any' or 'host', or the actual MAC.
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
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10,
                                                  action='permit',
                                                  source='host 192.168.0.3')
        """
        kwargs['address_type'] = 'ip'
        return self.__add_ip_acl_rules(**kwargs)

    def add_ipv6_rule_acl(self, **kwargs):
        """
        Add ACL rule to an existing IPv6 ACL.
        Args:
            acl_name (str): Name of the access list.
            address_type (str): ACL address type, ip or ipv6.
            acl_rules (array): List of ACL sequence rules.
            seq_id (int): Sequence number of the rule.
            action (str): Action to apply on the traffic (deny/permit/hard-drop).
            protocol_type (str): Type of IP packets to be filtered (<0-255>, tcp, udp, icmp or ip).
            source (str): Source filter, can be 'any' or 'host', or the actual MAC address.
            destination (str): Destination filter, can be 'any' or 'host', or the actual MAC.
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
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
                                             address_type='ipv6')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10,
                                                  action='permit',
                                                  source='host 2:2::2:2')
        """
        kwargs['address_type'] = 'ipv6'
        return self.__add_ip_acl_rules(**kwargs)

    def __delete_acl_rules(self, **kwargs):
        """
        Remove ACL rule from an existing ACL.
        Args:
            address_type (str): ACL address type, ip or ipv6 or mac.
            acl_name (str): Name of the access list.
            seq_ids (list): Rule sequence-ids.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.
        """
        address_type = kwargs.pop('address_type', '')
        acl_name = kwargs.pop('acl_name', '')
        seq_ids = kwargs.pop('seq_ids', [])
        callback = kwargs.pop('callback', self._callback)
        seqs_list = []
        result = {}

        acl = self.get_acl_type(acl_name)
        self.logger.info('Successfully identified the acl_type as (%s:%s)',
                         acl['protocol'], acl['type'])
        if address_type is 'ip' and acl['protocol'] is not 'ip':
            raise ValueError('ACL %s is not compatible for IPV4 acl rule', acl_name)
        if address_type is 'ipv6' and acl['protocol'] is not 'ipv6':
            raise ValueError('ACL %s is not compatible for IPV6 acl rule', acl_name)
        if address_type is 'mac' and acl['protocol'] is not 'mac':
            raise ValueError('ACL %s is not compatible for L2 acl rule', acl_name)
        address_type = acl['protocol']
        acl_type = acl['type']
        for seq_id in seq_ids:
            seq_dict = self.get_seq(acl_name, seq_id, acl_type, address_type)
            if not seq_dict:
                self.logger.warning("ACL %s has no rule with seq_id %s", acl_name, seq_id)
                result['Seq-%s' % str(seq_id)] = None
                continue
            seqs_list.append(seq_dict)

        for seq_dict in seqs_list:
            self.logger.info('Deleting rule on ACL %s at seq_id %s', acl_name,
                             str(seq_dict['seq_id']))
            config = self.__generate_acl_rule_xml(address_type, acl_type, acl_name,
                                                  [seq_dict], delete=True)
            callback(config)
            self.logger.info('Successfully removed rule from ACL %s', acl_name)
            result['Seq-%s' % str(seq_dict['seq_id'])] = True
        return result

    def delete_l2_acl_rule(self, **kwargs):
        """
        Remove ACL rule from an existing L2 ACL.
        Args:
            acl_name (str): Name of the access list.
            seq_ids (list): Rule sequence-ids for bulk operation.
            seq_ids (int): Rule sequence-id.
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
            >>>     print dev.acl.add_mac_acl_rule(acl_name='Acl_1', seq_id=20,
                                                   action='permit', source='host',
                                                   srchost='2222.2222.2222')
            True
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_ids='10,20')
            True
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10)
            None
        """
        seq_ids = kwargs.pop('seq_ids', [])
        seq_id = kwargs.pop('seq_id', -1)
        if seq_id != -1:
            seq_ids.append(seq_id)
        kwargs['address_type'] = 'mac'
        kwargs['seq_ids'] = seq_ids
        return self.__delete_acl_rules(**kwargs)

    def delete_ipv4_acl_rule(self, **kwargs):
        """
        Remove ACL rule from an existing IPv4 ACL.
        Args:
            acl_name (str): Name of the access list.
            seq_ids (list): Rule sequence-ids for bulk operation.
            seq_ids (int): Rule sequence-id.
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
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10,
                                                  action='permit',
                                                  source='host 192.168.0.3')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_ids='10,20')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10)
        """
        seq_ids = kwargs.pop('seq_ids', [])
        seq_id = kwargs.pop('seq_id', -1)
        if seq_id != -1:
            seq_ids.append(seq_id)
        kwargs['address_type'] = 'ip'
        kwargs['seq_ids'] = seq_ids
        return self.__delete_acl_rules(**kwargs)

    def delete_ipv6_acl_rule(self, **kwargs):
        """
        Remove ACL rule from an existing IPv6 ACL.
        Args:
            acl_name (str): Name of the access list.
            seq_ids (list): Rule sequence-ids for bulk operation.
            seq_ids (int): Rule sequence-id.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
                                             address_type='ipv6')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10,
                                                  action='permit',
                                                  source='host 2:2::2:2')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_ids='10,20')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10)
        """
        seq_ids = kwargs.pop('seq_ids', [])
        seq_id = kwargs.pop('seq_id', -1)
        if seq_id != -1:
            seq_ids.append(seq_id)
        kwargs['address_type'] = 'ipv6'
        kwargs['seq_ids'] = seq_ids
        return self.__delete_acl_rules(**kwargs)
