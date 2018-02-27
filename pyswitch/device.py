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

from pyswitch.RestDevice import RestDevice
from pyswitch.NetConfDevice import NetConfDevice
from pyswitch.SnmpCliDevice import SnmpCliDevice
from pyswitch.snmp.snmpconnector import SnmpConnector as SNMPDevice
from pyswitch.snmp.snmpconnector import SnmpUtils as SNMPUtils
from pyswitch.snmp.snmpconnector import SNMPError as SNMPError
from pyswitch.snmp.SnmpMib import SnmpMib as MIB


class Reply:

    def __init__(self, xml):
        self.data = xml


# pylint: disable=E1101
class Device(object):
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
        kwargs['base'] = self
        self.connection_type = kwargs.get('connection_type', 'REST')

        conn = kwargs.get('conn')
        host = conn[0]
        auth_snmp = kwargs.get('auth_snmp', (None, None, None, None))

        snmpconfig = auth_snmp[3]
        snmpver = 0
        sysobj = ''

        if snmpconfig:
            snmpport = snmpconfig['snmpport']
            snmpver = snmpconfig['version']
            snmpv2c = snmpconfig['snmpv2c']
            v3user = snmpconfig['v3user']
            v3auth = snmpconfig['v3auth']
            v3priv = snmpconfig['v3priv']
            authpass = snmpconfig['authpass']
            privpass = snmpconfig['privpass']

        if snmpver == 2 or snmpver == 3:
            try:
                snmpdev = SNMPDevice(host=host, port=snmpport, version=snmpver, community=snmpv2c,
                                     username=v3user, authproto=v3auth, authkey=authpass,
                                     privproto=v3priv, privkey=privpass, timeout=0.5, retries=1)
                sysobj = str(snmpdev.get(MIB.mib_oid_map['sysObjectId']))
            except SNMPError:
                """
                   if SNMP is not supported then fallback to other connection type
                """
                pass

        if sysobj in SNMPUtils.SNMP_DEVICE_MAP:
            self.connection_type = 'SNMPCLI'

        if self.connection_type is 'SNMPCLI':
            self.device_type = SnmpCliDevice(sysobj, **kwargs)
        if self.connection_type is 'REST':
            self.device_type = RestDevice(**kwargs)
        elif self.connection_type is 'NETCONF':
            self.device_type = NetConfDevice(**kwargs)

    def __enter__(self):
        self.device_type.__enter__()
        return self

    def __exit__(self, exctype, excisnt, exctb):
        return self.device_type.__exit__(exctype, excisnt, exctb)

    @property
    def asset(self):
        return self.device_type._mgr

    @property
    def os_type(self):
        return self.device_type.os_type

    @property
    def suports_rbridge(self):
        return self.device_type.suports_rbridge

    @property
    def platform_type(self):
        return self.device_type.platform_type

    @property
    def firmware_version(self):
        return self.device_type.firmware_version

    def _callback_main(self, call, handler='edit_config', target='running',
                       source='startup'):
        return self.device_type.__callback_main(self, call, handler, target, source)

    def reconnect(self):
        return self.device_type.reconnect()

    def find_interface_by_mac(self, **kwargs):
        return self.device_type.find_interface_by_mac(**kwargs)

    def close(self):
        return self.device_type.close()
