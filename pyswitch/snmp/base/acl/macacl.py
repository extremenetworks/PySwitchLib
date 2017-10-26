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


class MacAcl(object):
    """
    The MacAcl class holds all the functions assocaiated with
    Mac Access Control list.
    Attributes:
        None
    """

    def parse_action(self, **parameters):
        """
        parse supported actions by MLX platform
        Args:
            parameters is the dict containing actoin key to parse for.
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'action' not in parameters:
            raise ValueError("\'action\' not present in parameters arg")

        action = parameters['action']

        if parameters['action'] in ['permit', 'deny']:
            return parameters['action']

        raise ValueError("The \'action\' value {} is invalid. Specify "
                         "\'deny\' or \'permit\' supported "
                         "values".format(action))

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

    def parse_source(self, **parameters):
        """
        parse the source param.
        Args:
            parameters is the dict containing source, srchost and
            src_mac_addr_mask keys to parse for.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'source' not in parameters:
            return None

        if 'src_mac_addr_mask' not in parameters:
            raise ValueError("\'src_mac_addr_mask\' not present "
                             "in parameters arg")

        src = parameters['source']
        src_mac_addr_mask = parameters['src_mac_addr_mask']

        if src == "any":
            return "any"
        elif self.is_valid_mac(src):
            if self.is_valid_mac(src_mac_addr_mask):
                return src + ' ' + src_mac_addr_mask

        raise ValueError("Invalid {} mask: {}. Supported format is \
            HHHH.HHHH.HHHH HHHH.HHHH.HHHH".format(src, src_mac_addr_mask))

    def parse_dst(self, **parameters):
        """
        parse the dst param
        Args:
            parameters is the dict containing dst, dsthost and
            dst_mac_addr_mask keys to parse for.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'dst' not in parameters:
            return None

        if 'dst_mac_addr_mask' not in parameters:
            raise ValueError("\'dst_mac_addr_mask\' not present parameter arg")

        dst = parameters['dst']
        dst_mac_addr_mask = parameters['dst_mac_addr_mask']

        if dst == "any":
            return "any"
        elif self.is_valid_mac(dst):
            if self.is_valid_mac(dst_mac_addr_mask):
                return dst + ' ' + dst_mac_addr_mask

        raise ValueError("Invalid {} mask: {}. Supported format is "
                         "HHHH.HHHH.HHHH HHHH.HHHH.HHHH"
                         .format(dst, dst_mac_addr_mask))

    def parse_vlan(self, **parameters):
        """
        parse the vlan param
        Args:
            parameters is the dict containing vlan key to be parsed.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'vlan' not in parameters:
            return None

        vlan = parameters['vlan']

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
            parameters is the dict containing ethertype key to be parsed.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'ethertype' not in parameters:
            return None

        ethertype = parameters['ethertype']

        if not ethertype:
            return None

        if ethertype in ['arp', 'fcoe', 'ipv4-15', 'ipv6', 'any']:
            return 'etype ' + ethertype

        if ethertype.isdigit():
            if int(ethertype) >= 1536 or int(ethertype) <= 65535:
                return 'etype ' + ethertype

        raise ValueError("The ethertype value {} is invalid."
                         " Specify Integer or \'any\', \'arp\', "
                         "\'fcoe\', \'ipv4-15\', \'ipv6\'".format(ethertype))

    def parse_arp_guard(self, **parameters):
        """
        parse the arp_guard param
        Args:
            parameters is the dict containing arp_guard key to be parsed.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'arp_guard' not in parameters:
            return None

        arp_guard = parameters['arp_guard']

        if arp_guard == 'False':
            return None

        if 'ethertype' not in parameters:
            raise ValueError("The \'arp-guard\' value {} is invalid."
                             " Can be supported ethertype arp only"
                             .format(arp_guard))

        ethertype = parameters['ethertype']

        if arp_guard == 'True' and ethertype == 'arp':
            return 'arp-guard'

        raise ValueError("\'arp_guard\' configuration allowed"
                         " only for \'arp\' ethertype")

    def parse_drop_precedence(self, **parameters):
        """
        parse the drop_precedence_force param
        Args:
            parameters is the dict containing drop_precedence_force
            key to be parsed.
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

        if drop_precedence.isdigit():
            if int(drop_precedence) >= 0 or int(drop_precedence) <= 3:
                    return 'drop-precedence ' + drop_precedence

        raise ValueError("The \'drop-precedence\' value {} is invalid."
                         " Supported range is 0 to 3".format(drop_precedence))

    def parse_drop_precedence_force(self, **parameters):
        """
        parse the drop_precedence_force param
        Args:
            parameters is the dict containing drop_precedence_force
            key to be parsed.
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

        if drop_precedence_force.isdigit():
            if int(drop_precedence_force) >= 0 or \
               int(drop_precedence_force) <= 3:
                return 'drop-precedence-force ' + drop_precedence_force

        raise ValueError("The \'drop-precedence-force\' value {} is invalid."
                         " Supported range is 0 to 3"
                         .format(drop_precedence_force))

    def parse_log(self, **parameters):
        """
        parse the log param
        Args:
            parameters is the dict containing log key to be parsed.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'log' not in parameters:
            return None

        log = parameters['log']

        if log == 'True':
            if 'mirror' not in parameters:
                return 'log'
            mirror = parameters['mirror']
            if mirror == 'False':
                return 'log'
        else:
            return None

        raise ValueError("The \'log\' value {} is invalid."
                         " log can not be configured along with mirror"
                         .format(log))

    def parse_mirror(self, **parameters):
        """
        parse the mirror param
        Args:
            parameters is the dict containing mirror key to be parsed.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'mirror' not in parameters:
            return None

        mirror = parameters['mirror']

        if mirror == 'True':
            if 'log' not in parameters:
                return 'mirror'
            log = parameters['log']
            if log == 'False':
                return 'mirror'
        else:
            return None

        raise ValueError("The \'mirror\' value {} is invalid."
                         " mirror can not be configured along with mirror"
                         .format(mirror))

    def parse_priority(self, **parameters):
        """
        parse the priority param
        Args:
            parameters is the dict containing priority key to be parsed.
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

        if priority.isdigit():
            if int(priority) >= 0 or int(priority) <= 7:
                return 'priority ' + priority

        raise ValueError("The \'priority\' value {} is invalid."
                         " Supported range is 0 to 7".format(priority))

    def parse_priority_force(self, **parameters):
        """
        parse the priority_force param
        Args:
            parameters is the dict containing priority_force key to be parsed.
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

        if priority_force.isdigit():
            if int(priority_force) >= 0 or int(priority_force) <= 7:
                return 'priority-force ' + priority_force

        raise ValueError("The \'priority_force\' value {} is invalid."
                         " Supported range is 0 to 7".format(priority_force))

    def parse_priority_mapping(self, **parameters):
        """
        parse the priority_mapping param
        Args:
            parameters is the dict containing priority_mapping key to be parsed
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

        if priority_mapping.isdigit():
            if int(priority_mapping) >= 0 or int(priority_mapping) <= 7:
                return 'priority-mapping ' + priority_mapping

        raise ValueError("The \'priority_mapping\' value {} is invalid."
                         " Supported range is 0 to 7".format(priority_mapping))
