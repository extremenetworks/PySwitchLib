from __future__ import absolute_import
import unittest
from pyswitch.device import Device
import pprint
import yaml
from attrdict import AttrDict

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
class DeviceTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DeviceTestCase, self).__init__(*args, **kwargs)
        with open('config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.DeviceTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)


    def test_wrong_ip_address(self):
        self.conn = ('10.31.18.231', '22')
        with self.assertRaises(Exception) as context:
            with Device(conn=self.conn, auth=self.auth) as dev:
                dev.firmware_version


    def test_firmware_version(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.firmware_version)

    def test_mac_table(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.mac_table)

    def test_find_interface_by_mac(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(
                dev.find_interface_by_mac(
                    mac_address='11:12:12:32:23:23'))
