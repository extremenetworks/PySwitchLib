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
        if self.has_rbridge_id:
            return 'rbridge_id_%s' % method
        else:
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
            vlan_id: ID for the VLAN interface being created. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        try:
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
            return False

    def get_vlan_int(self, vlan_id):
        try:
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
            return False
