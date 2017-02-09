import unittest
from pynos.device import Device


class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = ('10.37.18.131', '22')
        self.auth = ('admin', 'password')

    def test_bgp_enabled(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.bgp.local_asn(local_as='65535', vrf='test_ipv4',
                                       rbridge_id='1')

            output = dev.interface.interface_detail
            print output
