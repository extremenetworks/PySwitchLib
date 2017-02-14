from __future__ import absolute_import
import unittest
import pprint
from pyswitch.device import Device


class VCSTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = ('10.37.18.131', '22')
        self.auth = ('admin', 'password')
        self.vcs_ipv4_address = '10.37.18.190/20'
        self.vcs_ipv6_address = '2620:100:0:fe07:227:f8ff:fec9:b04c/64'

    def test_vcs(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            pprint.pprint(dev.vcs.vcs_nodes)

    def test_vcs_vip(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.vcs.vcs_vip(vip=self.vcs_ipv4_address)
            dev.vcs.vcs_vip(vip=self.vcs_ipv6_address)

            op = dev.vcs.vcs_vip(get=True)

            self.assertEqual({'ipv4_vip': self.vcs_ipv4_address,
                              'ipv6_vip': self.vcs_ipv6_address
                              }, op)

            dev.vcs.vcs_vip(vip=self.vcs_ipv4_address, delete=True)
            dev.vcs.vcs_vip(vip=self.vcs_ipv6_address, delete=True)
            op = dev.vcs.vcs_vip(get=True)
            self.assertEqual({'ipv4_vip': None, 'ipv6_vip': None
                              }, op)
