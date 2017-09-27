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
