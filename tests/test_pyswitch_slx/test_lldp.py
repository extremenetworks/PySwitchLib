from __future__ import absolute_import
import unittest
from pyswitch.device import Device
import pprint
import yaml
from attrdict import AttrDict


class LLDPTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(LLDPTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch_slx/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.LLDPTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def test_lldp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.lldp.neighbors())
