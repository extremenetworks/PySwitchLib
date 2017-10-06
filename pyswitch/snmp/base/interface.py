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

from pyswitch.snmp.SnmpMib import SnmpMib as SnmpMib
from pyswitch.exceptions import InvalidVlanId


class Interface(object):
    """
    The Interface class holds all the actions assocaiated with the Interfaces
    of a SNMPCLI device.

    Attributes:
        None
    """

    @property
    def valid_int_types(self):

        return []

    @property
    def valid_intp_types(self):

        return []

    @property
    def l2_mtu_const(self):
        return (None, None)

    @property
    def has_rbridge_id(self):
        return False

    def method_prefix(self, method):
        return method

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
        self._callback = callback

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
        pass

    def del_vlan_int(self, vlan_id):
        """
        Delete VLAN Interface.

        Args:
            vlan_id (int): ID for the VLAN interface being deleted. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            InvalidVlanId, ValueError

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.85.107', '22')
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     vlan_list = [300]
            ...     output = dev.interface.add_vlan_int(vlan_list, 'vlan_300')
            ...     output = dev.interface.get_vlan_int(300)
            ...     assert output == True
            ...     ret = dev.interface.del_vlan_int(300)
            ...     assert ret == True
        """
        try:
            if vlan_id < 1 and vlan_id > 4090:
                raise InvalidVlanId("VLAN id must be between 1-4090")
            row_status = SnmpMib.mib_oid_map['dot1qVlanStaticRowStatus']
            oid = row_status + "." + str(vlan_id)
            config = (oid, 6)
            ret_value = self._callback(config, handler='snmp-set')
            if ret_value:
                return True
            else:
                return False

        except Exception as error:
            reason = error.message
            raise ValueError('Failed to delete VLAN %d due to %s', vlan_id, reason)

    def get_vlan_int(self, vlan_id):
        """
        Get VLAN Interface.

        Args:
            vlan_id: ID for the VLAN interface being queried. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            InvalidVlanId

        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.85.107', '22')
            >>> auth = ('admin', 'admin')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     vlan_list = [300]
            ...     output = dev.interface.add_vlan_int(vlan_list, 'vlan_300')
            ...     ret = dev.interface.get_vlan_int(300)
            ...     assert ret == True
        """
        try:
            if vlan_id < 1 and vlan_id > 4090:
                raise InvalidVlanId("VLAN id must be between 1-4090")
            row_status = SnmpMib.mib_oid_map['dot1qVlanStaticRowStatus']
            # Get the rowstatus for vlan_id if it exists
            oid = row_status + "." + str(vlan_id)
            ret_value = self._callback(oid, handler='snmp-get')
            if ret_value:
                return True
            else:
                return False

        except Exception as error:
            reason = error.message
            raise ValueError('Failed to get VLAN %d due to %s', vlan_id, reason)

    def get_interface_name_id_mapping(self, ifname_list=None):
        """
        convert interface names to interface id. Function accepts a list of interface names \
        for which interface id is needed. If list is empty all interface name->id map is \
        returned

        Args:
            ifname_list (list): List of interfaces for which ifid is required ['ethernet1/1']

        Returns:
            dictionary of ifname to id mappings

        Raises:
            None

        """
        ifXtable_oid = SnmpMib.mib_oid_map['ifXEntry']
        config = {}
        config['oid'] = ifXtable_oid
        config['columns'] = {1: 'if_name'}
        config['fetch_all'] = False
        ifname_table = self._callback(config, handler='snmp-walk')
        ifname_to_id_map = {}
        for row in ifname_table.rows:
            if_name, value = row['if_name'], row['_row_id']
            ifname_to_id_map.update({if_name: value})

        if ifname_list is None:
            return ifname_to_id_map
        # Build a dict of ifname to id mappings for the interfaces and return
        ifname_dict = {}
        for item in ifname_list:
            ifname_dict.update({item: ifname_to_id_map[item]})
        return ifname_dict

    def get_interface_id_name_mapping(self, ifname_list=None):
        """
        convert interface id to name. Function accepts a list of interface ids \
        for which interface name is needed. If list is empty all interface id->name map is \
        returned
        Args:
            ifname_list (list): List of interfaces for which ifname is required [1, 2]

        Returns:
            dictionary of ifid to ifname mappings

        Raises:
            None

        """
        ifXtable_oid = SnmpMib.mib_oid_map['ifXEntry']
        config = {}
        config['oid'] = ifXtable_oid
        config['columns'] = {1: 'if_name'}
        config['fetch_all'] = False
        ifname_table = self._callback(config, handler='snmp-walk')
        ifid_to_name_map = {}
        for row in ifname_table.rows:
            if_name, if_id = row['if_name'], row['_row_id']
            ifid_to_name_map.update({if_id: if_name})

        if ifname_list is None:
            return ifid_to_name_map
        # Build a dict of id to ifname id mappings for the interfaces and return
        ifname_dict = {}
        for item in ifname_list:
            ifname_dict.update({item: ifid_to_name_map[str(item)]})
        return ifname_dict
