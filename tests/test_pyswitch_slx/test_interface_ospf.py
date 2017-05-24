from __future__ import absolute_import

import unittest

import yaml
from attrdict import AttrDict

from pyswitch.device import Device


class InterfaceOSPFTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InterfaceOSPFTestCase, self).__init__(*args, **kwargs)
        with open('config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.InterfaceOSPFTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password

            self.area = str(switch.area)
            self.intf_name = str(switch.intf_name)
            self.intf_type = str(switch.intf_type)

            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def setUp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.services.ospf()
            op = dev.services.ospf(get=True)
            self.assertEqual(op)
            dev.ospf.ospf_area(area='10')
            op = dev.ospf.ospf_area(get=True)
            self.assertEqual(op)

            dev.services.ospf(vrf='111')
            op = dev.services.ospf(get=True, vrf='111')
            self.assertEqual(op)
            dev.ospf.ospf_area(vrf='111', area='10')
            op = dev.ospf.ospf_area(get=True, vrf='111')
            self.assertEqual(op)

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.ospf.ospf_area(delete=True)
            dev.services.ospf(enable=False)

            dev.ospf.ospf_area(vrf='111', delete=True)
            dev.services.ospf(enable=False, vrf='111')

    def test_enable_ospf_on_intf(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.ip_ospf(
                intf_type='loopback',
                intf_name='11'
                area='10')
            op = dev.interface.ip_ospf(
                intf_type='loopback',
                intf_name='11',
                get=True)
            self.assertEqual(op)
