from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceOverlayGatewayTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceOverlayGatewayTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceOverlayGatewayTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

            self.gw_name = str(switch.gw_name)
            self.loopback_id = str(switch.loopback_id)

            self.int_name = str(switch.int_name)
            self.int_type = str(switch.int_type)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_loopback(
                lb_name=self.loopback_id,
                rbridge_id=self.rbridge_id)

    def test_overlay_gateway_create_and_delete(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            # Create
            dev.interface.overlay_gateway_name(gw_name=self.gw_name)
            gw_name = dev.interface.overlay_gateway_name(get=True)
            # print 'Created Gateway: %s' % gw_name
            self.assertEqual(gw_name, self.gw_name)

            dev.interface.overlay_gateway_name(
                gw_name=self.gw_name, delete=True)
            gw_name = dev.interface.overlay_gateway_name(get=True)
            # print 'Deleted Gateway: %s' % gw_name
            self.assertEqual(gw_name, None)

    def test_overlay_gateway_activate(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.overlay_gateway_name(gw_name=self.gw_name)
            dev.interface.overlay_gateway_activate(
                gw_name=self.gw_name)
            activated = dev.interface.overlay_gateway_activate(
                gw_name=self.gw_name, get=True)
            # print 'Activate State: %s' % activated
            self.assertEqual(activated, True)

    def test_overlay_gateway_deactivate(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.overlay_gateway_name(gw_name=self.gw_name)
            dev.interface.overlay_gateway_activate(
                gw_name=self.gw_name)
            activated = dev.interface.overlay_gateway_activate(
                gw_name=self.gw_name, get=True)
            # print 'Activate State: %s' % activated
            self.assertEqual(activated, True)

            # Deactivated
            dev.interface.overlay_gateway_activate(
                gw_name=self.gw_name, delete=True)
            activated = dev.interface.overlay_gateway_activate(
                gw_name=self.gw_name, get=True)
            # print 'Activate State: %s' % activated
            self.assertEqual(activated, None)

    def test_overlay_gateway_type(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.overlay_gateway_name(gw_name=self.gw_name)
            dev.interface.overlay_gateway_type(
                gw_name=self.gw_name, gw_type='layer2-extension')

            type = dev.interface.overlay_gateway_type(
                gw_name=self.gw_name, get=True)
            self.assertEqual(type, 'layer2-extension')

    def test_overlay_gateway_loopback_id(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.overlay_gateway_name(gw_name=self.gw_name)

            dev.interface.overlay_gateway_loopback_id(
                gw_name=self.gw_name, loopback_id=self.loopback_id)
            output = dev.interface.overlay_gateway_loopback_id(
                gw_name=self.gw_name, get=True)

            self.assertEqual(output, self.loopback_id)

            output = dev.interface.overlay_gateway_loopback_id(
                gw_name=self.gw_name, delete=True)
            output = dev.interface.overlay_gateway_loopback_id(
                gw_name=self.gw_name, get=True)

            self.assertIsNone(output, self.loopback_id)

    def test_overlay_gateway_vlan_vni_auto(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.overlay_gateway_name(gw_name=self.gw_name)
            dev.interface.overlay_gateway_type(
                gw_name=self.gw_name, gw_type='layer2-extension')
            dev.interface.overlay_gateway_activate(
                gw_name=self.gw_name)
            dev.interface.overlay_gateway_vlan_vni_auto(
                gw_name=self.gw_name)

            output = dev.interface.overlay_gateway_vlan_vni_auto(
                gw_name=self.gw_name, get=True)
            # print 'vlan_vni_auto %s' % output

            self.assertEqual(output, True)

            dev.interface.overlay_gateway_vlan_vni_auto(
                gw_name=self.gw_name, delete=True)
            output = dev.interface.overlay_gateway_vlan_vni_auto(
                gw_name=self.gw_name, get=True)
            # print 'vlan_vni_auto %s' % output
            self.assertEqual(output, None)

    def test_overlay_gateway_attach_rbridge_id(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.overlay_gateway_name(gw_name=self.gw_name)
            dev.interface.overlay_gateway_loopback_id(
                gw_name=self.gw_name, loopback_id=self.loopback_id)
            dev.interface.overlay_gateway_attach_rbridge_id(
                gw_name=self.gw_name, rbridge_id=self.rbridge_id)
            rb_id = dev.interface.overlay_gateway_attach_rbridge_id(
                gw_name=self.gw_name, get=True)
            # print 'attach_rbridge_id %s' % rb_id
            self.assertEqual(rb_id, '1')

            dev.interface.overlay_gateway_attach_rbridge_id(
                gw_name=self.gw_name, rbridge_id='1', delete=True)
            rb_id = dev.interface.overlay_gateway_attach_rbridge_id(
                gw_name=self.gw_name, get=True)
            # print 'attach_rbridge_id %s' % rb_id
            self.assertEqual(rb_id, None)

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_loopback(lb_name=self.loopback_id,
                                          rbridge_id=self.rbridge_id,
                                          enable=False)
            dev.interface.overlay_gateway_name(gw_name=self.gw_name,
                                               delete=True)
