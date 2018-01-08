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

        self.logger.info('Creating ACL {} ({}:{})'.format(
                         kwargs['acl_name'], kwargs['address_type'],
                         kwargs['acl_type']))

        cmd = acl_template.acl_create

        t = jinja2.Template(cmd)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.debug(config)
        callback(config)

        self.logger.info('Successfully created ACL {}'
                         .format(kwargs['acl_name']))
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

        self.logger.info('Deleting ACL {}'
                         .format(user_data))

        t = jinja2.Template(acl_template.acl_delete)
        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.debug(config)
        callback(config)

        self.logger.info('Successfully deleted ACL {}'
                         .format(kwargs['acl_name']))
        return True

    def delete_acl_rule(self, **kwargs):
        # Parse params
        acl_name = self.ap.parse_acl_name(**kwargs)
        seq_id = self.ap.parse_seq_id(**kwargs)
        callback = kwargs.pop('callback', self._callback)

        acl = self._get_acl_info(acl_name, get_seqs=True)
        acl_type = acl['type']
        address_type = acl['protocol']

        self.logger.info('Successfully identified the acl_type as ({}:{})'
                         .format(address_type, acl_type))

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

        self.logger.debug(config)

        callback(config)

        self.logger.info('Successfully deleted rule ACL {}'.format(acl_name))
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

    def validate_interfaces(self, callback, user_data):

        for intf in user_data['interface_list']:
            self.logger.info('Validating interface ({}:{})'
                             .format(user_data['intf_type'], intf))
            invalid_intf = True

            user_data['intf'] = intf
            cmd = acl_template.get_interface_by_name
            t = jinja2.Template(cmd)
            config = t.render(**user_data)
            config = ' '.join(config.split())

            self.logger.debug(config)
            rpc_response = callback(config, handler='get')
            # xml.etree.ElementTree.dump(rpc_response)
            for elem in rpc_response.iter():
                if elem.text == intf:
                    invalid_intf = False
                    break
            if invalid_intf:
                raise ValueError("{} interface {} does not exist."
                                 .format(user_data['intf_type'], intf))

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

            self.logger.info("{} rules configured successfully"
                             .format(configured_count))
            self.logger.error("{} rules could not be configured"
                              .format(unconfigured_count))
            self.logger.error("rules with seq_id equal to and above {}"
                              " seq_id could not be configured"
                              .format(conflicting_seq_ids[0]))

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

            self.logger.info("{} rules configured successfully"
                             .format(configured_count))
            self.logger.error("{} rules could not be configured"
                              .format(unconfigured_count))
            self.logger.error("rules with seq_id equal to and above {} could"
                              " not be configured".format(failed_seq_id))

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

        self.logger.info('Successfully identified the acl_type as ({}:{})'
                         .format(address_type, acl_type))

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
            self.logger.debug(config)

            try:
                callback(config)
            except Exception as rpc_err:
                raise ValueError(rpc_err)

        self.logger.info('Successfully deleted rule ACL {}'.format(acl_name))
        return True
