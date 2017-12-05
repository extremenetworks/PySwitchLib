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

        if 'vlan' not in kwargs or not kwargs['vlan']:
            raise ValueError("vlan is required parameter to configure"
                             " ethertype")

        ethertype = kwargs['ethertype']

        if ethertype in ['arp', 'fcoe', 'ipv4']:
            return ethertype

        if ethertype.isdigit():
            if int(ethertype) >= 1536 or int(ethertype) <= 65535:
                return ethertype

        raise ValueError("The ethertype value {} is invalid."
                         " Specify Integer or \'arp\', " "\'fcoe\', \'ipv4\'"
                         .format(ethertype))

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
        if 'vlan' not in kwargs or not kwargs['vlan']:
            return None

        vlan = kwargs['vlan']

        if int(vlan) >= 1 and int(vlan) <= 4095:
            return str(vlan)

        raise ValueError("Invalid \'vlan\' {} in kwargs"
                         .format(vlan))
