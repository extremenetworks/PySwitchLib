"""
import pyswitch.utilities
from pyswitch.exceptions import InvalidVlanId
"""

import re

from pyswitch.snmp.base.interface import Interface as BaseInterface
from pyswitch.snmp.SnmpMib import SnmpMib as SnmpMib
from pyswitch.snmp.mlx.SnmpMLXMib import SnmpMLXMib as SnmpMLXMib
from hnmp import mac_address

# from pyswitch.utilities import Util


class Interface(BaseInterface):
    """
      The Interface class holds all the actions associated with the Interfaces
      of a MLX device.

      Attributes:
          None
      """

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
        super(Interface, self).__init__(callback)

    @property
    def valid_int_types(self):

        return [
            'ethernet',
            'port_channel',
            'loopback',
            've'
        ]

    @property
    def valid_intp_types(self):
        return [
            'ethernet'

        ]

    @property
    def l2_mtu_const(self):
        # TBD change below defaults
        minimum_mtu = 1548
        maximum_mtu = 9216
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_mtu_const(self):
        # TBD change below defaults
        minimum_mtu = 1300
        maximum_mtu = 9194
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_ipv6_mtu_const(self):
        # TBD change below defaults
        minimum_mtu = 1300
        maximum_mtu = 9194
        return (minimum_mtu, maximum_mtu)

    @property
    def has_rbridge_id(self):
        return False

    def fabric_isl(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def fabric_trunk(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def ip_anycast_gateway(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def add_vlan_int(self, vlan_id_list, desc=None):
        """
        Add VLAN Interface. VLAN interfaces are required for VLANs even when
        not wanting to use the interface for any L3 features.

        Args:
            vlan_id_list: List of VLAN interface being created. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        try:
            cli_arr = []
            for vlan in vlan_id_list:
                cli_arr.append('vlan' + " " + str(vlan) + " " + 'name' + " " + desc)
            self._callback(cli_arr, handler='cli-set')
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to create VLAN due to %s', reason)

    def create_port_channel(self, ports, int_type, portchannel_num, mode, desc=None):
        """create port channel

        args:
            int_type (str): type of interface. (ethernet, , etc)
            ports(list): port numbers (1/1, 2/1 etc)
            portchannel_num (int): port-channel number (1, 2, 3, etc).
            mode (str): mode of port-channel (static, dynamic)
            desc: name of port-channel

        returns:
            return True for success and False for failure.

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.
        """
        try:
            cli_arr = []
            if desc is None:
                raise ValueError('Port channel description is NULL for PO %d', portchannel_num)
            if len(desc) < 1 or len(desc) > 64:
                raise ValueError('Port-channel name should be 1-64 characters')
            # Check if a port-channel exists with same id TBD in action
            cli_arr.append('lag' + " " + desc + " " + str(mode) + " " + 'id' +
                    " " + str(portchannel_num))
            # Add ports to port-channel
            port_list = []
            for port in ports:
                port_list.append(int_type + " " + port)
            port_list_str = " ".join(port_list)
            cli_arr.append('ports' + " " + port_list_str)
            # select primary port
            cli_arr.append('primary-port' + " " + ports[0])
            # deploy the port channel
            cli_arr.append('deploy')
            # Enable the member ports
            cli_arr.append('enable' + " " + port_list_str)
            self._callback(cli_arr, handler='cli-set')
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to create Port-channel due to %s', reason)

    def remove_port_channel(self, portchannel_num):
        """delete port channel

        args:
            portchannel_num (int): port-channel number (1, 2, 3, etc).

        returns:
            return True for success and False for failure.

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.
        """
        try:
            # To delete the LAG, first disable member ports
            # get the member ports of LAG
            cli_arr = []
            cli_arr = 'show running-config' + " " + 'lag' + " " + "id" + " " + str(portchannel_num)
            output = self._callback(cli_arr, handler='cli-get')
            for item in output.split("\n"):
                if "lag" in item:
                    lag_str = item
                if "ports" in item:
                    disable_ports = item[7:]
                    break
            lag_str_list = lag_str.split()
            cli_arr = []
            cli_arr.append('lag' + " " + lag_str_list[1])
            cli_arr.append('disable' + " " + disable_ports)
            cli_arr.append('no' + " " + 'lag' + " " + lag_str_list[1])
            self._callback(cli_arr, handler='cli-set')
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to delete Port-channel due to %s', reason)

    @property
    def port_channels(self):
        """
        list[dict]: A list of dictionary items of port channels.
        Args:

        returns:
            returns a list of dictionary items of all port channels including member ports

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.
        """
        # Get the list of port-channels
        cli_arr = []
        cli_arr = 'show running-config' + " " + 'lag'
        po_list = []
        output = self._callback(cli_arr, handler='cli-get')
        member_ports_str_list = []
        for item in output.split("\n"):
            if "lag" in item:
                lag_str_list = item.split()
                # store (lag name, type)
                po_list.append((lag_str_list[1], lag_str_list[2], lag_str_list[4]))
            if "ports" in item:
                member_ports_str = item[7:]
                member_ports_str_list.append((lag_str_list[1], member_ports_str))
        # Retrieve the elements for each LAG
        ifname_list = []
        for po in po_list:
            # print po[1], po[2], po[0]
            ifname_list.append("LAG" + str(po[2]))
        # Get ifindex for LAGxx where xx is PO id
        ifname_index_map = self.get_interface_name_id_mapping(ifname_list)
        result = []
        # For each PO collect the information.
        for po in po_list:
            interface_list = []
            lag_ifindex = ifname_index_map[str("LAG" + str(po[2]))]
            aggregator_id = po[2]
            aggregator_type = 'standard'
            is_vlag = False
            aggregator_mode = po[1]
            if aggregator_mode == 'dynamic':
                sys_priority_oid = SnmpMib.mib_oid_map['dot3adAggActorSystemPriority'] \
                    + "." + str(lag_ifindex)
                system_priority = self._callback(sys_priority_oid, handler='snmp-get')
                actor_sys_id_oid = SnmpMib.mib_oid_map['dot3adAggActorSystemID'] + "." + lag_ifindex
                actor_system_id = mac_address(self._callback(actor_sys_id_oid, handler='snmp-get'))
                partner_sys_pri_oid = SnmpMib.mib_oid_map['dot3adAggPartnerSystemPriority'] + \
                    "." + lag_ifindex
                partner_oper_priority = self._callback(partner_sys_pri_oid, handler='snmp-get')
                partner_sys_id_oid = SnmpMib.mib_oid_map['dot3adAggPartnerSystemID'] + "." + \
                    lag_ifindex
                partner_system_id = mac_address(self._callback(partner_sys_id_oid,
                                            handler='snmp-get'))
                admin_key_oid = SnmpMib.mib_oid_map['dot3adAggActorAdminKey'] + "." + lag_ifindex
                admin_key = self._callback(admin_key_oid, handler='snmp-get')

                oper_key_oid = SnmpMib.mib_oid_map['dot3adAggActorOperKey'] + "." + lag_ifindex
                oper_key = self._callback(oper_key_oid, handler='snmp-get')
                partner_oper_key_oid = SnmpMib.mib_oid_map['dot3adAggPartnerOperKey'] + "." + \
                    lag_ifindex
                partner_oper_key = self._callback(partner_oper_key_oid, handler='snmp-get')
            else:
                system_priority = ''
                actor_system_id = ''
                partner_oper_priority = ''
                partner_system_id = ''
                admin_key = ''
                oper_key = ''
                partner_oper_key = ''
            rx_link_count = 0
            tx_link_count = 0
            individual_agg = 0
            ready_agg = 0

            # Get member port list of LAG using SNMP fdryLinkAggregationGroupIfList
            # TBD move below to another function
            lag_name = po[0]
            lag_name = re.sub('"', '', lag_name)
            ifid_name = {}
            ifid_name = self.get_port_channel_member_ports(lag_name)
            for item in ifid_name:
                rbridge_id = 0
                int_type = 'ethernet'
                int_name = ifid_name[item].strip('ethernet')
                actor_port = item  # TBD to confirm
                sync = 0  # TBD extract from CLI?
                port_channel_interface = {'rbridge-id': rbridge_id,
                                          'interface-type': int_type,
                                          'interface-name': int_name,
                                          'actor_port': actor_port,
                                          'sync': sync}
                interface_list.append(port_channel_interface)
            results = {'interface-name': lag_name,
                       'interfaces': interface_list,
                       'aggregator_id': aggregator_id,
                       'aggregator_type': aggregator_type,
                       'is_vlag': is_vlag,
                       'aggregator_mode': aggregator_mode,
                       'system_priority': system_priority,
                       'actor_system_id': actor_system_id,
                       'partner-oper-priority': partner_oper_priority,
                       'partner-system-id': partner_system_id,
                       'admin-key': admin_key,
                       'oper-key': oper_key,
                       'partner-oper-key': partner_oper_key,
                       'rx-link-count': rx_link_count,
                       'tx-link-count': tx_link_count,
                       'individual-agg': individual_agg,
                       'ready-agg': ready_agg}
            print "result", results
            result.append(results)
        return result

    def get_port_channel_member_ports(self, lag_name=None):
        """ Returns a map of port-channel member ports

        args:
            lag_name (str) - port-channel name/descr (for e.g po50)

        returns:
            return - dict containing port-channel member map (ifid: ifname)

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.
        """
        if lag_name is None:
                raise ValueError('Port-channel name is NULL')
        key_len = len(lag_name)
        if key_len < 1 or key_len > 64:
            raise ValueError('Port-channel name should be 1-64 characters')
        # Convert PO name to ASCII to construct the key to
        # fdryLinkAggregationGroupTable
        key_oid = [ord(c) for c in lag_name]
        lag_name_oid = ""
        for item in key_oid:
            lag_name_oid = lag_name_oid + "." + str(item)
        lag_grp_list_oid = SnmpMLXMib.mib_oid_map['fdryLinkAggregationGroupIfList'] + \
            "." + str(key_len) + str(lag_name_oid)
        lag_grp_list = self._callback(lag_grp_list_oid, handler='snmp-get')
        # member_ports is hexstring
        member_list = []
        member_list = [(ord(c)) for c in lag_grp_list]
        # Remove all 0's from list
        while 0 in member_list:
            member_list.remove(0)
        # Get the interface name/num for a given interface id
        ifid_name_map = {}
        ifid_name_map = self.get_interface_id_name_mapping(member_list)
        return ifid_name_map
