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


import xml.etree.ElementTree
import jinja2
import math
import pyswitch.utilities as utilities
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

        self.logger.info(config)
        callback(config)

        self.logger.info('Successfully created ACL {}'
                         .format(kwargs['acl_name']))
        return True

    def _parse_params_for_create_acl(self, **kwargs):
        # Check for supported and mandatory kwargs
        supported_params = ['address_type', 'acl_name', 'acl_type']
        mandatory_params = ['address_type', 'acl_name', 'acl_type']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

        user_data = {}
        user_data['acl_name'] = self.mac.parse_acl_name(**kwargs)
        user_data['address_type'] = self.mac.parse_address_type(**kwargs)
        user_data['acl_type'] = self.mac.parse_acl_type(**kwargs)

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
        # Check for supported and mandatory kwargs
        supported_params = ['acl_name']
        mandatory_params = ['acl_name']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

        # Parse params
        acl_name = self.mac.parse_acl_name(**kwargs)
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

        self.logger.info(config)
        callback(config)

        self.logger.info('Successfully deleted ACL {}'
                         .format(kwargs['acl_name']))
        return True

    def delete_acl_rule(self, **kwargs):
        mandatory_params = ['acl_name', 'seq_id']
        supported_params = ['acl_name', 'seq_id',
                            'count', 'log', 'dst', 'arp_guard','source',
                            'copy_sflow', 'mirror', 'action', 'delete']
        utilities._validate_parameters(mandatory_params,
                                       supported_params, kwargs)

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

        if int(seq_id) not in acl['seq_ids']:
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
            t = jinja2.Template(acl_template.acl_rule_ipv46_delete)

        config = t.render(**user_data)
        config = ' '.join(config.split())

        self.logger.info(config)

        callback(config)

        self.logger.info('Successfully deleted rule ACL {}'.format(acl_name))
        return True

    def delete_ipv4_acl_rule(self, **kwargs):
        self.delete_acl_rule(**kwargs)

    def delete_ipv6_acl_rule(self, **kwargs):
        self.delete_ipv4_acl_rule(**kwargs)

    def delete_l2_acl_rule(self, **kwargs):
        self.delete_acl_rule(**kwargs)

    def _get_seq_ids(self, acl_elem, ret):

        # xml.etree.ElementTree.dump(acl_elem)
        seq_ids = []
        for elem in acl_elem.iter():
            if 'seq-id' in elem.tag:
                seq_ids.append(int(elem.text))

        ret['seq_ids'] = seq_ids
        return True

    def _get_acl_details(self, acl_name, cmd, get_seqs=False):
        """
        Return acl-type as dict 
            {'type':'standard'/'extended;, 'protocol':'mac'/'ip'/'ipv6'}.
        """
        ret = None
        seq_element = None

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
                            self._get_seq_ids(parent, ret)

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
        else: # Generate a valid seq_id if user has not specified
            if sequences:
                last_seq_id = max(sequences)
                next_seq_id = (last_seq_id + 10) // 10 * 10

        return next_seq_id
