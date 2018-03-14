
from pyswitch.snmp.base.interface import Interface as BaseInterface
from pyswitch.snmp.SnmpMib import SnmpMib as SnmpMib
import pyswitch.utilities
from pyswitch.exceptions import InvalidVlanId, InvalidLoopbackName
import re
from pyswitch.snmp.mlx.SnmpMLXMib import SnmpMLXMib as SnmpMLXMib
from hnmp import mac_address
from ipaddress import ip_interface


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
    def valid_l2_int_types(self):

        return [
            'ethernet',
            'port_channel'
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
        minimum_mtu = 576
        maximum_mtu = 9198
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_ipv6_mtu_const(self):
        # TBD change below defaults
        minimum_mtu = 1280
        maximum_mtu = 9198
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
                if desc is None:
                    cli_arr.append('vlan' + " " + str(vlan))
                else:
                    cli_arr.append('vlan' + " " + str(vlan) + " " + 'name' + " " + '"' + desc + '"')
            output = self._callback(cli_arr, handler='cli-set')
            prev = None
            for line in output.split('\n'):
                temp = line
                if 'Error' in line:
                    vlan_error = re.search(r'#vlan (.+)', prev)
                    if vlan_error:
                        failed_vlan = vlan_error.group(1)
                    raise ValueError("Failed to create VLAN " + failed_vlan + " " + str(line))
                prev = temp
            return True
        except Exception as error:
            reason = error.message
            raise ValueError(reason)

    def create_port_channel(self, ports, int_type, portchannel_num, mode, po_exists,
                        po_deployed, desc=None):
        """create port channel

        args:
            int_type (str): type of interface. (ethernet, , etc)
            ports(list): port numbers (1/1, 2/1 etc)
            portchannel_num (int): port-channel number (1, 2, 3, etc).
            mode (str): mode of port-channel (static, dynamic)
            po_exists (bool): notifies is PO is already created
            po_deployed (bool): Is PO already deployed
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
            ...                         50, 'static', False, 'po50')
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
            if int_type != 'ethernet':
                raise ValueError('Not a valid interface type (%s) for MLX' % (int_type))
            # Check if a port-channel exists with same id TBD in action
            cli_arr.append('lag' + " " + '"' + desc + '"' + " " + str(mode) + " " + 'id' +
                    " " + str(portchannel_num))
            # Add ports to port-channel
            port_list = []
            member_cnt = 0
            for port in ports:
                port_list.append(int_type + " " + port)
            port_list_str = " ".join(port_list)
            cli_arr.append('ports' + " " + port_list_str)
            if po_exists:
                # Determine if primary port election is required
                lag_member_dict = {}
                lag_member_dict = self.get_port_channel_member_ports(desc)
                member_cnt = len(lag_member_dict)
            if member_cnt == 0 or not po_deployed:
                # select primary port
                cli_arr.append('primary-port' + " " + ports[0])
            # deploy the port channel
            if not po_deployed:
                cli_arr.append('deploy')
            # Enable the member ports
            cli_arr.append('enable' + " " + port_list_str)
            output = self._callback(cli_arr, handler='cli-set')
            for line in output.split('\n'):
                if 'Error' in line:
                    # Skip the error if PO exists
                    skip_str = 'ports already exist in LAG'
                    if po_exists and skip_str in line:
                        continue
                    else:
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
        po_list = self.get_port_channel_info()
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
                       'ready-agg': ready_agg,
                       'deployed': deploy}
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
        cli_arr = 'show lacp lag_name ' + '"' + str(lag_name) + '"'
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

    def get_port_channel_info(self):
        """ Returns a port-channel list containing LAG info

        args:
            None

        returns:
            return - list of port channels containing name, LAG id, type, deploy

        raises:
            ValueError
        """
        cli_arr = 'show lag | inc Deployed'
        po_list = []
        output = self._callback(cli_arr, handler='cli-get')
        if output == '':
            return po_list

        error = re.search(r'Error(.+)', output)
        if error:
            raise ValueError("%s" % error.group(0))
        for line in output.split("\n"):
            if 'keep-alive' in line:
                continue
            po_name = re.search(r'LAG \"(.+)\" ID (.+) \((.+) Deployed\)', line)
            if po_name is None:
                continue
            lag_name = po_name.group(1)
            lag_id = po_name.group(2)
            type = po_name.group(3)
            if 'Not' in type:
                deploy = False
            else:
                deploy = True
            if 'static' in type:
                lag_type = 'static'
            elif 'dynamic' in type:
                lag_type = 'dynamic'
            po_list.append((lag_name, lag_type, lag_id, deploy))
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

        if int_type == 'port_channel':
            name = self.get_lag_primary_port(name)
            int_type = 'ethernet'

        port_id = self.get_snmp_port_id_by_intf_name(int_type, name)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types
        ifAdminStatus_oid = SnmpMib.mib_oid_map['ifAdminStatus']
        ifadminStatus_index = ifAdminStatus_oid + '.' + str(port_id)
        if port_id is None:
            raise ValueError(' Invalid port-id')

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

    def get_oper_state(self, **kwargs):
        """Get interface operational state.

        Args:
            int_type (str): Type of interface. (ethernet, etc).
            name (str): Name of interface. (1/1, etc).

        Returns:
            oper state - up/down

        Raises:
            KeyError: if `int_type`, `name` is not passed

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         oper_state = dev.interface.get_oper_state(
            ...                         int_type='ethernet', name='1/1')
        """

        int_type = kwargs.pop('int_type').lower()
        name = str(kwargs.pop('name'))

        if_type = int_type
        if int_type == 'port-channel':
            int_type = 'port_channel'
            if_type = 'LAG'
        if_id = self.get_snmp_port_id_by_intf_name(if_type, name)
        if if_id is None:
            raise ValueError('Invalid if_id')
        oid = SnmpMib.mib_oid_map['ifOperStatus']
        operState_oid = oid + '.' + str(if_id)

        valid_int_types = self.valid_int_types
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             str(valid_int_types))
        oper_state = self._callback(operState_oid, handler='snmp-get')
        if oper_state == 1:
            return 'up'
        elif oper_state == 2:
            return 'down'
        else:
            return 'invalid'

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

        if int_type == 'port_channel':
            name = self.get_lag_primary_port(name)
            int_type = 'ethernet'

        port_id = self.get_snmp_port_id_by_intf_name(int_type, name)
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
            if_desc = callback(ifAlias_oid)

            if get:
                return if_desc
            else:
                desc = str(kwargs.pop('desc'))
                if if_desc == desc:
                    raise UserWarning('Interface description %s is already'
                                      ' configured' % desc)
                ifdescr_args = (ifAlias_oid, desc)
                return callback(ifdescr_args, handler='snmp-set')
        except AttributeError:
            return None
        except UserWarning as e:
            raise UserWarning('%s' % str(e.message))
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to set interface description to %s' % (reason))
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
        int_types = self.valid_l2_int_types

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s"
                             % str(int_types))
        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of y/z for '
                             'physical interfaces or x for port channel.')

        if kwargs.pop('get', False):
            return None
        else:
            return True

    def acc_vlan(self, **kwargs):
        """Set/get/delete access VLAN on a port.
        Args:
            int_type (str): Type of interface. (ethernet, port_channel)
            get (bool): Get config instead of editing config. (True, False)
            name (str): Name of interface. (1/1, 1/2, etc)
            vlan (str): VLAN ID to set as the access VLAN.
            delete (bool):  True to remove a untagged port from a vlan
            callback (function): A function executed upon completion of the
                method.
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
        int_types = self.valid_l2_int_types
        cli_arr = []

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s"
                             % repr(int_types))
        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of y/z for '
                             'physical interfaces or x for port channel.')

        if int_type == 'port_channel':
            name = self.get_lag_primary_port(name)
            int_type = 'ethernet'

        cli_cmd = 'show interface ' + ' ' + int_type + ' ' + name

        pre_config_pat = r'VLAN (\d+) \(untagged\)'
        get_vlan = 0
        try:
            cli_output = callback(cli_cmd, handler='cli-get')
            get_vlan_config = re.search(pre_config_pat, cli_output)
            if get_vlan_config:
                get_vlan = get_vlan_config.group(1).strip()
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to get vlan %s' % (reason))

        if kwargs.pop('get', False):
            return get_vlan

        vlan = kwargs.pop('vlan')
        if not pyswitch.utilities.valid_vlan_id(vlan):
            raise InvalidVlanId("`name` must be between `1` and `4090`")

        cli_arr.append('vlan' + ' ' + str(vlan))

        if kwargs.pop('delete', False):
            cli_arr.append('no untagged' + ' ' + int_type + ' ' + name)
        else:
            cli_arr.append('untagged' + ' ' + int_type + ' ' + name)
            if get_vlan == vlan:
                raise UserWarning('interface %s, already untagged'
                                'memberport of vlan %s' % (name, vlan))
        try:
            cli_res = callback(cli_arr, handler='cli-set')
            pyswitch.utilities.check_mlx_cli_set_error(cli_res)
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to add untagged member port to vlan %s'
                          % (reason))

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
            cli_cmd = 'show runn interface ' + int_type + ' ' + name
            cli_output = callback(cli_cmd, handler='cli-get')
            if re.search(r'ipv6 address', cli_output):
                ipv6_a = re.search(r'ipv6 address (.+)',
                        cli_output)
                ipv6_addr = ipv6_a.group(1).strip()
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

        int_types = ['ethernet', 'port_channel']
        valid_actions = ['add', 'remove']

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" %
                             repr(int_types))

        action = kwargs.pop('action')
        vlan = kwargs.pop('vlan', None)

        if action is None and vlan == []:
            raise ValueError("vlan id must be passed for MLX")

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

        try:
            ifname_Ids = self.get_interface_name_id_mapping()
            lag_name = self.get_lag_id_name_map(str(name))
        except KeyError:
            raise ValueError('Interface %s %s is not found on device' %
                (int_type, name))
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
        if primary_match is None or primary_match.group(1).strip() == 'none':
            raise ValueError('primary port is not found for lag %s' % lag_id)
        return primary_match.group(1).strip()

    # pylint: disable=E1101
    def ip_mtu(self, **kwargs):
        """Set/get the interface mtu.

        Args:
            int_type (str): Type of interface. (ethernet,port_channel and ve
                , etc)
            name (str): Name of interface. (1/4, 4/4, etc)
            mtu (str): IPv4 MTU value should be between 576 to  8982
                IPv6 MTU value should be between 1280 to  8982

            callback (function): A function executed upon completion of the
                method.

        Returns:
            Return mtu or True.

        Raises:
            ValueError: if `int_type`, `name`, or `mtu` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.ip_mtu(mtu='1666',
            ...         int_type='ethernet', name='1/1')
            ...         dev.interface.ip_mtu() # doctest:
            +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        version = kwargs.pop('version', 4)

        callback = kwargs.pop('callback', self._callback)

        int_types = self.valid_int_types

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if int_type == 'port_channel':
            name = self.get_lag_primary_port(name)
            int_type = 'ethernet'

        port_id = self.get_snmp_port_id_by_intf_name(int_type, name)
        mtu_oid = SnmpMib.mib_oid_map['snRtIpPortIfMtu'] + '.' + str(port_id)
        mtu_v6_oid = SnmpMib.mib_oid_map['ipv6IfEffectiveMtu'] + '.' + str(port_id)

        if kwargs.pop('get', False):
            ipv4_mtu = callback(mtu_oid)
            ipv6_mtu = callback(mtu_v6_oid)
            return {'ipv4': ipv4_mtu, 'ipv6': ipv6_mtu}

        mtu = kwargs.pop('mtu')

        if not pyswitch.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of y/z for '
                             'physical interfaces.')
        if version == 6:
            minimum_mtu, maximum_mtu = self.l3_ipv6_mtu_const
        else:
            minimum_mtu, maximum_mtu = self.l3_mtu_const

        if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
            raise ValueError(
                "Incorrect mtu value %s-%s" %
                (minimum_mtu, maximum_mtu))
        cli_arr = []
        cli_arr.append('interface ' + int_type + ' ' + name)
        if version == 4:
            cli_arr.append('ip mtu ' + str(mtu))
        else:
            cli_arr.append('ipv6 mtu ' + str(mtu))

        try:
            cli_res = callback(cli_arr, handler='cli-set')
            pyswitch.utilities.check_mlx_cli_set_error(cli_res)
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to set IPv%s MTU %s' % (version, reason))

    def vrf(self, **kwargs):
        """Create a vrf.
        Args:
            vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): False, the vrf is created and True if its to
                be deleted (True, False). Default value will be False if not
                specified.
            callback (function): A function executed upon completion of the
                method.

            Returns:
               Return True.
        Raises:
            ValueError: if  `vrf_name` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vrf(vrf_name=vrf1 )
            ...         output = dev.interface.vrf(vrf_name=vrf1
            ...         ,delete=True)

        """
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []

        if not get_config:
            vrf_name = kwargs['vrf_name']
            vrf_name = '"' + vrf_name + '"'
            cli_arr = []
            if delete:
                cli_arr.append('no vrf ' + vrf_name)
            else:
                cli_arr.append('vrf ' + vrf_name)

            try:
                cli_res = callback(cli_arr, handler='cli-set')
                pyswitch.utilities.check_mlx_cli_set_error(cli_res)
                return True
            except Exception as error:
                reason = error.message
                raise ValueError('Failed to create/delete vrf %s' % (reason))

        elif get_config:
            cli_cmd = "show vrf detail | inc VRF"
            try:
                cli_output = callback(cli_cmd, handler='cli-get')
            except Exception as error:
                reason = error.message
                raise ValueError('Failed to get vrf details %s' % (reason))

            for line in cli_output.split('\n'):
                vrf_pattern = re.search(r'VRF (.+), default (.+)', line)
                if vrf_pattern:
                    vrf_name = vrf_pattern.group(1)
                    result.append({'vrf_name': vrf_name})
            return result

    def vrf_afi(self, **kwargs):
        """Configure Target VPN Extended Communities
           Args:
               vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
               afi (str): Address family (ip/ipv6).
               rd (str) : Route Distinguiser <asn:nn or vpn rd> mandatory for
               mlx vrf create
               get (bool): Get config instead of editing config.
                           List all the details of
                           all afi under all vrf(True, False)

               delete (bool): True to delet the ip/ipv6 address family
                   Default value will be False if not specified.
               callback (function): A function executed upon completion of the
                   method.
           Returns:
               Return True.
           Raises:
               KeyError: if rd is not passed.
           Examples:
               >>> import pyswitch.device
               >>> switches = ['10.24.85.107']
               >>> auth = ('admin', 'admin')
               >>> for switch in switches:
               ...    conn = (switch, '22')
               ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
               ...         output = dev.interface.vrf_vni(afi="ip",
               ...         vrf_name="vrf1", rd='9:9')
               ...         output = dev.interface.vrf_vni(afi="ip",
               ...         vrf_name="vrf1", get=True)
               ...         output = dev.interface.vrf_vni(afi="ip",
               ...         vrf_name="vrf1", delete=True)
           """

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        if not get_config:
            cli_arr = []
            afi = kwargs['afi']
            afi = 'ipv4' if (afi == 'ip') else afi
            vrf_name = kwargs['vrf_name']
            vrf_name = '"' + vrf_name + '"'
            cli_arr.append('vrf ' + vrf_name)

            if delete is True:
                cli_arr.append('no address-family ' + afi)
            else:
                rd = kwargs.pop('rd', None)
                if(rd is None):
                    raise KeyError('rd value is missing for mlx platform')
                cli_arr.append('rd ' + str(rd))
                cli_arr.append('address-family ' + afi)
            try:
                cli_res = callback(cli_arr, handler='cli-set')
                pyswitch.utilities.check_mlx_cli_set_error(cli_res)
                return True
            except Exception as error:
                reason = error.message
                raise ValueError('Failed to set/reset vrf afi %s' % (reason))

        elif get_config:
            vrf_name = kwargs.pop('vrf_name', '')
            vrf_name = '"' + vrf_name + '"'

            cli_cmd = 'show vrf ' + vrf_name
            cli_output = callback(cli_cmd, handler='cli-get')

            if re.search('Address Family IPv4', cli_output):
                ipv4_unicast_enabled = True
            else:
                ipv4_unicast_enabled = False

            if re.search('Address Family IPv6', cli_output):
                ipv6_unicast_enabled = True
            else:
                ipv6_unicast_enabled = False

            return {'ipv4': ipv4_unicast_enabled, 'ipv6': ipv6_unicast_enabled}

    def create_ve(self, **kwargs):
        """
        Add Ve Interface
        Args:
            ve_name (str): VE interface name
            enable (bool): True - Create False - Delete, default - True
            vlan_router_ve() should be called prior to calling this function
            for both create and delete VE
            get (bool) : If True return the list of VE names, default- False
        Returns:
            return True/False for enable
            return list of VE names when get=True
        Raises:
            KeyError: if `ve_name` is not passed.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.create_ve(
            ...                     ve_name='100')
            ...         output = dev.interface.create_ve(
            ...                     get=True,
            ...                     ve_name='100')
            ...         output = dev.interface.create_ve(
            ...                     enable=False,
            ...                     ve_name='100')
        """

        ve_name = kwargs.pop('ve_name', '')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)

        if get:
            enable = None
            ve_list = []
            cli_arr = 'show running-config interface | inc interface ve'
            output = self._callback(cli_arr, handler='cli-get')
            for line in output.split('\n'):
                info = re.search(r'interface ve (.+)', line)
                if info is None:
                    continue
                ve_id = info.group(1)
                if ve_id:
                    ve_list.append(ve_id)
            return ve_list

        if not enable:
            cli_arr = 'no interface ' + 've' + ' ' + ve_name
            output = self._callback(cli_arr, handler='cli-set')
            # No error handling reqd as vlan_router_ve() removes the VE
            return True
        else:
            cli_arr = 'interface ' + 've' + ' ' + ve_name
            output = self._callback(cli_arr, handler='cli-set')
            error = re.search(r'Error(.+)', output)
            if error:
                raise ValueError("%s" % error.group(0))
            return True

    def ve_interfaces(self, **kwargs):
        """list[dict]: A list of dictionary items describing the operational
        state of ve interfaces along with the ip address associations.

        Args:
            callback (function): A function executed upon completion of the
                method
        Returns:
            Return list of dict containing VE interface info

        Raises:
            None

        Examples:
            >>> import pyswitch.device
            >>> conn = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.ve_interfaces()
        """

        ve_list = []
        cli_arr = 'show running-config interface | inc interface ve'
        output = self._callback(cli_arr, handler='cli-get')
        error = re.search(r'Error(.+)', output)
        if error:
            raise ValueError("%s" % error.group(0))
        # Populate the VE interface list with default data and update later
        for line in output.split('\n'):
            info = re.search(r'interface ve (.+)', line)
            if info is None:
                continue
            ve_id = info.group(1)
            if_name = 'Ve ' + ve_id
            ve_info = {'interface-type': 've',
                       'interface-name': str(ve_id),
                       'if-name': if_name,
                       'interface-state': 'down',
                       'interface-proto-state': 'down',
                       'ip-address': 'unassigned'}
            ve_list.append(ve_info)
        cli_arr = 'show ip interface | inc ve'
        output = self._callback(cli_arr, handler='cli-get')
        error = re.search(r'Error(.+)', output)
        if error:
            raise ValueError("%s" % error.group(0))
        for line in output.split('\n'):
            info = re.search(r've (.+)', line)
            if info is not None:
                list = info.group(0).split()
                int_name = list[1]
                int_state = list[5]
                int_proto_state = list[6]
                cli_arr = 'show ip interface ve' + ' ' + int_name
                cli_out = self._callback(cli_arr, handler='cli-get')
                ve_ip = re.search(r'ip address:(.+)', cli_out)
                if ve_ip:
                    ip_address = ve_ip.group(1).strip()
                else:
                    ip_address = 'unassigned'
                # Check if the VE already is added to list
                for item in ve_list:
                    if item['interface-name'] == int_name and item['ip-address'] == 'unassigned':
                        item['ip-address'] = ip_address
                        item['interface-state'] = int_state
                        item['interface-proto-state'] = int_proto_state
        # pprint.pprint(ve_list)
        return ve_list

    def add_int_vrf(self, **kwargs):
        """
        Add L3 Interface in Vrf. Currently supports VE interface.
        TBD for other ethernet and loopback interfaces

        Args:
            int_type(str): L3 interface type on which the vrf needs to be configured.
            name(str):L3 interface name on which the vrf needs to be configured.
            vrf_name(str): Vrf name with which the L3 interface needs to be associated.
            enable (bool): If vrf fowarding should be enabled or disabled.
                        default is enabled.
            get (bool) : Get VRF config when get=True, default is False
        Returns:
            return VRF when get=True. return None if no VRF is associated
            True or ValueError for create and delete
        Raises:
            ValueError: if `int_type`, `name`, `vrf` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.add_int_vrf(
            ...                     int_type='ve',
            ...                     name='200',
            ...                     vrf_name='red')
            ...         vrf = dev.interface.add_int_vrf(
            ...                     get=True, int_type='ve',
            ...                     name='200')
            ...         assert(vrf == 'red')
            ...         output = dev.interface.add_int_vrf(
            ...                     enable=False,
            ...                     int_type='ve',
            ...                     name='200',
            ...                     vrf_name='red')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        name = kwargs.pop('name')

        int_type = kwargs.pop('int_type').lower()
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        in_vrf_name = kwargs.pop('vrf_name', 'Default')
        valid_int_types = self.valid_int_types

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                    repr(valid_int_types))
        if get:
            if int_type == 've':
                cli_arr = 'show ip interface ve ' + name
                cli_res = self._callback(cli_arr, handler='cli-get')
                error = re.search(r'Error(.+)', cli_res)
                if error:
                    return None
                result = re.search(r'Port belongs to VRF: (.+)', cli_res)
                vrf_name = result.group(1).strip()
                return vrf_name
        if not enable:
            if int_type == 've':
                cli_arr = []
                cli_arr.append('interface ve ' + name)
                cli_arr.append('no vrf forwarding ' + '"' + in_vrf_name + '"')
                cli_res = self._callback(cli_arr, handler='cli-set')
                error = re.search(r'Error(.+)', cli_res)
                if error:
                    raise ValueError("%s" % error.group(0))
                return True
        if int_type == 've':
            cli_arr = []
            cli_arr.append('interface ve ' + name)
            cli_arr.append('vrf forwarding ' + '"' + in_vrf_name + '"')
            cli_res = self._callback(cli_arr, handler='cli-set')
            error = re.search(r'Error(.+)', cli_res)
            if error:
                raise ValueError("%s" % error.group(0))
            return True

    def vlan_router_ve(self, **kwargs):
        """Configure/get/delete router interface ve on a vlan.

        Args:
            vlan_id (str): Vlan number.
            ve_config (str) : router ve interface
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the router ve on the vlan.(True, False)

        Returns:
            return True/False for create/delete
            return VE name/None for get

        Raises:
            KeyError: if `vlan_id`, `ve_config`  is not specified.
            ValueError: if `vlan_id` is not a valid value.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vlan_router_ve(
            ...         vlan_id='100', ve_config='200')
            ...         output = dev.interface.vlan_router_ve(
            ...         get=True, vlan_id='100')
            ...         output = dev.interface.vlan_router_ve(
            ...         delete=True, vlan_id='100', ve_config='200')
        """
        vlan = kwargs.pop('vlan_id')
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)

        if not self.valid_vlan_id(vlan):
            raise InvalidVlanId(
                'VLAN Id %s not in range 1 to 4090.' % vlan)
        if delete:
            ve_config = kwargs.pop('ve_config')
            cli_arr = []
            cli_arr.append('vlan ' + vlan)
            cli_arr.append('no router-interface ve ' + ve_config)
            cli_res = self._callback(cli_arr, handler='cli-set')
            error = re.search(r'Error(.+)', cli_res)
            if error:
                raise ValueError("%s" % error.group(0))
            return True

        if not get_config:
            ve_config = kwargs.pop('ve_config')
            cli_arr = []
            cli_arr.append('vlan ' + vlan)
            cli_arr.append('router-interface ve ' + ve_config)
            cli_res = self._callback(cli_arr, handler='cli-set')
            error = re.search(r'Error(.+)', cli_res)
            if error:
                raise ValueError("%s" % error.group(0))
            return True
        elif get_config:
            cli_arr = 'show vlan ' + str(vlan) + ' | inc Ve'
            cli_res = self._callback(cli_arr, handler='cli-get')
            if cli_res != '':
                ve_info = re.search(r'Ve(.+?) is', cli_res)
                return ve_info.group(1)
            else:
                return None

    def ip_address(self, **kwargs):
        """
        Set/Get IP Address on an Interface.

        Args:
            int_type (str): Type of interface. ('ethernet' etc)
            name (str): Name of interface id 1/1, 1/2 etc.
            ip_addr (str): IPv4/IPv6 IP Address..
                Ex: 10.10.10.1/24 or 2001:db8::/48
            delete (bool): True is the IP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            get (bool): Get Ipv4/Ipv6 address. (True, False)

        Returns:
            Return True/False. get returns Ipv4/Ipv6 address

        Raises:
            KeyError: if `int_type`, `name`, or `ip_addr` is not passed.
            ValueError: if `int_type`, `name`, or `ip_addr` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...        int_type = 'ethernet'
            ...        name = '4/1'
            ...        ip_addr = '20.10.10.1/24'
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, get=True)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr)
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', get=True)
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, delete=True)
            ...        ip_addr = 'fc00:1:3:1ad3:0:0:23:a/64'
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, get=True)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
        """

        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))

        delete = kwargs.pop('delete', False)
        valid_int_types = self.valid_int_types

        get = kwargs.pop('get', False)

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))
        if int_type == 've':
            if not self.valid_ve_id(name):
                raise ValueError("Ve Id must be between `1` and `255`")
        elif int_type == 'loopback':
            if not self.valid_loopback_number(name):
                raise InvalidLoopbackName('Loopback number must be between 1 and 64')
        if not get:
            ip_addr = str(kwargs.pop('ip_addr'))
            ipaddress = ip_interface(unicode(ip_addr))
            if delete:
                cli_arr = []
                cli_arr.append('interface ' + int_type + ' ' + name)
                if ipaddress.version == 4:
                    cli_arr.append('no ip address ' + ip_addr)
                elif ipaddress.version == 6:
                    cli_arr.append('no ipv6 address ' + ip_addr)
                cli_res = self._callback(cli_arr, handler='cli-set')
                error = re.search(r'Error(.+)', cli_res)
                if error:
                    raise ValueError("%s" % error.group(0))
                return True
            else:
                cli_arr = []
                cli_arr.append('interface ' + int_type + ' ' + name)
                if ipaddress.version == 4:
                    cli_arr.append('ip address ' + ip_addr)
                elif ipaddress.version == 6:
                    cli_arr.append('ipv6 address ' + ip_addr)
                cli_res = self._callback(cli_arr, handler='cli-set')
                error = re.search(r'Error(.+)', cli_res)
                if error:
                    raise ValueError("%s" % error.group(0))
                return True

        if get:
                cli_arr = []
                cli_arr.append('show ip interface ' + int_type + ' ' + name)
                cli_res = self._callback(cli_arr, handler='cli-get')
                error = re.search(r'Error(.+)', cli_res)
                if error:
                    raise ValueError("%s" % error.group(0))
                ipv4 = re.search(r'ip address: (.+)', cli_res)
                ipv4_add = ipv4.group(1)
                cli_arr.append('show running-config interface ' + int_type + ' ' + name)
                cli_res = self._callback(cli_arr, handler='cli-get')
                error = re.search(r'Error(.+)', cli_res)
                if error:
                    raise ValueError("%s" % error.group(0))
                for line in cli_res.split('\n'):
                    if 'ipv6 address' in line:
                        if 'link-local' not in line:
                            ipv6 = re.search(r'ipv6 address: (.+)', line)
                            ipv6_add = ipv6.group(1)
                            break
                return {'ipv4_address': ipv4_add,
                        'ipv6_address': ipv6_add}

    def ipv6_link_local(self, **kwargs):
        """Enable/Get auto configure ipv6 link local address on interfaces

        Args:
            int_type: Interface type on which the ipv6 link local needs to be
             configured.
            name: 'Ve' or 'loopback' or 'ethernet' interface name.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True - disable auto configuration of link-local
                           False - enable auto configuration of link-local
        Returns:
            Return True/False

        Raises:
            KeyError: if `int_type`, `name` is not passed.
            ValueError: if `int_type`, `name` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.85.107', '22')
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...    output = dev.interface.ipv6_link_local(name='500',
            ...     int_type='ve')
            ...    output = dev.interface.ipv6_link_local(get=True,name='500',
            ...     int_type='ve')
            ...    output = dev.interface.ipv6_link_local(delete=True,
            ...     name='500', int_type='ve')
        """
        int_type = kwargs.pop('int_type').lower()
        int_name = kwargs.pop('name')
        valid_int_types = self.valid_int_types
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if kwargs.pop('get', False):
            cli_arr = 'show ipv6 interface ' + int_type + ' ' + int_name
            cli_res = self._callback(cli_arr, handler='cli-get')
            error = re.search(r'Error(.+)', cli_res)
            if error:
                raise ValueError("%s" % error.group(0))
            ipv6 = re.search(r'IPv6 is enabled', cli_res)
            if ipv6:
                return True
            else:
                return False

        if kwargs.pop('delete', False):
            cli_arr = []
            cli_arr.append('interface ' + int_type + ' ' + int_name)
            cli_arr.append('no ipv6 enable')
            cli_res = self._callback(cli_arr, handler='cli-set')
            error = re.search(r'Error(.+)', cli_res)
            if error:
                raise ValueError("%s" % error.group(0))
            return True
        else:
            cli_arr = []
            cli_arr.append('interface ' + int_type + ' ' + int_name)
            cli_arr.append('ipv6 enable')
            cli_res = self._callback(cli_arr, handler='cli-set')
            error = re.search(r'Error(.+)', cli_res)
            if error:
                raise ValueError("%s" % error.group(0))
            return True

    def valid_vlan_id(self, vlan_id):
        """Validates a VLAN ID.

        Args:
            vlan_id (integer): VLAN ID to validate.  If passed as ``str``, it will
                be cast to ``int``.

        Returns:
            bool: True if it is a valid VLAN ID. False if not.

        Raises:
            None
        """
        minimum_vlan_id = 1
        maximum_vlan_id = 4090
        return minimum_vlan_id <= int(vlan_id) <= maximum_vlan_id

    def valid_ve_id(self, ve_id):
        """Validates a VE ID.

        Args:
            ve_id (integer): VE Id to validate.  If passed as str, it will
                be cast to int.

        Returns:
            bool: True if it is a valid VE ID. False if not.

        Raises:
            None
        """

        min_ve_id = 1
        max_ve_id = 255
        return min_ve_id <= int(ve_id) <= max_ve_id

    def valid_loopback_number(self, loopback_number):
        """Validates a loopback interface Id.

        Args:
            loopback_number (integer): Loopback port number to validate.
                If passed as ``str``, it will be cast to ``int``.
        Returns:
            bool: ``True`` if it is a valid loopback_number.  ``False`` if not.

        Raises:
            None
        """
        minimum_loopback_id = 1
        maximum_loopback_id = 64
        return minimum_loopback_id <= int(loopback_number) <= maximum_loopback_id

    def is_ve_id_required(self):
        """ Check if VE id is required for creating VE or vlan id is sufficient
        """
        return True

    def is_vlan_rtr_ve_config_req(self):
        """ Check if router interface config is required for VLAN
        """
        return True

    def vrrpe_vip(self, **kwargs):
        """Set/get vrrpe VIP.

        Args:
            int_type (str): Type of interface. (ethernet and ve).
            name (str): Name of interface. (4/6, VE name etc).
            vrid (str): vrrpev3 ID.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, the VIP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            vip (str): IPv4/IPv6 Virtual IP Address.
            callback (function): A function executed upon completion of the
                method.

        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vip` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vip` is invalid.

        Returns:
            Return True or list of VIPs.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.12.91']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output =dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89', vrid='11', vip='10.0.1.10')
            ...         output = dev.interface.vrrpe_vip(get=True,
            ...         int_type='ve', name='89')
            ...         output =dev.interface.vrrpe_vip(delete=True,
            ...         int_type='ve', name='89',vrid='1',
            ...         vip='10.0.0.10')
        """
        int_type = kwargs.pop('int_type').lower()
        version = kwargs.pop('version', 4)
        name = kwargs.pop('name', )
        get = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ve', 'ethernet']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if get:
            result = []
            vip_list = []
            vrid_match = r'VRID (\d+)'
            if version == 4:
                cli_cmd = 'show ip vrrp-extended ' + int_type + ' ' + name
                vip_match = r'virtual ip address (.+)'
            else:
                cli_cmd = 'show ipv6 vrrp-extended ' + int_type + ' ' + name
                vip_match = r'virtual ipv6 address (.+)'

            output = callback(cli_cmd, handler='cli-get')

            if(re.search(r'error', output)):
                raise ValueError('VRRP-E is not configured or invalid input')

            for line in output.split('\n'):
                if(re.search(vrid_match, line)):
                    vrid = re.search(vrid_match, line).group(1).strip()
                elif(re.search(vip_match, line)):
                    vips = re.search(vip_match, line).group(1).strip().split()
                    for vip in vips:
                        vip_list.append(vip)
                elif(re.search(r'short-path-forwarding', line)):
                    result.append({'vrid': vrid, 'vip': vip_list})
                    del vip_list
                    vip_list = []

            return result

        vrid = kwargs.pop('vrid')
        vip = kwargs.pop('vip', '')
        if vip != '':
            ipaddress = ip_interface(unicode(vip))
            version = ipaddress.version
        else:
            version = 4

        cli_arr = []
        cli_arr.append('interface ' + int_type + ' ' + name)
        if version == 4:
            if delete:
                cli_arr.append('ip vrrp-extended vrid ' + str(vrid))
                cli_arr.append('no activate')
                cli_arr.append('no ip-address ' + vip)
            else:
                cli_arr.append('ip vrrp-extended vrid ' + str(vrid))
                cli_arr.append('backup')
                cli_arr.append('ip-address ' + vip)
                cli_arr.append('activate')
        else:
            if delete:
                cli_arr.append('ipv6 vrrp-extended vrid ' + str(vrid))
                cli_arr.append('no activate')
                cli_arr.append('no ipv6-address ' + vip)
            else:
                cli_arr.append('ipv6 vrrp-extended vrid ' + str(vrid))
                cli_arr.append('backup')
                cli_arr.append('ipv6-address ' + vip)
                cli_arr.append('activate')
        try:
            cli_res = callback(cli_arr, handler='cli-set')
            pyswitch.utilities.check_mlx_cli_set_error(cli_res)
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('failed to create/delete VRRP vip %s' % (reason))

    def vrrpe_vmac(self, **kwargs):
        """Set vrrpe virtual mac.

        Args:
            int_type (str): Type of interface. (ethernet and ve).
            name (str): Name of interface. (1/1 , 10  etc).
            vrid (str): vrrpev3 ID.
            enable (bool): If vrrpe virtual MAC should be enabled
                or disabled.Default:``True``.
            get (bool): Get config instead of editing config. (True, False)
            virtual_mac (str):Virtual mac-address in the format
            HHHH.HHHH.HHHH
            callback (function): A function executed upon completion
            of the  method.

        Returns:
            Return True or virtual mac.
        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vmac` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vmac` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.12.91']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.services.vrrpe(enable=False)
            ...         output = dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89',vrid='1',
            ...         vip='2002:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         output = dev.services.vrrpe(enable=False)
            ...         output = dev.interface.vrrpe_vmac(int_type='ve',
            ...         name='89', vrid='1', virtual_mac='aaaa.bbbb.cccc')
        """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        enable = kwargs.pop('enable', True)
        version = kwargs.pop('version', 4)
        get = kwargs.pop('get', False)
        virtual_mac = kwargs.pop('virtual_mac', False)

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ethernet', 've']
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if get:
            vrid_match = r'VRID (\d+)'
            vmac_match = r'virtual mac (.+)'
            if version == 4:
                cli_cmd = 'show ip vrrp-extended ' + int_type + ' ' + name
            else:
                cli_cmd = 'show ipv6 vrrp-extended ' + int_type + ' ' + name

            output = callback(cli_cmd, handler='cli-get')

            if(re.search(r'error', output)):
                raise ValueError('VRRP-E is not configured or invalid input')

            vmac_get = False
            for line in output.split('\n'):
                if(re.search(vrid_match, line)):
                    node_vrid = re.search(vrid_match, line).group(1).strip()
                    if(node_vrid == vrid):
                        vmac_get = True
                elif(re.search(vmac_match, line)) and vmac_get:
                    vmac = re.search(vmac_match, line).group(1).strip()
                    return vmac

        if virtual_mac:
            cli_arr = []
            cli_arr.append('interface ' + int_type + ' ' + name)
            if version == 4:
                if not enable:
                    cli_arr.append('ip vrrp-extended vrid ' + str(vrid))
                    cli_arr.append('no virtual-mac ' + virtual_mac)
                else:
                    cli_arr.append('ip vrrp-extended vrid ' + str(vrid))
                    cli_arr.append('virtual-mac ' + virtual_mac)
            else:
                if not enable:
                    cli_arr.append('ipv6 vrrp-extended vrid ' + str(vrid))
                    cli_arr.append('no virtual-mac ' + virtual_mac)
                else:
                    cli_arr.append('ipv6 vrrp-extended vrid ' + str(vrid))
                    cli_arr.append('virtual-mac ' + virtual_mac)
            try:
                cli_res = callback(cli_arr, handler='cli-set')
                pyswitch.utilities.check_mlx_cli_set_error(cli_res)
                return True
            except Exception as error:
                reason = error.message
                raise ValueError('failed to create/delete VRRP vip %s' % (reason))

    def vrrpe_vrid(self, **kwargs):
        """Set/get vrrpe vrid.

        Args:
            int_type (str): Type of interface. (ethernet and ve).
            name (str): Name of interface. (4/6, VE name etc).
            vrid (str): vrrpev3 ID.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, the VIP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            callback (function): A function executed upon completion of the
                method.

        Raises:
            KeyError: if `int_type`, `name`, `vrid`,  is not passed.
            ValueError: if `int_type`, `name`, `vrid`,  is invalid.

        Returns:
            Return True or list of vrid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.12.91']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output =dev.interface.vrrpe_vrid(int_type='ve',
            ...         name='89', vrid='11')
            ...         output = dev.interface.vrrpe_vrid(get=True,
            ...         int_type='ve', name='89')
            ...         output =dev.interface.vrrpe_vrid(delete=True,
            ...         int_type='ve', name='89',vrid='1')
        """

        int_type = kwargs.pop('int_type').lower()
        version = kwargs.pop('version', 4)
        name = kwargs.pop('name', )
        get = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ve', 'ethernet']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if get:
            result = []
            vrid_match = r'VRID (\d+)'
            if version == 4:
                cli_cmd = 'show ip vrrp-extended ' + int_type + ' ' + name
            else:
                cli_cmd = 'show ipv6 vrrp-extended ' + int_type + ' ' + name

            output = callback(cli_cmd, handler='cli-get')

            if(re.search(r'error', output)):
                raise ValueError('VRRP-E is not configured or invalid input')

            for line in output.split('\n'):
                if(re.search(vrid_match, line)):
                    vrid = re.search(vrid_match, line).group(1).strip()
                    result.append(vrid)
            return result

        vrid = kwargs.pop('vrid')
        cli_arr = []
        cli_arr.append('interface ' + int_type + ' ' + name)
        if version == 4:
            if delete:
                cli_arr.append('no ip vrrp-extended vrid ' + str(vrid))
            else:
                cli_arr.append('ip vrrp-extended vrid ' + str(vrid))
        else:
            if delete:
                cli_arr.append('no ipv6 vrrp-extended vrid ' + str(vrid))
            else:
                cli_arr.append('ipv6 vrrp-extended vrid ' + str(vrid))
        try:
            cli_res = callback(cli_arr, handler='cli-set')
            pyswitch.utilities.check_mlx_cli_set_error(cli_res)
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('failed to create/delete VRRP vrid group %s' % (reason))

    def vrrpe_spf_basic(self, **kwargs):
        """Set/get vrrpe short path forwarding.

        Args:
            int_type (str): Type of interface. (ethernet and ve).
            name (str): Name of interface. (1/1 , 10  etc).
            vrid (str): vrrpev3 ID.
            enable (bool): If vrrpe short path forwarding should be enabled
                or disabled.Default:``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion
            of the  method.

        Returns:
            Return True or False
        Raises:
            KeyError: if `int_type`, `name`, `vrid`, is not passed.
            ValueError: if `int_type`, `name`, `vrid`,  is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.12.91']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.services.vrrpe(enable=False)
            ...         output = dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89',vrid='1',
            ...         vip='2002:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         output = dev.services.vrrpe(enable=False)
            ...         output = dev.interface.vrrpe_spf_basic(int_type='ve',
            ...         name='89', vrid='1')
        """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        enable = kwargs.pop('enable', True)
        version = kwargs.pop('version', 4)
        get = kwargs.pop('get', False)

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ethernet', 've']
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if get:
            vrid_match = r'VRID (\d+)'
            spf_match = r'short-path-forwarding (.+)'
            if version == 4:
                cli_cmd = 'show ip vrrp-extended ' + int_type + ' ' + name
            else:
                cli_cmd = 'show ipv6 vrrp-extended ' + int_type + ' ' + name

            output = callback(cli_cmd, handler='cli-get')

            if(re.search(r'error', output)):
                raise ValueError('VRRP-E is not configured or invalid input')

            spf_get = False
            for line in output.split('\n'):
                if(re.search(vrid_match, line)):
                    node_vrid = re.search(vrid_match, line).group(1).strip()
                    if(node_vrid == vrid):
                        spf_get = True
                elif(re.search(spf_match, line)) and spf_get:
                    spf_status = re.search(spf_match, line).group(1).strip()
                    if(spf_status == 'disabled'):
                        return False
                    else:
                        return True

        cli_arr = []
        cli_arr.append('interface ' + int_type + ' ' + name)
        if version == 4:
            if not enable:
                cli_arr.append('ip vrrp-extended vrid ' + str(vrid))
                cli_arr.append('no short-path-forwarding')
            else:
                cli_arr.append('ip vrrp-extended vrid ' + str(vrid))
                cli_arr.append('short-path-forwarding')
        else:
            if not enable:
                cli_arr.append('ipv6 vrrp-extended vrid ' + str(vrid))
                cli_arr.append('no short-path-forwarding')
            else:
                cli_arr.append('ipv6 vrrp-extended vrid ' + str(vrid))
                cli_arr.append('short-path-forwarding')
        try:
            cli_res = callback(cli_arr, handler='cli-set')
            pyswitch.utilities.check_mlx_cli_set_error(cli_res)
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('failed to create/delete VRRP vip %s' % (reason))

    def get_eth_l3_interfaces(self, **kwargs):
        """list[dict]: A list of dictionary items describing ethernet l3
        interfaces

        Args:
            callback (function): A function executed upon completion of the
                method
        Returns:
            Return list of dict containing ethernet l3 interface info

        Raises:
            None

        Examples:
            >>> import pyswitch.device
            >>> conn = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.get_eth_l3_interfaces()
        """
        eth_l3_list = []
        callback = kwargs.pop('callback', self._callback)
        cli_arr = 'show ip interface | inc eth'
        output = callback(cli_arr, handler='cli-get')
        error = re.search(r'Error(.+)', output)
        if error:
            raise ValueError("%s" % error.group(0))
        # Populate the VE interface list with default data and update later
        for line in output.split('\n'):
            if(re.search(r'eth ', line)):
                info = re.split('\s+', line)
                eth_id = info[1]
                if_name = info[0] + ' ' + info[1]
                eth_info = {'interface-type': 'ethernet',
                            'interface-name': str(eth_id),
                            'if-name': if_name,
                            'interface-state': info[5],
                            'interface-proto-state': info[6],
                            'ip-address': info[2]}

                eth_l3_list.append(eth_info)
        return eth_l3_list

    def vrrpe_supported_intf(self, **kwargs):
        """
        validate vrrpe supported interface type

        Args:
        intf_type(str): 've' or 'ethernet'
        Returns:
                   None
        Raises:
             valueError if intf type is not ve or ethernet

        Examples:
            >>> import pyswitch.device
            >>> conn = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.vrrpe_supported_intf('ethernet')
        """
        valid_int_types = ['ethernet', 've']
        int_type = kwargs.pop('intf_type').lower()
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

    @property
    def get_vlans(self):
        """ Get the list of VLAN configured
        Args:
            None
        Returns:
            List of VLANs
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth_snmp = ('admin', 'admin', None,
            >>>              {'version': 2,
            >>>               'snmpport': 161,
            >>>               'snmpv2c': 'public',
            >>>               'v3user':'',
            >>>               'v3priv':'', 'v3auth':'',
            >>>               'authpass':'', 'privpass':''})
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth_snmp=auth_snmp) as dev:
            ...         output = dev.interface.get_vlans
        """
        vlan_oid = SnmpMib.mib_oid_map['dot1qVlanStaticEntry']
        config = {}
        config['oid'] = vlan_oid
        config['columns'] = {5: 'row_status'}
        config['fetch_all'] = False
        list = []
        vlan_table = self._callback(config, handler='snmp-walk')
        for row in vlan_table.rows:
            vlan = row['_row_id']
            list.append(vlan)
        return list

    def get_vlan_port_map(self, untagged_ports):
        """ Get the list of ports associated with vlan
            Each element in the list is a dict containing vlan and list of interfaces
            [{'vlan':10, 'interfaces':[1/1, 2/1]}, {'vlan': 20, 'interfaces':[4/1]}]
        Args:
            None
            untagged_ports (bool) - True/False
        Returns:
            List of dictionary of vlan->port mappings
            if untagged_ports is True get the list of vlan->untagged port mappings
            else get the list of vlan->tagged+untagged port mappings
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth_snmp = ('admin', 'admin', None,
            >>>              {'version': 2,
            >>>               'snmpport': 161,
            >>>               'snmpv2c': 'public',
            >>>               'v3user':'',
            >>>               'v3priv':'', 'v3auth':'',
            >>>               'authpass':'', 'privpass':''})
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth_snmp=auth_snmp) as dev:
            ...         output = dev.interface.get_vlan_port_map(untagged_ports=False)
            ...         output = dev.interface.get_vlan_port_map(untagged_ports=True)
        """
        vlan_oid = SnmpMib.mib_oid_map['dot1qVlanStaticEntry']
        config = {}
        config['oid'] = vlan_oid
        if untagged_ports:
            config['columns'] = {4: 'ports'}
        else:
            config['columns'] = {2: 'ports'}
        config['fetch_all'] = False
        vlan_table = self._callback(config, handler='snmp-walk')
        vlan_list = []
        for row in vlan_table.rows:
            key = row['_row_id']
            ports = row['ports']
            key_oid = [hex(ord(c)) for c in ports]
            # extract ports from each slot
            slot_octet = 1
            list = []
            # In SNMP output each slot occupies 6 octets (48 bits) accomodating 48 ports
            # Max slots is 32 and total octets is 192
            for i in range(0, 192, 6):
                slot_octet = key_oid[i: 6 + i]
                list.append(slot_octet)
            slot_num = 1
            port_list = []
            j = 0
            for slot in list:
                k = 0
                for octet in slot:
                    x = int(octet, 16)
                    for i in range(8):
                        if (x & (1 << i) != 0):
                            port = k + 8 - i
                            int_name = str(slot_num) + '/' + str(port)
                            port_list.append(int_name)
                    k = k + 8
                    j += 1
                slot_num += 1
            vlan = {'vlan': key,
                    'interfaces': port_list}
            vlan_list.append(vlan)
        return vlan_list

    def validate_interface_vlan(self, **kwargs):
        """ Check if interface vlan(s) mapping exist
        Args:
           vlan_list(str): List of VLAN's
           intf_type(str): interface type
           intf_name(str): interface name e.g 0/1, 2/1/1, 1, 2
           int_mode (str): intf mode. Not applicable for MLX
        Returns:
            True - if mapping of port->vlans exist
            False - if mapping doesn't exist
        Raises:
            KeyError - If input args vlan_list, int_name are not passed
            ValueError - invalid intf type
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth_snmp = ('admin', 'admin', None,
            >>>              {'version': 2,
            >>>               'snmpport': 161,
            >>>               'snmpv2c': 'public',
            >>>               'v3user':'',
            >>>               'v3priv':'', 'v3auth':'',
            >>>               'authpass':'', 'privpass':''})
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth_snmp=auth_snmp) as dev:
            ...         output = dev.interface.validate_interface_vlan(vlan_list=[100,200],
            ...         intf_type='ethernet', intf_name='2/1')
            ...         output = dev.interface.validate_interface_vlan(vlan_list=[100,200],
            ...         intf_type='port_channel', intf_name='10')
        """
        vlan_list = kwargs.pop('vlan_list')
        intf_name = kwargs.pop('intf_name')
        intf_type = kwargs.pop('intf_type')
        intf_mode = kwargs.pop('intf_mode', None)
        all_true = True
        if not (intf_type == 'ethernet' or intf_type == 'port_channel'):
            raise ValueError('Invalid interface type for MLX')
        if intf_type == 'port_channel':
            lag_name = self.get_lag_id_name_map(str(intf_name))
            if lag_name is None:
                raise ValueError('Invalid interface name')
            # get the member ports of LAG
            ifid_name = self.get_port_channel_member_ports(lag_name)
            # pick a member of port-channel
            if ifid_name:
                intf = ifid_name[next(iter(ifid_name))]
                intf_name = intf.strip('ethernet')
            else:
                # Port-channel doesn't have any member ports
                return False
        vlan_port = self.get_vlan_port_map(untagged_ports=False)
        untag_port = self.get_vlan_port_map(untagged_ports=True)
        entry3 = {}
        tagged_port = []
        tagged_list = []
        for entry1, entry2 in zip(vlan_port, untag_port):
            s = set(entry2['interfaces'])
            tagged_list = [x for x in entry1['interfaces'] if x not in s]
            entry3 = {'vlan': entry1['vlan'],
                      'interfaces': tagged_list}
            tagged_port.append(entry3)
        if intf_mode == 'access':
            temp_vlan_port = untag_port
        elif intf_mode == 'trunk':
            temp_vlan_port = tagged_port

        for vlan_id in vlan_list:
            is_vlan_present = False
            is_intf_name_present = False
            for entry in temp_vlan_port:
                if str(entry['vlan']) == str(vlan_id):
                    is_vlan_present = True
                    if intf_name in entry['interfaces']:
                        is_intf_name_present = True
                        break
                    else:
                        is_intf_name_present = False
                        break
                else:
                    continue
            # Given vlan is not matching with any vlan->port mapping
            if not is_vlan_present:
                all_true = False
                break
            if is_vlan_present and not is_intf_name_present:
                all_true = False
                break

        return all_true

    def mac_move_detect_enable(self, **kwargs):
        """Enable mac move detect. Not supported on MLX platform
        Args:
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True - delete mac move detection
                           False - Enable mac move detection
        Returns:
            error
        Raises:
            NotImplementedError
        """
        raise NotImplementedError("Not supported for MLX platform")

    def get_snmp_port_id_by_intf_name(self, int_type, int_name):
        """ Get SNMP port-id using interface type and name
        Args:
           int_type(str): interface type
           int_name(str): interface name e.g 0/1, 2/1/1, 1, 2
        Returns:
            snmp port-id
        Raises:
            ValueError - invalid intf type and name
        """

        try:
            ifname_Ids = self.get_interface_name_id_mapping()
            port_id = ifname_Ids[int_type + int_name]
        except KeyError:
            raise ValueError('Interface %s %s is not found on device' %
                (int_type, int_name))
        return port_id
