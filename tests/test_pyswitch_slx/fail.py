import sys
import traceback


def test_ethernet_get(asset):
    print asset.interface_ethernet_get(ethernet='3/3', resource_depth=3)


def test_admin_state(asset):
    print asset.interface_ve_update(global_ve_shutdown=False, ve=791)


def test_vrrpe_vip(asset):
    asset.protocol_vrrp_update(vrrp_extended=False)
    asset.ipv6_protocol_vrrp_update(vrrp_extended=False)
    asset.protocol_vrrp_update(vrrp=True)
    asset.ipv6_protocol_vrrp_update(vrrp=True)
    asset.vlan_create(vlan='78')
    asset.interface_ve_create(ve='78')
    asset.interface_ve_ip_address_create(
        ve='78', address=(
            '9.9.19.1/24', False, False, False))
    asset.interface_ve_vrrp_group_create(vrrp=('3', '3'), ve='78')
    print asset.interface_ve_vrrp_group_virtual_ip_create(
        vrrp=('3', '3'),
        ve='78',
        virtual_ip='9.9.19.2')


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

    asset = pyswitchlib.asset.Asset('10.24.4.215', ('admin', 'password'))
    # asset = pyswitchlib.asset.Asset('10.37.18.131', ('admin', 'password'))

    # call(test_admin_state,asset)
    call(test_ethernet_get, asset)
    # call(test_vrrpe_vip, asset)
