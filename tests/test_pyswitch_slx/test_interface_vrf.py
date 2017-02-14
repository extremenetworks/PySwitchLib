from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceVRFTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceVRFTestCase, self).__init__(*args, **kwargs)
        with open('config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceVRFTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

            self.vrf = str(switch.vrf)

            self.rd = str(switch.rd)

            self.afi = str(switch.afi)

            self.rt = str(switch.rt)

            self.rt_value = str(switch.rt_value)

            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrf(vrf_name=self.vrf,
                              rbridge_id=self.rbridge_id)

    def test_add_int_vrf(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.switchport(name=self.int_name,
                                     int_type=self.int_type,
                                     enabled=False)

            dev.interface.add_int_vrf(vrf_name=self.vrf,
                                      name=self.int_name,
                                      int_type=self.int_type,
                                      rbridge_id=self.rbridge_id)
            op = dev.interface.add_int_vrf(get=True,
                                           name=self.int_name,
                                           int_type=self.int_type,
                                           rbridge_id=self.rbridge_id)
            self.assertEqual(self.vrf, op)

            dev.interface.add_int_vrf(enable=False,
                                      name=self.int_name,
                                      int_type=self.int_type,
                                      rbridge_id=self.rbridge_id)
            op = dev.interface.add_int_vrf(get=True,
                                           name=self.int_name,
                                           int_type=self.int_type,
                                           rbridge_id=self.rbridge_id)
            self.assertIsNone(op)

    def test_vrf(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.vrf(vrf_name=self.vrf,
                                       rbridge_id=self.rbridge_id)
            output = dev.interface.vrf(get=True,
                                       rbridge_id=self.rbridge_id)
            self.assertIn(
                {'vrf_name': self.vrf}, output)
            output = dev.interface.vrf(vrf_name=self.vrf,
                                       rbridge_id=self.rbridge_id,
                                       delete=True)
            output = dev.interface.vrf(get=True,
                                       rbridge_id=self.rbridge_id)
            self.assertNotIn(
                {'vrf_name': self.vrf}, output)

    def test_vrf_afi(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrf_afi(
                vrf_name=self.vrf,
                afi='ipv4',
                rbridge_id=self.rbridge_id)

            op = dev.interface.vrf_afi(
                vrf_name=self.vrf,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertEqual({'ipv4': True, 'ipv6': False}, op)

            dev.interface.vrf_afi(
                vrf_name=self.vrf,
                afi='ipv4',
                rbridge_id=self.rbridge_id,
                delete=True)

            op = dev.interface.vrf_afi(
                vrf_name=self.vrf,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertEqual({'ipv4': False, 'ipv6': False}, op)

    def test_vrf_afi_ipv6(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrf_afi(
                vrf_name=self.vrf,
                afi='ipv6',
                rbridge_id=self.rbridge_id)

            op = dev.interface.vrf_afi(
                vrf_name=self.vrf,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertEqual({'ipv4': False, 'ipv6': True}, op)

            dev.interface.vrf_afi(
                vrf_name=self.vrf,
                afi='ipv6',
                rbridge_id=self.rbridge_id,
                delete=True)

            op = dev.interface.vrf_afi(
                vrf_name=self.vrf,
                rbridge_id=self.rbridge_id,
                get=True)
            self.assertEqual({'ipv4': False, 'ipv6': False}, op)

    def test_vrf_rd(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.vrf_route_distiniguisher(
                vrf_name=self.vrf, rbridge_id=self.rbridge_id, rd=self.rd)

            output = dev.interface.vrf_route_distiniguisher(
                get=True, vrf_name=self.vrf, rbridge_id=self.rbridge_id)
            print output
            self.assertIn({'rd': self.rd, 'vrf_name': self.vrf}, output)

            output = dev.interface.vrf_route_distiniguisher(
                vrf_name=self.vrf, delete=True, rbridge_id=self.rbridge_id,
                rd=self.rd)

    def test_vrf_afi_rt_evpn(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.vrf_afi_rt_evpn(
                vrf_name=self.vrf,
                rbridge_id=self.rbridge_id,
                afi=self.afi,
                rt=self.rt,
                rt_value=self.rt_value)

            output = dev.interface.vrf_afi_rt_evpn(
                vrf_name=self.vrf, afi=self.afi, rbridge_id=self.rbridge_id,
                get=True)
            self.assertIn({'afi': self.afi, 'rbridge_id': self.rbridge_id,
                           'rt': [
                               self.rt], 'rtvalue': [self.rt_value],
                           'vrf_name': self.vrf}, output)

            output = dev.interface.vrf_afi_rt_evpn(
                vrf_name=self.vrf,
                rbridge_id=self.rbridge_id,
                afi=self.afi,
                rt=self.rt,
                rt_value=self.rt_value,
                delete_rt=True)
            output = dev.interface.vrf_afi_rt_evpn(
                vrf_name=self.vrf, afi=self.afi,
                rbridge_id=self.rbridge_id, get=True)
            self.assertNotIn({'afi': self.afi,
                              'rbridge_id': self.rbridge_id, 'rt': [
                                  self.rt], 'rtvalue': [self.rt_value],
                              'vrf_name': self.vrf},
                             output)

    def test_fabric_isl(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            with self.assertRaises(ValueError) as context:
                dev.interface.fabric_isl(
                    int_type=self.int_type,
                    name=self.int_name,
                    enabled=False)
                print context

    def test_fabric_trunk(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            with self.assertRaises(ValueError) as context:
                dev.interface.fabric_trunk(
                    int_type=self.int_type, name=self.int_name, enabled=False)
                print context

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.vrf(vrf_name=self.vrf,
                              rbridge_id=self.rbridge_id, delete=True)
