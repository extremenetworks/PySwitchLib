from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceSwitchPort(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceSwitchPort, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch_slx/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceSwitchPort.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

            self.vlan = str(switch.vlan)
            self.second_vlan = str(switch.second_vlan)
            self.gvlan = str(switch.gvlan)

            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.switchport(name=self.int_name,
                                     int_type=self.int_type)
            dev.interface.add_vlan_int(vlan_id=self.vlan)
            dev.interface.add_vlan_int(vlan_id=self.second_vlan)

    def test_switchport(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.switchport(name=self.int_name,
                                              int_type=self.int_type)
            output = dev.interface.switchport(name=self.int_name,
                                              int_type=self.int_type,
                                              get=True)
            self.assertEqual(True, output)
            output = dev.interface.switchport(name=self.int_name,
                                              int_type=self.int_type,
                                              enabled=False)
            output = dev.interface.switchport(name=self.int_name,
                                              int_type=self.int_type,
                                              get=True)
            self.assertEqual(None, output)

    def test_enable_switchport(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.enable_switchport(
                inter_type=self.int_type, inter=self.int_name)
            output = dev.interface.switchport(name=self.int_name,
                                              int_type=self.int_type,
                                              get=True)
            self.assertEqual(True, output)

            dev.interface.disable_switchport(
                inter_type=self.int_type, inter=self.int_name)
            self.assertEqual(True, output)

    def test_trunk_mode(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.trunk_mode(name=self.int_name,
                                              int_type=self.int_type,
                                              mode='trunk')
            output = dev.interface.trunk_mode(name=self.int_name,
                                              int_type=self.int_type,
                                              get=True)
            self.assertEqual(output, 'trunk')

            output = dev.interface.trunk_mode(name=self.int_name,
                                              int_type=self.int_type,
                                              mode='trunk-no-default-native')
            output = dev.interface.trunk_mode(name=self.int_name,
                                              int_type=self.int_type,
                                              get=True)
            self.assertEqual(output, 'trunk-no-default-native')

    def test_access_mode(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.access_mode(name=self.int_name,
                                               int_type=self.int_type,
                                               mode='access')
            output = dev.interface.access_mode(name=self.int_name,
                                               int_type=self.int_type,
                                               get=True)
            self.assertEqual(output, 'access')

    def test_acc_vlan(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.access_mode(name=self.int_name,
                                      int_type=self.int_type,
                                      mode='access')
            dev.interface.acc_vlan(name=self.int_name,
                                   int_type=self.int_type,
                                   vlan=self.vlan)

            op = dev.interface.acc_vlan(name=self.int_name,
                                        int_type=self.int_type,
                                        get=True)
            self.assertEqual(self.vlan, op)

            dev.interface.acc_vlan(name=self.int_name,
                                   int_type=self.int_type,
                                   vlan=self.vlan, delete=True)

            op = dev.interface.acc_vlan(name=self.int_name,
                                        int_type=self.int_type,
                                        get=True)
            self.assertNotEqual(self.vlan, op)

    def test_trunk_allowed_vlan(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.trunk_mode(name=self.int_name,
                                     int_type=self.int_type,
                                     mode='trunk')
            dev.interface.trunk_allowed_vlan(name=self.int_name,
                                             int_type=self.int_type,
                                             vlan=self.vlan,
                                             action='add')
            dev.interface.trunk_allowed_vlan(name=self.int_name,
                                             int_type=self.int_type,
                                             vlan=self.second_vlan,
                                             action='add')
            op = dev.interface.trunk_allowed_vlan(name=self.int_name,
                                                  int_type=self.int_type,
                                                  get=True)
            self.assertEqual('%s,%s' % (self.vlan, self.second_vlan), op)

    def test_trunk_allowed_ctag_vlan(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.add_vlan_int(vlan_id=self.gvlan)
            dev.interface.trunk_mode(name=self.int_name,
                                     int_type=self.int_type,
                                     mode='trunk')
            dev.interface.trunk_allowed_vlan(name=self.int_name,
                                             int_type=self.int_type,
                                             vlan=self.gvlan,
                                             ctag=self.second_vlan,
                                             action='add')

    def test_access_vlan(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.access_vlan(
                inter_type=self.int_type,
                inter=self.int_name,
                vlan_id=self.vlan)

            dev.interface.del_access_vlan(
                inter_type=self.int_type,
                inter=self.int_name,
                vlan_id=self.vlan)

    def test_spanning_tree_state(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.spanning_tree_state(name=self.int_name,
                                              int_type=self.int_type,
                                              enabled=True)
            op = dev.interface.spanning_tree_state(name=self.int_name,
                                                   int_type=self.int_type,
                                                   get=True)

            self.assertTrue(op)

            dev.interface.spanning_tree_state(name=self.int_name,
                                              int_type=self.int_type,
                                              enabled=False)

            op = dev.interface.spanning_tree_state(name=self.int_name,
                                                   int_type=self.int_type,
                                                   get=True)
            self.assertFalse(op)

    def test_tag_native_vlan(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.trunk_mode(name=self.int_name,
                                     int_type=self.int_type,
                                     mode='trunk')
            output = dev.interface.tag_native_vlan(name=self.int_name,
                                                   int_type=self.int_type)
            output = dev.interface.tag_native_vlan(name=self.int_name,
                                                   int_type=self.int_type,
                                                   get=True)
            self.assertTrue(output)
            output = dev.interface.tag_native_vlan(
                name=self.int_name,
                int_type=self.int_type, enabled=False)
            output = dev.interface.tag_native_vlan(name=self.int_name,
                                                   int_type=self.int_type,
                                                   get=True)

            self.assertIsNone(output)

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.switchport(name=self.int_name,
                                     int_type=self.int_type,
                                     enabled=False)
            dev.interface.del_vlan_int(vlan_id=self.vlan)
            dev.interface.del_vlan_int(vlan_id=self.second_vlan)
