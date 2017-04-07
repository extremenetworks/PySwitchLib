from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfacePortChannelCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfacePortChannelCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfacePortChannelCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)
            self.portchannel_id = str(switch.portchannel_id)
            self.minimum_links = str(switch.minimum_links)
            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)
            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        pass

    def test_remove_port_channel(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_portchannel(name=self.portchannel_id)
            dev.interface.remove_port_channel(port_int=self.portchannel_id)
            op = dev.interface.create_portchannel(
                name=self.portchannel_id, get=True)
            self.assertIsNone(op)

    def test_port_channel(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_portchannel(name=self.portchannel_id)
            op = dev.interface.create_portchannel(
                name=self.portchannel_id, get=True)
            self.assertIsNotNone(op)
            dev.interface.create_portchannel(
                name=self.portchannel_id, enable=False)

            op = dev.interface.create_portchannel(
                name=self.portchannel_id, get=True)
            self.assertIsNone(op)

    def test_port_channel_create(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_portchannel(name=self.portchannel_id)
            output = dev.interface.channel_group(
                name=self.int_name,
                int_type=self.int_type,
                port_int=self.portchannel_id,
                channel_type='standard',
                mode='active')
            output = dev.interface.channel_group(
                name=self.int_name, int_type=self.int_type, get=True)
            self.assertEqual(output,
                             {'port_int': self.portchannel_id,
                              'channel_type': 'standard',
                              'mode': 'active'})
            output = dev.interface.channel_group(
                name=self.int_name, int_type=self.int_type, delete=True)
            output = dev.interface.channel_group(
                name=self.int_name, int_type=self.int_type, get=True)
            self.assertEqual(
                output, {
                    'port_int': None, 'channel_type': None, 'mode': None})

    def test_port_channel_minimum_links(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_portchannel(name=self.portchannel_id)

            output = dev.interface.port_channel_minimum_links(
                name=self.portchannel_id, minimum_links=self.minimum_links)
            output = dev.interface.port_channel_minimum_links(
                name=self.portchannel_id, get=True)
            self.assertEqual(self.minimum_links, output)
            dev.interface.remove_port_channel(port_int=self.portchannel_id)

    def test_port_channel_speed(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_portchannel(name=self.portchannel_id)

            output = dev.interface.port_channel_speed(
                name=self.portchannel_id, po_speed='100000')
            output = dev.interface.port_channel_speed(
                name=self.portchannel_id, get=True)
            self.assertEqual('100000', output)
            dev.interface.remove_port_channel(port_int=self.portchannel_id)

