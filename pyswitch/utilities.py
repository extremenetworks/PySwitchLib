#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Systems, Inc.

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
from jsonpath_rw import parse
from ipaddress import ip_interface


def find(data, expr):
    x = parse(expr).find(data)
    if len(x) > 0:
        return x[0].value
    return None


def findText(data, expr):
    x = find(data, expr)
    return x if x else ''


def findlist(data, expr):
    x = find(data, expr)
    if isinstance(x, list):
        return x
    else:
        y = []
        if x:
            y.append(x)
        return y


def findall(data, expr):
    return [match.value for match in parse(expr).find(data)]


class RestInterfaceError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidBgpArgs(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def get_bgp_api(api=None, vrf='default', n_addr=None, rbridge_id=1,
                os='nos', afi=None, feature='', op='_update',
                resource_depth=1, evpn_n_addr=None, args=None):
    if not args:
        args = dict()
    if os is 'nos':
        args['rbridge_id'] = rbridge_id
        bgp_api = "rbridge_id_router_bgp{afi}{vrf}{feature}{op}"
    else:
        bgp_api = "router_bgp{afi}{vrf}{feature}{op}"

    afi4 = "_address_family_ipv4_unicast"
    afi6 = "_address_family_ipv6_unicast"
    afil = "_address_family_l2vpn_evpn"
    if op is '_get':
        args['resource_depth'] = resource_depth
    if afi and afi == 'ipv4':
        if vrf != 'default':
            if n_addr:
                args['af_ipv4_neighbor_addr'] = n_addr
            args['af_vrf'] = vrf
            bgp_api = bgp_api.format(
                afi=afi4, vrf="_vrf", feature=feature, op=op)
        else:
            if n_addr:
                args['af_ipv4_neighbor_address'] = n_addr
            bgp_api = bgp_api.format(afi=afi4, vrf="", feature=feature, op=op)
    elif afi and afi == 'ipv6':
        if vrf != 'default':
            if n_addr:
                args['af_ipv6_neighbor_addr'] = n_addr
            args['af_ipv6_vrf'] = vrf
            bgp_api = bgp_api.format(
                afi=afi6, vrf="_vrf", feature=feature, op=op)
        else:
            if n_addr:
                args['af_ipv6_neighbor_address'] = n_addr
            bgp_api = bgp_api.format(afi=afi6, vrf="", feature=feature, op=op)
    elif afi and afi == 'l2vpn':
        if n_addr:
            args['neighbor_addr'] = n_addr
        if evpn_n_addr:
            args['evpn_neighbor_ipv4'] = evpn_n_addr
        bgp_api = bgp_api.format(afi=afil, vrf="", feature=feature, op=op)
    elif not afi:
        if n_addr:
            # HACK please come up with a better way.
            if afi4 in feature:
                args['af_ipv4_neighbor_address'] = n_addr
            elif afi6 in feature:
                args['af_ipv6_neighbor_address'] = n_addr
            else:
                if ':' in n_addr:
                    args['neighbor_ipv6_addr'] = n_addr
                else:
                    args['neighbor_addr'] = n_addr
        if evpn_n_addr:
            ip_addr = ip_interface(unicode(evpn_n_addr))
            if ip_addr.version == 4:
                args['evpn_neighbor_ipv4'] = evpn_n_addr
            else:
                args['evpn_neighbor_ipv6'] = evpn_n_addr
        bgp_api = bgp_api.format(afi='', vrf='', feature=feature, op=op)
    if api and vrf == 'default':
        return (api, args)
    return (bgp_api, args)


def valid_vlan_id(vlan_id, extended=True):
    """Validates a VLAN ID.

    Args:
        vlan_id (integer): VLAN ID to validate.  If passed as ``str``, it will
            be cast to ``int``.
        extended (bool): If the VLAN ID range should be considered extended
            for Virtual Fabrics.

    Returns:
        bool: ``True`` if it is a valid VLAN ID.  ``False`` if not.

    Raises:
        None

    Examples:
        >>> import pyswitch.utilities
        >>> vlan = '565'
        >>> pyswitch.utilities.valid_vlan_id(vlan)
        True
        >>> extended = False
        >>> vlan = '6789'
        >>> pyswitch.os.base.utilities.valid_vlan_id(vlan, extended=extended)
        False
        >>> pyswitch.os.base.utilities.valid_vlan_id(vlan)
        True
    """
    minimum_vlan_id = 1
    maximum_vlan_id = 4095
    if extended:
        maximum_vlan_id = 8191
    return minimum_vlan_id <= int(vlan_id) <= maximum_vlan_id


def valid_interface(int_type, name):
    """Validates an interface type and name.

    Args:
        int_type (str): Interface type.  Examples: `gigabitethernet`,
            `tengigabitethernet`, `port_channel`.
        name (str): Port designator.  Examples: `225/0/1`, `1/0/1`, `1`.

    Returns:
        bool: ``True`` if it is a valid interface.  ``False`` if not.

    Raises:
        None

    Examples:
        >>> import pyswitch.utilities
        >>> int_type = 'tengigabitethernet'
        >>> name = '225/0/1'
        >>> pyswitch.utilities.valid_interface(int_type, name)
        True
        >>> name = '5/0'
        >>> pyswitch.os.base.utilities.valid_interface(int_type, name)
        False
        >>> int_type = 'port_channel'
        >>> name = '1'
        >>> pyswitch.os.base.utilities.valid_interface(int_type, name)
        True
        >>> int_type = 'port_channel'
        >>> name = '1/0'
        >>> pyswitch.os.base.utilities.valid_interface(int_type, name)
        False
    """

    if int_type == 'port_channel':
        return valid_port_channel_name(name)
    if int_type == 've':
        return valid_vlan_id(name)
    else:
        return valid_physical_name(name, int_type)


def valid_port_channel_name(name):
    """Validates a Port-Channel.

    Do not use this method directly.  Use ``valid_interface`` instead.

    Args:
        name (str): Port designator.  Examples: `1`, `768`, `3476`.

    Returns:
        bool: ``True`` if it is a valid port-channel.  ``False`` if not.

    Raises:
        None
    """
    return re.search(r'^[0-9]{1,4}$', name) is not None


def valid_physical_name(name, type):
    """Validates a physical interface.

    Do not use this method directly.  Use ``valid_interface`` instead.

    Args:
        name (str): Port designator.  Examples: `225/0/1`, `1/0/1`.

    Returns:
        bool: ``True`` if it is a valid physical interface.  ``False`` if not.

    Raises:
        None
    """
    if type == 'ethernet':
        pattern = r'^[0-9]{1,3}/[0-9]{1,3}(:[1-4])?$'
    else:
        pattern = r'^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}(:[1-4])?$'
    return re.search(pattern, name) is not None
