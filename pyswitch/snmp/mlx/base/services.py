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
import pyswitch.utilities
import re


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
            mac_addr = pyswitch.utilities.convert_mac_colon_to_dot_format(mac)
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

    @property
    def mac_table(self, **kwargs):
        """ Get mac address details in dict
        Args:
            None
        Returns:
            Return list of dict containing MAC information
        Raises:
            None
        Examples:
        >>> import pyswitch.device
        >>> switches = ['10.24.85.107']
        >>> auth = ('admin', 'admin')
        >>> for switch in switches:
        ...     conn = (switch, '22')
        ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
        ...         output = dev.services.mac_table
        """
        mactable_oid = SnmpMib.mib_oid_map['dot1qTpFdbEntry']
        config = {}
        config['oid'] = mactable_oid
        config['columns'] = {2: 'port',
                             3: 'status'}

        config['fetch_all'] = False
        mac_list = []
        mac_table = self._callback(config, handler='snmp-walk')
        for row in mac_table.rows:
            ifid = row['port']
            ifid_list = []
            ifid_list.append(ifid)
            interface_obj = Interface(self._callback)
            ifid_name_map = interface_obj.get_interface_id_name_mapping(ifname_list=ifid_list)
            if_name = ifid_name_map[ifid]
            if 'ethernet' in if_name:
                interface_type = 'ethernet'
                interface_name = if_name[8:]
            elif 'LAG' in if_name:
                interface_type = 'port-channel'
                interface_name = if_name[3:]
            else:
                interface_type = 'unknown'
                interface_name = 'unknown'
            status = row['status']
            if status == 5:
                mac_type = 'static'
            elif status == 3:
                mac_type = 'dynamic'
            else:
                mac_type = 'invalid'
            key = row['_row_id']
            key_list = key.split('.', 1)
            vlan = key_list[0]
            int_arr = key_list[1].split('.')
            mac = [format(int(i), '02x') for i in int_arr]
            mac_addr = ":".join(mac)
            interface = interface_type + interface_name
            mac_list.append(dict(mac_address=mac_addr, interface_type=interface_type,
                              interface_name=interface_name, interface=interface,
                              state='active', vlan=vlan, type=mac_type))
        return mac_list

    def vrrpe(self, **kwargs):
        """Enable or Disable Vrrpe.
        Args:
            ip_version (str): The IP version ('4' or '6') for which vrrpe
                should be enabled/disabled.  Default: `4`.
            enable (bool): If vrrpe should be enabled or disabled.  Default:
                ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.
        Returns:
            Return True.

        Raises:
            ValueError if VRRP-E set/get fails

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.12.91', '10.24.12.95']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.services.vrrpe(enable=False)
            ...         dev.services.vrrpe(enable=True)
            ...         dev.services.vrrpe()
            Traceback (most recent call last):
            KeyError
        """
        ip_version = kwargs.pop('ip_version', '4')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        if get:
            enable = None

        if get:
            try:
                cli_cmd = 'show ip vrrp-extended'
                output = callback(cli_cmd, handler='cli-get')
                if(re.search(r'is not enabled', output)):
                    ipv4_vrrpe = False
                else:
                    ipv4_vrrpe = True

                cli_cmd = 'show ipv6 vrrp-extended'
                output = callback(cli_cmd, handler='cli-get')
                if(re.search(r'is not enabled', output)):
                    ipv6_vrrpe = False
                else:
                    ipv6_vrrpe = True

                return {'ipv4_vrrpe': ipv4_vrrpe, 'ipv6_vrrpe': ipv6_vrrpe}

            except Exception as error:
                reason = error.message
                raise ValueError('Failed to get VRRP-E status %s' % (reason))

        cli_arr = []
        if int(ip_version) == 4:
            if not enable:
                cli_arr.append('no router vrrp-extended')
            else:
                cli_arr.append('router vrrp-extended')
        else:
            if not enable:
                cli_arr.append('no ipv6 router vrrp-extended')
            else:
                cli_arr.append('ipv6 router vrrp-extended')

        try:
            cli_res = callback(cli_arr, handler='cli-set')
            pyswitch.utilities.check_mlx_cli_set_error(cli_res)
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to create VRRP-E router %s' % (reason))
