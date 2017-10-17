"""
Copyright 2017 Brocade Communications Systems, Inc

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

from hnmp import SNMP as SNMP
from hnmp import SNMPError as SNMPError
from hnmp import TYPES as TYPES
from hnmp import is_ipv4_address as is_ipv4_address
from hnmp import _convert_value_to_native as convert_value_to_native
from pysnmp.entity.rfc3413.oneliner import cmdgen

from pysnmp.proto.rfc1902 import (
    Integer,
    IpAddress,
    OctetString,
)


class SnmpUtils:

    """
        SNMP_DEVICE_MAP:
           This map  holds the mapping of sysobjectid to
        (devicetype, firmwaretype). The device which
        needs SNMPCLI device should be part of the list.
        E.g.
          'sysobjectid':('devicetype', 'ostype')

        DEVICE_FIRMWARE_MAP:
           This map consists of firmware name to SNMP OID
        through which firmwareversion can be obtained.
    """

    SNMP_DEVICE_MAP = {

        '1.3.6.1.4.1.1991.1.3.44.1.2': ('MLX16', 'NI'),
        '1.3.6.1.4.1.1991.1.3.44.2.2': ('MLX8', 'NI'),
        '1.3.6.1.4.1.1991.1.3.44.3.2': ('MLX4', 'NI'),
        '1.3.6.1.4.1.1991.1.3.44.4.2': ('MLX32', 'NI'),
        '1.3.6.1.4.1.1991.1.3.55.1.2': ('MLXXMR16', 'NI'),
        '1.3.6.1.4.1.1991.1.3.55.2.2': ('MLXXMR8', 'NI'),
        '1.3.6.1.4.1.1991.1.3.55.3.2': ('MLXXMR4', 'NI'),
        '1.3.6.1.4.1.1991.1.3.55.4.2': ('MLXXMR32', 'NI'),
        '1.3.6.1.4.1.1991.1.3.49.1': ('CES2024F', 'NI'),
        '1.3.6.1.4.1.1991.1.3.49.2': ('CES2024C', 'NI'),
        '1.3.6.1.4.1.1991.1.3.49.3': ('CES2048F', 'NI'),
        '1.3.6.1.4.1.1991.1.3.49.4': ('CES2048C', 'NI'),
        '1.3.6.1.4.1.1991.1.3.49.5': ('CES2048FX', 'NI'),
        '1.3.6.1.4.1.1991.1.3.49.6': ('CES2048CX', 'NI'),
        '1.3.6.1.4.1.1991.1.3.49.7': ('CES2024F4X', 'NI'),
        '1.3.6.1.4.1.1991.1.3.49.8': ('CES2024C4X', 'NI'),
        '1.3.6.1.4.1.1991.1.3.51.1': ('CER2024F', 'NI'),
        '1.3.6.1.4.1.1991.1.3.51.2': ('CER2024C', 'NI'),
        '1.3.6.1.4.1.1991.1.3.51.3': ('CER2048F', 'NI'),
        '1.3.6.1.4.1.1991.1.3.51.4': ('CER2048C', 'NI'),
        '1.3.6.1.4.1.1991.1.3.51.5': ('CER2048FX', 'NI'),
        '1.3.6.1.4.1.1991.1.3.51.6': ('CER2048CX', 'NI'),
        '1.3.6.1.4.1.1991.1.3.51.7': ('CER2024F4X', 'NI'),
        '1.3.6.1.4.1.1991.1.3.51.8': ('CER2024C4X', 'NI'),
    }

    DEVICE_FIRMWARE_MAP = {
        'NI': '1.3.6.1.4.1.1991.1.1.2.1.11.0',
    }


class SnmpConnector(SNMP):

    def __init__(self, host, port=161, timeout=1, retries=5, community="public", version=2,
                 username="", authproto="sha", authkey="", privproto="aes128", privkey=""):
        SNMP.__init__(self, host, port, timeout, retries, community, version, username, authproto,
                      authkey, privproto, privkey)

    def set_multiple(self, oid):
        """
        Sets a single OID value. If you do not pass value_type hnmp will
        try to guess the correct type. Autodetection is supported for:

        * int and float (as Integer, fractional part will be discarded)
        * IPv4 address (as IpAddress)
        * str (as OctetString)

        Unfortunately, pysnmp does not support the SNMP FLOAT type so
        please use Integer instead.
        """

        varbindlist = list()
        snmpsecurity = self._get_snmp_security()
        for i in range(len(oid)):
            value_type = None
            value = oid[i][1]
            if len(oid[i]) == 3:
                value_type = oid[i][2]

            if value_type is None:
                if isinstance(value, int):
                    data = Integer(value)
                elif isinstance(value, float):
                    data = Integer(value)
                elif isinstance(value, str):
                    if is_ipv4_address(value):
                        data = IpAddress(value)
                    else:
                        data = OctetString(value)
                else:
                    raise TypeError(
                        "Unable to autodetect type. Please pass one of "
                        "these strings as the value_type keyword arg: "
                        ", ".join(TYPES.keys())
                    )
            else:
                if value_type not in TYPES:
                    raise ValueError("'{}' is not one of the supported types: {}".format(
                        value_type,
                        ", ".join(TYPES.keys())
                    ))
                data = TYPES[value_type](value)
            oid_tup = (oid[i][0], data)
            varbindlist.append(oid_tup)

        try:
            engine_error, pdu_error, pdu_error_index, objects = self._cmdgen.setCmd(
                snmpsecurity,
                cmdgen.UdpTransportTarget((self.host, self.port), timeout=self.timeout,
                                          retries=self.retries),
                *varbindlist
            )
            if engine_error:
                raise SNMPError(engine_error)
            if pdu_error:
                raise SNMPError(pdu_error.prettyPrint())
        except Exception as e:
            raise SNMPError(e)

        _, value = objects[0]
        value = convert_value_to_native(value)
        return value

    def get_os_version(self, oid=None):
        if oid is not None:
            raw = self.get(oid)
            return raw
        return None
