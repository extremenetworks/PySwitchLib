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
import socket
import ipaddress
import pyswitch.utilities
import xml.etree.ElementTree as ElementTree
from xml.etree.ElementTree import Element

from ipaddress import ip_interface
from jsonpath_rw import parse
import itertools


class Util(object):
    def __init__(self, data):
        if isinstance(data, Element):
            for child in data.getiterator():
                child.tag = child.tag.split('}', 1)[1]
            self.root = data
        elif data != '':
            self.root = ElementTree.fromstring(data)
        else:
            self.root = Element('empty')

    def find(self, node, expr):
        x = node.find(expr)
        if x is not None:
            return x.text
        return None

    def find_with_ns(self, node, expr_with_name_space):
        x = node.find(expr_with_name_space)
        if x is not None:
            return x.text
        return None

    def findNode(self, node, expr):
        return node.find(expr)

    def findlist(self, node, expr):
        return node.findall(expr)

    def findText(self, data, expr):
        x = self.find(data, expr)
        return x if x else ''

    def findall(self, data, expr):
        return [match.text for match in data.findall(expr)]


def get_two_tuple_version(fullver):
    ver_tuple = fullver.split('.')
    return '%s.%s' % (ver_tuple[0], ver_tuple[1])


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
    if int_type == 'vlan':
        return re.search(r'^[0-9]{1,4}$', name) is not None
    if int_type == 'management':
        return re.search(r'^[0-9]$', name) is not None
    if int_type == 'loopback':
        return valid_lopback_number(name)
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


def valid_lopback_number(loopback_number):
    """Validates a VLAN ID.

    Args:
        loopback_number (integer): Loopback port number to validate.
            If passed as ``str``, it will be cast to ``int``.
    Returns:
        bool: ``True`` if it is a valid loopback_number.  ``False`` if not.

    Raises:
        None

    Examples:
        >>> import pyswitch.utilities
        >>> loopback_number = '2'
        >>> pyswitch.utilities.valid_lopback_number(loopback_number)
        True
        >>> extended = False
        >>> vlan = '256'
        >>> pyswitch.os.base.utilities.valid_lopback_number(loopback_number)
    """
    minimum_loopback_id = 1
    maximum_loopback_id = 255
    return minimum_loopback_id <= int(loopback_number) <= maximum_loopback_id


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


def get_vlan_list(vlan_id):
    """ Expand the vlan_id values into a list """
    vlan_list = []
    vlanlist = vlan_id.split(',')
    for val in vlanlist:
        temp = expand_vlan_range(vlan_id=val)
        if temp is None:
            raise ValueError('Reserved/Control/Invalid vlans passed in args `vlan_id`')

        vlan_list.append(temp)

    vlan_list = list(itertools.chain.from_iterable(vlan_list))
    return vlan_list


def expand_vlan_range(vlan_id):
    """Fail the task if vlan id is zero or one or above 4096 .
    """

    re_pattern1 = r"^(\d+)$"
    re_pattern2 = r"^(\d+)\-?(\d+)$"
    re_pattern3 = r"^(\d+)\,?(\d+)$"

    if re.search(re_pattern1, vlan_id):
        try:
            vlan_id = (int(vlan_id),)
        except ValueError:
            return None
    elif re.search(re_pattern2, vlan_id):
        try:
            vlan_id = re.match(re_pattern2, vlan_id)
        except ValueError:
            return None

        vlan_id = range(int(vlan_id.groups()[0]), int(
            vlan_id.groups()[1]) + 1)
    elif re.search(re_pattern3, vlan_id):
        vlan_id = vlan_id.split(",")
    else:
        return None

    for vid in vlan_id:
        if vid > 4096:
            extended = "true"
        else:
            extended = "false"

        tmp_vlan_id = valid_vlan_id(vid, extended=extended)
        if not tmp_vlan_id:
            return None

    return vlan_id


def check_mlx_cli_set_error(cli_res):
    """
       check whether any error or invalid input during cli-set operation
    """
    error = re.search(r'(E|e)rror(.+)', cli_res)
    invalid_input = re.search(r'Invalid input', cli_res)
    if error:
        raise ValueError("%s" % error.group(0))
    if invalid_input:
        raise ValueError("%s" % invalid_input.group(0))
    return True


def is_valid_ip_network(addr):
    """
    Checks whether address represents a valid IPv4 or IPv6 address,
    or the network doesn't have host bits set.
    (example 'addr': '192.168.0.0/28' or '2001:db8::/46')
    """
    try:
        ipaddress.ip_network(addr)
        return True
    except socket.error:
        return False


