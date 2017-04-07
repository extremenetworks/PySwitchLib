from __future__ import absolute_import
import unittest
from pyswitch.device import Device
import pprint
import yaml
from attrdict import AttrDict


class DeviceTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DeviceTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch_slx/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.DeviceTestCase.switch

            self.switch_ip = switch.ip
            self.wrong_ip = switch.wrong_ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def test_firmware_version(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.firmware_version)

    def test_wrong_ip(self):
        self.conn = (self.wrong_ip, '22')
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.firmware_version)
