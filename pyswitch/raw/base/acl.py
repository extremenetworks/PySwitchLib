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

import abc
import logging


class Acl(object):
    """
    The Acl class holds all the functions assocaiated with the Access Control list.

    Attributes:
        None
    """
    __metaclass__ = abc.ABCMeta

    os_type = None

    @abc.abstractmethod
    def __init__(self, callback):
        """
        ACL init function.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            ACL Object
        """
        logging.basicConfig(format='pyswitch.raw.base.acl.Acl: %(levelname)s  %(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self._callback = callback

    @abc.abstractmethod
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
            True
            >>>     print dev.acl.create_acl(acl_name='Acl_2', acl_type='extended',
                                             address_type='ip')
            True
            >>>     print dev.acl.create_acl(acl_name='Acl_3', acl_type='extended',
                                             address_type='ipv6')
            True
        """
        return

    @abc.abstractmethod
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
            True
            >>>     print dev.acl.delete_acl(acl_name='Acl_2')
            None
            >>>     print dev.acl.delete_acl(acl_name='Acl_1')
            True
        """
        return

    @abc.abstractmethod
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
            True
            >>>     print dev.acl.apply_acl(intf_type='ethernet', intf_names='0/1,0/2',
                                            acl_name='Acl_1', acl_direction='in',
                                            traffic_type='switched')
            True
        """
        return

    @abc.abstractmethod
    def remove_acl(self, **kwargs):
        """
        Remove ACL from a physical port, port channel, VE or management interface.
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
            True
            >>>     print dev.acl.apply_acl(intf_type='ethernet', intf_names='0/1,0/2',
                                            acl_name='Acl_1', acl_direction='in',
                                            traffic_type='switched')
            True
            >>>     print dev.acl.remove_acl(intf_type='ethernet', intf_names='0/1,0/2',
                                            acl_name='Acl_1', acl_direction='in',
                                            traffic_type='switched')
            True
        """
        return

    @abc.abstractmethod
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
            True
            >>>     print dev.acl.add_mac_acl_rule(acl_name='Acl_1', seq_id=20,
                                                   action='permit', source='host',
                                                   srchost='2222.2222.2222')
            True
        """
        return

    @abc.abstractmethod
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
            True
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_id=10,
                                                  action='permit',
                                                  source='host 192.168.0.3')
            True
        """
        return

    @abc.abstractmethod
    def remove_acl_rule(self, **kwargs):
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
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1', seq_ids='10,20')
            True
        """
        return
