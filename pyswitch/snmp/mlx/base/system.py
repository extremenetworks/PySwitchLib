
from pyswitch.snmp.base.system import System as BaseSystem
import re


class System(BaseSystem):
    """
        System class containing all system level methods and attributes.
    """

    def __init__(self, callback):
        """
        System init method.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            System Object

        Raises:
            None
        """

        super(System, self).__init__(callback)

    def system_l2_mtu(self, **kwargs):
        """Set system mtu.

            Args:

                mtu (str): Value between 1298 and 9216
                callback (function): A function executed upon completion of
                the method.

            Returns:
                Return True or raise ValueError

            Raises:
                KeyError: if `int_type`, `name`, or `mtu` is not specified.
                ValueError: if `int_type`, `name`, or `mtu` is invalid.

            Examples:
                >>> import pyswitch.device
                >>> switches = ['10.24.85.107']
                >>> auth = ('admin', 'admin')
                >>> for switch in switches:
                ...  conn = (switch, '22')
                ...  with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...         output = dev.system.system_l2_mtu(mtu='1666')
                ...         assert output == '1666'
                ...         output = dev.system.system_l2_mtu(mtu='1667')
                ...         assert output == '1667'
                ...         output = dev.system.system_l2_mtu(get=True)
                ...         print output
        """

        callback = kwargs.pop('callback', self._callback)
        mtu = kwargs.pop('mtu')

        minimum_mtu = 1298
        maximum_mtu = 9216
        if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
            raise ValueError(
                "Incorrect mtu value, Valid Range %s-%s" %
                (minimum_mtu, maximum_mtu))

        cli_cmd = 'show max-frame-size'
        cli_res = callback(cli_cmd, handler='cli-get')
        mtu_match = re.search(r'Default max frame size for ETH : (.+)', cli_res)

        # default system mtu
        system_mtu = 1548

        if mtu_match:
            system_mtu = mtu_match.group(1)

        if kwargs.pop('get', False):
            return int(system_mtu)

        if int(mtu) == int(system_mtu):
            raise UserWarning("system MTU:%s is already configured" % mtu)

        cli_arr = []
        cli_arr.append('default-max-frame-size' + ' ' + str(mtu))
        cli_res = callback(cli_arr, handler='cli-set')
        error = re.search(r'Error:(.+)', cli_res)
        if error:
            raise ValueError("%s" % error.group(0))
        else:
            success_msg = re.search(r'Reload required.(.+)', cli_res)

        if success_msg:
            raise UserWarning("successfully set system l2 mtu: %s" % success_msg.group(0))

    def system_ip_mtu(self, **kwargs):
        """Set system mtu.

            Args:

                mtu (str): Value between 576  and 9198 for ipv4
                           Value between 1280 - 9198 for ipv6
                version (int) : 4 or 6
                callback (function): A function executed upon completion of
                    the method.

            Returns:
                Return value of True.

            Raises:
                ValueError:  `mtu` is invalid.

            Examples:
                >>> import pyswitch.device
                >>> switches = ['10.24.85.107']
                >>> auth = ('admin', 'admin')
                >>> for switch in switches:
                ...  conn = (switch, '22')
                ...  with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...         output = dev.system.system_ip_mtu(mtu='1666')
                ...         output = dev.system.system_ip_mtu(mtu='1667',version=6)
            """

        callback = kwargs.pop('callback', self._callback)
        version = kwargs.pop('version', 4)

        mtu = kwargs.pop('mtu')

        cli_arr = []

        if version is 4:
            minimum_mtu = 576
            maximum_mtu = 9198
            if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
                raise ValueError(
                    "Incorrect mtu value, Valid Range %s-%s" %
                    (minimum_mtu, maximum_mtu))
            cli_arr.append('ip global-mtu' + ' ' + str(mtu))

        if version is 6:
            minimum_mtu = 1280
            maximum_mtu = 9198
            if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
                raise ValueError(
                    "Incorrect mtu value, Valid Range %s-%s" %
                    (minimum_mtu, maximum_mtu))

            cli_arr.append('ipv6 global-mtu' + ' ' + str(mtu))

        try:
            cli_res = callback(cli_arr, handler='cli-set')
            error = re.search(r'Error (.+)', cli_res)
            invalid_input = re.search(r'Invalid input', cli_res)
            if error:
                raise ValueError("%s" % error.group(0))
            if invalid_input:
                raise ValueError("%s" % invalid_input.group(0))
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to set system l3 mtu %s' % (reason))

    def persist_config(self, **kwargs):
        """Perform write memory operation.

            Args:
                callback (function): A function executed upon completion of
                    the method.
            Returns:
                Return 'completed' or 'failed'.
            Raises:
                ValueError: If the CLI operation fails on the device.
            Examples:
                >>> import pyswitch.device
                >>> switches = ['10.24.85.107']
                >>> auth = ('admin', 'admin')
                >>> for switch in switches:
                ...  conn = (switch, '22')
                ...  with pyswitch.device.Device(conn=conn, auth=auth) as dev:
                ...         output = dev.system.persist_config()
            """
        callback = kwargs.pop('callback', self._callback)
        try:
            cli_res = callback('write memory', handler='cli-set')
            success_msg = re.search(r'Write startup-config done', cli_res)
            if not success_msg:
                response = 'failed'
            else:
                response = 'completed'
            return response
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to perform persist operation due to %s',
                             (reason))
