from __future__ import absolute_import

import unittest

from pyswitch.device import Device


class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = ('10.37.18.131', '22')
        self.auth = ('admin', 'password')

    def test_ipv6_address(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.ip_address(
                int_type='loopback',
                name='1',
                rbridge_id='1',
                ip_addr='fc01:1:3:1ad3:0:0:23:a/128')
            dev.interface.ip_address(
                int_type='loopback',
                name='1',
                rbridge_id='1',
                ip_addr='fc01:1:3:1ad3:0:0:23:a/128',
                delete=True)

            dev.interface.ip_address(
                int_type='loopback',
                name='1',
                rbridge_id='1',
                ip_addr='10.32.35.2/32')
            dev.interface.ip_address(
                int_type='loopback',
                name='1',
                rbridge_id='1',
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
             name=self.rbridge_id, rbridge_id='1', ip_addr='10.32.35.2/32')
            dev.interface.ip_address(int_type='loopback',
            name='1', rbridge_id='1',
                                     ip_addr='fc01:1:3:1ad3:0:0:23:a/128')
            dev.interface.ip_address(int_type='ve', name='1',
            rbridge_id='1', ip_addr='10.32.55.2/24')
            dev.interface.ip_address(int_type='ve', name='1',
             rbridge_id='1', ip_addr='fc02:1:3:1ad3:0:0:23:a/64')

            ## Delete
            dev.interface.ip_address(int_type='tengigabitethernet',
             name='1/0/6', ip_addr='10.32.45.1/24', delete=True)
            dev.interface.ip_address(int_type='tengigabitethernet',
             name='1/0/6', ip_addr='fc00:1:3:1ad3:0:0:23:a/64',
                                     delete=True)

            dev.interface.ip_address(int_type='loopback', name='1',
            rbridge_id='1', ip_addr='10.32.35.2/32',
                                     delete=True)
            dev.interface.ip_address(int_type='loopback', name='1',
            rbridge_id='1',
                    ip_addr='fc01:1:3:1ad3:0:0:23:a/128', delete=True)

            dev.interface.ip_address(int_type='ve', name='1',
            rbridge_id='1', ip_addr='10.32.55.2/24', delete=True)
            dev.interface.ip_address(int_type='ve', name='1',
            rbridge_id='1', ip_addr='fc02:1:3:1ad3:0:0:23:a/64',
                                     delete=True)

            print dev.interface.ip_address(int_type='ve', name='1',
            rbridge_id='1', ip_addr='10.32.55.2/24', get=True)
            print dev.interface.ip_address(int_type='loopback', name='1',
             rbridge_id='1', ip_addr='10.32.35.2/32',
                                           get=True)
            print dev.interface.ip_address(int_type='tengigabitethernet',
            name='1/0/6', ip_addr='10.32.45.1/24',
                                           get=True)

            print dev.interface.get_ip_addresses(
            int_type='tengigabitethernet', name='1/0/16', version=4)
            """

    """
     Overlay Gateway related - starts
    """

    """
         Overlay Gateway related - ends
    """

    def test_admin_state(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.admin_state(
                int_type='tengigabitethernet',
                name='1/0/6',
                enabled=True)
            op = dev.interface.admin_state(
                int_type='tengigabitethernet', name='1/0/6', get=True)
            self.assertTrue(op)
            dev.interface.admin_state(
                int_type='tengigabitethernet',
                name='1/0/6',
                enabled=False)
            op = dev.interface.admin_state(
                int_type='tengigabitethernet', name='1/0/6', get=True)
            self.assertFalse(op)

            dev.interface.admin_state(
                rbridge_id='1',
                int_type='ve',
                name='1',
                enabled=False)
            op = dev.interface.admin_state(
                rbridge_id='1',
                int_type='ve',
                name='1',
                get=True)
            self.assertFalse(op)
            dev.interface.admin_state(
                rbridge_id='1', int_type='ve', name='1', enabled=True)
            op = dev.interface.admin_state(
                rbridge_id='1',
                int_type='ve',
                name='1',
                get=True)
            self.assertTrue(op)

            dev.interface.admin_state(
                rbridge_id='1',
                int_type='loopback',
                name='1',
                enabled=False)
            op = dev.interface.admin_state(
                rbridge_id='1',
                int_type='loopback',
                name='1',
                get=True)
            self.assertFalse(op)
            dev.interface.admin_state(
                rbridge_id='1',
                int_type='loopback',
                name='1',
                enabled=True)
            op = dev.interface.admin_state(
                rbridge_id='1',
                int_type='loopback',
                name='1',
                get=True)
            self.assertTrue(op)

            dev.interface.admin_state(
                int_type='port_channel', name='1', enabled=True)
            op = dev.interface.admin_state(
                int_type='port_channel', name='1', get=True)
            self.assertTrue(op)

            dev.interface.admin_state(
                int_type='port_channel', name='1', enabled=False)
            op = dev.interface.admin_state(
                int_type='port_channel', name='1', get=True)
            self.assertFalse(op)

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


class InterfaceGenericCase(unittest.TestCase):

    def setUp(self):
        self.rbridge_id = '1'
        self.loopback_id = '12'
        self.mtu = '1666'
        self.vlan = '34'
        self.second_vlan = 909
        self.ip_mtu = '8000'
        self.ipv6_mtu = '8080'
        self.bfd_rx = '300'
        self.bfd_tx = '300'
        self.bfd_multiplier = '3'
        self.description = 'desc123'
        self.int_name = '1/0/11'
        self.int_type = 'tengigabitethernet'
        self.int_ip = '10.32.95.12/24'
        self.port_int = '21'
        self.switch_ip = '10.37.18.131'
        self.admin_password = 'password'
        self.conn = (self.switch_ip, '22')
        self.auth = ('admin', self.admin_password)

        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_portchannel(name=self.port_int)
            dev.interface.add_vlan_int(self.vlan)
            dev.interface.create_ve(
                ve_name=self.vlan,
                rbridge_id=self.rbridge_id)
            dev.interface.create_loopback(
                lb_name=self.loopback_id,
                rbridge_id=self.rbridge_id)

    def test_mac_move_detect_enable(self):
        self.conn = ('10.37.18.135', '22')
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.mac_move_detect_enable()
            op = dev.interface.mac_move_detect_enable(get=True)
            self.assertTrue(op)
            dev.interface.mac_move_detect_enable(delete=True)
            op = dev.interface.mac_move_detect_enable(get=True)
            self.assertIsNone(op)

    def test_mac_move_limit(self):
        self.conn = ('10.37.18.135', '22')
        self.mac_move_limit = '32'
        self.default_mac_move = '20'
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.mac_move_limit(mac_move_limit=self.mac_move_limit)
            op = dev.interface.mac_move_limit(get=True)
            self.assertEqual(op, self.mac_move_limit)
            dev.interface.mac_move_limit(delete=True)
            op = dev.interface.mac_move_limit(get=True)
            self.assertEqual(op, self.default_mac_move)

    def test_fabric_neighbor(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.fabric_neighbor(
                int_type=self.int_type,
                name=self.int_name)
            op = dev.interface.fabric_neighbor(
                int_type=self.int_type,
                name=self.int_name,
                get=True)
            self.assertTrue(op)
            dev.interface.fabric_neighbor(
                int_type=self.int_type,
                name=self.int_name,
                enabled=False)
            op = dev.interface.fabric_neighbor(
                int_type=self.int_type,
                name=self.int_name,
                get=True)
            self.assertIsNone(op)

    def test_v6_nd_suppress_ra(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.v6_nd_suppress_ra(name=self.int_name,
                                                     int_type=self.int_type)
            output = dev.interface.v6_nd_suppress_ra(
                name=self.int_name, int_type=self.int_type, get=True)
            self.assertTrue(output)
            output = dev.interface.v6_nd_suppress_ra(
                name=self.int_name, int_type=self.int_type, enabled=False)
            output = dev.interface.v6_nd_suppress_ra(
                name=self.int_name, int_type=self.int_type, get=True)
            self.assertIsNone(output)

            output = dev.interface.v6_nd_suppress_ra(
                int_type='ve', name=self.vlan, rbridge_id=self.rbridge_id)
            output = dev.interface.v6_nd_suppress_ra(
                int_type='ve', name=self.vlan, rbridge_id=self.rbridge_id,
                get=True)
            self.assertTrue(output)

            output = dev.interface.v6_nd_suppress_ra(
                int_type='ve', name=self.vlan, rbridge_id=self.rbridge_id,
                enabled=False)
            output = dev.interface.v6_nd_suppress_ra(
                int_type='ve', name=self.vlan, rbridge_id=self.rbridge_id,
                get=True)
            self.assertIsNone(output)

    def test_set_ip(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.switchport(name=self.int_name,
                                     int_type=self.int_type,
                                     enabled=False)
            dev.interface.set_ip(
                inter_type=self.int_type,
                inter=self.int_name,
                ip_addr=self.int_ip)
            output = dev.interface.ip_address(
                int_type=self.int_type, name=self.int_name, get=True)
            ipv4_address = output['ipv4_address']
            self.assertIn(self.int_ip, ipv4_address)

            dev.interface.ip_address(
                int_type=self.int_type,
                name=self.int_name,
                ip_addr=self.int_ip,
                delete=True)

            output = dev.interface.ip_address(
                int_type=self.int_type, name=self.int_name, get=True)
            ipv4_address = output['ipv4_address']
            self.assertNotIn(self.int_ip, ipv4_address)

    def test_description(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.description(
                int_type=self.int_type,
                name=self.int_name,
                desc=self.description)
            op = dev.interface.description(
                int_type=self.int_type, name=self.int_name, get=True)
            self.assertEqual(self.description, op)

            dev.interface.description(
                int_type='vlan',
                name=self.vlan,
                desc=self.description)
            op = dev.interface.description(
                int_type='vlan', name=self.vlan, get=True)
            self.assertEqual(self.description, op)

            dev.interface.description(
                int_type='port_channel',
                name=self.port_int,
                desc=self.description)
            op = dev.interface.description(
                int_type='port_channel', name=self.port_int, get=True)
            self.assertEqual(self.description, op)

    def test_vlan(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.add_vlan_int(vlan_id=self.second_vlan)
            op = dev.interface.get_vlan_int(vlan_id=self.second_vlan)
            print op

        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.del_vlan_int(vlan_id=self.second_vlan)

    def test_anycast(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            mac = '0011.2233.4455'
            dev.services.vrrpe(rbridge_id=self.rbridge_id, enable=False)
            dev.services.vrrpe(
                rbridge_id=self.rbridge_id,
                enable=False,
                ip_version='6')

            dev.services.vrrp(rbridge_id=self.rbridge_id, enabled=False)
            dev.services.vrrp(
                rbridge_id=self.rbridge_id,
                enabled=False,
                ip_version='6')

            output = dev.interface.anycast_mac(rbridge_id=self.rbridge_id,
                                               mac=mac)
            output = dev.interface.anycast_mac(rbridge_id=self.rbridge_id,
                                               get=True)
            self.assertEqual(mac, output)

            dev.interface.anycast_mac(rbridge_id=self.rbridge_id,
                                      delete=True)
            output = dev.interface.anycast_mac(rbridge_id=self.rbridge_id,
                                               get=True)
            self.assertIsNone(output)

    def test_ipv6_link_local(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.ipv6_link_local(
                int_type='ve', name=self.vlan, rbridge_id=self.rbridge_id)
            output = dev.interface.ipv6_link_local(
                int_type='ve', name=self.vlan, rbridge_id=self.rbridge_id,
                get=True)
            print 'VE ipv6_link_local : ', output
            self.assertEqual(True, output)

            output = dev.interface.ipv6_link_local(
                int_type='ve', name=self.vlan, rbridge_id=self.rbridge_id,
                delete=True)
            output = dev.interface.ipv6_link_local(
                int_type='ve', name=self.vlan, rbridge_id=self.rbridge_id,
                get=True)
            print 'VE ipv6_link_local : ', output
            self.assertEqual(None, output)

            #
            output = dev.interface.ipv6_link_local(
                int_type='loopback',
                name=self.loopback_id,
                rbridge_id=self.rbridge_id)
            output = dev.interface.ipv6_link_local(
                int_type='loopback',
                name=self.loopback_id,
                rbridge_id=self.rbridge_id,
                get=True)
            print 'loopback ipv6_link_local : ', output
            self.assertEqual(None, output)

    def test_proxy_arp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.proxy_arp(name=self.int_name,
                                             int_type=self.int_type,
                                             enabled=True)
            output = dev.interface.proxy_arp(name=self.int_name,
                                             int_type=self.int_type,
                                             get=True)
            print 'tengigabitethernet proxy_arp ', output
            self.assertEqual(output, True)
            output = dev.interface.proxy_arp(name=self.int_name,
                                             int_type=self.int_type,
                                             enabled=False)
            output = dev.interface.proxy_arp(name=self.int_name,
                                             int_type=self.int_type,
                                             get=True)
            print 'tengigabitethernet proxy_arp ', output
            self.assertEqual(output, None)

            output = dev.interface.channel_group(
                name=self.int_name,
                int_type=self.int_type,
                port_int=self.port_int,
                channel_type='standard',
                mode='active')

            output = dev.interface.proxy_arp(name=self.port_int,
                                             int_type='port_channel',
                                             enabled=True)
            output = dev.interface.proxy_arp(name=self.port_int,
                                             int_type='port_channel',
                                             get=True)
            print 'tengigabitethernet proxy_arp ', output
            self.assertEqual(output, True)
            output = dev.interface.proxy_arp(name=self.port_int,
                                             int_type='port_channel',
                                             enabled=False)
            output = dev.interface.proxy_arp(name=self.port_int,
                                             int_type='port_channel',
                                             get=True)
            print 'tengigabitethernet proxy_arp ', output
            self.assertEqual(output, None)

    def test_arp_suppression(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.arp_suppression(name=self.vlan)
            output = dev.interface.arp_suppression(name=self.vlan, get=True)
            self.assertTrue(output)
            output = dev.interface.arp_suppression(
                name=self.vlan, enable=False)
            output = dev.interface.arp_suppression(name=self.vlan, get=True)
            self.assertIsNone(output)

    def test_mtu(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            # self.assertTrue(False, 'Delete not implemented')
            output = dev.interface.mtu(mtu=self.mtu,
                                       name=self.int_name,
                                       int_type=self.int_type)
            output = dev.interface.mtu(get=True,
                                       name=self.int_name,
                                       int_type=self.int_type)
            self.assertEqual(self.mtu, output)

            output = dev.interface.mtu(mtu=self.mtu,
                                       name=self.port_int,
                                       int_type='port_channel')
            output = dev.interface.mtu(get=True,
                                       name=self.port_int,
                                       int_type='port_channel')
            self.assertEqual(self.mtu, output)

    def test_ip_mtu(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.ip_mtu(mtu=self.ip_mtu,
                                          name=self.int_name,
                                          int_type=self.int_type)
            output = dev.interface.ip_mtu(get=True,
                                          name=self.int_name,
                                          int_type=self.int_type)

            self.assertEqual(self.ip_mtu, output['ipv4'])

    def test_ipv6_mtu(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.ip_mtu(mtu=self.ipv6_mtu,
                                          name=self.int_name, version=6,
                                          int_type=self.int_type)
            output = dev.interface.ip_mtu(get=True,
                                          name=self.int_name, version=6,
                                          int_type=self.int_type)

            self.assertEqual(self.ipv6_mtu, output['ipv6'])

    def test_bfd(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.bfd(
                name=self.int_name,
                int_type=self.int_type,
                rx=self.bfd_rx,
                tx=self.bfd_tx,
                multiplier=self.bfd_multiplier)
            output = dev.interface.bfd(name=self.int_name,
                                       int_type=self.int_type, get=True)
            self.assertEqual({'rx': self.bfd_rx, 'tx': self.bfd_rx,
                              'multiplier': self.bfd_multiplier}, output)

            output = dev.interface.bfd(name=self.int_name,
                                       int_type=self.int_type, delete=True)
            output = dev.interface.bfd(name=self.int_name,
                                       int_type=self.int_type, get=True)
            self.assertEqual(
                {'rx': None, 'tx': None, 'multiplier': None}, output)

    def test_ip_unumbered(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            donor_type = 'loopback'

            output = dev.interface.switchport(
                name=self.int_name, int_type=self.int_type, enabled=False)

            output = dev.interface.ip_unnumbered(
                name=self.int_name,
                int_type=self.int_type,
                donor_type=donor_type,
                donor_name=self.loopback_id)
            output = dev.interface.ip_unnumbered(
                name=self.int_name, int_type=self.int_type, get=True)
            self.assertEqual({'donor_type': donor_type,
                              'donor_name': self.loopback_id}, output)

            output = dev.interface.ip_unnumbered(
                name=self.int_name, int_type=self.int_type, delete=True)
            output = dev.interface.ip_unnumbered(
                name=self.int_name, int_type=self.int_type, get=True)
            self.assertEqual({'donor_type': None, 'donor_name': None}, output)

    def test_conversational_arp(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.conversational_arp(
                rbridge_id=self.rbridge_id)
            output = dev.interface.conversational_arp(
                rbridge_id=self.rbridge_id, get=True)
            self.assertTrue(output)
            output = dev.interface.conversational_arp(
                rbridge_id=self.rbridge_id, delete=True)
            output = dev.interface.conversational_arp(
                rbridge_id=self.rbridge_id, get=True)
            self.assertIsNone(output)

    def test_conversational_mac(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            output = dev.interface.conversational_mac()
            output = dev.interface.conversational_mac(get=True)
            self.assertTrue(output)
            output = dev.interface.conversational_mac(delete=True)
            output = dev.interface.conversational_mac(get=True)
            self.assertIsNone(output)

    def tearDown(self):
        with Device(conn=self.conn, auth=self.auth) as dev:
            dev.interface.create_portchannel(name=self.port_int, enable=False)
            dev.interface.del_vlan_int(self.vlan)
            dev.interface.create_ve(
                ve_name=self.vlan,
                rbridge_id=self.rbridge_id,
                enable=False)
            dev.interface.create_loopback(
                lb_name=self.loopback_id,
                rbridge_id=self.rbridge_id,
                enable=False)
