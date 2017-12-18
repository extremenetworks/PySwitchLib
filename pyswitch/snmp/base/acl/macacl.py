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
from aclparam_parser import AclParamParser


class MacAcl(AclParamParser):
    """
    The MacAcl class holds all the functions assocaiated with
    Mac Access Control list.
    Attributes:
        None
    """

    def is_valid_mac(self, mac_addr):
        """
        This will only validate the HHHH.HHHH.HHHH MAC format.
        Will need to be expanded to validate other formats of MAC.
        Args:
            mac_addr
        Return:
            True for success
            False for failure
        """
        if re.match('[0-9A-Fa-f]{4}[.][0-9A-Fa-f]{4}[.][0-9A-Fa-f]{4}$',
                    mac_addr):
            return True

        return False

    def parse_source_dst_param(self, mac_param, mask_param):
        if mac_param == "any":
            return "any"

        if not mask_param:
            raise ValueError("MAC MASK required param if MAC is not \'any\'")

        if not self.is_valid_mac(mac_param):
            raise ValueError("Invalid MAC format. Supported format is "
                             "HHHH.HHHH.HHHH")

        if not self.is_valid_mac(mask_param):
            raise ValueError("Invalid MAC MASK format. Supported format is "
                             "HHHH.HHHH.HHHH")

        return mac_param + ' ' + mask_param

    def parse_source(self, **parameters):
        """
        parse the source param.
        Args:
            parameters contains:
                source (string): Source filter, can be 'any' or
                    the actual MAC in HHHH.HHHH.HHHH format.
                src_mac_addr_mask (string): Mask for the source MAC
                    in HHHH.HHHH.HHHH format.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        src_mac_addr_mask = None
        if 'source' not in parameters or not parameters['source']:
            raise ValueError("\'source\' is required param for MLX")

        if 'src_mac_addr_mask' in parameters:
            src_mac_addr_mask = parameters['src_mac_addr_mask']

        return self.parse_source_dst_param(parameters['source'],
                                           src_mac_addr_mask)

    def parse_dst(self, **parameters):
        """
        parse the dst param
        Args:
            parameters contains:
                dst (string): Destination filter, can be 'any' or
                    the actual MAC in HHHH.HHHH.HHHH format.
                dst_mac_addr_mask (string): Mask for the destination MAC
                    in HHHH.HHHH.HHHH format.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        dst_mac_addr_mask = None
        if 'dst' not in parameters or not parameters['dst']:
            raise ValueError("\'dst\' is required param")

        if 'dst_mac_addr_mask' in parameters:
            dst_mac_addr_mask = parameters['dst_mac_addr_mask']

        return self.parse_source_dst_param(parameters['dst'],
                                           dst_mac_addr_mask)

    def parse_vlan(self, **parameters):
        """
        parse the vlan param
        Args:
            parameters contains:
                vlan(string): 'any' or 1-4096
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'vlan' not in parameters:
            return None

        vlan = parameters['vlan']
        if not vlan:
            return None

        if vlan:
            if vlan.isdigit():
                if int(vlan) > 0 and int(vlan) < 4096:
                    return vlan
            elif vlan == 'any':
                return 'any'

        raise ValueError("The \'vlan\' value {} is invalid."
                         " Specify \'any\' or \'1-4095\' supported values"
                         .format(vlan))

    def parse_ethertype(self, **parameters):
        """
        parse the ethertype param
        Args:
            parameters contains:
                ethertype(string): EtherType, can be 'arp',
                    'fcoe', 'ipv4-l5', 'ipv6' or
                    custom value between 1536 and 65535.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'ethertype' not in parameters or not parameters['ethertype']:
            return None

        if 'vlan' not in parameters or not parameters['vlan']:
            raise ValueError("vlan is required parameter to configure"
                             " ethertype")

        ethertype = parameters['ethertype']

        if ethertype in ['arp', 'fcoe', 'ipv4-l5', 'ipv6', 'any']:
            return 'etype ' + ethertype

        if ethertype.isdigit():
            if int(ethertype) >= 1536 or int(ethertype) <= 65535:
                return 'etype ' + str(hex(int(ethertype)))[2:]

        raise ValueError("The ethertype value {} is invalid."
                         " Specify Integer or \'any\', \'arp\', "
                         "\'fcoe\', \'ipv4-l5\', \'ipv6\'".format(ethertype))

    def parse_arp_guard(self, **parameters):
        """
        parse the arp_guard param
        Args:
            parameters contains:
                arp_guard( string): Enables arp-guard for the rule
                ethertype(string): EtherType, can be 'arp', 'fcoe',
                    'ipv4-l5', 'ipv6' or
                    custom value between 1536 and 65535.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'arp_guard' not in parameters or parameters['arp_guard'] != 'True':
            return None

        if 'ethertype' not in parameters or parameters['ethertype'] != 'arp':
            raise ValueError("arp guard acl cannot be configured for etype "
                             "other than ARP !!")

        if 'action' not in parameters or parameters['action'] != 'permit':
            raise ValueError("arp guard cannot be configured for action {}"
                             .format(parameters['action']))

        if 'log' in parameters and parameters['log'] == 'True':
            raise ValueError("\'arp_guard\' and \'log\' can not be configured "
                             "together")

        if 'mirror' in parameters and parameters['mirror'] == 'True':
            raise ValueError("\'arp_guard\' and \'mirror\' can not be "
                             "configured together")
        return 'arp-guard'

    def parse_drop_precedence(self, **parameters):
        """
        parse the drop_precedence_force param
        Args:
            parameters contains:
                drop_precedence_force( string): Matches the specified value
                    against the drop_precedence_force value of the packet to
                    filter.  Allowed values are 0 through 3.

                drop_precedence( string): Matches the specified value
                    against the drop_precedence value of the packet to
                    filter.  Allowed values are 0 through 3.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence' not in parameters:
            return None

        if not parameters['drop_precedence']:
            return None

        drop_precedence = parameters['drop_precedence']

        if 'drop_precedence_force' in parameters and \
                parameters['drop_precedence_force']:
            raise ValueError("drop-precedence-force and drop-precedence "
                             "can not be enabled at the same time!")

        if drop_precedence.isdigit():
            if int(drop_precedence) >= 0 or int(drop_precedence) <= 3:
                    return 'drop-precedence ' + drop_precedence

        raise ValueError("The \'drop-precedence\' value {} is invalid."
                         " Supported range is 0 to 3".format(drop_precedence))

    def parse_drop_precedence_force(self, **parameters):
        """
        parse the drop_precedence_force param
        Args:
            parameters contains:
                drop_precedence_force( string): Matches the specified value
                    against the drop_precedence_force value of the packet to
                    filter.  Allowed values are 0 through 3.

                drop_precedence( string): Matches the specified value
                    against the drop_precedence value of the packet to
                    filter.  Allowed values are 0 through 3.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence_force' not in parameters:
            return None

        if not parameters['drop_precedence_force']:
            return None

        drop_precedence_force = parameters['drop_precedence_force']

        if 'drop_precedence' in parameters and parameters['drop_precedence']:
            raise ValueError("drop-precedence-force and drop-precedence "
                             "can not be enabled at the same time!")

        if drop_precedence_force.isdigit():
            if int(drop_precedence_force) >= 0 or \
               int(drop_precedence_force) <= 3:
                return 'drop-precedence-force ' + drop_precedence_force

        raise ValueError("The \'drop-precedence-force\' value {} is invalid."
                         " Supported range is 0 to 3"
                         .format(drop_precedence_force))

    def parse_priority(self, **parameters):
        """
        parse the priority param
        Args:
            parameters contains:
                priority(integer): Matches the specified value against the
                    priority value of the packet to filter.
                    Allowed values are 0 through 7.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority' not in parameters:
            return None

        priority = parameters['priority']

        if not priority:
            return None

        if 'priority_force' in parameters and parameters['priority_force']:
            raise ValueError("priority and priority-force can not be "
                             "enabled at the same time!")

        if int(priority) >= 0 or int(priority) <= 7:
            return 'priority ' + str(priority)

        raise ValueError("The \'priority\' value {} is invalid."
                         " Supported range is 0 to 7".format(priority))

    def parse_priority_force(self, **parameters):
        """
        parse the priority_force param
        Args:
            parameters contains:
                priority_force(integer): Matches specified value against the
                    priority_force value of the packet to filter.
                    Allowed values are 0 through 7.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority_force' not in parameters:
            return None

        priority_force = parameters['priority_force']

        if not priority_force:
            return None

        if 'priority' in parameters and parameters['priority']:
            raise ValueError("priority and priority-force can not be "
                             "enabled at the same time!")

        if int(priority_force) >= 0 or int(priority_force) <= 7:
            return 'priority-force ' + str(priority_force)

        raise ValueError("The \'priority_force\' value {} is invalid."
                         " Supported range is 0 to 7".format(priority_force))

    def parse_priority_mapping(self, **parameters):
        """
        parse the priority_mapping param
        Args:
            parameters contains:
                priority_mapping(integer): Matches specified value against the
                    priority_mapping value of the packet to filter.
                    Allowed values are 0 through 7.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority_mapping' not in parameters:
            return None

        priority_mapping = parameters['priority_mapping']

        if not priority_mapping:
            return None

        if int(priority_mapping) >= 0 or int(priority_mapping) <= 7:
            return 'priority-mapping ' + str(priority_mapping)

        raise ValueError("The \'priority_mapping\' value {} is invalid."
                         " Supported range is 0 to 7".format(priority_mapping))
