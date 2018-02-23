import abc


class AbstractDevice:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self, exctype, excisnt, exctb):
        pass

    @abc.abstractproperty
    def os_type(self):
        pass

    @abc.abstractproperty
    def suports_rbridge(self):
        pass

    @abc.abstractproperty
    def platform_type(self):
        pass

    @abc.abstractproperty
    def firmware_version(self):
        pass

    @abc.abstractmethod
    def _callback_main(self, call, handler='edit_config', target='running',
                       source='startup'):
        pass

    @abc.abstractmethod
    def reconnect(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass


class DeviceCommError(Exception):
    """
    Error with device communication.
    """
    pass
