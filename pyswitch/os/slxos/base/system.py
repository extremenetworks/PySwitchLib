from pyswitch.utilities import Util
from pyswitch.os.base.system import System as BaseSystem
import xml.etree.ElementTree as ET


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
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `router_id` is not specified.
        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.86.60', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.router_id(router_id='10.24.39.211')
        """
        router_id = kwargs.pop('router_id')
        callback = kwargs.pop('callback', self._callback)

        rid_args = {'router_id': router_id}
        config = ('ip_router_id_update', rid_args)
        return callback(config)

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
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
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
            callback (function): A function executed upon completion of the method.  The only
            parameter passed to `callback` will be the ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id` is not specified.
        Examples:
            >>> import pyswitch.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
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
            >>> import pyswitch.device
            >>> conn = ('10.24.39.202', '22')
            >>> auth = ('admin', 'password')
            >>> with pyswitch.device.Device(conn=conn, auth=auth) as dev:
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
                callback (function): A function executed upon completion of method.  The only
                parameter passed to `callback` will be ``ElementTree`` `config`.

            Returns:
                Return value of `callback`.

            Raises:
                KeyError: if `int_type`, `name`, or `mtu` is not specified.
                ValueError: if `int_type`, `name`, or `mtu` is invalid.

            Examples:
                >>> import pyswitch.device
                >>> switches = ['10.24.86.57']
                >>> auth = ('admin', 'password')
                >>> for switch in switches:
                ...  conn = (switch, '22')
                ...  with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...         output = dev.system.system_ip_mtu(mtu='1666')
                ...         output = dev.system.system_ip_mtu(get=True)
                ...         assert output == '1666'
                ...         output = dev.system.system_ip_mtu(mtu='1667',version=6)
                ...         output = dev.system.system_ip_mtu(get=True,version=6)
                ...         assert output == '1667'
        """

        callback = kwargs.pop('callback', self._callback)
        version = kwargs.pop('version', 4)
        if version is 4:
            ip_prefix = 'ip'
            # ns = '{urn:brocade.com:mgmt:brocade-ip-access-list}'
        if version is 6:
            ip_prefix = 'ipv6'
            # ns = '{urn:brocade.com:mgmt:brocade-mld-snooping}'

        if kwargs.pop('get', False):
            method_name = '%s_mtu_get' % ip_prefix
            config = (method_name, {})
            op = callback(config, handler='get_config')

            util = Util(op.data)
            return util.find(util.root, './/mtu')

        mtu = kwargs.pop('mtu')

        if version is 4:
            minimum_mtu = 1300
            maximum_mtu = 9194
            if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
                raise ValueError(
                    "Incorrect mtu value, Valid Range %s-%s" %
                    (minimum_mtu, maximum_mtu))
        if version is 6:
            minimum_mtu = 1300
            maximum_mtu = 9194
            if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
                raise ValueError(
                    "Incorrect mtu value, Valid Range %s-%s" %
                    (minimum_mtu, maximum_mtu))

        mtu_name = 'global_%s_mtu' % ip_prefix
        mtu_args = {mtu_name: mtu}

        method_name = '%s_mtu_update' % ip_prefix

        config = (method_name, mtu_args)
        return callback(config)

    def system_l2_mtu(self, **kwargs):
        """Set system mtu.

            Args:

                mtu (str): Value between 1522 and 9216
                version (int) : 4 or 6
                callback (function): A function executed upon completion of method.  The only
                parameter passed to `callback` will be ``ElementTree`` `config`.

            Returns:
                Return value of `callback`.

            Raises:
                KeyError: if `int_type`, `name`, or `mtu` is not specified.
                ValueError: if `int_type`, `name`, or `mtu` is invalid.

            Examples:
                >>> import pyswitch.device
                >>> switches = ['10.24.86.57']
                >>> auth = ('admin', 'password')
                >>> for switch in switches:
                ...  conn = (switch, '22')
                ...  with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...         output = dev.system.system_l2_mtu(mtu='1666')
                ...         output = dev.system.system_l2_mtu(get=True)
                ...         assert output == '1666'
            """

        callback = kwargs.pop('callback', self._callback)

        if kwargs.pop('get', False):
            method_name = 'mtu_get'
            config = (method_name, {})
            op = callback(config, handler='get_config')

            util = Util(op.data)
            return util.find(util.root, './/mtu')

        mtu = kwargs.pop('mtu')

        minimum_mtu = 1548
        maximum_mtu = 9216
        if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
            raise ValueError(
                "Incorrect mtu value, Valid Range %s-%s" %
                (minimum_mtu, maximum_mtu))

        mtu_name = 'global_l2_mtu'
        mtu_args = {mtu_name: mtu}

        method_name = 'mtu_update'

        config = (method_name, mtu_args)
        return callback(config)

    def persist_config(self, **kwargs):
        """ save the configurations on the device.
        Args:
            src_name (str): 'running-config/default-config'
            dst_name (str): 'startup-config'
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return session_id value.
        Raises:
            ValueError when `src_name` is not passed
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.system.persist_config(src_name='running-config')
        """
        src = kwargs.pop('src_name')
        dst = kwargs.pop('dst_name', 'startup-config')

        if src not in ['running-config', 'default-config']:
            raise ValueError('`src_name` must be running-config/default-config')
        if dst != 'startup-config':
            raise ValueError('`dst_name` must be startup-config')

        save_args = dict(src=src, dest=dst)
        config = ('bna_config_cmd_rpc', save_args)
        response = self._callback(config, 'get')
        return self.parse_persist_config_response(response)

    def parse_persist_config_response(self, response):

        session_id = ''
        if response.data != '<output></output>':
            root = ET.fromstring(response.data)
            session_status = root.find('status').text
            if session_status == 'in-progress':
                session_id = root.find('session-id').text
                return session_id
        return session_id

    def persist_config_status(self, session_id):
        """
        Method to check save operation status

        args:
            None

        Returns:
            Returns save config status message
        Example:
                >>> import pyswitch.device
                >>> switches = ['10.24.86.60']
                >>> auth = ('admin', 'password')
                >>> for switch in switches:
                ...     conn = (switch, '22')
                ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...     status = dev.system.persist_config_status(session_id=2)
                ...     print(status)
        """
        save_res_args = dict(session_id=session_id)
        re_config = ('bna_config_cmd_status_rpc', save_res_args)
        res_response = self._callback(re_config, 'get')
        save_result = ''
        if res_response.data != '<output></output>':
            root = ET.fromstring(res_response.data)
            save_result = root.find('status').text
        return save_result
