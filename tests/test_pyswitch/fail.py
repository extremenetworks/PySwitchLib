import sys
import traceback


def test_arp_aging_timeout(asset):
    # Rest opration fails
    print asset.interface_tengigabitethernet_ip_arp_aging_timeout_update(
        arp_aging_timeout='21',
        tengigabitethernet='135/0/20')


def test_ethernet_get(asset):
    # asset.interface_ethernet_get(ethernet='3/3', resource_depth=3)

    print asset.vlan_create(vlan='78')
    print asset.rbridge_id_interface_ve_create(rbridge_id='135', ve='78')
    print asset.rbridge_id_interface_ve_ip_address_create(rbridge_id='1', ve='78',
                                                    address=(
                                                    '9.9.19.1/24', False,
                                                    False, False))


def test_vmac(asset):
    asset.show_firmware_version_rpc()
    asset.rbridge_id_protocol_vrrp_update(vrrp=False, rbridge_id='1')
    asset.rbridge_id_ipv6_protocol_vrrp_update(vrrp=False, rbridge_id='1')
    asset.rbridge_id_protocol_vrrp_extended_update(rbridge_id='1',
                                                   vrrp_extended=True)
    asset.rbridge_id_ipv6_protocol_vrrp_extended_update(rbridge_id='1',
                                                        vrrp_extended=True)
    asset.vlan_create(vlan='78')
    asset.rbridge_id_interface_ve_create(rbridge_id='1', ve='78')
    asset.show_firmware_version_rpc()
    asset.rbridge_id_interface_ve_ipv6_vrrp_extended_group_create(vrrpv3e='3',
                                                                  ve='78',
                                                                  rbridge_id='1')
    print asset.rbridge_id_interface_ve_vrrp_extended_group_update(vrrpe='3',
                                                             ve='78',
                                                             virtual_mac='02e0.5200.00xx',
                                                             rbridge_id='1')


def call(method, asset):
    try:
        method(asset)
    except:
        traceback.print_exc(file=sys.stdout)
        pass
    finally:
        print '**************************************************\n'


if __name__ == '__main__':
    import pyswitchlib.asset

    # asset = pyswitchlib.asset.Asset('10.24.4.215', ('admin', 'password'))
    asset = pyswitchlib.asset.Asset('10.37.18.131', ('admin', 'password'))

    call(test_vmac, asset)
