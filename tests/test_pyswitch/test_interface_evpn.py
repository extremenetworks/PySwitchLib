from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceEVPNTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceEVPNTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceEVPNTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

            self.evpn = str(switch.evpn)
            self.duplicate_mac_timer_value = str(
                switch.duplicate_mac_timer_value)
            self.max_count = str(switch.max_count)

            self.bfd_rx = str(switch.bfd_rx)
            self.bfd_tx = str(switch.bfd_tx)
            self.bfd_multiplier = str(switch.bfd_multiplier)
            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_evpn_instance(rbridge_id=self.rbridge_id,
                                               evpn_instance_name=self.evpn)

    def test_create_evpn(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.create_evpn_instance(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn)
            output = dev.interface.create_evpn_instance(
                rbridge_id=self.rbridge_id, get=True)
            self.assertEqual(output['instance_name'], self.evpn)
            output = dev.interface.create_evpn_instance(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn,
                enable=False)
            output = dev.interface.create_evpn_instance(
                rbridge_id=self.rbridge_id, get=True)
            self.assertIsNone(output['instance_name'])

    def test_create_evpn_instance_rt_both_ignore_as(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.evpn_instance_rt_both_ignore_as(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn)
            output = dev.interface.create_evpn_instance(
                rbridge_id=self.rbridge_id, get=True,
                evpn_instance_name=self.evpn)
            print output
            output = dev.interface.evpn_instance_rt_both_ignore_as(
                rbridge_id=self.rbridge_id, get=True)
            self.assertTrue(output)
            output = dev.interface.evpn_instance_rt_both_ignore_as(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn,
                enable=False)
            output = dev.interface.evpn_instance_rt_both_ignore_as(
                rbridge_id=self.rbridge_id, get=True)
            self.assertIsNone(output)

    def test_evpn_instance_duplicate_mac_timer(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.evpn_instance_duplicate_mac_timer(
                rbridge_id=self.rbridge_id,
                evpn_instance_name=self.evpn,
                duplicate_mac_timer_value=self.duplicate_mac_timer_value)
            output = dev.interface.evpn_instance_duplicate_mac_timer(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn,
                get=True)
            print output
            self.assertEqual(output, self.duplicate_mac_timer_value)

            dev.interface.evpn_instance_duplicate_mac_timer(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn,
                enable=False)

            output = dev.interface.evpn_instance_duplicate_mac_timer(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn,
                get=True)
            print output
            self.assertIsNone(output)

    def test_evpn_instance_mac_timer_max_count(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.evpn_instance_mac_timer_max_count(
                rbridge_id=self.rbridge_id,
                evpn_instance_name=self.evpn,
                max_count=self.max_count)
            output = dev.interface.evpn_instance_mac_timer_max_count(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn,
                get=True)
            print output
            self.assertEqual(output, self.max_count)

            dev.interface.evpn_instance_mac_timer_max_count(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn,
                enable=False)
            output = dev.interface.evpn_instance_mac_timer_max_count(
                rbridge_id=self.rbridge_id, evpn_instance_name=self.evpn,
                get=True)
            print output
            self.assertIsNone(output)

    def test_evpn_instance_mac_timer_max_count_1(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.evpn_instance_rd_auto(
                rbridge_id=self.rbridge_id,
                evpn_instance_name=self.evpn)

            self.assertIsNone(output)

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_evpn_instance(rbridge_id=self.rbridge_id,
                                               evpn_instance_name=self.evpn,
                                               enable=False)