def is_valid_mac_address(mac):
    """
    This will only validate the HHHH.HHHH.HHHH MAC format.
    """
    if re.match('[0-9A-Fa-f]{4}[.][0-9A-Fa-f]{4}[.][0-9A-Fa-f]{4}$', mac):
        return True
    else:
        return False


def is_valid_ip_address(addr, address_type):
    """
    This will only validate the IPv4 and IPv6 addresses.
    """
    try:
        if address_type == 'ipv6':
            socket.inet_pton(socket.AF_INET6, addr)
        else:
            socket.inet_pton(socket.AF_INET, addr)
        return True
    except socket.error:
        return False


def extend_interface_range(intf_type, intf_name, logger=None):
    msg = None
    int_list = intf_name
    re_pattern1 = r"^(\d+)\-?(\d+)$"
    re_pattern2 = r"^(\d+)\/(\d+)\-?(\d+)$"
    re_pattern3 = r"^(\d+)\/(\d+)\/(\d+)\-?(\d+)$"

    if re.search(re_pattern1, int_list):
        try:
            int_list = re.match(re_pattern1, int_list)
        except Exception:
            return None

        if logger and int(int_list.groups()[0]) == int(int_list.groups()[1]):
            logger.info("Use range command only for unique values")
        int_list = range(int(int_list.groups()[0]), int(
            int_list.groups()[1]) + 1)

    elif re.search(re_pattern2, int_list):
        try:
            temp_list = re.match(re_pattern2, int_list)
        except Exception:
            return None

        if logger and int(temp_list.groups()[1]) == int(temp_list.groups()[2]):
            logger.info("Use range command only for unique values")
        intList = range(int(temp_list.groups()[1]), int(
            temp_list.groups()[2]) + 1)
        int_list = []
        for intf in intList:
            int_list.append(temp_list.groups()[0] + '/' + str(intf))
        int_list = int_list

    elif re.search(re_pattern3, int_list):
        try:
            temp_list = re.match(re_pattern3, int_list)
        except Exception:
            return None

        if logger and int(temp_list.groups()[2]) == int(temp_list.groups()[3]):
            logger.info("Use range command only for unique values")
        intList = range(int(temp_list.groups()[2]), int(
            temp_list.groups()[3]) + 1)
        int_list = []
        for intf in intList:
            int_list.append(temp_list.groups()[0] + '/' + temp_list.groups()[1] + '/' +
                            str(intf))
        int_list = int_list
    else:
        msg = 'Invalid interface format'

    if msg is not None:
        if logger:
            logger.error(msg)
        return None

    return int_list


def validate_interface(intf_type, intf_name, rbridge_id=None, os_type=None, logger=None):
    msg = None
    # int_list = intf_name
    re_pattern1 = r"^(\d+)$"
    re_pattern2 = r"^(\d+)\/(\d+)\/(\d+)(:(\d+))?$"
    re_pattern3 = r"^(\d+)\/(\d+)(:(\d+))?$"
    intTypes = ["port_channel", "gigabitethernet", "tengigabitethernet",
                "fortygigabitethernet", "hundredgigabitethernet", "ethernet"]
    NosIntTypes = [
        "gigabitethernet",
        "tengigabitethernet",
        "fortygigabitethernet"]
    if os_type is None or os_type == "nos":
        if rbridge_id is None and 'loopback' in intf_type:
            msg = 'Must specify `rbridge_id` when specifying a `loopback`'
        elif rbridge_id is None and 've' in intf_type:
            msg = 'Must specify `rbridge_id` when specifying a `ve`'
        elif rbridge_id is not None and intf_type in intTypes:
            msg = 'Should not specify `rbridge_id` when specifying a ' + intf_type
        elif re.search(re_pattern1, intf_name):
            intf = intf_name
        elif re.search(re_pattern2, intf_name) and intf_type in NosIntTypes:
            intf = intf_name
        elif re.search(re_pattern3, intf_name) and 'ethernet' in intf_type:
            intf = intf_name
        else:
            msg = 'Invalid interface format'
    elif os_type == "slxos":
        if re.search(re_pattern1, intf_name):
            intf = intf_name
        elif re.search(re_pattern2, intf_name) and intf_type in NosIntTypes:
            intf = intf_name
        elif re.search(re_pattern3, intf_name) and 'ethernet' in intf_type:
            intf = intf_name
        else:
            msg = 'Invalid interface format'

    if msg is not None:
        if logger:
            logger.error(msg)
        return False

    intTypes = ["ve", "loopback", "ethernet"]
    if intf_type not in intTypes:
        tmp_vlan_id = pyswitch.utilities.valid_interface(
            intf_type, name=str(intf))

        if not tmp_vlan_id:
            if logger:
                logger.error(
                    "Not a valid interface type %s or name %s", intf_type, intf)
            return False

    return True


