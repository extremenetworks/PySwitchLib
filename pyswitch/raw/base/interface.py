import logging

from pyswitch.raw.nos.base import template
from pyswitch.utilities import Util


class Interface(object):
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
        self._callback = callback

    @property
    def valid_int_types(self):

        return []

    @property
    def has_rbridge_id(self):
        return True

    def method_prefix(self, method):
        if self.has_rbridge_id:
            return 'rbridge_id_%s' % method
        else:
            return method



    def create_loopback(self, **kwargs):
        """
        Add loopback Interface .
        Args:
            lb_name: loopback name with which the Ve interface needs to be
             created.
            enable (bool): If vrf fowarding should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            ValueError: if `ve_name` is invalid.
        Examples:
            >>> import pyswitch.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pyswitch.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.create_loopback(
             ...         lb_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_loopback(
            ...         get=True,
            ...         rbridge_id='1')
            ...         output = dev.interface.create_loopback(
            ...         enable=False,
            ...         lb_name='101',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        lb_name = kwargs.pop('lb_name', '')

        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        ve_args = dict()
        if self.has_rbridge_id:
            rbridge_id = kwargs.pop('rbridge_id', '1')
            ve_args['rbridge_id'] = rbridge_id
        if get:
            enable = None

        method_name = self.method_prefix('interface_loopback_')

        if get:
            config = getattr(template, self.method_prefix('interface_loopback_get')).format(**ve_args)
            output = callback(config, handler='get_config')
            util = Util(output)
            return util.findall(util.root, './/id')

        ve_args['loopback'] = lb_name
        if not enable:
            method_name = "%sdelete" % method_name
        else:
            method_name = "%screate" % method_name
        config = getattr(template, method_name).format(**ve_args)
        return callback(config,handler='edit_config')


