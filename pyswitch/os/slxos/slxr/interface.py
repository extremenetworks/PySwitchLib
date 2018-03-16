from pyswitch.os.slxos.base.interface import Interface as BaseInterface


class Interface(BaseInterface):
    """
      The Interface class holds all the actions assocaiated with the Interfaces
      of a NOS device.

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

    def vrrpe_vmac(self, **kwargs):
        """Set vrrpe virtual mac.

        Args:
            int_type (str): Type of interface. (ethernet,
                ve, etc).
            name (str): Name of interface. (1/5, 0/10, etc).
            vrid (str): vrrpev3 ID.
            enable (bool): If vrrpe virtual MAC should be enabled
                or disabled.Default:``True``.
            get (bool): Get config instead of editing config. (True, False)
            virtual_mac (str):Virtual mac-address in the format
            02e0.5200.00xx.
            callback (function): A function executed upon completion
            of the  method.  The only parameter passed to `callback`
            will be the ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vmac` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vmac` is invalid.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vmac` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vmac` is invalid.

        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.services.vrrpe(enable=False)
            ...         output = dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89',vrid='1',
            ...         vip='2002:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         output = dev.services.vrrpe(enable=False)
            ...         output = dev.interface.vrrpe_vmac(int_type='ve',
            ...         name='89', vrid='1', virtual_mac='aaaa.bbbb.cccc')
        """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        enable = kwargs.pop('enable', True)
        version = kwargs.pop('version', 4)
        get = kwargs.pop('get', False)
        virtual_mac = kwargs.pop('virtual_mac', '02e0.5200.00xx')

        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ve']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        arguments = {int_type: name}

        if get:
            if version == 4:
                method_name = 'interface_%s_vrrp_extended_group_' \
                              'get' % int_type
                vrid_name = 'vrrpe'
            else:
                method_name = 'interface_%s_ipv6_vrrp_extended_group_' \
                              'get' % int_type
                vrid_name = 'vrrpv3e'

            arguments[vrid_name] = vrid
            config = (method_name, arguments)
            x = callback(config, handler='get_config')
            if '<virtual-mac>02e0.5200.00xx</virtual-mac>' in x.data:
                return '02e0.5200.00xx'
            else:
                return None

        if version == 4:
            method_name = 'interface_%s_vrrp_extended_group_virtual' \
                          '_mac_' % int_type
            vrid_name = 'vrrpe'
            vmac_name = 'virtual_mac'
        else:
            method_name = 'interface_%s_ipv6_vrrp_extended_group_virtual' \
                          '_mac_' % int_type
            vrid_name = 'vrrpv3e'
            vmac_name = 'virtual_mac'

        arguments[vrid_name] = vrid

        if not enable:
            method_name = "%sdelete" % method_name
        else:
            arguments[vmac_name] = virtual_mac
            method_name = "%supdate" % method_name
        config = (method_name, arguments)
        return callback(config)
