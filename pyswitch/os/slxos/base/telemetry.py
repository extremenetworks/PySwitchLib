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
from pyswitch.utilities import Util


class Telemetry(object):
    """
    Telemetry class containing all methods and attributes for configuring telemetry
    """
    def __init__(self, callback):
        """Telemetry service init method.

                Args:
                    callback: Callback function that will be called for each action.

                Returns:
                    None

                Raises:
                    None
                """
        self._callback = callback

    def telemetry_profile_validate(self, profile_name, interval, intf_range):
        if profile_name is not None:
            if len(profile_name) not in xrange(3, 64):
                raise ValueError("profile_name %s must be in range `3-64`", profile_name)
        if interval is not None:
            if interval not in xrange(0, 4294967295):
                raise ValueError("interval %d must be in range `0-4294967295`", interval)
        if intf_range is not None:
            if len(intf_range) not in xrange(1, 1000):
                raise ValueError("profile_name %s must be in range `1-1000`", intf_range)

    def telemetry_collector_validate(self, collector_name, profile_type, profile_name, encoding_fmt,
             collector_port):
        sys_util_name = 'default_system_utilization_statistics'
        intf_name = 'default_interface_statistics'
        if collector_name is not None:
            if len(collector_name) not in xrange(1, 32):
                raise ValueError("collector_name %s must be in range `1-32`", collector_name)
            if collector_name.isnumeric() is True:
                raise ValueError("collector_name %s must be an Alphanumeric", collector_name)
            if collector_name[0].isnumeric() is True:
                raise ValueError("collector_name %s must start with Alphabet", collector_name)
        if profile_name is not None:
            if len(profile_name) not in xrange(3, 64):
                raise ValueError("profile_name %s must be in range `3-64`", profile_name)
            if profile_name != sys_util_name and profile_name != intf_name:
                raise ValueError("profile_name %s is invalid", profile_name)
        if profile_type is not None:
            if profile_type != 'interface-profile' and profile_type != 'system-profile':
                raise ValueError("profile_type in collector_name %s is invalid", collector_name)
        if encoding_fmt is not None:
            if encoding_fmt != 'json' and encoding_fmt != 'gpb':
                raise ValueError("encoding format in collector_name %s is invalid", collector_name)
        if collector_port is not None:
            if collector_port not in xrange(0, 65535):
                raise ValueError("collector_port %d must be in range `0-65535`", collector_port)

    def collector_create(self, **kwargs):
        """
        Method to create telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_activate: optional, 'True' or 'False'. by default 'False'

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_create(collector=('Profile1'))
            ...     response = device.telemetry.collector_create(collector=('Profile1'),
            ...                                               collector_activate='True')
            ...
        """
        (collector_name) = kwargs.pop('collector')
        collector_activate = kwargs.pop('collector_activate', False)

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector created"
        argument = {'collector': (collector_name),
                    'collector_activate': collector_activate
                    }
        config = ('telemetry_collector_create', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_delete(self, **kwargs):
        """
        Method to delete telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_delete(collector=('Profile1'))
            ...
        """
        (collector_name) = kwargs.pop('collector')

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector deleted"
        argument = {'collector': (collector_name)}
        config = ('telemetry_collector_delete', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_profile_create(self, **kwargs):
        """
        Method to create profile in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_profile: Mandatory
                    collector_profiletype(str): type of the telemetry collector profile
                    collector_profilename(str): name of the telemetry collector profile

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_profile_create(collector=('Profile1'),
            ...            collector_profile=('interface-type', 'default_interface_statistics'))
            ...
        """
        (collector_name) = kwargs.pop('collector')
        (profile_type, profile_name) = kwargs.pop('collector_profile')

        self.telemetry_collector_validate(collector_name, profile_type, profile_name, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector profile created"
        argument = {'collector': (collector_name),
                    'collector_profile': (profile_type, profile_name)
                    }
        config = ('telemetry_collector_profile_create', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_profile_delete(self, **kwargs):
        """
        Method to delete the profile configured in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_profile: Mandatory
                    collector_profiletype(str): type of the telemetry collector profile
                    collector_profilename(str): name of the telemetry collector profile

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_profile_delete(collector=('Profile1'),
            ...            collector_profile=('interface-type', 'default_interface_statistics'))
            ...
        """
        (collector_name) = kwargs.pop('collector')
        (profile_type, profile_name) = kwargs.pop('collector_profile')

        self.telemetry_collector_validate(collector_name, profile_type, profile_name, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector profile deleted"
        argument = {'collector': (collector_name),
                    'collector_profile': (profile_type, profile_name)
                    }
        config = ('telemetry_collector_profile_delete', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_activate_delete(self, **kwargs):
        """
        Method to delete the activate configured in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_activate_delete(collector=('Profile1'))
            ...
        """
        (collector_name) = kwargs.pop('collector')

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector activate deleted"
        argument = {'collector': (collector_name)
                    }
        config = ('telemetry_collector_activate_delete', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_encoding_delete(self, **kwargs):
        """
        Method to delete the encoding format configured in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_encoding_delete(collector=('Profile1'))
            ...
        """
        (collector_name) = kwargs.pop('collector')

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector encoding deleted"
        argument = {'collector': (collector_name)
                    }
        config = ('telemetry_collector_encoding_delete', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_activate_update(self, **kwargs):
        """
        Method to update the activate configured in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_activate: 'True' or 'False'

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_activate_update(collector=('Profile1'),
            ...                  collector_activate='True')
            ...
        """
        (collector_name) = kwargs.pop('collector')
        collector_activate = kwargs.pop('collector_activate', False)

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector activate updated"
        argument = {'collector': (collector_name),
                    'collector_activate': collector_activate
                    }
        config = ('telemetry_collector_activate_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_encoding_update(self, **kwargs):
        """
        Method to update the encoding format configured in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_encoding: 'json' or 'gpb'

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_encoding_update(collector=('Profile1'),
            ...                                      collector_encoding='json')
            ...
        """
        (collector_name) = kwargs.pop('collector')
        collector_encoding = kwargs.pop('collector_encoding')

        self.telemetry_collector_validate(collector_name, None, None, collector_encoding, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector encoding updated"
        argument = {'collector': (collector_name),
                    'collector_encoding': collector_encoding
                    }
        config = ('telemetry_collector_encoding_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_update(self, **kwargs):
        """
        Method to update the telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_activate: 'True' or 'False'

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_update(collector=('Profile1'),
            ...                            collector_activate='True')
            ...
        """
        (collector_name) = kwargs.pop('collector')
        collector_activate = kwargs.pop('collector_activate', False)

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector updated"
        argument = {'collector': (collector_name),
                    'collector_activate': collector_activate
                    }
        config = ('telemetry_collector_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_ip_port_update(self, **kwargs):
        """
        Method to update the ip address and port configured in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_ip: ip address of the collector
                 collector_port: port of the collector

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_ip_port_update(collector=('Profile1'),
            ...                           collector_ip='10.0.0.1', collector_port=1000)
            ...
        """
        (collector_name) = kwargs.pop('collector')
        collector_ip = kwargs.pop('collector_ip')
        collector_port = kwargs.pop('collector_port')

        self.telemetry_collector_validate(collector_name, None, None, None, collector_port)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector ip address and port updated"
        argument = {'collector': (collector_name),
                    'collector_ip_address': collector_ip,
                    'collector_port': collector_port
                    }
        config = ('telemetry_collector_ip_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_ip_address_update(self, **kwargs):
        """
        Method to update the ip address configured in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_ip: ip address of the collector

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_ip_address_update
            ...                  (collector=('Profile1'), collector_ip='10.0.0.1')
            ...
        """
        (collector_name) = kwargs.pop('collector')
        collector_ip = kwargs.pop('collector_ip')

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector ip address updated"
        argument = {'collector': (collector_name),
                    'collector_ip': collector_ip
                    }
        config = ('telemetry_collector_ip_collector_ip_address_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_port_update(self, **kwargs):
        """
        Method to update the port configured in telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector
                 collector_port: port of the collector

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_port_update(collector=('Profile1'),
            ...                                          collector_port=1000)
            ...
        """
        (collector_name) = kwargs.pop('collector')
        collector_port = kwargs.pop('collector_port')

        self.telemetry_collector_validate(collector_name, None, None, None, collector_port)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry collector port updated"
        argument = {'collector': (collector_name),
                    'collector_port': collector_port
                    }
        config = ('telemetry_collector_ip_port_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def interface_profile_update(self, **kwargs):
        """
        Method to update the telemetry interface profile
        args:
            kwargs:
                 interface: Mandatory
                    name(str): name of the interface-profile
                 interval: interface-profile interval

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.interface_profile_update(interface=('Profile1'),
            ...                                                               interval=60)
            ...
        """
        (name) = kwargs.pop('interface')
        interval = kwargs.pop('interval')

        self.telemetry_profile_validate(name, interval, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry interface-profile updated"
        argument = {'interface': (name),
                    'interval': interval
                    }
        config = ('telemetry_profile_interface_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def interface_profile_interval_update(self, **kwargs):
        """
        Method to update the interval value in telemetry interface profile
        args:
            kwargs:
                 interface: Mandatory
                    name(str): name of the interface-profile
                 interval: interface-profile interval

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.interface_profile_update(interface=('Profile1'),
            ...                                                          interval=60)
            ...
        """
        (name) = kwargs.pop('interface')
        interval = kwargs.pop('interval')

        self.telemetry_profile_validate(name, interval, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry interface-profile interval updated"
        argument = {'interface': (name),
                    'interval': interval
                    }
        config = ('telemetry_profile_interface_interval_update', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def interface_profile_interval_delete(self, **kwargs):
        """
        Method to delete the interval configuration on telemetry interface profile
        args:
            kwargs:
                 interface: Mandatory
                    name(str): name of the interface-profile

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.interface_profile_interval_delete
            ...                                             (interface=('Profile1'))
            ...
        """
        (name) = kwargs.pop('interface')

        self.telemetry_profile_validate(name, None, None)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry interface-profile interval deleted"
        argument = {'interface': (name),
                    }
        config = ('telemetry_profile_interface_interval_delete', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def interface_profile_interface_create(self, **kwargs):
        """
        Method to create the interface configuration on telemetry interface profile
        args:
            kwargs:
                 interface: Mandatory
                    name(str): name of the interface-profile
                 interface_:
                    interface_range(str): range of the interface

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.interface_profile_interval_delete
            ...                                          (interface=('Profile1'))
            ...
        """
        (name) = kwargs.pop('interface')
        (intf_range) = kwargs.pop('interface_')

        self.telemetry_profile_validate(name, None, intf_range)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry interface-profile interface created"
        argument = {'interface': (name),
                    'interface_': (intf_range)
                    }
        config = ('telemetry_profile_interface_interface_create', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def interface_profile_interface_delete(self, **kwargs):
        """
        Method to delete the interface configuration on telemetry interface profile
        args:
            kwargs:
                 interface: Mandatory
                    name(str): name of the interface-profile
                 interface_:
                    interface_range(str): range of the interface

        Returns:
            Returns dictionary keys (status_code, status_message). status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.interface_profile_interval_delete
            ...                                (interface=('Profile1'))
            ...
        """
        (name) = kwargs.pop('interface')
        (intf_range) = kwargs.pop('interface_')

        self.telemetry_profile_validate(name, None, intf_range)

        status = dict()
        # set default status buffer
        status['status_code'] = 0
        status['status_message'] = "telemetry interface-profile interface deleted"
        argument = {'interface': (name),
                    'interface_': (intf_range)
                    }
        config = ('telemetry_profile_interface_interface_delete', argument)
        try:
            response = self._callback(config, 'POST')
            if response.data != '':
                status['status_code'] = -1
                status['status_message'] = response.data
        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_get(self, **kwargs):
        """
        Method to get the telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector

        Returns:
            Returns dictionary keys (status_code, profile_type, profile_name).
            status_code=0 for SUCCESS and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_get(collector=('Profile1'))
            ...
        """
        (collector_name) = kwargs.pop('collector')

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        status['status_code'] = 0
        status['status_message'] = "Telemetry Collector get"
        # set default status buffer
        argument = {'collector': (collector_name)}
        config = ('telemetry_collector_get', argument)
        try:
            response = self._callback(config, handler='get_config')
            if response.data != '<output></output>':
                status['status_message'] = response.data
            else:
                status['status_code'] = -1
                status['status_message'] = 'Telemetry Collector not Found'

        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status

    def collector_activate_get(self, **kwargs):
        """
        Method to get activate status of telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector

        Returns:
            Returns True for SUCCESS
            and False for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_activate_get(collector=('Profile1'))
            ...
        """
        (collector_name) = kwargs.pop('collector')

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        # set default status buffer
        argument = {'collector': (collector_name)}
        config = ('telemetry_collector_activate_get', argument)
        try:
            response = self._callback(config, handler='get_config')
            if response.data == '':
                return False
            else:
                util = Util(response.data)
                activate_status = util.find(util.root, './/activate')
                if activate_status and activate_status == 'true':
                    return True
                else:
                    return False

        except Exception:
            return False

        return True

    def collector_profile_get(self, **kwargs):
        """
        Method to get profile of telemetry collector
        args:
            kwargs:
                 collector: Mandatory
                    collector_name(str): name of the telemetry collector

        Returns:
            Returns dictionary keys (status_code, profile_type, profile_name).
                     status_code=0 for SUCCESS
            and status_code=-1 for FAILURE

        Example:
            >>> import pyswitch.device
            >>> switch = '10.24.86.57'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as device:
            ...     response = device.telemetry.collector_profile_get(collector=('Profile1'))
            ...
        """
        (collector_name) = kwargs.pop('collector')

        self.telemetry_collector_validate(collector_name, None, None, None, None)

        status = dict()
        status['status_code'] = 0
        # set default status buffer
        argument = {'collector': (collector_name)}
        config = ('telemetry_collector_profile_get', argument)
        try:
            response = self._callback(config, handler='get_config')
            util = Util(response.data)
            profiletype = util.find(util.root, './/collector-profiletype')
            profilename = util.find(util.root, './/collector-profilename')
            if profiletype and profilename:
                status['profile_type'] = profiletype
                status['profile_name'] = profilename
            else:
                status['status_code'] = -1
                status['status_message'] = 'Collector Profile is not present'

        except Exception, exc:
            status['status_code'] = -1
            status['status_message'] = 'Exception:' + exc.message

        return status
