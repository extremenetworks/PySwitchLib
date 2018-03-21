"""
Copyright 2017 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


# import xml.etree.ElementTree
import jinja2
import re
from xmljson import parker
import json
import pyswitch
from pyswitch.utilities import Util
import pyswitch.raw.slx_nos.acl.params_validator as params_validator
from pyswitch.raw.base.acl import Acl as BaseAcl
from pyswitch.raw.slx_nos.acl import acl_template
from pyswitch.raw.slx_nos.acl.aclparam_parser import AclParamParser


class SlxNosAcl(BaseAcl):
    """
    The Acl class holds all the functions assocaiated
    with the Access Control list of a SLXOS or NOS device.

    Attributes:
        None
    """
    RULE_CHUNK_SIZE = 200
    IPV6_RULE_CHUNK_SIZE = 1
    MAC_RULE_CHUNK_SIZE = 1

    def __init__(self, callback):
        """
        ACL init function.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            ACL Object

        Raises:
            ValueError
        """
        super(SlxNosAcl, self).__init__(callback)

        self._ap = AclParamParser()

    @property
    def ap(self):
        return self._ap

    def create_acl(self, **kwargs):
        """
        Create an Access Control List.
        Args:
            address_type (str): ACL address type, ip or ipv6 or mac.
            acl_type (str): ACL type, extended or standard.
            acl_name (str): Unique name for ACL.
            callback (function): A function executed upon completion
                of the method. The only parameter passed to `callback` will be
                the ``ElementTree`` `config`.
        Returns:
            True,False or None for Success, failure and no-change respectively.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.create_acl(acl_name='Acl_2',
                                             acl_type='extended',
                                             address_type='ip')
            >>>     print dev.acl.create_acl(acl_name='Acl_3',
                                             acl_type='extended',
                                             address_type='ipv6')
        """
        # Validate required and accepted parameters
        params_validator.validate_params_slx_nos_create_acl(**kwargs)

        # Parse params
        user_data = self._parse_params_for_create_acl(**kwargs)

        callback = kwargs.pop('callback', self._callback)

        cmd = acl_template.acl_create

        t = jinja2.Template(cmd)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        callback(config)
        return True

    def _parse_params_for_create_acl(self, **kwargs):
        # Check for supported and mandatory kwargs

        user_data = {}
        user_data['acl_name'] = self.ap.parse_acl_name(**kwargs)
        user_data['address_type'] = self.ap.parse_address_type(**kwargs)
        user_data['acl_type'] = self.ap.parse_acl_type(**kwargs)

        return user_data

    def delete_acl(self, **kwargs):
        """
        Delete Access Control List.
        Args:
            acl_name (str): Name of the access list.
            callback (function): A function executed upon completion
                of the method.  The only parameter passed to `callback`
                will be the ``ElementTree`` `config`.
        Returns:
            True, False or None for Success, failure and no-change respectively

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='mac')
            >>>     print dev.acl.delete_acl(acl_name='Acl_2')
            >>>     print dev.acl.delete_acl(acl_name='Acl_1')
        """
        # Validate required and accepted parameters
        params_validator.validate_params_slx_nos_delete_acl(**kwargs)

        # Parse params
        acl_name = self.ap.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)
        acl = self._get_acl_info(acl_name)

        user_data = {'acl_name': acl_name,
                     'address_type': acl['protocol'],
                     'acl_type': acl['type']}

        t = jinja2.Template(acl_template.acl_delete)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        callback(config)
        return True

    def delete_acl_rule(self, **kwargs):
        # Parse params
        acl_name = self.ap.parse_acl_name(**kwargs)
        seq_id = self.ap.parse_seq_id(**kwargs)
        callback = kwargs.pop('callback', self._callback)

        acl = self._get_acl_info(acl_name, get_seqs=True)
        acl_type = acl['type']
        address_type = acl['protocol']

        # Validate seq_id if user has specified
        if not seq_id:
            raise ValueError('seq_id is required to delete rule for {}'
                             .format(acl_name))

        sequences = acl['seq_ids']
        if not sequences or int(seq_id) not in list(sequences):
            raise ValueError("seq_id {} does not exists."
                             .format(seq_id))

        user_data = {}
        user_data['acl_type'] = acl_type
        user_data['address_type'] = address_type
        user_data['seq_id'] = seq_id
        user_data['acl_name'] = acl_name

        if address_type == 'mac':
            t = jinja2.Template(acl_template.acl_rule_mac_delete)
        else:
            t = jinja2.Template(acl_template.acl_rule_ipx_delete)

        config = t.render(**user_data)
        config = ' '.join(config.split())

        callback(config)
        return True

    def delete_ipv4_acl_rule(self, **kwargs):
        # Validate required and accepted parameters
        params_validator.validate_params_slx_nos_delete_acl_rule(**kwargs)

        self.delete_acl_rule(**kwargs)

    def delete_ipv6_acl_rule(self, **kwargs):
        # Validate required and accepted parameters
        params_validator.validate_params_slx_nos_delete_acl_rule(**kwargs)

        self.delete_acl_rule(**kwargs)

    def delete_l2_acl_rule(self, **kwargs):
        # Validate required and accepted parameters
        params_validator. \
            validate_params_nos_delete_add_or_remove_l2_acl_rule(**kwargs)

        self.delete_acl_rule(**kwargs)

    def _get_seq_ids(self, acl_elem, ret):

        # xml.etree.ElementTree.dump(acl_elem)
        seq_ids = []
        for elem in acl_elem.iter():
            if 'seq-id' in elem.tag:
                seq_ids.append(int(elem.text))

        return seq_ids

    def _get_acl_details(self, acl_name, cmd, get_seqs=False):
        """
        Return acl-type as dict
            {'type':'standard'/'extended;, 'protocol':'mac'/'ip'/'ipv6'}.
        """
        ret = None

        for address_type in ['mac', 'ip', 'ipv6']:
            for acl_type in ['standard', 'extended']:

                t = jinja2.Template(cmd)
                config = t.render(acl_type=acl_type,
                                  address_type=address_type,
                                  acl_name=acl_name)
                config = ' '.join(config.split())

                rpc_response = self._callback(config, handler='get')
                # xml.etree.ElementTree.dump(rpc_response)

                parent = None
                for elem in rpc_response.iter():

                    if elem.text == acl_name:
                        ret = {'type': acl_type,
                               'protocol': address_type,
                               'seq_ids': None}
                        if get_seqs:
                            ret['seq_ids'] = self._get_seq_ids(parent, ret)

                        return ret
                    parent = elem

        return ret

    def _get_acl_info(self, acl_name, get_seqs=False):

        cmd = acl_template.acl_get_config
        ret = self._get_acl_details(acl_name, cmd, get_seqs)
        if ret:
            return ret

        # Check for acl name with no rules created
        cmd = acl_template.acl_get_config_name
        ret = self._get_acl_details(acl_name, cmd, get_seqs)
        if ret:
            return ret

        raise ValueError('Failed to identify acl_type. '
                         'Check if the ACL {} exists'.format(acl_name))

    def _get_acl_info_rest(self, rest_device, acl_name, get_seqs=False):
        """
        Return acl-type as dict
            {'type':'standard'/'extended;, 'protocol':'mac'/'ip'/'ipv6'}.
        """
        ret = None
        seq_ids = []

        config = ''
        for address_type in ['mac', 'ip', 'ipv6']:
            for acl_type in ['standard', 'extended']:

                method = address_type + '_access_list_' + acl_type
                config = (method + '_get', {})
                output = rest_device._callback(config, handler='get_config')
                util = Util(output.data)
                for rcvd_name in util.root.findall(".//name"):
                    if rcvd_name.text == acl_name:
                        ret = {'type': acl_type, 'protocol': address_type,
                               'seq_ids': None}

                        if get_seqs:
                            config = (method + '_seq_get',
                                      {acl_type: acl_name})
                            output = rest_device. \
                                _callback(config, handler='get_config')
                            util = Util(output.data)
                            for rcvd_seqs in util.root.findall(".//seq-id"):
                                seq_ids.append(int(rcvd_seqs.text))
                            ret['seq_ids'] = seq_ids
                        return ret

        raise ValueError('Failed to identify acl_type. '
                         'Check if the ACL {} exists'.format(acl_name))

    def _get_next_seq_id(self, sequences, user_seq_id):

        next_seq_id = 10

        # Validate seq_id if user has specified
        if user_seq_id:
            if int(user_seq_id) in sequences:
                raise ValueError("Access-list entry with sequence number {} "
                                 "already exists.".format(user_seq_id))
            next_seq_id = user_seq_id
        else:  # Generate a valid seq_id if user has not specified
            if sequences:
                last_seq_id = max(sequences)
                next_seq_id = (last_seq_id + 10) // 10 * 10

        return next_seq_id

    def set_seq_id_for_bulk_rules(self, existing_seq_ids, acl_rules):

        user_seq_ids = [rule['seq_id'] for rule in acl_rules
                        if 'seq_id' in rule and rule['seq_id']]

        # There are configured rules and user has requested rules with seq_ids
        if existing_seq_ids and user_seq_ids:

            # Validate if user has provided all or none seq_id
            if len(user_seq_ids) != len(acl_rules):
                raise ValueError("User should provide seq_id for all or none "
                                 "of the rules")

            # Validate if user provided ids are not overlapping
            overlapping_ids = set(user_seq_ids).intersection(existing_seq_ids)
            if overlapping_ids:
                    raise ValueError("These sequence ids are already "
                                     "configured: {}".format(overlapping_ids))

            acl_rules = sorted(acl_rules, key=lambda k: k['seq_id'])

        elif user_seq_ids:
            # Validate if user has provided all or none seq_id
            if len(user_seq_ids) != len(acl_rules):
                raise ValueError("User should provide seq_id for all or none "
                                 "of the rules")

            acl_rules = sorted(acl_rules, key=lambda k: k['seq_id'])

        elif existing_seq_ids:
            next_seq_id = (max(existing_seq_ids) + 10) // 10 * 10

            # Assign seq_id to all the rules.
            for rule in acl_rules:
                rule['seq_id'] = next_seq_id
                next_seq_id = next_seq_id + 10
        else:
            next_seq_id = 10

            # Assign seq_id to all the rules.
            for rule in acl_rules:
                rule['seq_id'] = next_seq_id
                next_seq_id = next_seq_id + 10

        return True

    def process_bulk_rpc_error_msg(self, rpc_err, acl_rules):
        rpc_err = str(rpc_err)
        if "Error: Access-list entry already exists" in rpc_err:
            re_cmp = re.compile(r'\d+')
            conflicting_seq_ids = re_cmp.findall(rpc_err)

            configured = []
            configured_count = 0
            unconfigured = []
            unconfigured_count = 0

            for rule in acl_rules:
                if rule['seq_id'] < int(conflicting_seq_ids[0]):
                    configured.append(rule)
                    configured_count = configured_count + 1
                else:
                    unconfigured.append(rule)
                    unconfigured_count = unconfigured_count + 1

        raise ValueError(rpc_err)

    def process_response_ipv6_rule_bulk_req(self, rpc_err, acl_rules,
                                            failed_seq_id):
        rpc_err = str(rpc_err)
        if "Error: Access-list entry already exists" in rpc_err:

            configured_count = 0
            unconfigured_count = 0

            for rule in acl_rules:
                if rule['seq_id'] < int(failed_seq_id):
                    configured_count = configured_count + 1
                else:
                    unconfigured_count = unconfigured_count + 1
        raise ValueError(rpc_err)

    def delete_ipv4_acl_rule_bulk(self, **kwargs):
        """
        Delete ACL rules from IPv4 ACL.
        Args:
            acl_name (str): Name of the access list.
            seq_ids(string): Range of ACL sequence rules.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='ip')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1',
                        acl_rules = [{"seq_id": 10, "action": "permit",
                                      "source": "host 192.168.0.3")
        """
        # Validate required and accepted parameters
        params_validator.validate_params_slx_nos_delete_acl_rule(**kwargs)

        # Parse params
        acl_name = self.ap.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)

        acl = self._get_acl_info(acl_name, get_seqs=True)
        acl_type = acl['type']
        address_type = acl['protocol']

        if address_type != 'ip':
            raise ValueError("IPv4 Rule can not be added to non-ip ACL."
                             "ACL {} is of type {}"
                             .format(acl_name, address_type))

        seq_range = self.ap.parse_seq_id_by_range(acl['seq_ids'], **kwargs)
        user_data_list = [{'seq_id': seq_id} for seq_id in seq_range]

        # send the rules in a chunk of Acl.RULE_CHUNK_SIZE
        chunks = [user_data_list[i:i + SlxNosAcl.RULE_CHUNK_SIZE]
                  for i in
                  xrange(0, len(user_data_list), SlxNosAcl.RULE_CHUNK_SIZE)]

        for chunk in chunks:
            t = jinja2.Template(acl_template.acl_rule_ipx_delete_bulk)
            config = t.render(address_type=address_type,
                              acl_type=acl_type,
                              acl_name=acl_name,
                              user_data_list=chunk)
            config = ' '.join(config.split())

            try:
                callback(config)
            except Exception as rpc_err:
                raise ValueError(rpc_err)

        return True

    def delete_ipv6_acl_rule_bulk(self, **kwargs):
        """
        Delete ACL rules from IPv6 ACL.
        Args:
            acl_name (str): Name of the access list.
            seq_ids(string): Range of ACL sequence rules.
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='ip')
            >>>     print dev.acl.add_ip_acl_rule(acl_name='Acl_1',
                        acl_rules = [{"seq_id": 10, "action": "permit",
                                      "source": "host 192.168.0.3")
        """
        # Validate required and accepted parameters
        params_validator.validate_params_slx_nos_delete_acl_rule(**kwargs)

        # Parse params
        acl_name = self.ap.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)

        acl = self._get_acl_info(acl_name, get_seqs=True)
        acl_type = acl['type']
        address_type = acl['protocol']
        seq_range = self.ap.parse_seq_id_by_range(acl['seq_ids'], **kwargs)
        user_data_list = [{'seq_id': seq_id} for seq_id in seq_range]

        # send the rules in a chunk of Acl.IPV6_RULE_CHUNK_SIZE
        chunks = [user_data_list[i:i + SlxNosAcl.IPV6_RULE_CHUNK_SIZE]
                  for i in xrange(0, len(user_data_list),
                                  SlxNosAcl.IPV6_RULE_CHUNK_SIZE)]

        for chunk in chunks:
            t = jinja2.Template(acl_template.acl_rule_ipx_delete_bulk)
            config = t.render(address_type=address_type,
                              acl_type=acl_type,
                              acl_name=acl_name,
                              user_data_list=chunk)
            config = ' '.join(config.split())

            try:
                callback(config)
            except Exception as rpc_err:
                raise ValueError(rpc_err)
        return True

    def delete_l2_acl_rule_bulk(self, **kwargs):
        """
        Delete ACL rules from MAC ACL.
        Args:
            acl_name (str): Name of the access list.
            seq_id(string): Range of ACL sequences seq_id="10,30-40"
        Returns:
            True, False or None for Success, failure and no-change respectively
            for each seq_ids.

        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.create_acl(acl_name='Acl_1',
                                             acl_type='standard',
                                             address_type='ip')
            >>>     print dev.acl.delete_l2_acl_rule_bulk(acl_name='Acl_1',
                                                          seq_id="10,30-40")
        """
        # Validate required and accepted parameters
        params_validator. \
            validate_params_nos_delete_add_or_remove_l2_acl_rule(**kwargs)

        # Parse params
        acl_name = self.ap.parse_acl_name(**kwargs)
        callback = kwargs.pop('callback', self._callback)

        acl = self._get_acl_info(acl_name, get_seqs=True)
        acl_type = acl['type']
        address_type = acl['protocol']
        seq_range = self.ap.parse_seq_id_by_range(acl['seq_ids'], **kwargs)
        user_data_list = [{'seq_id': seq_id} for seq_id in seq_range]

        # send the rules in a chunk of Acl.MAC_RULE_CHUNK_SIZE
        chunks = [user_data_list[i:i + SlxNosAcl.MAC_RULE_CHUNK_SIZE]
                  for i in xrange(0, len(user_data_list),
                                  SlxNosAcl.MAC_RULE_CHUNK_SIZE)]

        for chunk in chunks:
            t = jinja2.Template(acl_template.acl_rule_mac_delete_bulk)
            config = t.render(address_type=address_type,
                              acl_type=acl_type,
                              acl_name=acl_name,
                              user_data_list=chunk)
            config = ' '.join(config.split())

            try:
                callback(config)
            except Exception as rpc_err:
                raise ValueError(rpc_err)
        return True

    def _get_acl_rules(self, rest_device, address_type, acl_type,
                       acl_name, sequences):
        """
        Return list of rules configured for acl_name
        """
        rules_list = []
        method = address_type + '_access_list_' + acl_type + '_seq_get'
        config = (method, {acl_type: acl_name, 'resource_depth': 2})
        output = rest_device._callback(config, handler='get_config')
        util = Util(output.data)

        for rcvd_seq in util.root.findall(".//seq"):
            if rcvd_seq is not None:
                seq_id = int(rcvd_seq.find('seq-id').text)
                if seq_id in sequences:
                    sequences.remove(seq_id)
                    pd = parker.data(rcvd_seq)
                    rules_list.append(pd)

        return rules_list

    def get_acl_rules(self, **kwargs):
        """
        Returns the number of congiured rules
        Args:
            acl_name (str): Name of the access list.
        Returns:
            Number of rules configured,
        Examples:
            >>> from pyswitch.device import Device
            >>> with Device(conn=conn, auth=auth,
                            connection_type='NETCONF') as dev:
            >>>     print dev.acl.get_acl_rules(acl_name='Acl_1',
                                                seq_id='all')
        """

        # Validate required and accepted parameters
        params_validator.validate_params_get_acl_rules(**kwargs)

        # Parse params
        acl_name = self.ap.parse_acl_name(**kwargs)

        if 'device' not in kwargs or not kwargs['device']:
            raise ValueError('Need device object to proceed')

        netc_device = kwargs['device'].device_type
        with pyswitch.device.Device(conn=netc_device._conn,
                                    auth=netc_device._auth,
                                    connection_type='REST') as rest_device:

            acl = self._get_acl_info_rest(rest_device.device_type,
                                          acl_name, get_seqs=True)
            acl_type = acl['type']
            address_type = acl['protocol']
            seq_range = self.ap.parse_seq_id_by_range(acl['seq_ids'], **kwargs)

            rules_list = self._get_acl_rules(rest_device.device_type,
                                             address_type, acl_type, acl_name,
                                             seq_range)
            resp_body = json.dumps(rules_list)
            return resp_body
