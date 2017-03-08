import pyswitch.utilities as util


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
        """

        get_system_uptime = ('get_system_uptime_rpc', {})

        results = self._callback(get_system_uptime, handler='get')

        system_uptime = dict(days=util.find(results.json, '$..days'),
                             hours=util.find(results.json, '$..hours'),
                             minutes=util.find(results.json, '$..minutes'),
                             seconds=util.find(results.json, '$..seconds'))
        return system_uptime
