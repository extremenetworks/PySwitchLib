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

import sys
import logging
from pyswitch.snmp.snmpconnector import SnmpConnector as SNMPDevice
from pyswitch.snmp.snmpconnector import SNMPError as SNMPError
from pyswitch.AbstractDevice import AbstractDevice
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
#import pyswitch.os.base.snmp

import re

"""
ROUTER_ATTRS = ['snmp', 'interface', 'bgp', 'lldp', 'system', 'services',
             'fabric_service', 'vcs', 'isis', 'ospf', 'mpls']

NI_VERSIONS = {
    '6.1.0T163': {
        'snmp': pyswitch.os.base.snmp.SNMP,
    },
}
"""

class DeviceCommError(Exception):
    """
    Error with device communication.
    """
    pass


class Reply:
    def __init__(self, data):
        self.data = data


class SnmpCliDevice(AbstractDevice):
    """
    Device object holds the state for a single NOS device.

    Attributes:
        bgp: BGP related actions and attributes.
        interface: Interface related actions and attributes.
        snmp: SNMP related actions and attributes.
        lldp: LLDP related actions and attributes.
        system: System level actions and attributes.
    """

    def __init__(self, **kwargs):
        """

        """
        self.base = kwargs.pop('base')
        self._conn = kwargs.pop('conn')
        self.host = self._conn[0]
        self._auth = kwargs.pop('auth', (None, None))
        self._test = kwargs.pop('test', False)
        self._callback = kwargs.pop('callback', None)
        self._snmpVersion = kwargs.pop('snmpver', 2)
        self._snmpPort = kwargs.pop('snmpport', 161)
        self._snmpV2c = kwargs.pop('snmpv2c', 'public')

        if self._callback is None:
            self._callback = self._callback_main

        self._mgr = {}

        self.reconnect()

        version_list = self.firmware_version
        self._os_type = version_list[0][2]
        self.fullver = version_list[0][1]

        """
        thismodule = sys.modules[__name__]
        os_table = getattr(thismodule, '%s_VERSIONS' %
                           str(self.os_type).upper())

        if fullver in os_table:
           ver = fullver
        else:
           ver = util.get_two_tuple_version(fullver)


        for router_attr in ROUTER_ATTRS:
            if router_attr in os_table[ver]:
                setattr(
                    self.base,
                    router_attr,
                    os_table[ver][router_attr](
                        self._callback))
        """
        #setattr(self.base, 'snmp', NI_VERSIONS['6.1.0T163']['snmp'](self._callback))

        setattr(self, 'asset', self._mgr)


    def __enter__(self):
        if not 'cli' in self._mgr or not 'snmp' in self._mgr:
            self.reconnect()

        return self

    def __exit__(self, exctype, excisnt, exctb):
        if 'cli' in self._mgr or 'snmp' in self._mgr:
            self.close()
        pass

    @property
    def connection(self):
        """
        Poll if object is still connected to device in question.
        Args:
            None
        Returns:
            bool: True if connected, False if not.
        Raises:
            None
        """
        if self._test is False:
            return self._mgr['snmp'].connected
        else:
            return False

    @property
    def mac_table(self):
        """list[dict]: the MAC table of the device.

        """
        pass

    @property
    def os_type(self):
        return self._os_type

    @property
    def suports_rbridge(self):
        return False

    @property
    def firmware_version(self):
        """
        Returns firmware version.

        Args:
            None

        Returns:
            Dictionary

        Raises:
            None

        """
        return self._mgr['snmp'].get_os_version()

    def _callback_main(self, call, handler='snmp-get', target='running',
                       source='startup'):
        """
        Callback for SNMP/CLI calls.
        Args:
        Returns:
            None
        Raises:
            None
        """

        try:

            if handler == 'snmp-get':
                value = self._mgr['snmp'].get(call)
            elif handler == 'snmp-walk':
                value = self._mgr['snmp'].table(call)
            elif handler == 'snmp-set':
                if len(call) == 3:
                    value = self._mgr['snmp'].set(call[0], call[1], call[2])
                else:
                    value = self._mgr['snmp'].set(call[0], call[1])
            elif handler == 'snmp-set-multiple':
                value = self._mgr['snmp'].set_multiple(call)
            elif handler == "cli-set":
                self._mgr['cli'].enable()
                value = self._mgr['cli'].send_config_set(call)
            elif handler == "cli-get":
                value = self._mgr['cli'].send_command(call)
        except (SNMPError) as error:
            logging.error(error)
            raise DeviceCommError
        except:
            print "CLI error" 
            raise DeviceCommError

        return value

    def reconnect(self):
        """
        Reconnect session with device.

        Args:
            None

        Returns:
            bool: True if reconnect succeeds, False if not.

        Raises:
            None
        """
        if not 'snmp' in self._mgr:
            self._mgr['snmp'] = SNMPDevice(host=self.host, port=self._snmpPort,
                                           version=self._snmpVersion,
                                           community=self._snmpV2c)
	if not 'cli' in self._mgr:
            # FIXME: Revisit this logic
            opt = {'device_type': 'brocade_netiron'}
            opt['ip'] = self.host
            opt['username'] = self._auth[0]
            opt['password'] = self._auth[1]
            opt['global_delay_factor'] = 0.5
            # FIXME: Do we need to catch error??
            net_connect = None
            try:
                net_connect = ConnectHandler(**opt)
            except (NetMikoTimeoutException, NetMikoAuthenticationException,) as e:
                reason = e.message
                raise ValueError('Failed to execute valueerror cli on due to %s',  reason)
            except SSHException as e:
                reason = e.message
                raise ValueError('Failed to execute cli on due to %s', reason)
            except Exception as e:
                reason = e.message
                raise ValueError('Failed to execute due to %s', reason)

            if net_connect is not None:
                self._mgr['cli'] = net_connect

        return True

    def find_interface_by_mac(self, **kwargs):
        pass

    def close(self):
        if 'snmp' in self._mgr:
            del self._mgr['snmp']
        if 'cli' in self._mgr:
            self._mgr['cli'].disconnect()
            del self._mgr['cli']
        pass



if __name__  == '__main__':
    import time

    start = time.time()


    conn = ('10.24.85.107', '22')
    #conn = ('10.24.84.173', '22')
    auth = ('admin', 'admin')

    from pyswitch.device import Device
    dev = Device(conn=conn, auth=auth)

    #dev.interface.add_vlan_int(vlan_id='234')
    vers =  dev.firmware_version
    print vers[0][1]
     
    print dev.os_type
    print dev.suports_rbridge
    #print dev.interface.port_channels
    #print dev.mac_table
    #kwargs = {'handler': 'snmp-get', 'call': '1.3.6.1.2.1.1.2.0'}
    #descr = dev.snmp.test_snmpdev(handler='snmp-get', call='1.3.6.1.2.1.1.2.0')
    #print descr

    #config_commands = 'show interface eth 1/2'
    #output = dev.snmp.test_snmpdev(handler='cli-get', call=config_commands)
    #print output

    """
    from pyswitch.device import Device
    dev = Device(conn=conn, auth=auth)
    for vlan_id in range(2,4090):
        dev.interface.add_vlan_int(vlan_id=vlan_id)
    """
    end = time.time()
    print(end - start)
