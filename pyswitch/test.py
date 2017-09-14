#/bin/bash

import pyswitch.device
from threading import Timer

#switches = ['10.24.86.60']
switches = ['10.24.81.223']
auth = ('admin', 'password')

protocol_type = 'scp'
host_ip = '10.31.2.25'
proto_username = 'fvt'
proto_password = 'pray4green'
firmware_path = '/proj/sredev/nos7.3.0_pit_a_sre/nos7.3.0_pit_a_170907_0700/dist'
#firmware_path = '/proj/sredev/slxos17s.1.02_pit_a_davinci_bds_sre/slxos17s.1.02_pit_a_davinci_170831_0700/dist/'

class testfirmware:
    fwdl_monitor_timer = None
    last_proc_fwdl_entry = 0
    fwdl_complete = False

    def download(self, switch):
        conn = (switch, '22')
        with pyswitch.device.Device(conn=conn, auth=auth) as device:
            #print('successfully connected to %s to download firmware', self.host)
            fwdl_status_dictlist = device.firmware.download_firmware(protocol=protocol_type, host=host_ip,
                                                                     user_name=proto_username,
                                                                     password=proto_password,
                                                                     directory=firmware_path,
                                                                     os_type=device.os_type)
            num_entries = 0
            num_success = 0
            for fwdl_status_dict in fwdl_status_dictlist:
                num_entries += 1
                if device.os_type is 'nos':
                    print("Rbridge:%d Download Status code: %d Status message:%s", fwdl_status_dict['rbridge-id'],
                          fwdl_status_dict['status_code'],
                          fwdl_status_dict['status_msg'])
                else:
                    print("Download Status code: %d Status message:%s",
                          fwdl_status_dict['status_code'],
                          fwdl_status_dict['status_msg'])

                if fwdl_status_dict['status_code'] == 0:
                    num_success += 1

            if num_entries == num_success:
                """
                firmware download successful. Start Monitor process
                """
                self.last_proc_fwdl_entry = 0
                self.fwdl_monitor_timer = Timer(30, lambda: self.firmware_download_monitor_periodic(switch))
                self.fwdl_monitor_timer.start()
            else:
                print("Firmware download failed, not starting monitoring")

    def firmware_download_monitor_periodic(self, switch):
        conn = (switch, '22')
        try:
            with pyswitch.device.Device(conn=conn, auth=auth) as device:
                self.fwdl_monitor_timer = None
                fwdl_status_list = device.firmware.firmware_download_monitor()
                for fwdl_status in fwdl_status_list:
                    index = fwdl_status['index']
                    if index <= self.last_proc_fwdl_entry:
                        continue
                    else:
                        self.last_proc_fwdl_entry = index
                        print("Index: %d Blade:%s Time:%s Message:%s", index, fwdl_status['blade-name'],
                                         fwdl_status['timestamp'], fwdl_status['message'])
                        if fwdl_status['message'] == 'Firmware is downloaded successfully.':
                            print("All done. Process complete")
                            self.fwdl_complete = True
                        else:
                            pass
                if self.fwdl_complete is True:
                    self.last_proc_fwdl_entry = 0
                    self.fwdl_monitor_timer = None
                else:
                    self.fwdl_monitor_timer = Timer(30, lambda: self.firmware_download_monitor_periodic(switch))
                    self.fwdl_monitor_timer.start()
        except Exception, exc:
            print('Exception while getting device: %s', exc.message)
            self.fwdl_monitor_timer = Timer(30, lambda: self.firmware_download_monitor_periodic(switch))
            self.fwdl_monitor_timer.start()

    def testmain(self, switch):
        try:
            conn = (switch, '22')
            with pyswitch.device.Device(conn=conn, auth=auth) as device:
                print(device.os_type)
        except Exception, exc:
            print('Exception while getting device: %s', exc.message)

def main():
    tfmw = testfirmware()
    for switch in switches:
        tfmw.download(switch)
        #tfmw.firmware_download_monitor_periodic(switch)
        #tfmw.testmain(switch)


if __name__ == '__main__':
    main()