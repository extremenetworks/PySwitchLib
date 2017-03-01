from pyswitch.os.base.bgp import Bgp as BaseBgp


class Bgp(BaseBgp):
    """
      The Interface class holds all the actions assocaiated with the Interfaces
      of a SLXOS device.

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

        super(Bgp, self).__init__(callback)

    @property
    def valid_int_types(self):

        return [
            'ethernet',
            'port_channel'
        ]

    @property
    def valid_intp_types(self):
        return [
            'ethernet',
        ]

    @property
    def has_rbridge_id(self):
        return False

    @property
    def os(self):
        return 'slxos'
