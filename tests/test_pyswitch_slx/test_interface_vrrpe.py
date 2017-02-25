from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceVRRPETestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceVRRPETestCase, self).__init__(*args, **kwargs)
        with open('config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceVRRPETestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

            self.vrid = str(switch.vrid)
            self.second_vrid = str(switch.second_vrid)
            self.vip = str(switch.vip)
            self.ipv6_vip = str(switch.ipv6_vip)
            self.ipv6_add = str(switch.ipv6_add)
            self.vrid = str(switch.vrid)
            self.ipv6_vrid = str(switch.ipv6_vrid)
            self.vlan = str(switch.vlan)

            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.services.vrrp(rbridge_id=self.rbridge_id, enable=False)
            dev.services.vrrp(
                rbridge_id=self.rbridge_id,
                ip_version='6',
                enable=False)

            dev.services.vrrpe(rbridge_id=self.rbridge_id, enable=True)
            dev.services.vrrpe(
                rbridge_id=self.rbridge_id,
                enable=True,
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
                enable=False)

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

    def test_vrrpe_vrid(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id)
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.second_vrid,
                version=4,
                rbridge_id=self.rbridge_id)
            op = dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                version=4,
                rbridge_id=self.rbridge_id,
                get=True)

            self.assertIn(self.vrid, op)
            self.assertIn(self.second_vrid, op)

            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.ipv6_vrid,
                version=6,
                rbridge_id=self.rbridge_id)
            op = dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                version=6,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertIn(self.ipv6_vrid, op)

            # Delete
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id,
                delete=True)
            op = dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                version=4,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertNotIn(self.vrid, op)

            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.ipv6_vrid,
                version=6,
                rbridge_id=self.rbridge_id,
                delete=True)
            op = dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                version=6,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertNotIn(self.ipv6_vrid, op)

    def test_vrrpe_ve_spf(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id)

            dev.interface.vrrpe_spf_basic(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.vip,
                version=4,
                rbridge_id=self.rbridge_id)

            op = dev.interface.vrrpe_spf_basic(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertTrue(op)

            dev.interface.vrrpe_spf_basic(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.vip,
                version=4,
                rbridge_id=self.rbridge_id, enable=False)

            op = dev.interface.vrrpe_spf_basic(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertIsNone(op)

    def test_vrrpe_ve_spf_ipv6(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=6,
                rbridge_id=self.rbridge_id)

            dev.interface.vrrpe_spf_basic(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=6,
                rbridge_id=self.rbridge_id)

            op = dev.interface.vrrpe_spf_basic(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=6,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertTrue(op)

            dev.interface.vrrpe_spf_basic(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.vip,
                version=6,
                rbridge_id=self.rbridge_id, enable=False)

            op = dev.interface.vrrpe_spf_basic(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=6,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertIsNone(op)

    def test_vrrpe_ve_vip(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id)
            dev.interface.ip_address(name=self.vlan,
                                     int_type='ve',
                                     ip_addr='9.9.19.1/24')
            dev.interface.vrrpe_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.vip,
                rbridge_id=self.rbridge_id)

            op = dev.interface.vrrpe_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertIn({'vrid': self.vrid, 'vip': self.vip}, op)

            dev.interface.vrrpe_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.vip,
                rbridge_id=self.rbridge_id,
                delete=True)

            op = dev.interface.vrrpe_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertNotIn({'vrid': self.vrid, 'vip': self.vip}, op)

            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id,
                delete=True)

    def test_vrrpe_vip_ve_ipv6(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=6,
                rbridge_id=self.rbridge_id)
            dev.interface.ip_address(name=self.vlan,
                                     int_type='ve',
                                     ip_addr=self.ipv6_add)
            dev.interface.vrrpe_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.ipv6_vip,
                rbridge_id=self.rbridge_id)

            op = dev.interface.vrrpe_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=6,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertIn({'vrid': self.vrid, 'vip': self.ipv6_vip}, op)

            dev.interface.vrrpe_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                vip=self.ipv6_vip,
                rbridge_id=self.rbridge_id,
                delete=True)

            op = dev.interface.vrrpe_vip(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                rbridge_id=self.rbridge_id,
                get=True)

            self.assertNotIn({'vrid': self.vrid, 'vip': self.ipv6_vip}, op)

            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=6,
                rbridge_id=self.rbridge_id,
                delete=True)

    def test_vrrpe_vip_vmac(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=4,
                rbridge_id=self.rbridge_id)
            dev.interface.vrrpe_vmac(int_type='ve',
                                     name=self.vlan,
                                     vrid=self.vrid,
                                     rbridge_id=self.rbridge_id,
                                     virtual_mac='02e0.5200.00xx')
            op = dev.interface.vrrpe_vmac(int_type='ve',
                                          name=self.vlan,
                                          vrid=self.vrid,
                                          rbridge_id=self.rbridge_id,
                                          get=True)

            self.assertEqual('02e0.5200.00xx', op)
            dev.interface.vrrpe_vmac(int_type='ve',
                                     name=self.vlan,
                                     vrid=self.vrid,
                                     rbridge_id=self.rbridge_id,
                                     virtual_mac='02e0.5200.00xx',
                                     delete=True)
            op = dev.interface.vrrpe_vmac(int_type='ve',
                                          name=self.vlan,
                                          vrid=self.vrid,
                                          rbridge_id=self.rbridge_id,
                                          get=True)

            self.assertIsNone(op)

    def test_vrrpe_vip_ipv6_vmac(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrrpe_vrid(
                int_type='ve',
                name=self.vlan,
                vrid=self.vrid,
                version=6,
                rbridge_id=self.rbridge_id)
            dev.interface.vrrpe_vmac(int_type='ve',
                                     name=self.vlan,
                                     vrid=self.vrid,
                                     rbridge_id=self.rbridge_id,
                                     version=6,
                                     virtual_mac='02e0.5200.00xx')
            op = dev.interface.vrrpe_vmac(int_type='ve',
                                          name=self.vlan,
                                          vrid=self.vrid,
                                          version=6,
                                          rbridge_id=self.rbridge_id,
                                          get=True)

            self.assertEqual('02e0.5200.00xx', op)
            dev.interface.vrrpe_vmac(int_type='ve',
                                     name=self.vlan,
                                     vrid=self.vrid,
                                     rbridge_id=self.rbridge_id,
                                     version=6,
                                     virtual_mac='02e0.5200.00xx',
                                     delete=True)
            op = dev.interface.vrrpe_vmac(int_type='ve',
                                          name=self.vlan,
                                          vrid=self.vrid,
                                          version=6,
                                          rbridge_id=self.rbridge_id,
                                          get=True)

            self.assertisNone(op)
