from jinja2 import Template

import re
from xmljson import parker
import json
import template
from pyswitch.raw.base.interface import Interface as BaseInterface
from pyswitch.utilities import Util
from pyswitch.utilities import validate_interface


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

    def add_vlan_int(self, vlan_id_list, desc=None):
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
            raise ValueError(error.message)

    def del_vlan_int(self, vlan_id_list):
        """
        Delete VLAN Interfaces.

        Args:
            vlan_id_list: List of VLAN interfaces being deleted. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            ValueError
        """
        try:
            data_list = []
            for vlan_id in vlan_id_list:
                data_list.append(getattr(template, 'vlan_delete').format(vlan_id=vlan_id))
            str = "".join(data_list)

            config = getattr(template, 'vlan_bulk_delete').format(vlan_list=str)
            self._callback(config)
            return True

        except Exception as e:
            reason = e.message
            raise ValueError(reason)

    def overlay_gateway(self, **kwargs):
        """

        Creates Overlay Gateway

        Examples:
        >>> import pyswitch.device
        >>> conn = ('10.26.8.210', '22')
        >>> auth = ('admin', 'password')
        >>> with pyswitch.device.Device(conn=conn, auth=auth,connection_type='NETCONF') as dev:
        ...      output = dev.interface.overlay_gateway(gw_name='Leaf1', loopback_id=2,

        ...      gw_type = 'layer2-extension',vni_auto=False,rbridge_id=None)
        ...      output = dev.interface.overlay_gateway(get=True)
        ...      print output
        """
        get_config = kwargs.pop('get', False)

        if not get_config:
            gw_name = kwargs.pop('gw_name')
            gw_type = kwargs.pop('gw_type', 'layer2-extension')
            vni_auto = kwargs.pop('vni_auto', True)
            rbridge_id = kwargs.pop('rbridge_id', None)
            loopback_id = kwargs.pop('loopback_id', None)
            vni_auto_data = ""
            if vni_auto:
                vni_auto_data = getattr(template, 'overlay_gateway_vni_auto').format()

            config = getattr(template, 'overlay_gateway_create').format(gw_name=gw_name,
                                                                        gw_type=gw_type,
                                                                        loopback_id=loopback_id,
                                                                        vni_auto_data=vni_auto_data)

            self._callback(config)

            if rbridge_id:
                config = getattr(template, 'overlay_gateway_attach_rb').format(
                    gw_name=gw_name, gw_type=gw_type, rbridge_id=rbridge_id)
                self._callback(config)

        if get_config:
            config = getattr(template, 'overlay_gateway_get').format()
            rest_root = self._callback(config, handler='get_config')
            util = Util(rest_root)
            gw_name = util.find(util.root, './/name')
            gw_type = util.find(util.root, './/gw-type')
            loopback_id = util.find(util.root, './/loopback-id')
            rbridge_id = util.find(util.root, './/rb-add')
            activate = True if util.findNode(util.root, './/activate') is not None else False
            vni_auto = True if util.findNode(util.root, './/auto') is not None else False

            return {"gw_name": gw_name,
                    "gw_type": gw_type,
                    'loopback_id': loopback_id,
                    'rbridge_id': rbridge_id,
                    'activate': activate,
                    'vni_auto': vni_auto,
                    }

    def evpn_instance(self, **kwargs):
        """
        >>> import pyswitch.device
        >>> conn = ('10.37.18.136', '22')
        >>> auth = ('admin', 'password')
        >>> with pyswitch.device.Device(conn=conn, auth=auth,connection_type='NETCONF') as dev:
        ...      output = dev.interface.evpn_instance(get=True,rbridge_id='2')
        ...      print output
        ...      output = dev.interface.evpn_instance(evi_name='Leaf1', duplicate_mac_timer=10,

        ...      max_count = '5',rbridge_id=2)
        ...      output = dev.interface.evpn_instance(get=True,rbridge_id=2)
        ...      print output
        """

        get_config = kwargs.pop('get', False)

        if not get_config:
            evi_name = kwargs.pop('evi_name')
            duplicate_mac_timer = kwargs.pop('duplicate_mac_timer')
            max_count = kwargs.pop('max_count')
            rbridge_id = kwargs.pop('rbridge_id')

            t = Template(getattr(template, 'evpn_instance_create'))
            config = t.render(evi_name=evi_name, duplicate_mac_timer=duplicate_mac_timer,
                              duplicate_mac_timer_max_count=max_count,
                              rbridge_id=rbridge_id)
            self._callback(config)

            t = Template(getattr(template, 'evpn_instance_router_target_auto'))
            config = t.render(evi_name=evi_name, rbridge_id=rbridge_id)
            self._callback(config)

        if get_config:
            rbridge_id = kwargs.pop('rbridge_id')
            config = getattr(template, 'evpn_instance_get').format(rbridge_id=rbridge_id)
            rest_root = self._callback(config, handler='get_config')
            util = Util(rest_root)
            evi_name = util.find(util.root, './/instance-name')
            duplicate_mac_timer = util.find(util.root, './/duplicate-mac-timer-value')
            max_count = util.find(util.root, './/max-count')

            return {"evi_name": evi_name,
                    "duplicate_mac_timer": duplicate_mac_timer,
                    'max_count': max_count
                    }

    def fetch_interfaces_config(self, **kwargs):

        input_intfs = kwargs.get('interfaces', None)
        if not input_intfs:
            return True

        intf_dict = {}
        for item in input_intfs:

            _, intf_type, port = re.split('([a-zA-Z]_?[a-zA-Z]*)',
                                          item['interface'])
            intf_type = intf_type.strip()

            if intf_type not in intf_dict:
                intf_dict[intf_type] = []

            intf_dict[intf_type].append(port.strip())

        configs = []

        for k, v in intf_dict.iteritems():

            interface_names = ''
            for port in v:
                interface_names = interface_names + "name=\'" + port + '\' or '

            if len(interface_names) > 4:
                interface_names = interface_names[0:-4]

                t = Template(template.interfaces_config_get)
                config = t.render(intf_type=k, interface_names=interface_names)
                config = ' '.join(config.split())
                configs.append(config)

        def get_dict(d, result_dict):

            for key, val in d.iteritems():
                new_key = key.split('}')[-1]

                if isinstance(val, dict):
                    result_dict[new_key] = {}
                    get_dict(val, result_dict[new_key])
                elif isinstance(val, list):
                    result_dict[new_key] = []
                    for item in val:
                        result_dict[new_key].append({})
                        get_dict(item, result_dict[new_key][-1])
                else:
                    result_dict[new_key] = val

        result = []
        for c in configs:
            try:
                rpc_response = self._callback(c, handler='get')

                rsp_elem = None
                for elem in rpc_response.iter():
                    if elem.tag.split('}')[-1] == 'interface':
                        rsp_elem = elem
                        break

                if rsp_elem:
                    pd = parker.data(rsp_elem)
                    resp = json.dumps(pd)
                    resp = json.loads(resp)
                    c_result_dict = {}
                    get_dict(resp, c_result_dict)
                    result.append(c_result_dict)
            except Exception as err:
                print err

        return result

    def single_interface_config(self, interface, parameters):

        parameters.pop('interfaces', None)

        user_data = {'ip': interface['ip'],
                     'rbridge_id': interface['rbridge_id']}

        _, intf_type, port = re.split('([a-zA-Z]_?[a-zA-Z]*)',
                                      interface['interface'])

        if intf_type.lower() not in ['loopback', 've']:
            interface['rbridge_id'] = None

        if not validate_interface(intf_type.strip(), port.strip(),
                                  interface['rbridge_id'], 'nos'):
            raise ValueError("Invalid interface: {}{} on platform type: nos. "
                             "rbridge_id MUST be passed ONLY if interface type"
                             " is loopback. Provided rbridge_id: {}"
                             .format(intf_type, port, interface['rbridge_id']))

        if intf_type != 've':
            user_data['port'] = port.strip()
            user_data['intf_type'] = intf_type.strip()
            user_data.update(parameters)

            # configure interface params
            if intf_type == 'loopback':

                if interface['ip']:
                    if interface['ip'].split('/')[-1] != '32':
                        raise ValueError("{} is invalid ip address/mask"
                                         .format(interface['ip']))

                # This is limitation with switch, hence spliting
                # loopback creation and admin state seperately.
                t = Template(template.interfaces_loopback_ip_config_set)
                config = t.render(**user_data)
                config = ' '.join(config.split())
                self._callback(config)

                t = Template(template.interfaces_loopback_noshut_config_set)
            else:

                if interface['donor']:
                    _, donor_type, donor_name = re.split('([a-zA-Z]_?[a-zA-Z]*)',
                                                         interface['donor'])
                    user_data['donor_type'] = donor_type.strip()
                    user_data['donor_name'] = donor_name.strip()

                t = Template(template.interfaces_config_set)

            config = t.render(**user_data)
            config = ' '.join(config.split())
            self._callback(config)
        return True

    def validate_ipfabric_params(self, parameters):
        mtu = parameters.get('mtu', None)
        ip_mtu = parameters.get('ip_mtu', None)
        ipv6_mtu = parameters.get('ipv6_mtu', None)
        bfd_multiplier = parameters.get('bfd_multiplier', None)
        bfd_rx = parameters.get('bfd_rx', None)
        bfd_tx = parameters.get('bfd_tx', None)

        if not mtu or int(mtu) < 1522 or int(mtu) > 9216:
            raise ValueError("Invalid mtu: {}. Valid mtu range is 1522-9216"
                             .format(mtu))

        if not ip_mtu or int(ip_mtu) < 1300 or int(ip_mtu) > 9100:
            raise ValueError("Invalid ip_mtu: {}. Valid ip_mtu range is "
                             "1300-9100".format(ip_mtu))

        if not ipv6_mtu or int(ipv6_mtu) < 1280 or int(ipv6_mtu) > 9100:
            raise ValueError("Invalid ipv6_mtu: {}. Valid ipv6_mtu range is "
                             "1280-9100".format(ipv6_mtu))

        if bfd_multiplier:
            if int(bfd_multiplier) < 3 or int(bfd_multiplier) > 50:
                raise ValueError("Invalid bfd_multiplier: {}. Valid "
                                 "bfd_multiplier range is 3-50"
                                 .format(bfd_multiplier))

        if bfd_rx:
            if int(bfd_rx) < 50 or int(bfd_rx) > 30000:
                raise ValueError("Invalid bfd_rx: {}. Valid "
                                 "bfd_rx range is 50-30000"
                                 .format(bfd_rx))

        if bfd_tx:
            if int(bfd_tx) < 50 or int(bfd_tx) > 30000:
                raise ValueError("Invalid bfd_tx: {}. Valid "
                                 "bfd_tx range is 50-30000"
                                 .format(bfd_tx))

        return True
