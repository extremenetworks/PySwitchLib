from pprint import pprint

import unittest2 as unittest

import pyswitchlib.asset


class TestVlan(unittest.TestCase):

    def setUp(self):
        self.nos = pyswitchlib.asset.Asset(ip_addr='10.24.81.125',
                                           auth=('admin', 'password'),
                                           fw_ver='nos7.0.1')

    def test_vlan_create(self):
        pprint(self.nos.vlan_create(vlan=10))
        # assert(false)

    def test_vlan_update(self):

        pprint(self.nos.vlan_update(vlan=10,
                                    description='this_is_a_test_for_vlan_10'))

    def test_vlan_delete(self):
        pprint(self.nos.vlan_delete(vlan=10))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
