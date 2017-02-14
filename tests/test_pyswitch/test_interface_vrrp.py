from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceVRRPTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceVRRPTestCase, self).__init__(*args, **kwargs)
        with open('config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceVRRPTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

            self.vrid = str(switch.vrid)
            self.vip = str(switch.vip)
            self.ipv6_vip = str(switch.ipv6_vip)
            self.ipv6_add = str(switch.ipv6_add)
            self.vrid = str(switch.vrid)
            self.ipv6_vrid = str(switch.ipv6_vrid)
            self.vlan = str(switch.vlan)
            self.priority = str(switch.priority)

            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.services.vrrpe(rbridge_id=self.rbridge_id, enable=False)
            dev.services.vrrpe(
                rbridge_id=self.rbridge_id,
                ip_version='6',
                enable=False)

            dev.services.vrrp(rbridge_id=self.rbridge_id, enable=True)
            dev.services.vrrp(
                rbridge_id=self.rbridge_id,
                enabled=True,
                ip_version='6')
            dev.interface.add_vlan_int(self.vlan)

            dev.interface.create_ve(
                ve_name=self.vlan,
                rbridge_id=self.rbridge_id)

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.services.vrrp(rbridge_id=self.rbridge_id, enable=False)
            dev.services.vrrp(
                rbridge_id=self.rbridge_id,
                ip_version='6',
                enabled=False)

            dev.services.vrrpe(rbridge_id=self.rbridge_id, enable=False)
            dev.services.vrrpe(
                rbridge_id=self.rbridge_id,
                enable=False,
                ip_version='6')

            dev.interface.del_vlan_int(self.vlan)

            dev.interface.create_ve(
                ve_name=self.vlan,
                rbridge_id=self.rbridge_id,
                enable=False)

    def test_vrrp_ve_ipv6_vmac(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrrp_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id)

            dev.interface.vrrpe_vmac(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                virtual_mac='aaaa.bbbb.cccc',
                version=6,
                rbridge_id=self.rbridge_id)

    def test_vrrp_ve_vip(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.ip_address(name=self.vlan,
                                     int_type='ve',
                                     ip_addr='9.9.19.1/24')
            dev.interface.vrrp_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id)

            dev.interface.vrrp_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.vip,
                rbridge_id=self.rbridge_id)

            op = dev.interface.vrrp_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertEqual(op, self.vip)

            dev.interface.vrrp_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.vip,
                rbridge_id=self.rbridge_id,
                delete=True)

            op = dev.interface.vrrp_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertIsNone(op, self.vip)

            dev.interface.vrrp_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id,
                delete=True)

    def test_vrrp_ve_priority(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.ip_address(name=self.vlan,
                                     int_type='ve',
                                     ip_addr='9.9.19.1/24')
            dev.interface.vrrp_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id)

            dev.interface.vrrp_priority(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                ip_version=4,
                rbridge_id=self.rbridge_id,
                priority=self.priority)

            op = dev.interface.vrrp_priority(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                ip_version=4,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertEqual(op, self.priority)

            dev.interface.vrrp_priority(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                ip_version=4,
                rbridge_id=self.rbridge_id,
                priority=self.priority,
                delete=True)

            op = dev.interface.vrrp_priority(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                ip_version=4,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertIsNone(op)

            dev.interface.vrrp_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id,
                delete=True)
