"""
Copyright 2017 Brocade Communications Systems, Inc.

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
import re
import json
from ipaddress import ip_address
from ipaddress import ip_interface
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, \
    NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException


class Utils(object):
    """
        This class implements utlis like ping. This class takes extra argument
        like host and auth parameters which can be used to establish CLI connection.
        Attributes:
            None
    """

    def __init__(self, callback, host, auth):
        """
        utils object init.

        Args:
            callback: Callback function that will be called for each action.
            host: device mgmt_ip
            auth: authentication parameter for device ssh (username, password)

        Returns:

        Raises:
            None
        """
        self._callback = callback
        self._host = host
        self._auth = auth

    def _create_ping_cmd(self, targets, vrf, count, timeout_value, size):
        """
           Internal method to create ping command.
        """
        cli_cmd = []
        try:
            for numips in targets:
                check_valid_ip = ip_address(unicode(numips))
                numips = str(check_valid_ip)
                valid_address = ip_interface(unicode(numips))

                if valid_address.version == 4:
                    cli = "ping {} vrf {} count {} datagram-size {} timeout {}".format(
                        numips, vrf, count, size, timeout_value)
                elif valid_address.version == 6:
                    cli = "ping ipv6 {} vrf {} count {} datagram-size {} timeout {}".format(
                        numips, vrf, count, size, timeout_value)
                cli_cmd.append(cli)
            return cli_cmd
        except ValueError as e:
            raise AttributeError(e.message)

    def _execute_cli(self, opt, cli_list):
        """
           Internal method to create netmiko connection and
           execute CLI.
        """
        cli_output = {}
        try:
            net_connect = ConnectHandler(**opt)
            for cmd in cli_list:
                cmd = cmd.strip()
                cli_output[cmd] = (net_connect.send_command(cmd))
        except (NetMikoTimeoutException, NetMikoAuthenticationException,) as e:
            reason = e.message
            raise ValueError('Failed to execute cli on %s due to %s', opt['ip'], reason)

        except SSHException as e:
            reason = e.message
            raise ValueError('Failed to execute cli on %s due to %s', opt['ip'], reason)
        except Exception as e:
            reason = e.message
            # This is in case of I/O Error, which could be due to
            # connectivity issue or due to pushing commands faster than what
            #  the switch can handle
            raise ValueError('Failed to execute cli on %s due to %s', opt['ip'], reason)
        if not net_connect:
            net_connect.disconnect()
        return cli_output

    def ping(self, **kwargs):
        """
            Method to execute ping on given targets.
            Args:
                targets (array)   : One or more comma separated target IP addresses.
                vrf (string)      : VRF name. Default value "default-vrf".
                timeout_value(int): Timeout parameter for the ping command. Specifies
                                    the time (in seconds) to wait for a response.
                                    Default value 4 seconds.
                count(int)        : Count parameter for the ping command. Specifies
                                    the number of transmissions. Default value: 4.
                size(int)         : Datagram size. Default value 56.

            Returns:
                List of dict {'ip_address': <ipaddress>,
                              'result': <'fail' or 'pass'>
                              'packets transmitted' : <transmit count>
                              'packets received': <receive count>
                              'packet loss': <loss percentage>}
            Raises:
               ValueError: Invalid ip, connection failure, command execution error

            Examples:
               >>> import pyswitch.device
               >>> switches = ['10.24.39.211', '10.24.39.203']
               >>> auth = ('admin', 'password')
               >>> targets ="10.24.86.96,10.24.12.106"
               >>> count = 4
               >>> size = 56
               >>> timeout_value = 3
               >>> vrf = 'mgmt-vrf'
               >>> for switch in switches:
               ...     ping_output = []
               ...     conn = (switch, '22')
               ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
               ...         ping_output = device.utils.ping(targets=targets, count=count,
               ...                                         timeout_value=timeout_value,
               ...                                         vrf=vrf, size=size)
        """
        ipv4_address = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        ipv6_address = re.compile('(?:(?:[0-9A-Fa-f]{1,4}:){6}(?:[0-9A-Fa-f]{1,4}:'
                                  '[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]'
                                  '{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9]'
                                  '[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::(?:[0-9A-Fa-f]'
                                  '{1,4}:){5}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]'
                                  '{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4]'
                                  '[0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]'
                                  '{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]'
                                  '{1,4})?::(?:[0-9A-Fa-f]{1,4}:){4}(?:[0-9A-Fa-f]'
                                  '{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9]'
                                  '[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)'
                                  '{3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4]'
                                  '[0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]'
                                  '{1,4})?::(?:[0-9A-Fa-f]{1,4}:){3}(?:[0-9A-Fa-f]'
                                  '{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9]'
                                  '[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)'
                                  '{3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4]'
                                  '[0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:)'
                                  '{,2}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:)'
                                  '{2}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|'
                                  '[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}'
                                  '(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|'
                                  '(?:(?:[0-9A-Fa-f]{1,4}:){,3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]'
                                  '{1,4}:(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|'
                                  '(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)'
                                  '{3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))'
                                  '|(?:(?:[0-9A-Fa-f]{1,4}:){,4}[0-9A-Fa-f]{1,4})?::(?:'
                                  '[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9]'
                                  '[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|'
                                  '[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:'
                                  '[0-9A-Fa-f]{1,4}:){,5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]'
                                  '{1,4}|(?:(?:[0-9A-Fa-f]{1,4}:){,6}[0-9A-Fa-f]{1,4})?::)')

        targets = kwargs.pop('targets', None)
        vrf = kwargs.pop('vrf', 'default-vrf')
        count = kwargs.pop('count', 4)
        timeout_value = kwargs.pop('timeout_value', 1)
        if timeout_value is None:
            timeout_value = 1
        if timeout_value < 1 or timeout_value > 60:
            raise AttributeError("Invalid timeout value. Valid range 1 to 60")
        size = kwargs.pop('size', 56)
        if size is None:
            size = 56
        if size < 36 or size > 9100:
            raise AttributeError("Invalid size - valid range 36 to 9100")
        opt = {'device_type': 'brocade_vdx'}
        opt['ip'] = self._host
        opt['username'] = self._auth[0]
        opt['password'] = self._auth[1]
        opt['global_delay_factor'] = 0.5

        try:
            cli_list = self._create_ping_cmd(targets, vrf, count, timeout_value, size)
            cli_output = self._execute_cli(opt, cli_list)
        except Exception:
            raise

        failed_ips_list = []
        success_ips_list = []
        final_output = []
        status = True
        for key, value in cli_output.iteritems():
            output_dict = {}
            if ipv4_address.search(key):
                ip = ipv4_address.search(key).group()
            elif ipv6_address.search(key):
                ip = ipv6_address.search(key).group()
            value_list = value.splitlines()
            p_tx = p_rx = 0
            p_loss = '100'
            for i, line in enumerate(value_list):
                if line.startswith('--- ' + ip):

                    p_tx = re.search(r'(\d+)(\spackets\stransmitted)',
                                     str(value_list[i + 1])).group(1)
                    p_rx = re.search(r'(\d+)(\spackets\sreceived|\sreceived)',
                                     str(value_list[i + 1])).group(1)
                    p_loss = re.search(r'(\d+)(\%)(\spacket\sloss)',
                                       str(value_list[i + 1])).group(1)
            if 100 >= int(p_loss) > 0:
                failed_ips_list.append(str(ip))
                output_dict['ip_address'] = str(ip)
                output_dict['result'] = 'fail'
                output_dict['packets transmitted'] = int(p_tx)
                output_dict['packets received'] = int(p_rx)
                output_dict['packet loss'] = p_loss + "%"
                status = False
            elif int(p_loss) == 0:
                success_ips_list.append(str(ip))
                output_dict['ip_address'] = ip
                output_dict['result'] = 'pass'
                output_dict['packets transmitted'] = int(p_tx)
                output_dict['packets received'] = int(p_rx)
                output_dict['packet loss'] = p_loss + "%"
            final_output.append(output_dict)
        json_outputformat = json.dumps(
            final_output, sort_keys=True, indent=4, separators=(',', ': '))
        json_outputformat = json.loads(json_outputformat)
        return (status, json_outputformat)
