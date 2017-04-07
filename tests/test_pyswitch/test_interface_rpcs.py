from __future__ import absolute_import

import pprint
import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceRPCTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceRPCTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceRPCTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)
            self.vlan = str(switch.vlan)
            self.portchannel_id = str(switch.portchannel_id)
            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)
            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        pass

        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.add_vlan_int(vlan_id=self.vlan)
            dev.interface.create_ve(
                ve_name=self.vlan, rbridge_id=self.rbridge_id)
            dev.interface.create_portchannel(name=self.portchannel_id)
            dev.interface.channel_group(
                name=self.int_name,
                int_type=self.int_type,
                port_int=self.portchannel_id,
                channel_type='standard',
                mode='active')

    def test_ve_interfaces(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            op = dev.interface.ve_interfaces()
            pprint.pprint(op)
            ve_names = [item['if-name'] for item in op]
            ve_name = 'Ve %s' % self.vlan
            self.assertIn(ve_name, ve_names)

    def test_port_channels(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            op = dev.interface.port_channels
            print op

            port_channel_list = [item['aggregator_id'] for item in op]
            self.assertIn(self.portchannel_id, port_channel_list)

    def test_port_vlans(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.interface.vlans)

    def test_switch_port_list(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.interface.switchport_list)

    def test_single_interface_detail(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.interface.single_interface_detail(
                int_type='tengigabitethernet', name='1/0/31'))
            pprint.pprint(dev.interface.single_interface_detail(
                int_type='port-channel', name=self.portchannel_id))

    def test_interface_detail(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.interface.interface_detail)

    def test_interfaces(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.interface.interfaces)

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.del_vlan_int(vlan_id=self.vlan)
            dev.interface.create_ve(
                ve_name=self.vlan, rbridge_id=self.rbridge_id, enable=False)
            dev.interface.remove_port_channel(port_int=self.portchannel_id)
            dev.interface.channel_group(
                name=self.int_name, int_type=self.int_type, delete=True)
