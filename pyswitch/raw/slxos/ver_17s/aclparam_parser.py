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
    The AclParamParser class parses kwargs which are common for all the
    three ACL Types.
    Attributes:
        None
    """

    def parse_intf_type(self, **kwargs):
        """
        parse supported intf_type param
        Args:
            kwargs contains:
                intf_type(string): Allowed intf_type are,
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

        intf_type = kwargs['intf_type']
        address_type = kwargs['address_type']

        if address_type == "mac" and \
                intf_type in ['vlan', 'ethernet', 'port_channel']:
            return intf_type.replace("_", "-")

        if kwargs['intf_type'] in ['port_channel', 've', 'loopback',
                                   'ethernet', 'management', 'vlan']:
            return kwargs['intf_type'].replace("_", "-")

        raise ValueError("The \'intf_type\' value {} is invalid. "
                         "Supported - port_channel, ve, loopback, ethernet, "
                         "management and vlan"
                         .format(kwargs['intf_type']))

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

        if kwargs['acl_direction'] not in ['in', 'out']:
            raise ValueError("\'acl_direction\' can be in or out only")

        acl_direction = kwargs['acl_direction']
        intf_type = kwargs['intf_type']
        address_type = kwargs['address_type']

        if address_type == 'mac':

            if intf_type == 'port_channel':

                if acl_direction != 'in':
                    raise ValueError("direction can be \'in\' for "
                                     "port channel")

            elif intf_type == 'ethernet':
                if acl_direction != 'in':
                    raise ValueError("direction can be \'in\' for ethernet "
                                     "interface")
            elif intf_type == 'vlan':
                pass

            else:
                raise ValueError("mac access-list can not be configured on "
                                 "interface type: {}".format(intf_type))
        else:
            if 'intf_type' in kwargs and kwargs['intf_type'] == 'management' \
               and kwargs['acl_direction'] != 'in':
                raise ValueError("Management interface supports "
                                 "only \'acl_direction\': in")

        return acl_direction

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
