"""
Copyright 2015 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import pprint
import xml.etree.ElementTree as ET
import time, threading
import thread
from pyswitch.utilities import Util
from threading import Timer
import time

class Firmware(object):
    """
        Firmware class containing all methods and attributes for firmware downloading and
        status query.
    """
    valid_protocol_type = None
    #last_proc_fwdl_entry = 0
    #fwdl_monitor_timer = None


    def __init__(self, callback):
        """System init method.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            System Object

        Raises:
            None
        """
        self.valid_protocol_type = ['scp']
        self._callback = callback

    def download_firmware(self, **fdparam):
        """
        Method to download firmware on a switch

        Args:
            fdparam
                protocol(str): 'scp'
                host(str): IPv4 or IPv6 Address
                user_name(str): User Name
                password(str): Password
                directory(str): Path to image to be downloaded
                rbridge(0-9 or all): Rbridge id where the firmware need to be downloaded. Applicable only for NOS.
                auto_activate(bool): To activate new firmware on all nodes
                coldboot(bool): Perform non ISSU firmware download

        Return:
        """
        protocol = fdparam.pop('protocol')
        host = fdparam.pop('host')
        user_name = fdparam.pop('user_name')
        password = fdparam.pop('password')
        directory = fdparam.pop('directory')
        rbridge = fdparam.pop('rbridge', 'all')
        auto_activate = fdparam.pop('auto_activate', False)
        coldboot = fdparam.pop('coldboot', True)

        if protocol not in self.valid_protocol_type:
            raise ValueError('protocol must be one of:%s' %
                             repr(self.valid_protocol_type))


        #argument = {'rbridge_id': rbridge, 'auto_activate': auto_activate, 'coldboot': coldboot,
        #            'scp':(user_name, password, host, directory, 'release.plist')}

        argument = {'rbridge_id': rbridge, 'coldboot': coldboot,
                    'scp': (user_name, password, host, directory, 'release.plist')}
        config = ('firmware_download_rpc', argument)
        response = self._callback(config, 'get')
        util = Util(response.data)
        dictstatus = dict()
        if response.data != '<output></output>':
            download_status_code = int(util.find(util.root, 'fwdl-status'))
            download_status_code = download_status_code
            download_status_msg = util.find(util.root, 'fwdl-msg')
            if download_status_code != 0:
                dictstatus['status_code'] = download_status_code
                dictstatus['status_message'] = download_status_msg
                #print("Firmwaredownload Failed[Code: ", download_status_code, "String: ",
                #      download_status_msg)
            else:
                dictstatus['status_code'] = download_status_code
                dictstatus['status_message'] = 'Firmwaredownload Started'
                #print("Firmwaredownload Started")
                #self.last_proc_fwdl_entry = 0
                #print("Starting firmware download monitor event")
                #self.fwdl_monitor_timer = Timer(5, lambda: self.firmware_download_monitor())
                #self.fwdl_monitor_timer.start()
        else:
            dictstatus['status_code'] = -1
            dictstatus['status_message'] = 'Got empty response for firmwaredownload'
            #print("Got empty response for firmwaredownload")

        return dictstatus


    def firmware_download_monitor(self):
        argument = {}
        config = ('fwdl_status_rpc', argument)
        keys = ['index', 'blade-name', 'timestamp', 'message']
        dictlist = []

        response = self._callback(config, 'get')

        if response.data != '<output></output>':
            root = ET.fromstring(response.data)
            num_xml_fwdl_entries = int(root.find('number-of-entries').text)
            print(num_xml_fwdl_entries)
            for fwdl_entry in root.findall('fwdl-entries'):
                fwdl_index = int(fwdl_entry.find('index').text)
                blade_name = fwdl_entry.find('blade-name').text
                time_stamp = fwdl_entry.find('date-and-time-info').text
                message = fwdl_entry.find('message').text
                values = [fwdl_index, blade_name, time_stamp, message]
                dictlist.append(dict(zip(keys, values)))
        else:
            pass
        return dictlist