import pyswitch.device
switches = ['10.24.85.107']
auth = ('admin', 'admin')
for switch in switches:
    conn = (switch, '22')
    with pyswitch.device.Device(conn=conn, auth=auth) as dev:
        output = dev.system.system_l2_mtu(mtu='1666')
        print output
        output = dev.system.system_l2_mtu(get=True)
        print output
