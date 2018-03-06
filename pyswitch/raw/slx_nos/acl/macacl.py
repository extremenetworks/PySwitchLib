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
import pyswitch.utilities as utilities
from pyswitch.raw.slx_nos.acl.aclparam_parser import AclParamParser


class MacAcl(AclParamParser):
    """
    The MacAcl class holds all the functions assocaiated with
    Mac Access Control list.
    Attributes:
        None
    """

    def parse_source(self, **kwargs):
        """
        parse the source param.
        Args:
            kwargs contains:
                source(string): Destination filter, can be 'any' or 'host', or
                    the actual MAC of the destination in HHHH.HHHH.HHHH format.
                srchost(string):Destination MAC in HHHH.HHHH.HHHH format. The
                    value is required only when the src is 'host'
                src_mac_addr_mask(string): Mask for the source MAC in
                    HHHH.HHHH.HHHH format.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'source' not in kwargs or not kwargs['source']:
            raise ValueError("Missing \'source\' in kwargs")

        src = kwargs['source']
        src = ' '.join(src.split())

        ret = {"source": None, "srchost": None, "src_mac_addr_mask": None}

        if src == "any":
            ret['source'] = "any"
            return ret

        if src == "host":
            if 'srchost' not in kwargs or not kwargs['srchost']:
                raise ValueError("Missing \'srchost\' in kwargs")

            srchost = kwargs['srchost']
            srchost = ' '.join(srchost.split())

            utilities.validate_mac_address(srchost)
            ret['source'] = "host"
            ret['srchost'] = srchost
            return ret

        if 'src_mac_addr_mask' not in kwargs or \
                not kwargs['src_mac_addr_mask']:
            raise ValueError("Missing \'src_mac_addr_mask\' in kwargs")

        src_mac_addr_mask = kwargs['src_mac_addr_mask']
        src_mac_addr_mask = ' '.join(src_mac_addr_mask.split())

        utilities.validate_mac_address(src)
        utilities.validate_mac_address(src_mac_addr_mask)
        ret['source'] = src
        ret['mask'] = src_mac_addr_mask

        return ret

    def parse_dst(self, **kwargs):
        """
        parse the dst param.
        Args:
            kwargs contains:
                dst(string): Destination filter, can be 'any' or 'host', or
                    the actual MAC of the destination in HHHH.HHHH.HHHH format.
                dsthost(string):Destination MAC in HHHH.HHHH.HHHH format. The
                    value is required only when the dst is 'host'
                dst_mac_addr_mask(string): Mask for the destination MAC in
                    HHHH.HHHH.HHHH format.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'dst' not in kwargs or not kwargs['dst']:
            raise ValueError("Missing \'dst\' in kwargs")

        dst = kwargs['dst']
        dst = ' '.join(dst.split())

        ret = {"dst": None, "dsthost": None, "dst_mac_addr_mask": None}

        if dst == "any":
            ret['dst'] = "any"
            return ret

        if dst == "host":
            if 'dsthost' not in kwargs or not kwargs['dsthost']:
                raise ValueError("Missing \'dsthost\' in kwargs")

            dsthost = kwargs['dsthost']
            dsthost = ' '.join(dsthost.split())

            utilities.validate_mac_address(dsthost)
            ret['dst'] = "host"
            ret['dsthost'] = dsthost
            return ret

        if 'dst_mac_addr_mask' not in kwargs or \
                not kwargs['dst_mac_addr_mask']:
            raise ValueError("Missing \'dst_mac_addr_mask\' in kwargs")

        dst_mac_addr_mask = kwargs['dst_mac_addr_mask']
        dst_mac_addr_mask = ' '.join(dst_mac_addr_mask.split())

        utilities.validate_mac_address(dst)
        utilities.validate_mac_address(dst_mac_addr_mask)
        ret['dst'] = dst
        ret['mask'] = dst_mac_addr_mask
        return ret

    def parse_ethertype(self, **kwargs):
        """
        parse the ethertype param
        Args:
            kwargs contains:
                ethertype(string): EtherType, can be 'arp', 'fcoe', 'ipv4' or
                    custom value between 1536 and 65535.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'ethertype' not in kwargs or not kwargs['ethertype']:
            return None

        ethertype = kwargs['ethertype']

        if ethertype in ['arp', 'fcoe', 'ipv4']:
            return ethertype

        if ethertype.isdigit():
            if int(ethertype) >= 1536 or int(ethertype) <= 65535:
                return ethertype

        raise ValueError("The ethertype value {} is invalid."
                         " Specify Integer or \'arp\', " "\'fcoe\', \'ipv4\'"
                         .format(ethertype))

    def parse_slx_ethertype(self, **kwargs):
        """
        parse the ethertype param
        Args:
            kwargs contains:
                ethertype(string): EtherType, can be 'arp', 'fcoe', 'ipv4' or
                    custom value between 1536 and 65535.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'ethertype' not in kwargs or not kwargs['ethertype']:
            return None

        ethertype = kwargs['ethertype']

        if ethertype in ['arp', 'fcoe', 'ipv4', 'ipv6']:
            return ethertype

        if ethertype.isdigit():
            if int(ethertype) >= 1536 or int(ethertype) <= 65535:
                return ethertype

        raise ValueError("The ethertype value {} is invalid."
                         " Specify Integer or \'arp\', " "\'fcoe\', \'ipv4\'"
                         " \'ipv6\'".format(ethertype))

    def parse_vlan_id(self, vlan):

        if vlan == "any":
            return vlan

        if vlan.isdigit():
            if int(vlan) >= 1 and int(vlan) <= 4095:
                return str(vlan)

        raise ValueError("Invalid \'vlan\' {} in kwargs"
                         .format(vlan))

    def parse_single_tagged_vlan(self, ret, **kwargs):
        vlan = kwargs['vlan']

        val = vlan.split()
        len_val = len(val)

        if len_val == 1:
            ret['vlan_id'] = self.parse_vlan_id(val[0])
            return ret

        if len_val == 2:
            ret['vlan_id'] = self.parse_vlan_id(val[0])
            if ret['vlan_id'] == "any":
                raise ValueError("Invalid mask for vlan = any")
            if re.match("^0x([0-9a-fA-F]{3})$", val[1]):
                ret['mask'] = str(val[1])
                return ret

        raise ValueError("Invalid \'vlan\' {} in kwargs"
                         .format(vlan))

    def parse_double_tagged_vlan(self, ret, **kwargs):
        vlan = kwargs['vlan']

        val = vlan.split()
        len_val = len(val)

        if len_val == 2:  # outer and inner
            ret['outervlan'] = self.parse_vlan_id(val[0])
            ret['innervlan'] = self.parse_vlan_id(val[1])
            return ret

        if len_val == 3:  # (outer+mask & inner) or (outer & inner+mask)
            ret['outervlan'] = self.parse_vlan_id(val[0])

            if re.match("^0x([0-9a-fA-F]{3})$", val[1]):
                if ret['outervlan'] == "any":
                    raise ValueError("Invalid mask for outervlan = any")
                ret['outermask'] = val[1]
                ret['innervlan'] = self.parse_vlan_id(val[2])
                return ret
            else:
                ret['innervlan'] = self.parse_vlan_id(val[1])
                if re.match("^0x([0-9a-fA-F]{3})$", val[2]):
                    if ret['innervlan'] == "any":
                        raise ValueError("Invalid mask for innervlan = any")
                    ret['innermask'] = val[2]
                    return ret

        if len_val == 4:  # outer+mask & inner+mask
            ret['outervlan'] = self.parse_vlan_id(val[0])
            if re.match("^0x([0-9a-fA-F]{3})$", val[1]):
                if ret['outervlan'] == "any":
                    raise ValueError("Invalid mask for outervlan = any")
                ret['outermask'] = val[1]

            ret['innervlan'] = self.parse_vlan_id(val[2])
            if re.match("^0x([0-9a-fA-F]{3})$", val[3]):
                if ret['innervlan'] == "any":
                    raise ValueError("Invalid mask for innervlan = any")
                ret['innermask'] = val[3]
                return ret

        raise ValueError("Invalid \'vlan\' {} in kwargs"
                         .format(vlan))

    def parse_vlan(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                vlan(integer): VLAN interface to which the ACL is bound
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        vlan_tag_format = None
        if 'vlan_tag_format' in kwargs and kwargs['vlan_tag_format']:
            vlan_tag_format = kwargs['vlan_tag_format'].lower()
            vlan_tag_format = ' '.join(vlan_tag_format.split()).lower()

        if 'vlan' not in kwargs or not kwargs['vlan']:
            return None

        ret = {'vlan_id': None,
               'mask': None,
               'outervlan': None,
               'outermask': None,
               'innervlan': None,
               'innermask': None}

        if not vlan_tag_format:
            ret['vlan_id'] = self.parse_vlan_id(kwargs['vlan'])
            return ret

        if vlan_tag_format == 'untagged':
            self.parse_single_tagged_vlan(ret, **kwargs)
            return ret

        if vlan_tag_format == 'single-tagged':
            self.parse_single_tagged_vlan(ret, **kwargs)
            return ret

        if vlan_tag_format == 'double-tagged':
            self.parse_double_tagged_vlan(ret, **kwargs)
            return ret

        raise ValueError("Invalid \'vlan_tag_format\' {} in kwargs"
                         .format(vlan_tag_format))

    def parse_vlan_tag_format(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                vlan(integer): VLAN interface to which the ACL is bound
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        if 'vlan_tag_format' not in kwargs or not kwargs['vlan_tag_format']:
            return None

        vlan_tag_format = kwargs['vlan_tag_format'].lower()
        vlan_tag_format = ' '.join(vlan_tag_format.split())

        if vlan_tag_format in ['untagged', 'single-tagged', 'double-tagged']:
            return vlan_tag_format

        raise ValueError("Invalid \'vlan_tag_format\' {} in kwargs"
                         .format(vlan_tag_format))

    def parse_pcp(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                pcp(string): Matches the specified value against the pcp
                    value of the packet to filter. Allowed 0 to 7.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'pcp' not in kwargs or not kwargs['pcp']:
            return None

        pcp = kwargs['pcp']
        pcp = ' '.join(pcp.split())

        pcp = pcp.split(',')[0]

        if pcp.isdigit():
            if int(pcp) >= 0 and int(pcp) <= 7:
                return pcp

        raise ValueError("Invalid \'pcp\' {} in kwargs"
                         .format(pcp))

    def parse_pcp_force(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                pcp(string): Matches the specified value against the pcp
                    value of the packet to filter. Allowed 0 to 7.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'pcp' not in kwargs or not kwargs['pcp']:
            return None

        pcp = kwargs['pcp']
        pcp = ' '.join(pcp.split())

        pcp = pcp.split(',')
        if len(pcp) == 2:
            pcp = pcp[1]
        else:
            return None

        if pcp.isdigit():
            if int(pcp) >= 0 and int(pcp) <= 7:
                return pcp

        raise ValueError("Invalid \'pcp\' {} in kwargs"
                         .format(pcp))

    def parse_drop_precedence_force(self, **kwargs):
        """
        parse the drop_precedence_force mapping param.
        Args:
            kwargs contains:
                drop_precedence_force(string):
                    drop_precedence_force value of the packet
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence_force' not in kwargs or \
                not kwargs['drop_precedence_force']:
            return None

        drop_precedence_force = kwargs['drop_precedence_force']
        drop_precedence_force = ' '.join(drop_precedence_force.split())

        if drop_precedence_force.isdigit():
            if int(drop_precedence_force) >= 0 and \
                    int(drop_precedence_force) <= 3:
                return 'drop-precedence-force ' + drop_precedence_force

        raise ValueError("drop-precedence-force value should be 0 - 3")

    def parse_arp_guard(self, **kwargs):
        """
        parse the arp_guard mapping param.
        Args:
            kwargs contains:
                arp_guard(string):
                    arp_guard value of the packet
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'arp_guard' not in kwargs or \
                not kwargs['arp_guard']:
            return None

        arp_guard = kwargs['arp_guard']
        arp_guard = ' '.join(arp_guard.split())

        if arp_guard.lower() != 'true':
            return None

        if 'ethertype' not in kwargs or not kwargs['ethertype']:
            raise ValueError("arp_guard is allowed only ethertype arp or 2054")

        ethertype = kwargs['ethertype']
        if ethertype == 'arp':
            return True

        if ethertype.isdigit() and int(ethertype) == 2054:
            return True

        raise ValueError("arp_guard is allowed only ethertype arp or 2054")
