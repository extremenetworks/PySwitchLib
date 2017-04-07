from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceVirtualPortTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceVirtualPortTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceVirtualPortTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

            self.loopback_id = str(switch.loopback_id)

            self.port_channel = str(switch.port_channel)
            self.vlan = str(switch.vlan)

            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)
            self.anycast_ip_address = str(switch.anycast_ip_address)
            self.anycast_ipv6_address = str(switch.anycast_ipv6_address)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.add_vlan_int(vlan_id=self.vlan)

    def test_create_loopback(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.create_loopback(
                lb_name=self.loopback_id, rbridge_id=self.rbridge_id)
            output = dev.interface.create_loopback(
                get=True, rbridge_id=self.rbridge_id)

            self.assertIn(self.loopback_id, output)

            output = dev.interface.create_loopback(
                lb_name=self.loopback_id, rbridge_id=self.rbridge_id,
                enable=False)
            output = dev.interface.create_loopback(
                get=True, rbridge_id=self.rbridge_id)
            self.assertNotIn(self.loopback_id, output)

    def test_create_ve(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.create_ve(
                ve_name=self.vlan, rbridge_id=self.rbridge_id)
            output = dev.interface.create_ve(
                get=True, rbridge_id=self.rbridge_id)

            self.assertIn(self.vlan, output)

            output = dev.interface.create_ve(
                ve_name=self.vlan, rbridge_id=self.rbridge_id, enable=False)
            output = dev.interface.create_ve(
                get=True, rbridge_id=self.rbridge_id)
            self.assertNotIn(self.vlan, output)

    def test_ip_anycast_gateway(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_ve(
                ve_name=self.vlan, rbridge_id=self.rbridge_id)

            output = dev.interface.ip_anycast_gateway(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                anycast_ip=self.anycast_ip_address)
            output = dev.interface.ip_anycast_gateway(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                get=True)
            self.assertIn(self.anycast_ip_address, output)
            dev.interface.ip_anycast_gateway(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                anycast_ip=self.anycast_ip_address,
                enable=False)
            output = dev.interface.ip_anycast_gateway(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                get=True)
            self.assertNotIn(self.anycast_ip_address, output)

            dev.interface.create_ve(
                ve_name=self.vlan, rbridge_id=self.rbridge_id, enable=False)

    def test_ipv6_anycast_gateway(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_ve(
                ve_name=self.vlan, rbridge_id=self.rbridge_id)

            output = dev.interface.ip_anycast_gateway(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                anycast_ip=self.anycast_ipv6_address)
            output = dev.interface.ip_anycast_gateway(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                get=True)
            self.assertIn(self.anycast_ipv6_address, output)
            dev.interface.ip_anycast_gateway(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                anycast_ip=self.anycast_ipv6_address,
                enable=False)
            output = dev.interface.ip_anycast_gateway(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                get=True)
            self.assertNotIn(self.anycast_ipv6_address, output)

            dev.interface.create_ve(
                ve_name=self.vlan, rbridge_id=self.rbridge_id, enable=False)

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.del_vlan_int(vlan_id=self.vlan)
