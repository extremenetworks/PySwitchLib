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

import xml.etree.ElementTree as ET


class Firmware(object):
    """
        Firmware class containing all methods and attributes for firmware downloading and
        status query.
    """
    valid_protocol_type = None

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

        args:
            fdparam
                protocol(str): 'scp'
                host(str): IPv4 or IPv6 Address
                user_name(str): User Name
                password(str): Password
                directory(str): Path to image to be downloaded
                rbridge(0-9 or all): Rbridge id where the firmware need to be downloaded.
                Applicable only for NOS.
                auto_activate(bool): To activate new firmware on all nodes
                coldboot(bool): Perform non ISSU firmware download

        Returns:
            Returns dictionary for firmwaredownload command.
        Example:
                >>> import pyswitch.device
                >>> switches = ['10.24.86.60']
                >>> auth = ('admin', 'password')
                >>> for switch in switches:
                ...     conn = (switch, '22')
                ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...     dictstatus = dev.firmware.download_firmware(protocol='scp',
                host='10.31.2.25',
                ...                          user_name='fvt', password='pray4green',
                ...
                directory='/proj/sredev/slxos17s.1.02_pit_a_davinci_bds_sre/slxos17s.1
                .02_pit_a_davinci_170823_1900/dist/',
                ...                         )
                ...     print(dictstatus)
        """
        protocol = fdparam.pop('protocol')
        host = fdparam.pop('host')
        user_name = fdparam.pop('user_name')
        password = fdparam.pop('password')
        directory = fdparam.pop('directory')
        rbridge = fdparam.pop('rbridge', 'all')
        auto_activate = fdparam.pop('auto_activate', True)
        coldboot = fdparam.pop('coldboot', False)
        os_type = fdparam.pop('os_type')

        if protocol not in self.valid_protocol_type:
            raise ValueError('protocol must be one of:%s' %
                             repr(self.valid_protocol_type))

        if os_type is 'nos':
            if coldboot is True:
                # coldboot does not work when auto_activate is specified
                argument = {'rbridge_id': rbridge, 'coldboot': coldboot,
                            'scp': (user_name, password, host, directory, 'release.plist')}
            else:
                argument = {'rbridge_id': rbridge, 'auto_activate': auto_activate,
                            'coldboot': coldboot,
                            'scp': (user_name, password, host, directory, 'release.plist')}
        else:
            argument = {'rbridge_id': rbridge, 'coldboot': coldboot,
                        'scp': (user_name, password, host, directory, 'release.plist')}

        config = ('firmware_download_rpc', argument)
        response = self._callback(config, 'get')
        return self.parse_firmware_download_response(os_type, response)

    def parse_firmware_download_response(self, os_type, response):
        keys = ['rbridge-id', 'status_code', 'status_msg']
        dictlist = []
        if os_type is 'nos':
            root = ET.fromstring(response.data)
            fwdl_cmd_status = int(root.find('fwdl-cmd-status').text)
            for cluster_output in root.findall('cluster-output'):
                rb_id = int(cluster_output.find('rbridge-id').text)
                fwdl_status = fwdl_cmd_status
                fwdl_msg = cluster_output.find('fwdl-msg').text
                values = [rb_id, fwdl_status, fwdl_msg]
                dictlist.append(dict(zip(keys, values)))
            if not dictlist:
                fwdl_msg = root.find('fwdl-cmd-msg').text
                values = [0, fwdl_cmd_status, fwdl_msg]
                dictlist.append(dict(zip(keys, values)))
        else:
            if response.data != '<output></output>':
                root = ET.fromstring(response.data)
                fwdl_status = int(root.find('fwdl-status').text)
                if fwdl_status != 0:
                    fwdl_msg = root.find('fwdl-msg').text
                else:
                    fwdl_msg = 'Firmwaredownload Started'
            else:
                fwdl_status = -1
                fwdl_msg = 'Got empty response for firmwaredownload'

            values = [0, fwdl_status, fwdl_msg]
            dictlist.append(dict(zip(keys, values)))

        return dictlist

    def firmware_download_monitor(self):
        """
        Method to check firmware download status

        args:
            None

        Returns:
            Returns dictionary list for firmwaredownload status. Each dictionary contains
            current progress message, index, time-stamp and blade information.
        Example:
                >>> import pyswitch.device
                >>> switches = ['10.24.86.60']
                >>> auth = ('admin', 'password')
                >>> for switch in switches:
                ...     conn = (switch, '22')
                ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...     dictlist = dev.firmware.firmware_download_monitor()
                ...     print(dictlist)
        """
        argument = {'api_timeout': (30, 30)}
        config = ('fwdl_status_rpc', argument)
        keys = ['index', 'blade-name', 'timestamp', 'message']
        dictlist = []

        response = self._callback(config, 'get')

        if response.data != '<output></output>':
            root = ET.fromstring(response.data)
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
