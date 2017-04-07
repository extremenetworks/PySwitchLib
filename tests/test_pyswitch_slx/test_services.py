from __future__ import absolute_import
import unittest
from pyswitch.device import Device
import yaml
from attrdict import AttrDict


class ServicesTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ServicesTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch_slx/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.ServicesTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.rbridge_id = str(switch.rbridge_id)

    def setUp(self):

        self.conn = (self.switch_ip, '22')
        self.auth = (self.switch_username, self.switch_pasword)
        """
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.anycast_mac(rbridge_id=self.rbridge_id,
                                  delete=True)
        """

    def test_vrrp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.services.vrrp(rbridge_id=self.rbridge_id, enable=True)
            dev.services.vrrp(
                rbridge_id=self.rbridge_id,
                ip_version='6',
                enable=True)
            op = dev.services.vrrp(rbridge_id=self.rbridge_id, get=True)
            self.assertTrue(op['ipv4_vrrp'])
            self.assertTrue(op['ipv6_vrrp'])
            dev.services.vrrp(rbridge_id=self.rbridge_id, enable=False)
            dev.services.vrrp(
                rbridge_id=self.rbridge_id,
                ip_version='6',
                enable=False)
            op = dev.services.vrrp(rbridge_id=self.rbridge_id, get=True)

            self.assertFalse(op['ipv4_vrrp'])
            self.assertFalse(op['ipv6_vrrp'])

    def test_vrrpe(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.services.vrrpe(rbridge_id=self.rbridge_id, enable=True)
            dev.services.vrrpe(
                rbridge_id=self.rbridge_id,
                ip_version='6',
                enable=True)
            op = dev.services.vrrpe(rbridge_id=self.rbridge_id, get=True)
            self.assertTrue(op['ipv4_vrrpe'])
            self.assertTrue(op['ipv6_vrrpe'])

            dev.services.vrrpe(rbridge_id=self.rbridge_id, enable=False)
            dev.services.vrrpe(
                rbridge_id=self.rbridge_id,
                ip_version='6',
                enable=False)
            op = dev.services.vrrpe(rbridge_id=self.rbridge_id, get=True)
            self.assertFalse(op['ipv4_vrrpe'])
            self.assertFalse(op['ipv6_vrrpe'])
