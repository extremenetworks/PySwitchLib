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

    call(test_arp_aging_timeout, asset)
