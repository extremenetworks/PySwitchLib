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

    def parse_mirror(self, **parameters):
        """
        parse the mirror param
        Args:
            parameters contains:
                log(string): Enables the logging
                mirror(string): Enables mirror for the rule.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'mirror' not in parameters or not parameters['mirror']:
            return None

        if parameters['mirror'].lower() == 'false':
            return None

        if parameters['mirror'].lower() == 'true':

            if 'action' in parameters and parameters['action'] and \
                    parameters['action'] != 'permit':
                raise ValueError(" Mirror keyword is applicable only for ACL"
                                 " permit clauses")

            if 'log' in parameters and parameters['log'] and \
                    parameters['log'].lower() == 'true':
                raise ValueError("Error: mirror and log keywords can not be "
                                 "used together")
            return 'mirror'

        raise ValueError("Invalid \'mirror\' value: {}"
                         .format(parameters['mirror']))

    def parse_log(self, **parameters):
        """
        parse the log param
        Args:
            parameters contains:
                log(string): Enables the logging
                mirror(string): Enables mirror for the rule.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'log' not in parameters or not parameters['log']:
            return None

        if parameters['log'].lower() == 'false':
            return None

        if parameters['log'].lower() == 'true':

            if 'mirror' in parameters and parameters['mirror'] and \
                    parameters['mirror'].lower() == 'true':
                raise ValueError("Error: mirror and log keywords can not be "
                                 "used together")
            return 'log'

        raise ValueError("Invalid \'log\' value: {}"
                         .format(parameters['log']))

    def parse_acl_name(self, **parameters):
        """
        parse acl name by MLX platform
        Args:
            parameters contains:
                acl_name(string): Allowed length of string is 255
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'acl_name' not in parameters or not parameters['acl_name']:
            raise ValueError("\'acl_name\' can not be empty string")

        if len(parameters['acl_name']) > 255:
            raise ValueError("\'acl_name\' can't be more than 255 characters")

        if parameters['acl_name'].lower() in ['all', 'test']:
            raise ValueError("{} cannot be used as an ACL name".format(
                             parameters['acl_name']))

        acl_name = parameters['acl_name'].strip()

        if not acl_name[0].isalpha():
            raise ValueError("The unique name for the ACL which must "
                             "begin with a-z, A-Z. {}"
                             .format(parameters['acl_name']))

        if " " in acl_name:
            acl_name = "\"" + acl_name + "\""

        return acl_name

    def parse_copy_sflow(self, **parameters):
        """
        parse copy-sflow for MLX platform
        Args:
            parameters contains:
                copy_sflow(string): Enables copy-sflow for the rule
        Returns:
            Return parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'copy_sflow' not in parameters or not parameters['copy_sflow']:
            return None

        copy_sflow = parameters['copy_sflow'].strip().lower()

        if copy_sflow == 'true':
            return 'copy-sflow'

        if copy_sflow == 'false':
            return None

        raise ValueError("\'copy_sflow\' can be \'true\' or \'false'\ only.")

    def parse_seq_id_by_range(self, configured_seq_ids, **parameters):
        """
        parse supported actions by platform
        Args:
            parameters contains:
                seq_id (string): Allowed seq_id is 1 to 214748364.
                                 Example:- { 10 | all | 1,2,3-10,20 }
        Returns:
            Return list of parsed string on success
        Raise:
            Raise ValueError exception
        Examples:

        """
        if 'seq_id' not in parameters or not parameters['seq_id']:
            raise ValueError('seq_id is required to delete rule for {}'
                             .format(parameters['acl_name']))

        if parameters['seq_id'].lower() == 'all':
            return configured_seq_ids

        sequences = parameters['seq_id'].split(',')

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
                             .format(parameters['seq_id']))

        # if any requested seq-id doesn't exist raise exception.
        invalid_seq_ids = list(set(seq_id_list) - set(configured_seq_ids))

        if len(invalid_seq_ids) > 0:
            raise ValueError("Error: Invalid seq_ids received: {}."
                             .format(invalid_seq_ids))

        return sorted(list(set(seq_id_list)), reverse=True)