def convert_mac_colon_to_dot_format(mac_addr):
    """
    Convert mac address in colon format to dot format
    For e.g convert aa:bb:cc:dd:ee:ff to aabb.ccdd.eeff

    Args(str):
        mac address in colon format

    Returns(str):
        mac address in dot format

    """
    mac = mac_addr.split(":")
    mac_addr_dot = "".join(mac[0:2]) + "." + "".join(mac[2:4]) + "." + "".join(mac[4:6])
    return mac_addr_dot


def _validate_parameters(mandatory_params, supported_params, parameters):

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_mandatory = list(set(mandatory_params) - set(received_params))
    if len(absent_mandatory) > 0:
        raise ValueError("mandatory parameters missing: {}"
                         .format(absent_mandatory))

    unsupported_params = list(set(received_params) - set(supported_params))
    if len(unsupported_params) > 0:
        raise ValueError("unsupported parameters provided: {}"
                         .format(unsupported_params))


def validate_ip_address(addr, address_type):
    """
    This will only validate the IPv4 and IPv6 addresses.
    """
    addr = ' '.join(addr.split())
    try:
        if address_type == 'ipv6':
            socket.inet_pton(socket.AF_INET6, addr)
        else:
            socket.inet_pton(socket.AF_INET, addr)
        return True
    except socket.error:
        raise ValueError("Invalid {} address: {}"
                         .format(address_type, addr))


def validate_mac_address(mac):
    """
    This will only validate the HHHH.HHHH.HHHH MAC format.
    """
    if re.match('[0-9A-Fa-f]{4}[.][0-9A-Fa-f]{4}[.][0-9A-Fa-f]{4}$', mac):
        return True
    else:
        raise ValueError("Invalid MAC {}".format(mac))


def validate_port_channel_id(plat_type, po_id):
    """
    This will check if the user entered port-channel id is
    within the supported range of each platform

    Args:
        plat_type: Like MLX4, CES2048F, BR-VDX6740, etc
        po_id: port channel id

    Returns:
        True/False, reason for failure

    """
    min_lag = 0
    max_lag = 0
    if plat_type == 'MLX4' or plat_type == 'MLX8' or \
       plat_type == 'MLX16' or plat_type == 'MLX32' or \
       plat_type == 'MLXXMR4' or plat_type == 'MLXXMR8' or \
       plat_type == 'MLXXMR16' or plat_type == 'MLXXMR32':
        min_lag = 1
        max_lag = 256
    elif plat_type == 'CES2024F' or plat_type == 'CES2024C' or \
            plat_type == 'CES2048F' or plat_type == 'CES2048C' or \
            plat_type == 'CES2048FX' or plat_type == 'CES2048CX' or \
            plat_type == 'CES2024F4X' or plat_type == 'CES2024C4X' or \
            plat_type == 'CER2024F' or plat_type == 'CER2024C' or \
            plat_type == 'CER2048F' or plat_type == 'CER2048C' or \
            plat_type == 'CER2048FX' or plat_type == 'CER2048CX' or \
            plat_type == 'CER2024F4X' or plat_type == 'CER2024C4X':
        min_lag = 1
        max_lag = 64
    elif plat_type == 'BR-VDX6740' or plat_type == 'VDX6740T-1G' or \
            plat_type == 'BR-VDX8770-4' or plat_type == 'BR-VDX8770-8' or \
            plat_type == 'BR-VDX6940-144S' or plat_type == 'BR-VDX6740T' or \
            plat_type == 'BR-VDX6940-36Q':
        min_lag = 1
        max_lag = 6144
    elif plat_type == 'BR-SLX9240' or plat_type == 'BR-SLX9140':
        min_lag = 1
        max_lag = 1024
    elif plat_type == 'BR-SLX9540':
        min_lag = 1
        max_lag = 64
    elif plat_type == 'BR-SLX9850-8' or plat_type == 'BR-SLX9850-4':
        min_lag = 1
        max_lag = 512
    else:
        return False, "Not a valid/supported platform type"
    if int(po_id) < min_lag or int(po_id) > max_lag:
        reason = "Invalid Port-channel id should be between " + str(min_lag) +\
            " and " + str(max_lag)
        return False, reason
    return True, "Success"
