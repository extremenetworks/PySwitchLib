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


class AclParamParser(object):
    """
    The AclParamParser class parses parameters which are common for all the
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
        if 'seq_id' not in kwargs or not kwargs ['seq_id']:
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

    def parse_drop_precedence_force(self, **parameters):
        """
        parse the drop_precedence_force mapping param.
        Args:
            parameters contains:
                drop_precedence_force(string):
                    drop_precedence_force value of the packet
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'drop_precedence_force' not in parameters or \
                not parameters['drop_precedence_force']:
            return None

        drop_precedence_force = parameters['drop_precedence_force']
        drop_precedence_force = ' '.join(drop_precedence_force.split())

        if drop_precedence_force.isdigit():
            if int(drop_precedence_force) >= 0 and \
                    int(drop_precedence_force) <= 3:
                return 'drop-precedence-force ' + drop_precedence_force

        raise ValueError("drop-precedence-force value should be 0 - 3")

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
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """

        if 'intf_type' not in kwargs or not kwargs['intf_type']:
            raise ValueError("\'intf_type\' not present in kwargs")

        if kwargs['intf_type'] in ['gigabitethernet', 'tengigabitethernet',
                                   'fortygigabitethernet', 'hundredgigabitethernet',
                                   'port_channel', 've', 'loopback', 'ethernet']:
            return kwargs['intf_type'].replace("_", "-")

        raise ValueError("The \'intf_type\' value {} is invalid. "
                         "Supported values are gigabitethernet, tengigabitethernet, "
                         "fortygigabitethernet, hundredgigabitethernet, "
                         "port_channel, ve, loopback and ethernet"
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
                traffic_type(string): Allowed traffic_type are switched or routed
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """

        if 'traffic_type' not in kwargs or not kwargs['traffic_type']:
            return None

        if kwargs['traffic_type'] in ['switched', 'routed']:
            return kwargs['traffic_type']

        raise ValueError("The \'traffic_type\' value {} is invalid. Specify "
                         "\'switched\' or \'routed\' supported values"
                         .format(kwargs['traffic_type']))

