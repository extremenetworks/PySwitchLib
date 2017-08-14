from pyswitch.raw.base.interface import Interface as BaseInterface
import template
import logging
class Interface(BaseInterface):
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
        return [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet',
            'port_channel'
        ]

    @property
    def valid_intp_types(self):
        return [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet',
        ]

    @property
    def l2_mtu_const(self):
        minimum_mtu = 1522
        maximum_mtu = 9216
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_mtu_const(self):
        minimum_mtu = 1300
        maximum_mtu = 9100
        return (minimum_mtu, maximum_mtu)

    @property
    def l3_ipv6_mtu_const(self):
        minimum_mtu = 1280
        maximum_mtu = 9100
        return (minimum_mtu, maximum_mtu)

    @property
    def has_rbridge_id(self):
        return True

    def add_vlan_int(self, vlan_id_list,desc=None):
        """
        Add VLAN Interface. VLAN interfaces are required for VLANs even when
        not wanting to use the interface for any L3 features.

        Args:
            vlan_id: ID for the VLAN interface being created. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        try:
            data_list = []
            for vlan_id in vlan_id_list:
                if desc:
                    data_list.append(getattr(template, 'vlan_id_desc').format(vlan_id=vlan_id,
                                                                              desc=desc))
                else:
                    data_list.append(getattr(template, 'vlan_id').format(vlan_id=vlan_id))

            str = "".join(data_list)

            config = getattr(template, 'vlan_create').format(vlan_list=str)
            self._callback(config)

        except Exception as error:
            logging.error(error)
            return False

