from __future__ import absolute_import
import unittest
from pyswitch.device import Device
import pprint
import yaml
from attrdict import AttrDict


class FabricServiceTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(FabricServiceTestCase, self).__init__(*args, **kwargs)
        with open('tests/test_pyswitch/config.yaml') as fileobj:
            cfg = AttrDict(yaml.safe_load(fileobj))
            switch = cfg.FabricServiceTestCase.switch

            self.switch_ip = switch.ip
            self.switch_username = switch.username
            self.switch_pasword = switch.password
            self.conn = (self.switch_ip, '22')
            self.auth = (self.switch_username, self.switch_pasword)

    def test_fabric_service(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.fabric_service.trill_links)
