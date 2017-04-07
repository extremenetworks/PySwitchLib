from pyswitch.utilities import Util
from pyswitch.os.base.system import System as BaseSystem


class System(BaseSystem):
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

        super(System, self).__init__(callback)

    def chassis_name(self, **kwargs):
        """Get device's chassis name/Model.
        """

        config = ('switch_attributes_get', {'resource_depth': 3})

        output = self._callback(config, handler='get_config')
        util = Util(output.data)
        chassis_name = util.find(util.root, './/chassis-name')
        return chassis_name

    def router_id(self, **kwargs):
        """Configures device's Router ID.
        Args:
            router_id (str): Router ID for the device.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `router_id` is not specified.
        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.router_id(router_id='10.24.39.211',
            ...     rbridge_id='225')
            ...     dev.system.router_id() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        raise ValueError('Not available on this Platform')

    def host_name(self, **kwargs):
        """Configures device's host name.
        Args:
            host_name (str): The host name of the device.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id` is not specified.
        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     dev.system.host_name(host_name='sw0')
            ...     output = dev.system.host_name(get=True)

        """
        is_get_config = kwargs.pop('get', False)

        if not is_get_config:
            host_name = kwargs.pop('host_name', 'sw0')
        else:
            host_name = ' '
        callback = kwargs.pop('callback', self._callback)
        rid_args = dict(host_name=host_name)

        config = ('switch_attributes_update', rid_args)

        if is_get_config:
            config = (
                'switch_attributes_get', {
                    'resource_depth': 2})
            output = callback(config, handler='get_config')
            util = Util(output.data)
            return util.find(util.root, './/host-name')

        return callback(config)

    def rbridge_id(self, **kwargs):
        """Configures device's rbridge ID. Setting this property will need
        a switch reboot
        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id` is not specified.
        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.rbridge_id(rbridge_id='225')
            ...     output = dev.system.rbridge_id(rbridge_id='225', get=True)
            ...     dev.system.rbridge_id() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        raise ValueError('Not available on this Platform')

    def maintenance_mode(self, **kwargs):
        """Configures maintenance mode on the device
        Args:
            rbridge_id (str): The rbridge ID of the device on which
            Maintenance mode
                will be configured in a VCS fabric.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id` is not specified.
        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.202', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.maintenance_mode(rbridge_id='226')
            ...     output = dev.system.maintenance_mode(rbridge_id='226',
            ...     get=True)
            ...     assert output == True
            ...     output = dev.system.maintenance_mode(rbridge_id='226',
            ...     delete=True)
            ...     output = dev.system.maintenance_mode(rbridge_id='226',
            ...     get=True)
            ...     assert output == False
        """
        raise ValueError('Not available on this Platform')

    def system_ip_mtu(self, **kwargs):
        """Set system mtu.

            Args:

                mtu (str): Value between 1522 and 9216
                version (int) : 4 or 6
                callback (function): A function executed upon completion of
                    method.  The only parameter passed to `callback` will be s
                    ``ElementTree`` `config`.

            Returns:
                Return value of `callback`.

            Raises:
                KeyError: if `int_type`, `name`, or `mtu` is not specified.
                ValueError: if `int_type`, `name`, or `mtu` is invalid.

            Examples:
                >>> import pyswitch.device
                >>> switches = ['10.24.39.211', '10.24.39.203']
                >>> auth = ('admin', 'password')
                >>> for switch in switches:
                ...  conn = (switch, '22')
                ...  with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...         output = dev.interface.system_mtu(mtu='1666')
                Traceback (most recent call last):
                KeyError
            """

        raise ValueError('Not available on this Platform')

    def system_l2_mtu(self, **kwargs):
        """Set system mtu.

            Args:

                mtu (str): Value between 1522 and 9216
                version (int) : 4 or 6
                callback (function): A function executed upon completion of
                    method.  The only parameter passed to `callback` will be
                    ``ElementTree`` `config`.

            Returns:
                Return value of `callback`.

            Raises:
                KeyError: if `int_type`, `name`, or `mtu` is not specified.
                ValueError: if `int_type`, `name`, or `mtu` is invalid.

            Examples:
                >>> import pyswitch.device
                >>> switches = ['10.24.39.211', '10.24.39.203']
                >>> auth = ('admin', 'password')
                >>> for switch in switches:
                ...  conn = (switch, '22')
                ...  with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...         output = dev.interface.system_l2_mtu(mtu='1666')
                Traceback (most recent call last):
                KeyError
            """

        raise ValueError('Not available on this Platform')
