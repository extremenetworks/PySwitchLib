from __future__ import absolute_import

import unittest

from pyswitch.device import Device


class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.switch_ip = '10.24.4.215'
        self.rbridge_id = '1'
        self.auth = ('admin', 'password')
        self.int_name = '3/4'
        self.vlan = '34'
        self.port_int = '21'
        self.loopback_id = '12'
        self.conn = (self.switch_ip, '22')
        self.admin_password = 'password'
        self.auth = ('admin', self.admin_password)
        self.int_type = 'ethernet'
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_portchannel(name=self.port_int)
            dev.interface.add_vlan_int(self.vlan)
            dev.interface.create_ve(
                ve_name=self.vlan,
                rbridge_id=self.rbridge_id)
            dev.interface.create_loopback(
                lb_name=self.loopback_id,
                rbridge_id=self.rbridge_id)

    def test_ipv6_address(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.ip_address(
                int_type='loopback',
                name='1',
                rbridge_id=self.rbridge_id,
                ip_addr='fc01:1:3:1ad3:0:0:23:a/128')
            dev.interface.ip_address(
                int_type='loopback',
                name='1',
                rbridge_id=self.rbridge_id,
                ip_addr='fc01:1:3:1ad3:0:0:23:a/128',
                delete=True)

            dev.interface.ip_address(
                int_type='loopback',
                name='1',
                rbridge_id=self.rbridge_id,
                ip_addr='10.32.35.2/32')
            dev.interface.ip_address(
                int_type='loopback',
                name='1',
                rbridge_id=self.rbridge_id,
                ip_addr='10.32.35.2/32',
                delete=True)

    def test_set_address(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            # Create

            dev.interface.ip_address(
                int_type='tengigabitethernet',
                name='1/0/6',
                ip_addr='10.32.45.1/24')
            """
            dev.interface.ip_address(int_type='tengigabitethernet',
             name='1/0/6', ip_addr='fc00:1:3:1ad3:0:0:23:a/64')
            dev.interface.ip_address(int_type='loopback',
             name=self.rbridge_id, rbridge_id=self.rbridge_id,
             ip_addr='10.32.35.2/32')
            dev.interface.ip_address(int_type='loopback',
            name='1', rbridge_id=self.rbridge_id,
                                     ip_addr='fc01:1:3:1ad3:0:0:23:a/128')
            dev.interface.ip_address(int_type='ve', name='1',
            rbridge_id=self.rbridge_id, ip_addr='10.32.55.2/24')
            dev.interface.ip_address(int_type='ve', name='1',
             rbridge_id=self.rbridge_id, ip_addr='fc02:1:3:1ad3:0:0:23:a/64')

            ## Delete
            dev.interface.ip_address(int_type='tengigabitethernet',
             name='1/0/6', ip_addr='10.32.45.1/24', delete=True)
            dev.interface.ip_address(int_type='tengigabitethernet',
             name='1/0/6', ip_addr='fc00:1:3:1ad3:0:0:23:a/64',
                                     delete=True)

            dev.interface.ip_address(int_type='loopback', name='1',
            rbridge_id=self.rbridge_id, ip_addr='10.32.35.2/32',
                                     delete=True)
            dev.interface.ip_address(int_type='loopback', name='1',
            rbridge_id=self.rbridge_id,
                    ip_addr='fc01:1:3:1ad3:0:0:23:a/128', delete=True)

            dev.interface.ip_address(int_type='ve', name='1',
            rbridge_id=self.rbridge_id, ip_addr='10.32.55.2/24', delete=True)
            dev.interface.ip_address(int_type='ve', name='1',
            rbridge_id=self.rbridge_id, ip_addr='fc02:1:3:1ad3:0:0:23:a/64',
                                     delete=True)

            print dev.interface.ip_address(int_type='ve', name='1',
            rbridge_id=self.rbridge_id, ip_addr='10.32.55.2/24', get=True)
            print dev.interface.ip_address(int_type='loopback', name='1',
             rbridge_id=self.rbridge_id, ip_addr='10.32.35.2/32',
                                           get=True)
            print dev.interface.ip_address(int_type='tengigabitethernet',
            name='1/0/6', ip_addr='10.32.45.1/24',
                                           get=True)

            print dev.interface.get_ip_addresses(
            int_type='tengigabitethernet', name='1/0/16', version=4)
            """

    def test_admin_sate_ethernet(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.admin_state(
                int_type=self.int_type,
                name=self.int_name,
                enabled=True)
            op = dev.interface.admin_state(
                int_type=self.int_type, name=self.int_name, get=True)
            self.assertTrue(op)
            dev.interface.admin_state(
                int_type=self.int_type,
                name=self.int_name,
                enabled=False)
            op = dev.interface.admin_state(
                int_type=self.int_type, name=self.int_name, get=True)
            self.assertFalse(op)

    def test_admin_state_ve(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.admin_state(
                rbridge_id=self.rbridge_id,
                int_type='ve',
                name=self.vlan,
                enabled=False)
            op = dev.interface.admin_state(
                rbridge_id=self.rbridge_id,
                int_type='ve',
                name=self.vlan,
                get=True)
            self.assertFalse(op)
            dev.interface.admin_state(
                rbridge_id=self.rbridge_id, int_type='ve', name=self.vlan,
                enabled=True)
            op = dev.interface.admin_state(
                rbridge_id=self.rbridge_id,
                int_type='ve',
                name=self.vlan,
                get=True)
            self.assertTrue(op)

    def test_admin_sate_port_channel(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.admin_state(
                int_type='port_channel', name=self.port_int, enabled=True)
            op = dev.interface.admin_state(
                int_type='port_channel', name=self.port_int, get=True)
            self.assertTrue(op)

            dev.interface.admin_state(
                int_type='port_channel', name=self.port_int, enabled=False)
            op = dev.interface.admin_state(
                int_type='port_channel', name=self.port_int, get=True)
            self.assertFalse(op)

    def test_admin_state_loopback(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.admin_state(
                rbridge_id=self.rbridge_id,
                int_type='loopback',
                name=self.loopback_id,
                enabled=False)
            op = dev.interface.admin_state(
                rbridge_id=self.rbridge_id,
                int_type='loopback',
                name=self.loopback_id,
                get=True)
            self.assertFalse(op)
            dev.interface.admin_state(
                rbridge_id=self.rbridge_id,
                int_type='loopback',
                name=self.loopback_id,
                enabled=True)
            op = dev.interface.admin_state(
                rbridge_id=self.rbridge_id,
                int_type='loopback',
                name=self.loopback_id,
                get=True)
            self.assertTrue(op)

    def test_int_ipv4_arp_aging_timout(self):
        self.conn = ('10.37.18.135', '22')
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.int_ipv4_arp_aging_timout(
                arp_aging_timeout='21', name='135/0/20',
                int_type='tengigabitethernet')
            op = dev.interface.int_ipv4_arp_aging_timout(
                name='135/0/20', int_type='tengigabitethernet', get=True)
            self.assertEqual(op, '21')
            dev.interface.int_ipv4_arp_aging_timout(
                name='135/0/20', int_type='tengigabitethernet', enable=False)

            op = dev.interface.int_ipv4_arp_aging_timout(
                name='135/0/20', int_type='tengigabitethernet', get=True)
            self.assertIsNone(op)

    def test_transport_service(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.add_vlan_int('6666')
            dev.interface.spanning_tree_state(name='6666',
                                              int_type='vlan',
                                              enabled=False)
            dev.interface.transport_service(vlan='6666', service_id=2)

    def test_lacp_timeout(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            int_type = 'tengigabitethernet'
            name = '1/0/10'
            dev.interface.channel_group(
                name=name,
                int_type=int_type,
                port_int='1',
                channel_type='standard',
                mode='active')
            dev.interface.lacp_timeout(
                name=name, int_type=int_type, timeout='long')

    def test_port_channel_vlag_ignore_split(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.port_channel_vlag_ignore_split(
                name='2', enabled=True)
            dev.interface.port_channel_vlag_ignore_split(
                name='2', enabled=False)

    """
     7.0.1
    """

    def test_ip_unumbered(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            int_type = 'tengigabitethernet'
            name = '1/0/6'
            donor_type = 'loopback'
            donor_name = '1'
            dev.interface.disable_switchport(
                inter_type=int_type, inter=name)
            dev.interface.ip_unnumbered(
                int_type=int_type,
                name=name,
                donor_type=donor_type,
                donor_name=donor_name)
