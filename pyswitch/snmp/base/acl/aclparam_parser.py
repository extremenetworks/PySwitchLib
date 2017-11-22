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

    def parse_seq_id(self, **parameters):
        """
        parse supported actions by MLX platform
        Args:
            parameters contains:
                seq_id (integer): Allowed seq_id is 1 to 214748364.
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'seq_id' not in parameters or not parameters['seq_id']:
            return None

        if parameters['seq_id'] > 0 and parameters['seq_id'] < 214748365:
            return str(parameters['seq_id'])

        raise ValueError("The \'seq_id\' value {} is invalid."
                         "Valid range for sequence is 1 to 214748364."
                         .format(parameters['seq_id']))

    def parse_action(self, **parameters):
        """
        parse supported actions by MLX platform
        Args:
            parameters contains:
                action (string): Allowed actions are 'permit' and 'deny'
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'action' not in parameters or not parameters['action']:
            raise ValueError("\'action\' not present in parameters arg")

        if parameters['action'] in ['permit', 'deny']:
            return parameters['action']

        raise ValueError("The \'action\' value {} is invalid. Specify "
                         "\'deny\' or \'permit\' supported "
                         "values".format(parameters['action']))
