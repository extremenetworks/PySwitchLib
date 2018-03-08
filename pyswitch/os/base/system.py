from pyswitch.utilities import Util


class System(object):
    """
        System class containing all system level methods and attributes.
        """

    def __init__(self, callback):
        """System init method.
        Args:
            callback: Callback function that will be called for each action.
        Returns:
            System Object
        Raises:
            None
        """

        self._callback = callback

    @property
    def uptime(self):
        """dict: device uptime
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.231']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.system.uptime
        """

        get_system_uptime = ('get_system_uptime_rpc', {})

        results = self._callback(get_system_uptime, handler='get')

        util = Util(results.data)

        system_uptime = dict(days=util.find(util.root, './/days'),
                             hours=util.find(util.root, './/hours'),
                             minutes=util.find(util.root, './/minutes'),
                             seconds=util.find(util.root, './/seconds'))
        return system_uptime

    def persist_config(self, **kwargs):
        raise ValueError('Persist configuration is not supported on this platform')

    def parse_persist_config_response(self, **kwargs):
        raise ValueError('Persist configuration is not supported on this platform')

    def persist_config_status(self, **kwargs):
        raise ValueError('Persist configuration is not supported on this platform')

    def clock_timezone(self, **kwargs):

        """ Add/Get clock timezone of the device
        Args:
            timezone(str): time-zone for the device
        Returns:
            Return value of the callback
        Raises:
            KeyError: if `host_name` is not passed.
            ValueError: if `host_name` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.85.107']
            >>> auth = ('admin', 'admin')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.system.clock_timezone(timezone='us/alaska', rbridge_id='1')
            ...         output = dev.system.clock_timezone(timezone='us/alaska')
            ...         output = dev.system.clock_timezone(get=True)
            ...         output = dev.system.clock_timezone(get=True, rbridge_id='1')
        """
        args = dict()
        rbridge_id = kwargs.pop('rbridge_id', None)
        if rbridge_id is not None:
            method_name = 'rbridge_id_clock_timezone_update'
            get_method_name = 'rbridge_id_clock_timezone_get'
        else:
            method_name = 'clock_update'
            get_method_name = 'clock_get'

        if rbridge_id is not None:
            args['rbridge_id'] = rbridge_id

        if kwargs.pop('get', False):
            result = dict()
            config = (get_method_name, args)
            output = self._callback(config, handler='get_config')
            util = Util(output.data)
            time_zone = util.find(util.root, './/timezone')
            result['zone'] = time_zone
            return result

        args['timezone'] = None
        timezone_arr = ['Africa/Dar_es_Salaam',
                        'America/Port-au-Prince',
                        'Antarctica/DumontDUrville',
                        'Antarctica/McMurdo',
                        'Etc/GMT']
        timezone = kwargs.pop('time_zone')
        for each_item in timezone_arr:
            if timezone.lower() == each_item.lower():
                args['timezone'] = each_item
        if args['timezone'] is None:
            args['timezone'] = timezone.title()
        config = (method_name, args)
        return self._callback(config)
