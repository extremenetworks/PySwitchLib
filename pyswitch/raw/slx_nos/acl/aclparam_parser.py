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

import pyswitch.utilities as utilities


class AclParamParser(object):
    """
    The AclParamParser class parses kwargs which are common for all the
    three ACL Types.
    Attributes:
        None
    """

    def parse_address_type(self, **kwargs):
        """
        parse supported address type by platform
        Args:
            kwargs contains:
                address_type(string): Allowed address_type are ip, ipv6, mac
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """

        if 'address_type' not in kwargs or not kwargs['address_type']:
            raise ValueError("\'address_type\' not present in kwargs")

        if kwargs['address_type'] in ['mac', 'ip', 'ipv6']:
            return kwargs['address_type']

        raise ValueError("The \'address_type\' value {} is invalid. Specify "
                         "\'mac\' or \'ip\' or \'ipv6\' supported values"
                         .format(kwargs['address_type']))

    def parse_acl_type(self, **kwargs):
        """
        parse supported acl type by platform
        Args:
            kwargs contains:
                acl_type(string): Allowed acl_type are standard or extended
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """

        if 'acl_type' not in kwargs or not kwargs['acl_type']:
            raise ValueError("\'acl_type\' not present in kwargs")

        if kwargs['acl_type'] in ['standard', 'extended']:
            return kwargs['acl_type']

        raise ValueError("The \'acl_type\' value {} is invalid. Specify "
                         "\'standard\' or \'extended\' supported values"
                         .format(kwargs['acl_type']))

    def parse_seq_id(self, **kwargs):
        """
        parse supported actions by platform
        Args:
            kwargs contains:
                seq_id (integer): Allowed seq_id is 1 to 214748364.
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'seq_id' not in kwargs or not kwargs['seq_id']:
            return None

        if kwargs['seq_id'] >= 0 and kwargs['seq_id'] <= 4294967290:
            return str(kwargs['seq_id'])

        raise ValueError("The \'seq_id\' value {} is invalid."
                         "Valid range for sequence is 0 to 4294967290."
                         .format(kwargs['seq_id']))

    def parse_action(self, **kwargs):
        """
        parse supported actions by platform
        Args:
            kwargs contains:
                action (string): Allowed actions are 'permit' and 'deny'
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """

        if 'action' not in kwargs or not kwargs['action']:
            raise ValueError("\'action\' not present in kwargs arg")

        if kwargs['action'] in ['permit', 'deny', 'hard-drop']:
            return kwargs['action']

        raise ValueError("The \'action\' value {} is invalid. Specify "
                         "\'deny\' or \'permit\' or \'hard-drop\' supported "
                         "values".format(kwargs['action']))

    def parse_count(self, **kwargs):
        """
        parse the count param
        Args:
            kwargs contains:
                count (string): Enables the packet count
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'count' not in kwargs or not kwargs['count']:
            return None

        if kwargs['count'] == 'True':
            return True

        return None

    def parse_acl_name(self, **kwargs):
        """
        parse acl name by platform
        Args:
            kwargs contains:
                acl_name(string): Allowed length of string is 63
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'acl_name' not in kwargs or not kwargs['acl_name']:
            raise ValueError("\'acl_name\' can not be empty string")

        if len(kwargs['acl_name']) > 63:
            raise ValueError("\'acl_name\' can't be more than 63 characters")

        if kwargs['acl_name'].lower() in ['all', 'test']:
            raise ValueError("{} cannot be used as an ACL name".format(
                             kwargs['acl_name']))

        return kwargs['acl_name']

    def parse_boolean_params(self, user_data, bool_params, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                urg(string): Enables urg for the rule
                ack(string): Enables ack for the rule
                push(string): Enables push for the rule
                fin(string): Enables fin for the rule
                rst(string): Enables rst for the rule
                sync(string): Enables sync for the rule
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        for key in bool_params:
            if key in kwargs and kwargs[key]:
                val = kwargs[key]
                val = ' '.join(val.split())
                if val.lower() == 'true':
                    user_data[key] = True
                else:
                    user_data[key] = None
            else:
                user_data[key] = None

        return True

    def parse_mirror(self, **kwargs):
        """
        parse the protocol type param.
        Args:
            kwargs contains:
                mirror(string): Enables mirror for the rule
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'mirror' not in kwargs or not kwargs['mirror']:
            return None

        if 'acl_type' not in kwargs or not kwargs['acl_type']:
            raise ValueError("\'acl_type\' not defined. mirror is supported"
                             "only for extended acl_type")

        if kwargs['acl_type'] != 'extended':
            raise ValueError("\'acl_type\' not defined. mirror is supported"
                             "only for extended acl_type")

        val = ' '.join(kwargs['mirror'].split())

        if val.lower() == 'true':
            return True

        return None

    def parse_drop_precedence_force(self, **kwargs):
        """
        parse the drop_precedence_force mapping param.
        Args:
            kwargs contains:
                drop_precedence_force(string):
                    drop_precedence_force value of the packet
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence_force' not in kwargs or \
                not kwargs['drop_precedence_force']:
            return None

        drop_precedence_force = kwargs['drop_precedence_force']
        drop_precedence_force = ' '.join(drop_precedence_force.split())

        if 'action' not in kwargs or not kwargs['action']:
            raise ValueError("\'action\' not present in kwargs arg")

        if kwargs['action'] != 'permit':
            raise ValueError("\'drop_precedence_force\' is configurable"
                             " only for action = permit")

        if drop_precedence_force.isdigit():
            if int(drop_precedence_force) >= 0 and \
                    int(drop_precedence_force) <= 2:
                return str(drop_precedence_force)

        raise ValueError("drop-precedence-force value should be 0 - 2")

    def parse_rbridge_id(self, **kwargs):
        """
        parse supported rbridge_id param
        Args:
            kwargs contains:
                rbridge_id(string): Allowed rbridge_id is 1 to 239
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        if 'rbridge_id' not in kwargs or not kwargs['rbridge_id']:
            return None

        if int(kwargs['rbridge_id']) >= 1 and int(kwargs['rbridge_id']) <= 239:
            return kwargs['rbridge_id']

        raise ValueError("The \'rbridge_id\' value {} is invalid. "
                         "Valid range for rbridge_id is 1 to 239."
                         .format(kwargs['rbridge_id']))

    def parse_intf_type(self, **kwargs):
        """
        parse supported intf_type param
        Args:
            kwargs contains:
                intf_type(string): Allowed intf_type are,
                          - gigabitethernet
                          - tengigabitethernet
                          - fortygigabitethernet
                          - hundredgigabitethernet
                          - port_channel
                          - ve
                          - loopback
                          - ethernet
                          - management
                          - vlan
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        if 'intf_type' not in kwargs or not kwargs['intf_type']:
            raise ValueError("\'intf_type\' not present in kwargs")

        if kwargs['intf_type'] not in ['ve', 'loopback']:
            if 'rbridge_id' in kwargs and kwargs['rbridge_id']:
                raise ValueError("\'rbridge_id\' not supported for intf_type: "
                                 "{}".format(kwargs['intf_type']))

        if kwargs['intf_type'] in ['gigabitethernet', 'tengigabitethernet',
                                   'fortygigabitethernet',
                                   'hundredgigabitethernet', 'port_channel',
                                   've', 'loopback', 'ethernet',
                                   'management', 'vlan']:
            return kwargs['intf_type'].replace("_", "-")

        raise ValueError("The \'intf_type\' value {} is invalid. "
                         "Supported - gigabitethernet, tengigabitethernet, "
                         "fortygigabitethernet, hundredgigabitethernet, ve, "
                         "port_channel, loopback, ethernet, management, vlan"
                         .format(kwargs['intf_type']))

    def parse_intf_names(self, **kwargs):
        """
        parse supported intf_name param
        Args:
            kwargs contains:
                intf_name(array): Array of interface names
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'intf_name' not in kwargs or not kwargs['intf_name']:
            raise ValueError("\'intf_name\' not present in kwargs")

        if 'intf_type' not in kwargs or not kwargs['intf_type']:
            raise ValueError("\'intf_type\' not present in kwargs")

        for intf in kwargs['intf_name']:
            if not utilities.valid_interface(kwargs['intf_type'], str(intf)):
                raise ValueError("Invalid \'intf_name\' {}".format(intf))

        return kwargs['intf_name']

    def parse_acl_direction(self, **kwargs):
        """
        parse supported acl_direction param
        Args:
                acl_direction(string): Allowed acl_direction are in or out
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """

        if 'acl_direction' not in kwargs or not kwargs['acl_direction']:
            raise ValueError("\'acl_direction\' not present in kwargs")

        if 'intf_type' in kwargs and kwargs['intf_type'] == 'management' \
           and kwargs['acl_direction'] != 'in':
            raise ValueError("Management interface supports only "
                             "\'acl_direction\': in")

        if kwargs['acl_direction'] in ['in', 'out']:
            return kwargs['acl_direction']

        raise ValueError("The \'acl_direction\' value {} is invalid. Specify "
                         "\'in\' or \'out\' supported values"
                         .format(kwargs['acl_direction']))

    def parse_traffic_type(self, **kwargs):
        """
        parse supported traffic_type param
        Args:
            kwargs contains:
                traffic_type(string): Allowed traffic_type are switched/routed
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """

        if 'traffic_type' not in kwargs or not kwargs['traffic_type']:
            return None

        if 'intf_type' in kwargs and kwargs['intf_type'] == 'management':
            raise ValueError("\'traffic_type\' not supported with {} interface"
                             .format(kwargs['intf_type']))

        if kwargs['traffic_type'] in ['switched', 'routed']:
            return kwargs['traffic_type']

        raise ValueError("The \'traffic_type\' value {} is invalid. Specify "
                         "\'switched\' or \'routed\' supported values"
                         .format(kwargs['traffic_type']))

    def parse_slx_traffic_type(self, **kwargs):
        """
        parse supported traffic_type param
        Args:
            kwargs contains:
                traffic_type(string): Allowed traffic_type are switched/routed
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """

        if 'traffic_type' not in kwargs or not kwargs['traffic_type']:
            return None

        if 'intf_type' in kwargs and kwargs['intf_type'] == 'management':
            raise ValueError("\'traffic_type\' not supported with {} interface"
                             .format(kwargs['intf_type']))

        if 'intf_type' in kwargs and kwargs['intf_type'] == 've':
            raise ValueError("\'traffic_type\' not supported with {} interface"
                             .format(kwargs['intf_type']))

        if kwargs['traffic_type'] in ['switched', 'routed']:
            return kwargs['traffic_type']

        raise ValueError("The \'traffic_type\' value {} is invalid. Specify "
                         "\'switched\' or \'routed\' supported values"
                         .format(kwargs['traffic_type']))

    def parse_seq_id_by_range(self, configured_seq_ids, **kwargs):
        """
        parse supported actions by platform
        Args:
            kwargs contains:
                seq_id (string): Allowed seq_id is 1 to 214748364.
                                 Example:- { 10 | all | 1,2,3-10,20 }
        Returns:
            Return list of parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'seq_id' not in kwargs or not kwargs['seq_id']:
            raise ValueError('seq_id is required to delete rule for {}'
                             .format(kwargs['acl_name']))

        if kwargs['seq_id'].lower() == 'all':
            return configured_seq_ids

        sequences = kwargs['seq_id'].split(',')

        invalid_input = False
        seq_id_list = []

        for x in sequences:
            if x.isdigit():
                seq_id_list.append(int(x))

            elif x[-1] == '-':
                if x[:-1].isdigit():
                    start_val = int(x[:-1])
                    # Assuming netconf response will is sorted
                    end_val = configured_seq_ids[-1]

                    for val in range(start_val, end_val + 1):
                        if val in configured_seq_ids:
                            seq_id_list.append(int(val))
                else:
                    invalid_input = True
                    break

            elif '-' in x:
                ranged_values = x.split('-')

                if len(ranged_values) == 2:
                    if ranged_values[0].isdigit() and \
                            ranged_values[1].isdigit():
                        start_val = int(ranged_values[0])
                        end_val = int(ranged_values[1])

                        if start_val > end_val:
                            start_val, end_val = end_val, start_val

                        for val in range(start_val, end_val + 1):
                            if val in configured_seq_ids:
                                seq_id_list.append(int(val))
                    else:
                        invalid_input = True
                        break
                else:
                    invalid_input = True
                    break
            else:
                invalid_input = True
                break

        if invalid_input:
            raise ValueError("Invalid seq_id received: {} Supported"
                             " format is {{ 10 | all | 1,2,3-10,20 }}"
                             .format(kwargs['seq_id']))

        # if any requested seq-id doesn't exist raise exception.
        invalid_seq_ids = list(set(seq_id_list) - set(configured_seq_ids))

        if len(invalid_seq_ids) > 0:
            raise ValueError("Error: Invalid seq_ids received: {}."
                             .format(invalid_seq_ids))

        return sorted(list(set(seq_id_list)), reverse=True)
