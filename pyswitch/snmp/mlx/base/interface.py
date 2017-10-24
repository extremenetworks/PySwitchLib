"""
import pyswitch.utilities
from pyswitch.exceptions import InvalidVlanId
"""

# import re

from pyswitch.snmp.base.interface import Interface as BaseInterface
from pyswitch.snmp.SnmpMib import SnmpMib as SnmpMib
import pyswitch.utilities
from pyswitch.exceptions import InvalidVlanId
import re
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
            desc (str): VLAN description

        Returns:
            True if command completes successfully or False if not.

        Raises:
            ValueError

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.85.107', '22')
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     vlan_list = [700,800, 900]
            ...     ret = dev.interface.add_vlan_int(vlan_list, 'vlan_name')
            ...     assert ret == True
        """
        try:
            cli_arr = []
            for vlan in vlan_id_list:
                self._callback(cli_arr, handler='cli-set')
                if desc is None:
                    cli_arr.append('vlan' + " " + str(vlan))
                else:
                    cli_arr.append('vlan' + " " + str(vlan) + " " + 'name' + " " + desc)
            self._callback(cli_arr, handler='cli-set')
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to create VLAN %s' % (reason))

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
        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.85.107', '22')
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     ports = ['2/1', '2/2']
            ...     output = dev.interface.create_port_channel(ports, 'ethernet',
            ...                         50, 'static', 'po50')
            ...     assert output == True
            ...     ifindex = dev.interface.get_port_channel_ifindex('po50')
            ...     assert len(str(ifindex)) >= 1
        """
        try:
            cli_arr = []
            if desc is None:
                raise ValueError('Port channel description is NULL for PO %d', portchannel_num)
            if len(desc) < 1 or len(desc) > 64:
                raise ValueError('Port-channel name should be 1-64 characters')
            if int(portchannel_num) < 1 or int(portchannel_num) > 256:
                raise ValueError('Port-channel id should be between 1 and 256')
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
            output = self._callback(cli_arr, handler='cli-set')
            for line in output.split('\n'):
                if 'Error' in line:
                    raise ValueError(str(line))
            return True
        except Exception as error:
            reason = str(error.message)
            raise ValueError("Failed to create Port-channel!! %s" % (reason))

    def remove_port_channel(self, port_int):
        """delete port channel

        args:
            port_int (str): port-channel number (1, 2, 3, etc).

        returns:
            return True for success and False for failure.

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.85.107', '22')
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     ports = ['2/1', '2/2']
            ...     output = dev.interface.create_port_channel(ports, 'ethernet',
            ...                         50, 'static', 'po50')
            ...     assert output == True
            ...     ifindex = dev.interface.get_port_channel_ifindex('po50')
            ...     assert len(str(ifindex)) >= 1
            ...     output = dev.interface.remove_port_channel(20)
            ...     assert output == True
        """
        try:
            lag_name = self.get_lag_id_name_map(str(port_int))
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
            rowstatus_oid = SnmpMLXMib.mib_oid_map['fdryLinkAggregationGroupRowStatus'] + \
                "." + str(key_len) + str(lag_name_oid)
            config = (rowstatus_oid, 6)
            ret_value = self._callback(config, handler='snmp-set')
            if ret_value:
                return True
            else:
                return False
        except Exception as error:
            reason = str(error.message)
            raise ValueError('Failed to delete Port-channel!! %s' % (reason))

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

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.85.107', '22')
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     ports = ['2/1', '2/2']
            ...     output = dev.interface.create_port_channel(ports, 'ethernet',
            ...                         50, 'static', 'po50')
            ...     assert output == True
            ...     result = dev.interface.port_channels
            ...     assert len(result) >= 1
        """
        # Get the list of port-channels
        po_list = []
        po_list = self.get_port_channel_list()
        # Retrieve the elements for each LAG
        result = []
        # For each PO collect the information.
        for po in po_list:
            interface_list = []
            lag_ifindex = str(self.get_port_channel_ifindex(str(po[0])))
            aggregator_id = self.get_port_channel_id(str(po[0]))
            deploy = po[3]
            aggregator_type = 'standard'
            is_vlag = False
            aggregator_mode = po[1]
            if aggregator_mode == 'dynamic' and deploy is True:
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
            lag_name = po[0]
            ifid_name = {}
            ifid_name = self.get_port_channel_member_ports(lag_name)
            for item in ifid_name:
                rbridge_id = 0
                int_type = 'ethernet'
                int_name = ifid_name[item].strip('ethernet')
                actor_port = item  # TBD to confirm
                sync = '0'
                if aggregator_mode == 'dynamic' and deploy is True:
                    port = self.get_lacp_member_info(lag_name, int_name)
                    if port['actor_agg'] is True and port['part_agg'] is True:
                        ready_agg = 1
                        if port['actor_coll'] is True and \
                           port['part_coll'] is True and \
                           port['actor_dist'] is True and \
                           port['part_dist'] is True:
                            sync = '1'
                    if int(port['tx_count']) > 0:
                        tx_link_count += 1
                    if int(port['rx_count']) > 0:
                        rx_link_count += 1

                port_channel_interface = {'rbridge-id': rbridge_id,
                                          'interface-type': int_type,
                                          'interface-name': int_name,
                                          'actor_port': actor_port,
                                          'sync': sync}
                interface_list.append(port_channel_interface)
            results = {'interface-name': lag_name,
                       'interfaces': interface_list,
                       'aggregator_id': str(aggregator_id),
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
            # print "result", results
            result.append(results)
        return result

    def get_lacp_member_info(self, lag_name, intf_name):
        """ Returns a dict containing all the LACP port specific information
            User needs to call this API only for dynamic LAG type.

        args:
            lag_name (str) - port-channel name/descr (for e.g po50)
            intf_name - interface number e.g 1/1, 2/1

        returns:
            return - dict containing LACP information of port-channel member

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.
        """
        cli_arr = 'show lacp lag_name ' + str(lag_name)
        output = self._callback(cli_arr, handler='cli-get')
        interface_info = {}
        for line in output.split('\n'):
            if 'Error' in line:
                raise ValueError(str(line))
            if intf_name in line:
                port_info = line.split()
                if port_info[1] == 'ACTR':
                    actor_oper_key = port_info[4]
                    actor_activity = True if port_info[5] == 'Yes' else False
                    actor_agg = True if port_info[7] == 'Agg' else False
                    actor_syn = True if port_info[8] == 'Syn' else False
                    actor_coll = True if port_info[9] == 'Col' else False
                    actor_dist = True if port_info[10] == 'Dis' else False
                    interface_info.update({
                        'int_name': intf_name,
                        'actor_oper_key': actor_oper_key,
                        'actor_agg': actor_agg,
                        'actor_syn': actor_syn,
                        'actor_coll': actor_coll,
                        'actor_dist': actor_dist,
                        'actor_activity': actor_activity,
                    })
                elif port_info[1] == 'PRTR':
                    part_oper_key = port_info[4]
                    part_activity = True if port_info[5] == 'Yes' else False
                    part_agg = True if port_info[7] == 'Agg' else False
                    part_syn = True if port_info[8] == 'Syn' else False
                    part_coll = True if port_info[9] == 'Col' else False
                    part_dist = True if port_info[10] == 'Dis' else False
                    interface_info.update({
                        'part_oper_key': part_oper_key,
                        'part_agg': part_agg,
                        'part_syn': part_syn,
                        'part_coll': part_coll,
                        'part_dist': part_dist,
                        'part_activity': part_activity,
                    })
                else:
                    rx_count = port_info[2]
                    tx_count = port_info[4]
                    interface_info.update({
                        'rx_count': rx_count,
                        'tx_count': tx_count,
                    })
        return interface_info

    def get_port_channel_member_ports(self, lag_name=None):
        """ Returns a map of port-channel member ports

        args:
            lag_name (str) - port-channel name/descr (for e.g po50)

        returns:
            return - dict containing port-channel member (ifid: ifname) mapping

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.85.107', '22')
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     ports = ['2/1', '2/2']
            ...     output = dev.interface.create_port_channel(ports, 'ethernet',
            ...                         50, 'static', 'po50')
            ...     assert output == True
            ...     output = dev.interface.get_port_channel_member_ports('po50')
            ...     assert len(output) >= 1
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
        # lag_grp_list is list of member_port ifid in hexstring with each member_port
        # taking 4 octets
        m_list = []
        m_list = [hex(ord(x)).lstrip("0x").zfill(2) for x in lag_grp_list]
        hex_list = ["0x" + x for x in [''.join(x) for x in zip(m_list[0::4],
                    m_list[1::4], m_list[2::4], m_list[3::4])]]
        # convert ifid list of member ports to decimals
        member_list = [int(c, 16) for c in hex_list]
        # Get the interface name/num for a given interface id
        ifid_name_map = {}
        ifid_name_map = self.get_interface_id_name_mapping(member_list)
        return ifid_name_map

    def get_port_channel_list(self):
        """ Returns a port-channel list

        args:
            None

        returns:
            return - list of port channels containing name, type, primary port, deploy

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.
        """
        cli_arr = 'show lag brief'
        po_list = []
        output = self._callback(cli_arr, handler='cli-get')
        lag_str_list = []
        start_parse = False
        for item in output.split("\n"):
            if "Deploy" in item:
                start_parse = True
                continue
            if start_parse is True:
                if item == '':
                    break
                lag_str_list = item.split()
                lag_name = lag_str_list[0]
                lag_type = lag_str_list[1]
                deploy = lag_str_list[2]
                if deploy == 'Y':
                    deploy = True
                else:
                    deploy = False
                primary_port = lag_str_list[4]
                po_list.append((lag_name, lag_type, primary_port, deploy))
        return po_list

    def get_port_channel_ifindex(self, lag_name=None):
        """ Returns a port-channel ifindex

        args:
            lag_name (str) - port-channel name/descr (for e.g po50)

        returns:
            return - port-channel ifindex

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
        lag_ifindex_oid = SnmpMLXMib.mib_oid_map['fdryLinkAggregationGroupIfIndex'] + \
            "." + str(key_len) + str(lag_name_oid)
        lag_ifindex = self._callback(lag_ifindex_oid, handler='snmp-get')
        return lag_ifindex

    def get_port_channel_id(self, lag_name=None):
        """ Returns a port-channel id given a lag name

        args:
            lag_name (str) - port-channel name/descr (for e.g po50)

        returns:
            return - port channel id

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
        lag_id_oid = SnmpMLXMib.mib_oid_map['fdryLinkAggregationGroupId'] + \
            "." + str(key_len) + str(lag_name_oid)
        lag_id = self._callback(lag_id_oid, handler='snmp-get')
        return lag_id

    def get_lag_id_name_map(self, lag_id):
        """ Returns a dict containing the port-channel id, port-channel name

        args:
            lag_id (str) - port-channel id

        returns:
            return - dict containing the port-channel id, port-channel name

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.
        """
        ifXtable_oid = SnmpMLXMib.mib_oid_map['fdryLinkAggregationGroupEntry']
        config = {}
        config['oid'] = ifXtable_oid
        config['columns'] = {12: 'lag_id'}
        config['fetch_all'] = False
        lag_group_table = self._callback(config, handler='snmp-walk')
        for row in lag_group_table.rows:
            id, value = row['lag_id'], row['_row_id']
            # Strip the length and convert ascii to string
            value = value.split('.')
            value.pop(0)
            value = [int(x) for x in value]
            lag_name = ''.join(chr(i) for i in value)
            if str(id) == lag_id:
                return lag_name

    def admin_state(self, **kwargs):
        """Set interface administrative state.

        Args:
            int_type (str): Type of interface. (ethernet, etc).
            name (str): Name of interface. (1/1, etc).
            enabled (bool): Is the interface enabled? (True, False)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `enabled` is not passed and
                `get` is not ``True``.
            ValueError: if `int_type`, `name`, or `enabled` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.admin_state(
            ...         int_type='ethernet', name='1/1',
            ...         enabled=False)
            ...         dev.interface.admin_state(
            ...         int_type='ethernet', name='1/1',
            ...         enabled=True)
        """

        int_type = kwargs.pop('int_type').lower()
        name = str(kwargs.pop('name'))
        get = kwargs.pop('get', False)
        if get:
            enabled = None
        else:
            enabled = kwargs.pop('enabled')
        ifname_Ids = self.get_interface_name_id_mapping()
        port_id = ifname_Ids[int_type + name]
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types
        ifAdminStatus_oid = SnmpMib.mib_oid_map['ifAdminStatus']
        ifadminStatus_index = ifAdminStatus_oid + '.' + str(port_id)
        if int_type == 'ethernet' and port_id is None:
            raise ValueError('pass valid port-id')

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             str(valid_int_types))

        if not isinstance(enabled, bool) and not get:
            raise ValueError('`enabled` must be `True` or `False`.')

        try:
            if get:
                value = callback(ifadminStatus_index)
                if value == 1:
                    enabled = True
                else:
                    enabled = False
                return enabled
            else:
                if enabled:
                    value = 1
                else:
                    value = 2
                state_args = (ifadminStatus_index, value)
                return callback(state_args, handler='snmp-set')
        except AttributeError:
            return None
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to set interface admin status to %s' % (reason))
        return None

    def description(self, **kwargs):
        """Set interface description.

        Args:
            int_type (str): Type of interface. (ethernet, etc).
            name (str): Name of interface. (1/1, etc).
            desc (str): The description of the interface.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `enabled` is not passed and
                `get` is not ``True``.
            ValueError: if `int_type`, `name`, or `desc` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.description(
            ...         int_type='ethernet', name='1/1',
            ...         desc='test')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """

        int_type = kwargs.pop('int_type').lower()
        get = kwargs.pop('get', False)
        name = str(kwargs.pop('name'))
        ifname_Ids = self.get_interface_name_id_mapping()
        port_id = ifname_Ids[int_type + name]
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types
        ifAlias = SnmpMib.mib_oid_map['ifAlias']
        ifAlias_oid = ifAlias + '.' + str(port_id)
        if int_type == 'ethernet' and port_id is None:
            raise ValueError('pass valid port-id')

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             str(valid_int_types))

        try:
            if get:
                if_desc = callback(ifAlias_oid)
                return if_desc
            else:
                desc = str(kwargs.pop('desc'))
                ifdescr_args = (ifAlias_oid, desc)
                return callback(ifdescr_args, handler='snmp-set')
        except AttributeError:
            return None
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to set interface admin status to %s' % (reason))
        return None

    def switchport(self, **kwargs):
        """Set interface switchport status.
           it is a dummy function for MLX as there is no switchport mode

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            enabled (bool): Is the interface enabled? (True, False)
            get (bool): Get config instead of editing config. (True, False)

        Returns:
            Return value of `True or False`.

        Raises:
            KeyError: if `int_type` or `name` is not specified.
            ValueError: if `name` or `int_type` is not a valid
                value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.switchport(name='1/1',
            ...         int_type='ethernet')
            ...         dev.interface.switchport()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s"
                             % str(int_types))
        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        if kwargs.pop('get', False):
            return None
        else:
            return True

    def acc_vlan(self, **kwargs):
        """Set access VLAN on a port.
        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/1, 1/2, etc)
            vlan (str): VLAN ID to set as the access VLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return True on success or raises ValueError on failure

        Raises:
            KeyError: if `int_type`, `name`, or `vlan` is not specified.
            ValueError: if `int_type`, `name`, or `vlan` is not valid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> int_type = 'ethernet'
            >>> name = '1/1'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.add_vlan_int('736')
            ...         output = dev.interface.acc_vlan(int_type=int_type,
            ...         name=name, vlan='736')
            ...         dev.interface.acc_vlan()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type')
        name = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        int_types = self.valid_int_types
        cli_arr = []

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s"
                             % repr(int_types))
        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of y/z for '
                             'physical interfaces or x for port channel.')

        vlan = kwargs.pop('vlan')
        if not pyswitch.utilities.valid_vlan_id(vlan):
            raise InvalidVlanId("`name` must be between `1` and `4096`")

        cli_arr.append('vlan' + ' ' + str(vlan))

        if kwargs.pop('delete', False):
            cli_arr.append('no untagged' + ' ' + int_type + ' ' + name)
        else:
            cli_arr.append('untagged' + ' ' + int_type + ' ' + name)

        cli_res = callback(cli_arr, handler='cli-set')
        error = re.search(r'Error:(.+)', cli_res)
        if error:
            raise ValueError("%s" % error.group(0))
        return True

    def get_ip_addresses(self, **kwargs):
        """
        Get IP Addresses already set on an Interface.

        Args:
            int_type (str): Type of interface. (ethernet).
            name (str): Name of interface id.
                 (For interface: 1/1, 1/2 etc).
            version (int): 4 or 6 to represent IPv4 or IPv6 address
            callback (function): A function executed upon completion of the
                 method.
            Returns:
            False or IP address on the specified interface.

        Raises:
            KeyError: if `int_type` or `name` is not passed.
            ValueError: if `int_type` or `name` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        int_type = 'ethernet'
            ...        name = '4/4'
            ...        version = 4
            ...        result = dev.interface.get_ip_addresses(
            ...        int_type=int_type, name=name, version=version)
            ...        print result
            ...        version = 6
            ...        result = dev.interface.get_ip_addresses(
            ...        int_type=int_type, name=name, version=version)
            ...        print result
        """

        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        version = int(kwargs.pop('version'))
        callback = kwargs.pop('callback', self._callback)

        if version == 4:
            cli_cmd = 'show ip inter' + ' ' + int_type + ' ' + name + ' | include address'
            cli_output = callback(cli_cmd, handler='cli-get')
            if re.search(r'ip address:', cli_output):
                ip = re.split(' ', cli_output)
                return ip[4]
            else:
                return False
        elif version == 6:
            cli_cmd = 'show ipv6 inter' + ' ' + int_type + ' ' + name
            cli_output = callback(cli_cmd, handler='cli-get')
            if re.search(r'IPv6 is enabled', cli_output):
                ipv6_s = re.search(r'(.+) \[Preferred\],  subnet is (.+)',
                        cli_output)
                subnet_s = re.search(r'::/(.+)', ipv6_s.group(2))
                ipv6_addr = ipv6_s.group(1).strip() + '/' + subnet_s.group(1)
                return ipv6_addr
            else:
                return False

    def mtu(self, **kwargs):
        """Set interface mtu.

        Args:
            int_type (str): Type of interface. (ethernet, etc)
            name (str): Name of interface. (1/1 etc)
            mtu (str): Value between 1522 and 9216
            callback (function): A function executed upon completion of the
                method.
        Returns:
            Return value of `mtu(str)`, True

        Raises:
            KeyError: if `int_type`, `name`, or `mtu` is not specified.
            ValueError: if `int_type`, `name`, or `mtu` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.mtu(mtu='1666',
            ...         int_type='ethernet', name='1/1')
            ...         output = dev.interface.mtu(get=True,
            ...         int_type='ethernet', name='1/1')
            ...         print output
            ...         dev.interface.mtu() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)

        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if kwargs.pop('get', False):
            cli_cmd = 'show interfaces' + ' ' + int_type + ' ' + name + ' ' + ' | inc MTU'
            cli_output = callback(cli_cmd, handler='cli-get')

            mtu = re.split(' ', cli_output)

            return mtu[1]

        else:
            raise ValueError("MLX Doesn't support per port L2 MTU configuration")
        return None

    def trunk_allowed_vlan(self, **kwargs):
        """Add member ports to a vlan.

        Args:
            int_type (str): Type of interface. (ethernet, port_channel)
            name (str): Name of interface. (1/1, 2/1, 50 etc)
            action (str): Action to take on trunk. (add, remove)
            vlan (str): vlan id for action. Only valid for add and remove.
            callback (function): A function executed upon completion of the
                method.

        Returns:
            Return True or Value Error.

        Raises:
            ValueError: if `int_type`, `name`.

        Examples:
            >>> def test_trunk_allowed_vlan():
            ...     import pyswitch.device
            ...     switches = ['10.24.85.107']
            ...     auth = ('admin', 'admin')
            ...     int_type = 'ethernet'
            ...     name = '1/4'
            ...     for switch in switches:
            ...         conn = (switch, '22')
            ...         with pyswitch.device.Device(conn=conn, auth=auth)
                            as dev:
            ...             output = dev.interface.add_vlan_int('25')
            ...             output = dev.interface.trunk_allowed_vlan(
            ...             int_type=int_type, name=name, action='add',
            ...             vlan='25')
            ...             # doctest: +IGNORE_EXCEPTION_DETAIL
            >>> test_trunk_allowed_vlan() # doctest: +SKIP
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)

        int_types = self.valid_int_types
        valid_actions = ['add', 'remove']

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" %
                             repr(int_types))

        action = kwargs.pop('action')
        vlan = kwargs.pop('vlan', None)

        if action not in valid_actions:
            raise ValueError('%s must be one of: %s' %
                             (action, valid_actions))

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of y/z for '
                             'physical interfaces or x for port channel.')

        if int_type == 'port_channel':
            name = self.get_lag_primary_port(name)
            int_type = 'ethernet'

        vlan_list = pyswitch.utilities.get_vlan_list(vlan)
        if vlan_list is None:
            raise ValueError('vlan or vlan range is not allowed')

        cli_arr = []
        for vid in vlan_list:
            cli_arr.append('vlan' + ' ' + str(vid))
            if action == 'add':
                cli_arr.append('tagged' + ' ' + int_type + ' ' + name)
            else:
                cli_arr.append('no tagged' + ' ' + int_type + ' ' + name)

        try:
            cli_res = callback(cli_arr, handler='cli-set')
            pyswitch.utilities.check_mlx_cli_set_error(cli_res)
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to add member port to vlan %s' % (reason))

    def trunk_mode(self, **kwargs):
        """ dummy function as MLX do not support trunk mode
        """
        pass

    def interface_exists(self, **kwargs):
        """check whether interface exist.

        Args:
            int_type (str): Type of interface. (ethernet)
            name (str): Name of interface. (1/1, 1/2 etc)
            callback (function): A function executed upon completion of the
                method.
        Returns:
            Return True or False

        Raises:
            ValueError: if `int_type`, `name`.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.interface_exists(
            ...         int_type='ethernet', name='1/1')
            ...         print output
            Traceback (most recent call last):
            KeyError
        """

        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))

        valid_int_types = self.valid_int_types

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))

        ifname_Ids = self.get_interface_name_id_mapping()
        lag_name = self.get_lag_id_name_map(str(name))
        if int_type + name in ifname_Ids or lag_name is not None:
            return True
        else:
            return False

    def get_lag_primary_port(self, lag_id):
        """
            returns lag primary ethernet port
        """
        cli_cmd = "show lag id" + ' ' + str(lag_id)
        cli_output = self._callback(cli_cmd, handler='cli-get')
        primary_match = re.search(r'Primary Port:  (.+)', cli_output)
        if primary_match is None or primary_match.group(1) is None:
            raise ValueError('primary port is not found for lag %s' % lag_id)
        return primary_match.group(1).strip()
