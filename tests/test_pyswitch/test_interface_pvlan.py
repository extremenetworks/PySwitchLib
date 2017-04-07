from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfacePrivateVlanTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfacePrivateVlanTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfacePrivateVlanTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

            self.pvlan = str(switch.pvlan)
            self.svlan = str(switch.svlan)

            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.add_vlan_int(vlan_id=self.pvlan)
            dev.interface.add_vlan_int(vlan_id=self.svlan)
            dev.interface.switchport(name=self.int_name,
                                     int_type=self.int_type)

    def test_private_vlan_type(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.private_vlan_type(name=self.pvlan,
                                            pvlan_type='isolated')
            op = dev.interface.private_vlan_type(get=True, name=self.pvlan)
            self.assertEqual(op, 'isolated')

    def test_vlan_pvlan_association_add(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.private_vlan_type(name=self.pvlan,
                                            pvlan_type='primary')
            dev.interface.private_vlan_type(name=self.svlan,
                                            pvlan_type='isolated')
            dev.interface.vlan_pvlan_association_add(
                name=self.pvlan, sec_vlan=self.svlan)
            op = dev.interface.vlan_pvlan_association_add(
                get=True, name=self.pvlan)
            self.assertEqual(op, self.svlan)

    def test_switchport_pvlan_mapping(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.private_vlan_mode(name=self.int_name,
                                            int_type=self.int_type,
                                            mode='promiscuous')
            dev.interface.private_vlan_type(name=self.pvlan,
                                            pvlan_type='primary')
            dev.interface.private_vlan_type(name=self.svlan,
                                            pvlan_type='isolated')
            dev.interface.vlan_pvlan_association_add(
                name=self.pvlan, sec_vlan=self.svlan)

            dev.interface.switchport_pvlan_mapping(
                int_type=self.int_type,
                name=self.int_name,
                pri_vlan=self.pvlan,
                sec_vlan=self.svlan)
            op = dev.interface.switchport_pvlan_mapping(
                int_type=self.int_type,
                name=self.int_name,
                get=True)
            self.assertEqual(
                {'pri_vlan': self.pvlan, 'sec_vlan': self.svlan}, op)
            dev.interface.switchport_pvlan_mapping(
                int_type=self.int_type,
                name=self.int_name,
                pri_vlan=self.pvlan,
                sec_vlan=self.svlan, delete=True)
            op = dev.interface.switchport_pvlan_mapping(
                int_type=self.int_type,
                name=self.int_name,
                get=True)
            self.assertNotEqual(
                {'pri_vlan': self.pvlan, 'sec_vlan': self.svlan}, op)

    def test_private_vlan_mode(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.private_vlan_mode(name=self.int_name,
                                                     int_type=self.int_type,
                                                     mode='trunk_promiscuous')
            output = dev.interface.private_vlan_mode(name=self.int_name,
                                                     int_type=self.int_type,
                                                     get=True)

            self.assertEqual(output, 'trunk_promiscuous')
            output = dev.interface.private_vlan_mode(name=self.int_name,
                                                     int_type=self.int_type,
                                                     mode='host')

            output = dev.interface.private_vlan_mode(name=self.int_name,
                                                     int_type=self.int_type,
                                                     get=True)
            self.assertEqual(output, 'host')

    def test_pvlan_host_association(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.private_vlan_type(name=self.pvlan,
                                                     pvlan_type='primary')
            output = dev.interface.private_vlan_type(name=self.svlan,
                                                     pvlan_type='isolated')
            output = dev.interface.vlan_pvlan_association_add(
                name=self.pvlan, sec_vlan=self.svlan)
            output = dev.interface.private_vlan_mode(name=self.int_name,
                                                     int_type=self.int_type,
                                                     mode='host')
            output = dev.interface.pvlan_host_association(
                int_type=self.int_type,
                name=self.int_name,
                pri_vlan=self.pvlan,
                sec_vlan=self.svlan)

            output = dev.interface.pvlan_host_association(
                int_type=self.int_type, name=self.int_name, get=True)
            self.assertEqual(output, (self.pvlan, self.svlan))

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.del_vlan_int(vlan_id=self.pvlan)
            dev.interface.del_vlan_int(vlan_id=self.svlan)

            dev.interface.switchport(name=self.int_name,
                                     int_type=self.int_type,
                                     enabled=False)
