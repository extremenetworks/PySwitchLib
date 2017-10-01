"""
import pyswitch.utilities
from pyswitch.exceptions import InvalidVlanId
"""

from pyswitch.snmp.base.interface import Interface as BaseInterface
# from pyswitch.utilities import Util


class Interface(BaseInterface):
    """
      The Interface class holds all the actions associated with the Interfaces
      of a MLX device.

      Attributes:
          None
      """

    def __init__(self, callback):
        """
        Interface init function.

        Args:
           callback: Callback function that will be called for each action.

        Returns:
           Interface Object

        Raises:
           None
        """
        super(Interface, self).__init__(callback)

    @property
    def valid_int_types(self):

        return [
            'ethernet',
            'port_channel',
            'loopback',
            've'
        ]

    @property
    def valid_intp_types(self):
        return [
            'ethernet'

        ]

    @property
    def l2_mtu_const(self):
        # TBD change below defaults
        minimum_mtu = 1548
        maximum_mtu = 9216
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_mtu_const(self):
        # TBD change below defaults
        minimum_mtu = 1300
        maximum_mtu = 9194
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_ipv6_mtu_const(self):
        # TBD change below defaults
        minimum_mtu = 1300
        maximum_mtu = 9194
        return (minimum_mtu, maximum_mtu)

    @property
    def has_rbridge_id(self):
        return False

    def fabric_isl(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def fabric_trunk(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def ip_anycast_gateway(self, **kwargs):
        raise ValueError('Not available on this Platform')

    def add_vlan_int(self, vlan_id_list, desc=None):
        """
        Add VLAN Interface. VLAN interfaces are required for VLANs even when
        not wanting to use the interface for any L3 features.

        Args:
            vlan_id_list: List of VLAN interface being created. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        try:
            cli_arr = []
            for vlan in vlan_id_list:
                cli_arr.append('vlan' + " " + str(vlan) + " " + 'name' + " " + desc)
            self._callback(cli_arr, handler='cli-set')
            return True
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to create VLAN due to %s', reason)
            return False

    def admin_state(self, **kwargs):
        """Set interface administrative state.

        Args:
            int_type (str): Type of interface. (ethernet, etc).
            name (str): Name of interface. (1/1, etc).
            enabled (bool): Is the interface enabled? (True, False)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `enabled` is not passed and
                `get` is not ``True``.
            ValueError: if `int_type`, `name`, or `enabled` are invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.admin_state(
            ...         int_type='ethernet', name='1/1',
            ...         enabled=False)
            ...         dev.interface.admin_state(
            ...         int_type='ethernet', name='1/1',
            ...         enabled=True)
        """

        int_type = kwargs.pop('int_type').lower()
        get = kwargs.pop('get', False)
        if get:
            enabled = None
        else:
            enabled = kwargs.pop('enabled')
        port_id = kwargs.pop('port_id', None)

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = self.valid_int_types
        ifAdminStatus_oid = "1.3.6.1.2.1.2.2.1.7"
        ifadminStatus_index = ifAdminStatus_oid + '.' + repr(port_id)
        if int_type == 'ethernet' and port_id is None:
            raise ValueError('pass valid port-id')

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if not isinstance(enabled, bool) and not get:
            raise ValueError('`enabled` must be `True` or `False`.')

        try:
            if get:
                value = callback(ifadminStatus_index)
                if value == 1:
                    enabled = True
                else:
                    enabled = False
                return enabled
            else:
                if enabled:
                    value = 1
                else:
                    value = 2
                state_args = (ifadminStatus_index, value)
                return callback(state_args, handler='snmp-set')
        except AttributeError:
            return None
        except Exception as error:
            reason = error.message
            raise ValueError('Failed to set interface admin status to %s',
                reason)
        return None
