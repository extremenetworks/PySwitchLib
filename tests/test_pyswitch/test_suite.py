import unittest

if __name__ == '__main__':
    from test.test_pyswitch.test_interface_OverlayGateway import \
        InterfaceOverlayGatewayTestCase
    from test.test_pyswitch.test_interface_vrf import InterfaceVRFTestCase
    from test.test_pyswitch.test_interface_pvlan import \
        InterfacePrivateVlanTestCase
    from test.test_pyswitch.test_interface_evpn import InterfaceEVPNTestCase
    from test.test_pyswitch.test_interface_virtual_port import \
        InterfaceVirtualPortTestCase
    from test.test_pyswitch.test_interface_port_channel import \
        InterfacePortChannelCase
    from test.test_pyswitch.test_interface_SwitchPort import \
        InterfaceSwitchPort
    from test.test_pyswitch.test_interface import InterfaceGenericCase
    from test.test_pyswitch.test_device import DeviceTestCase
    from test.test_pyswitch.test_fabric_service import FabricServiceTestCase
    from test.test_pyswitch.test_lldp import LLDPTestCase

    device = unittest.TestLoader().loadTestsFromTestCase(DeviceTestCase)
    fs = unittest.TestLoader().loadTestsFromTestCase(FabricServiceTestCase)
    lldp = unittest.TestLoader().loadTestsFromTestCase(LLDPTestCase)

    # interface related
    vrf = unittest.TestLoader().loadTestsFromTestCase(InterfaceVRFTestCase)
    ovg = unittest.TestLoader().loadTestsFromTestCase(
        InterfaceOverlayGatewayTestCase)
    pvlan = unittest.TestLoader().loadTestsFromTestCase(
        InterfacePrivateVlanTestCase)
    evpn = unittest.TestLoader().loadTestsFromTestCase(InterfaceEVPNTestCase)
    generic = unittest.TestLoader().loadTestsFromTestCase(
        InterfaceGenericCase)
    vp = unittest.TestLoader().loadTestsFromTestCase(
        InterfaceVirtualPortTestCase)
    portChannel = unittest.TestLoader().loadTestsFromTestCase(
        InterfacePortChannelCase)
    swp = unittest.TestLoader().loadTestsFromTestCase(InterfaceSwitchPort)

    alltests = unittest.TestSuite([
        device,
        fs,
        lldp,
        vrf,
        generic,
        portChannel,
        ovg,
        pvlan,
        swp,
        evpn,
        vp

    ])

    unittest.TextTestRunner(verbosity=2, failfast=False).run(alltests)
