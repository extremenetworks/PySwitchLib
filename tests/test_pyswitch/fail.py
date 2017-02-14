import sys
import traceback




def test_arp_aging_timeout(asset):
    # Rest opration fails
    print asset.interface_tengigabitethernet_ip_arp_aging_timeout_update(arp_aging_timeout='21',
                                                                         tengigabitethernet='135/0/20')



def test_ethernet_get(asset):

    #asset.interface_ethernet_get(ethernet='3/3', resource_depth=3)
    #asset.interface_tengigabitethernet_get(tengigabitethernet='3/3', resource_depth=3)
    print asset.interface_tengigabitethernet_ipv6_mtu_update(tengigabitethernet='1/0/11', mtu=8000)

def test_ip_unnumbered(asset):

    asset.rbridge_id_interface_loopback_create(rbridge_id='1', loopback='12')
    asset.interface_tengigabitethernet_ip_unnumbered_ip_donor_interface_name_delete(
        tengigabitethernet='1/0/11')

    # Fails saying that donor interface does not exist, This used to work
    # earlier
    print asset.interface_tengigabitethernet_ip_unnumbered_ip_donor_interface_name_update(tengigabitethernet='1/0/11',
                                                                                          ip_donor_interface_type='loopback',
                                                                                          ip_donor_interface_name='12')


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

    #asset = pyswitchlib.asset.Asset('10.24.4.215', ('admin', 'password'))
    asset = pyswitchlib.asset.Asset('10.37.18.131', ('admin', 'password'))
    """
    ## Access VLAN create fails because of the vlan tuple argument, access_group parameter does not accept None.
    ## On VDX platform access_group is not required
    ## Fails in Pybind
    x = asset.interface_tengigabitethernet_switchport_access_vlan_create(tengigabitethernet='1/0/6', vlan=('2',))
    print x

    ## For same reasons as create
    ## Fails in Pybind
    x = asset.interface_tengigabitethernet_switchport_access_vlan_create(tengigabitethernet='1/0/6', vlan=(2, None))
    print x
    """

    call(test_ethernet_get, asset)

