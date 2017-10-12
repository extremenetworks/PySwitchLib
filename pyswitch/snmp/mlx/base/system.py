
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

                mtu (str): Value between 1522 and 9216
                version (int) : 4 or 6
                callback (function): A function executed upon completion of
                the method.  The only parameter passed to `callback` will be
                 the
                    ``ElementTree`` `config`.

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
                ...         output = dev.system.system_l2_mtu(mtu='1667',version=6)
                ...         assert output == '1667'
        """

        callback = kwargs.pop('callback', self._callback)

        if kwargs.pop('get', False):
            cli_cmd = 'show max-frame-size'
            cli_res = callback(cli_cmd, handler='cli-get')
            mtu = re.search(r'Default max frame size for ETH : (.+)', cli_res)
            return mtu.group(1)

        mtu = kwargs.pop('mtu')

        minimum_mtu = 1298
        maximum_mtu = 9216
        if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
            raise ValueError(
                "Incorrect mtu value, Valid Range %s-%s" %
                (minimum_mtu, maximum_mtu))
        cli_arr = []
        cli_arr.append('default-max-frame-size' + ' ' + str(mtu))
        cli_res = callback(cli_arr, handler='cli-set')
        error = re.search(r'Error:(.+)', cli_res)
        if error:
            raise ValueError("%s" % error.group(0))
        else:
           success_msg = re.search(r'Reload required.(.+)', cli_res)

        return success_msg.group(0)
