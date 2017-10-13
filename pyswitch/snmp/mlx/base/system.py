
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

        if kwargs.pop('get', False):
            return mtu_match.group(1)

        if int(mtu) == int(mtu_match.group(1)):
            raise ValueError("system MTU:%s is already configured" % mtu)

        cli_arr = []
        cli_arr.append('default-max-frame-size' + ' ' + str(mtu))
        cli_res = callback(cli_arr, handler='cli-set')
        error = re.search(r'Error:(.+)', cli_res)
        if error:
            raise ValueError("%s" % error.group(0))
        else:
            success_msg = re.search(r'Reload required.(.+)', cli_res)

        return success_msg.group(0)
