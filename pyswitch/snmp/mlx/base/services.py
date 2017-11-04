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

from pyswitch.snmp.base.services import Services as BaseServices
from pyswitch.snmp.SnmpMib import SnmpMib as SnmpMib
from pyswitch.snmp.base.interface import Interface as Interface
from hnmp import mac_address


class Services(BaseServices):
    """
    The Services class holds all relevent methods and attributes for enabling
    and disabling services, such as VRRP, ARP.

    Attributes:
        None
    """

    def __init__(self, callback):
        """
        Services object init.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            Services Object

        Raises:
            None
        """
        super(Services, self).__init__(callback)

    @property
    def arp(self, **kwargs):
        """ Get ARP details in dict
        Args:
            None
        Returns:
            Return dict containing ARP information
        Raises:
            None
        Examples:
        >>> import pyswitch.device
        >>> switches = ['10.24.85.107']
        >>> auth = ('admin', 'admin')
        >>> for switch in switches:
        ...     conn = (switch, '22')
        ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
        ...         output = dev.services.arp
        """
        arptable_oid = SnmpMib.mib_oid_map['ipNetToPhysicalEntry']
        config = {}
        config['oid'] = arptable_oid
        config['columns'] = {4: 'mac_address',
                             6: 'arp_type',
                             7: 'state'}

        config['fetch_all'] = False
        arp_list = []
        arp_table = self._callback(config, handler='snmp-walk')
        for row in arp_table.rows:
            mac_addr = row['mac_address']
            arp_type = row['arp_type']
            entry_type = 'invalid'
            if arp_type == 3:
                entry_type = 'dynamic'
            elif arp_type == 4:
                entry_type = 'static'
            state = row['state']
            if state == 1:
                is_resolved = True
            else:
                is_resolved = False
            key = row['_row_id']
            mac = mac_address(mac_addr)
            # Convert mac to xxxx.xxxx.xxxx format
            mac = mac.split(":")
            mac_addr = "".join(mac[0:2]) + "." + "".join(mac[2:4]) + "." + "".join(mac[4:6])
            key_list = key.split('.', 3)
            ifid = key_list[0]
            ip_address = key_list[3]
            age = 0  # TBD backend is setting as '0'. Need to extract from CLI if needed
            ifid_list = []
            ifid_list.append(ifid)
            interface_obj = Interface(self._callback)
            ifid_name_map = interface_obj.get_interface_id_name_mapping(ifname_list=ifid_list)
            if_name = ifid_name_map[ifid]
            if 'ethernet' in if_name:
                interface_type = 'ethernet'
                interface_name = if_name[8:]
            elif 'management' in if_name:
                interface_type = 'management'
                interface_name = if_name[10:]
            elif 've' in if_name:
                interface_type = 've'
                interface_name = if_name[2:]
            else:
                interface_type = 'unknown'
                interface_name = 'invalid'
            arp_dict = {'ip-address': ip_address,
                        'mac-address': mac_addr,
                        'interface-type': interface_type,
                        'interface-name': interface_name,
                        'is-resolved': is_resolved,
                        'age': age,
                        'entry-type': entry_type
                        }
            arp_list.append(arp_dict)
        return arp_list
