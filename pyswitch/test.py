#/bin/bash

import pyswitch.device

def main():
    switches = ['10.24.86.60']
    #switches = ['10.24.81.200']
    auth = ('admin', 'password')
    for switch in switches:
        conn = (switch, '22')
        with pyswitch.device.Device(conn=conn, auth=auth) as dev:

            """
            FOR SLX
            """
            dict = dev.firmware.download_firmware(protocol='scp', host='10.31.2.25',
                                           user_name='fvt', password='pray4green',
                                           directory='/proj/sredev/slxos17s.1.02_pit_a_davinci_bds_sre/slxos17s.1.02_pit_a_davinci_170823_1900/dist/',
                                          )
            print(dict)
            """
            FOR NOS
            """

            #dev.firmware.download_firmware(protocol='scp', host='10.31.2.25',
            #                               user_name='fvt', password='pray4green',
            #                               directory='/proj/sredev/nos7.3.0_pit_a_sre/nos7.3.0_pit_a_170817_0700/dist',
            #                               )


            dictlist = dev.firmware.firmware_download_monitor()
            print(dictlist)

if __name__ == '__main__':
    main()