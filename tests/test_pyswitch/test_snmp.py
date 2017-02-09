from __future__ import absolute_import
import unittest
from pyswitch.device import Device


class SNMPTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = ('10.37.18.131', '22')
        self.auth = ('admin', 'password')

    def test_snmp_community(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.snmp.add_snmp_community(community='anm')
            dev.snmp.del_snmp_community(community='anm')

    def test_snmp_host(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.snmp.add_snmp_community(community='anm')
            dev.snmp.add_snmp_host(
                community='anm', host_info=(
                    '10.32.45.12', '123'))
            dev.snmp.del_snmp_host(
                community='anm', host_info=(
                    '10.32.45.12', '123'))
