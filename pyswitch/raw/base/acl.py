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

import template
import pyswitch.NetConfDevice


class Acl(object):
    """
    The Acl class holds all the functions assocaiated with the Access Control list
    of a NOS device.

    Attributes:
        None
    """

    seq_variables_ip_std = ('seq_id', 'action', 'src_host_any_sip', 'src_host_ip',
                            'src_mask', 'count', 'log')
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
                            'dport_number_range_higher_udp', 'dscp', 'urg', 'ack', 'push',
                            'fin', 'rst', 'sync', 'vlan', 'count', 'log')
    seq_variables_mac_std = ('seq_id', 'action', 'source', 'srchost',
                             'src_mac_addr_mask', 'count', 'log')
    seq_variables_mac_ext = ('seq_id', 'action', 'source', 'srchost',
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
        self._callback = callback

    def get_acl_type(self, acl_name):
        """
        Return acl-type as dict {'type':'standard'/'ectended;, 'protocol':'mac'/'ip'/'ipv6'}.
        """

        try:
            # Check 'acl_name' in the 'mac' 'standard' ACLs
            fltr = getattr(template, 'mac_fltr').format(acl_type='standard', acl_name=acl_name)
            config = getattr(template, 'acl_get_config').format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0].text == acl_name:
                return {'type': 'standard', 'protocol': 'mac'}
        except IndexError:
            pass        # acl_name not present in mac standard ACLs, pass for next checks.
        except:
            raise
        try:
            # Check 'acl_name' in the 'mac' 'extended' ACLs
            fltr = getattr(template, 'mac_fltr').format(acl_type='extended', acl_name=acl_name)
            config = getattr(template, 'acl_get_config').format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0].text == acl_name:
                return {'type': 'extended', 'protocol': 'mac'}
        except IndexError:
            pass        # acl_name not present in mac extended ACLs, pass for next checks.
        except:
            raise
        try:
            # Check 'acl_name' in the 'ip' 'standard' ACLs
            fltr = getattr(template, 'ipv4_fltr').format(acl_type='standard', acl_name=acl_name)
            config = getattr(template, 'acl_get_config').format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0][0].text == acl_name:
                return {'type': 'standard', 'protocol': 'ip'}
        except IndexError:
            pass        # acl_name not present in ip standard ACLs, pass for next checks.
        except:
            raise
        try:
            # Check 'acl_name' in the 'ip' 'extended' ACLs
            fltr = getattr(template, 'ipv4_fltr').format(acl_type='extended', acl_name=acl_name)
            config = getattr(template, 'acl_get_config').format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0][0].text == acl_name:
                return {'type': 'extended', 'protocol': 'ip'}
        except IndexError:
            pass        # acl_name not present in ip extended ACLs, pass for next checks.
        except:
            raise
        try:
            # Check 'acl_name' in the 'ipv6' 'standard' ACLs
            fltr = getattr(template, 'ipv6_fltr').format(acl_type='standard', acl_name=acl_name)
            config = getattr(template, 'acl_get_config').format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0][0].text == acl_name:
                return {'type': 'standard', 'protocol': 'ipv6'}
        except IndexError:
            pass        # acl_name not present in ipv6 standard ACLs, pass for next checks.
        except:
            raise
        try:
            # Check 'acl_name' in the 'ipv6' 'extended' ACLs
            fltr = getattr(template, 'ipv6_fltr').format(acl_type='extended', acl_name=acl_name)
            config = getattr(template, 'acl_get_config').format(filter=fltr)
            res = self._callback(config, handler='get')
            if res[0][0][0][0][0][0].text == acl_name:
                return {'type': 'extended', 'protocol': 'ipv6'}
        except IndexError:
            pass        # acl_name not present in ipv6 extended ACLs also.
        except:
            raise
        raise ValueError('Failed to identify acl_type. Check if the ACL %s exists' % acl_name)

    def get_seq(self, acl_name, seq_id, acl_type, address_type=None):
        """
        Return ACL rule sequence as dict() with given 'seq_id'
        or last sequence if 'seq_id' not given.
        """
        fltr = ""
        seqIdx = ""

        if address_type == 'mac':
            fltr = getattr(template, 'mac_fltr').format(acl_type=acl_type, acl_name=acl_name)
            seqIdx = "res[0][0][0][0][1]"
        elif address_type == 'ip':
            fltr = getattr(template, 'ipv4_fltr').format(acl_type=acl_type, acl_name=acl_name)
            seqIdx = "res[0][0][0][0][0][1]"
        elif address_type == 'ipv6':
            fltr = getattr(template, 'ipv6_fltr').format(acl_type=acl_type, acl_name=acl_name)
            seqIdx = "res[0][0][0][0][0]"

        config = getattr(template, 'acl_get_config').format(filter=fltr)
        try:
            res = self._callback(config, handler='get')
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
        except pyswitch.NetConfDevice.DeviceCommError:
            raise
        except:
            raise ValueError('Failed to get sequence details')

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
            Return value of `string` message.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
            ...                              address_type='mac')
            ...     print dev.acl.create_acl(acl_name='Acl_2', acl_type='extended',
            ...                              address_type='ip')
            ...     print dev.acl.create_acl(acl_name='Acl_3', acl_type='extended',
            ...                              address_type='ipv6')
        """

        address_type = kwargs.pop('address_type', '')
        acl_type = kwargs.pop('acl_type', '')
        acl_name = kwargs.pop('acl_name', '')
        callback = kwargs.pop('callback', self._callback)

        if address_type == 'mac':
            config = getattr(template, 'acl_create_mac')
        else:
            config = getattr(template, 'acl_create_ip')

        config = config.format(address_type=address_type,
                               acl_name=acl_name,
                               acl_type=acl_type,
                               delete='')
        callback(config)
        return 'Successfully created ACL %s' % acl_name

    def delete_acl(self, **kwargs):
        """
        Delete Access Control List.
        Args:
            address_type (str): ACL address type, ip or ipv6 or mac.
            acl_type (str): ACL type, extended or standard.
            acl_name (str): Name of the access list.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            Return value of `string` message.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
            ...                              address_type='mac')
            ...     print dev.acl.delete_acl(acl_name='Acl_1', acl_type='standard',
            ...                              address_type='mac')
        """

        address_type = kwargs.pop('address_type', '')
        acl_type = kwargs.pop('acl_type', '')
        acl_name = kwargs.pop('acl_name', '')
        callback = kwargs.pop('callback', self._callback)

        if address_type == 'mac':
            config = getattr(template, 'acl_create_mac')
        else:
            config = getattr(template, 'acl_create_ip')

        config = config.format(address_type=address_type,
                               acl_name=acl_name,
                               acl_type=acl_type,
                               delete='operation=\'delete\'')
        callback(config)
        return 'Successfully deleted ACL %s' % acl_name

    def apply_acl(self, **kwargs):
        """
        Apply an ACL to a physical port, port channel, VE or management interface.
        Args:
            rbridge_id (str): RBridge ID of the VDX switch under which VE will be configured
            address_type (str): ACL address type, ip or ipv6 or mac.
            intf_type (str): Interface type, (physical, port channel, VE or management interface).
            intf (str): Name of the Interface.
            acl_name (str): Name of the access list.
            acl_direction (str): Direction of ACL binding on the specified interface [in/out].
            traffic_type (str): Traffic type for the ACL being applied [switched/routed].
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            Return value of `string` message.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
            ...                              address_type='mac')
            ...     print dev.acl.apply_acl(address_type='mac', intf_type='tengigabitethernet',
            ...                             intf='1/0/2', acl_name='Acl_1',
            ...                             acl_direction='in', traffic_type='switched')
        """
        rbridge_id = kwargs.pop('rbridge_id', '')
        address_type = kwargs.pop('address_type', '')
        intf_type = kwargs.pop('intf_type', '').replace('_', '-')
        intf = kwargs.pop('intf', '')
        acl_name = kwargs.pop('acl_name', '')
        acl_direction = kwargs.pop('acl_direction', '')
        traffic_type = kwargs.pop('traffic_type', '')
        callback = kwargs.pop('callback', self._callback)

        if address_type == 'mac':
            acl_apply = getattr(template, 'acl_apply_mac')
        elif address_type == 'ip':
            acl_apply = getattr(template, 'acl_apply_ipv4')
        else:
            acl_apply = getattr(template, 'acl_apply_ipv6')

        acl_apply = acl_apply.format(address_type=address_type,
                                     intf_type=intf_type,
                                     intf=intf, acl_name=acl_name,
                                     acl_direction=acl_direction,
                                     traffic_type='' if not traffic_type else
                                     '<traffic-type>' + traffic_type + '</traffic-type>',
                                     delete='')
        if rbridge_id:
            config = getattr(template, 'rbridge_acl_apply')
        else:
            config = '<config> {acl_apply} </config>'

        config = config.format(rbridge_id=rbridge_id,
                               acl_apply=acl_apply)
        callback(config)
        return 'Successfully applied ACL %s on interface %s %s (%s)' \
               % (acl_name, intf_type, intf, acl_direction)

    def remove_acl(self, **kwargs):
        """
        Remove ACL from a physical port, port channel, VE or management interface.
        Args:
            rbridge_id (str): RBridge ID of the VDX switch under which VE will be configured
            address_type (str): ACL address type, ip or ipv6 or mac.
            intf_type (str): Interface type, (physical, port channel, VE or management interface).
            intf (str): Name of the Interface.
            acl_name (str): Name of the access list.
            acl_direction (str): Direction of ACL binding on the specified interface [in/out].
            traffic_type (str): Traffic type for the ACL being applied [switched/routed].
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            Return value of `string` message.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
            ...                              address_type='mac')
            ...     print dev.acl.apply_acl(address_type='mac', intf_type='tengigabitethernet',
            ...                             intf='1/0/2', acl_name='Acl_1',
            ...                             acl_direction='in', traffic_type='switched')
            ...     print dev.acl.remove_acl(address_type='mac', intf_type='tengigabitethernet',
            ...                              intf='1/0/2', acl_name='Acl_1',
            ...                              acl_direction='in', traffic_type='switched')
        """
        rbridge_id = kwargs.pop('rbridge_id', '')
        address_type = kwargs.pop('address_type', '')
        intf_type = kwargs.pop('intf_type', '').replace('_', '-')
        intf = kwargs.pop('intf', '')
        acl_name = kwargs.pop('acl_name', '')
        acl_direction = kwargs.pop('acl_direction', '')
        traffic_type = kwargs.pop('traffic_type', '')
        callback = kwargs.pop('callback', self._callback)

        if address_type == 'mac':
            acl_apply = getattr(template, 'acl_apply_mac')
        elif address_type == 'ip':
            acl_apply = getattr(template, 'acl_apply_ipv4')
        else:
            acl_apply = getattr(template, 'acl_apply_ipv6')

        acl_apply = acl_apply.format(address_type=address_type,
                                     intf_type=intf_type,
                                     intf=intf, acl_name=acl_name,
                                     acl_direction=acl_direction,
                                     traffic_type='' if not traffic_type else
                                     '<traffic-type>' + traffic_type + '</traffic-type>',
                                     delete='operation=\'delete\'')
        if rbridge_id:
            config = getattr(template, 'rbridge_acl_apply')
        else:
            config = '<config> {acl_apply} </config>'

        config = config.format(rbridge_id=rbridge_id,
                               acl_apply=acl_apply)
        try:
            callback(config)
        except Exception as e:
            if '<bad-element>access-group</bad-element>' in str(e):
                return 'ACL %s not present in the interface %s %s (%s)' \
                       % (acl_name, intf_type, intf, acl_direction)
            else:
                raise
        return 'Successfully removed ACL %s from interface %s %s (%s)' \
               % (acl_name, intf_type, intf, acl_direction)

    def add_acl_rule(self, **kwargs):
        """
        Add ACL rule to an existing ACL.
        Args:
            address_type (str): ACL address type, ip or ipv6 or mac.
            acl_type (str): ACL type, extended or standard.
            acl_name (str): Name of the access list.
            seqs_list (list(dict())): Rule sequences dictionary.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            Return value of `string` message.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
            ...                              address_type='mac')
            ...     print dev.acl.add_acl_rule(address_type='mac', acl_type='standard',
            ...                             acl_name='Acl_1', seqs_list='[
            ...     {'seq_id':'10', 'action':'permit', 'src_host_any_sip':'any', 'log':'true'},
            ...     {'action':'deny', 'src_host_any_sip':'host', 'src_host_ip':'2222.3333.4444'}]')
        """
        address_type = kwargs.pop('address_type', '')
        acl_type = kwargs.pop('acl_type', '')
        acl_name = kwargs.pop('acl_name', '')
        seqs_list = kwargs.pop('seqs_list', '')
        callback = kwargs.pop('callback', self._callback)

        sequences = ''
        user_seq_id = None
        if isinstance(seqs_list, list):
            if address_type == 'mac':
                if acl_type == 'standard':
                    seq_vars = self.seq_variables_mac_std
                else:
                    seq_vars = self.seq_variables_mac_ext
            else:
                if acl_type == 'standard':
                    seq_vars = self.seq_variables_ip_std
                else:
                    seq_vars = self.seq_variables_ip_ext
            for seq in seqs_list:
                seqxml = ''
                user_seq_id = seq['user_seq_id']
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
            config = getattr(template, 'acl_rule_mac')
        else:
            config = getattr(template, 'acl_rule_ip')

        config = config.format(address_type=address_type,
                               acl_name=acl_name,
                               acl_type=acl_type,
                               sequences=sequences)
        try:
            callback(config)
        except Exception as e:
            if 'Access-list entry already exists' in str(e) and user_seq_id is None:
                return str(e).split('%Error: ')[1]
            else:
                raise
        return 'Successfully added rules  on ACL %s' % acl_name

    def remove_acl_rule(self, **kwargs):
        """
        Remove ACL rule from an existing ACL..
        Args:
            address_type (str): ACL address type, ip or ipv6 or mac.
            acl_type (str): ACL type, extended or standard.
            acl_name (str): Name of the access list.
            seqs_list (list(dict())): Rule sequences dictionary.
            callback (function): A function executed upon completion of the method.
               The only parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            Return value of `string` message.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth, connection_type='NETCONF') as dev:
            ...     print dev.firmware_version
            ...     print dev.os_type
            ...     print dev.acl.create_acl(acl_name='Acl_1', acl_type='standard',
            ...                              address_type='mac')
            ...     print dev.acl.add_acl_rule(address_type='mac', acl_type='standard',
            ...                             acl_name='Acl_1', seqs_list='[
            ...     {'seq_id':'10', 'action':'permit', 'src_host_any_sip':'any', 'log':'true'},
            ...     {'action':'deny', 'src_host_any_sip':'host', 'src_host_ip':'2222.3333.4444'}]')
            ...     print dev.acl.remove_acl_rule(address_type='mac', acl_type='standard',
            ...                             acl_name='Acl_1', seqs_list='[
            ...                             {'seq_id':'10'}, {'seq_id':'20'}]')
        """
        address_type = kwargs.pop('address_type', '')
        acl_type = kwargs.pop('acl_type', '')
        acl_name = kwargs.pop('acl_name', '')
        seqs_list = kwargs.pop('seqs_list', '')
        callback = kwargs.pop('callback', self._callback)

        sequences = ''
        if isinstance(seqs_list, list):
            for seq in seqs_list:
                if 'seq_id' in seq and seq['seq_id'] is not None:
                    seqxml = '<seq-id>%s</seq-id>' % str(seq['seq_id'])
                sequences += "<seq operation=\'delete\'>\n{}</seq>\n".format(seqxml)

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
            config = getattr(template, 'acl_rule_mac')
        else:
            config = getattr(template, 'acl_rule_ip')

        config = config.format(address_type=address_type,
                               acl_name=acl_name,
                               acl_type=acl_type,
                               sequences=sequences)
        callback(config)
        return 'Successfully removed rules from ACL %s' % acl_name
