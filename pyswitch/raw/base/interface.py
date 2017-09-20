from jinja2 import Template

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

    def conversation_property(self, **kwargs):
        """

        Creates Overlay Gateway

        Examples:
        >>> import pyswitch.device
        >>> conn = ('10.26.8.210', '22')
        >>> auth = ('admin', 'password')
        >>> with pyswitch.device.Device(conn=conn, auth=auth,connection_type='NETCONF') as dev:
        ...      output = dev.interface.conversation_property(get=True)
        ...      print output
        """

        get_config = kwargs.pop('get', False)

        if not get_config:
            arp_aging_timeout = kwargs.pop('arp_aging_timeout', '300')
            mac_aging_timeout = kwargs.pop('mac_aging_timeout', '300')
            mac_legacy_aging_timeout = kwargs.pop('mac_legacy_aging_timeout', '1800')
            mac_move_limit = kwargs.pop('mac_move_limit', '5')
            t = Template(getattr(template, 'conversation_property_create'))
            config = t.render(arp_aging_timeout=arp_aging_timeout,
                              mac_aging_timeout=mac_aging_timeout,
                              mac_legacy_aging_timeout=mac_legacy_aging_timeout,
                              mac_move_limit=mac_move_limit)
            self._callback(config)

        if get_config:
            if get_config:
                config = getattr(template, 'mac_address_table_get').format()
                rest_root = self._callback(config, handler='get_config')
                util = Util(rest_root)
                conversational_mac = True if util.find(util.root,
                                                       './/learning-mode') is not None else False
                mac_aging_timeout = util.find(util.root, './/conversational-time-out')
                mac_legacy_aging_timeout = util.find(util.root, './/legacy-time-out')
                mac_move_limit = util.find(util.root, './/mac-move-limit')
                mac_move_enable = True if util.find(util.root,
                                                    './/mac-move-detect-enable') is not None else\
                    False

                config = getattr(template, 'host_table_get').format()
                rest_root = self._callback(config, handler='get_config')
                util = Util(rest_root)

                conversational_arp = True if util.find(util.root,
                                                       './/aging-mode') is not None else False
                arp_aging_timeout = util.find(util.root, './/conversational-time-out')

                return {"conversational_mac": conversational_mac,
                        "mac_aging_timeout": mac_aging_timeout,
                        'mac_legacy_aging_timeout': mac_legacy_aging_timeout,
                        'mac_move_limit': mac_move_limit,
                        'mac_move_enable': mac_move_enable,
                        "conversational_arp": conversational_arp,
                        "arp_aging_timeout": arp_aging_timeout,
                        }
