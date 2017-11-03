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


class IpAcl(object):
    """
    The IpAcl class holds all the functions assocaiated with
    IP Access Control list.
    Attributes:
        None
    """

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
        if 'action' not in parameters:
            raise ValueError("\'action\' not present in parameters arg")

        action = parameters['action']

        if parameters['action'] in ['permit', 'deny']:
            return parameters['action']

        raise ValueError("The \'action\' value {} is invalid. Specify "
                         "\'deny\' or \'permit\' supported "
                         "values".format(action))

    def parse_source(self, **parameters):
        """
        parse the source param.
        Args:
            parameters contains:
                source (string): Source filter, can be 'any' or
                    the MAC/Mask in HHHH.HHHH.HHHH/mask or
                    the host Mask in HHHH.HHHH.HHHH or
                    host <name | ip >
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'source' not in parameters:
            raise ValueError("\'source\' is parameters arg")

        src = parameters['source']
        src = ' '.join(src.split()).split()

        if src[0] == "any":
            return "any"
        elif src[0] == "host":
            return "host " + src[1]
        elif '/' in src[0]:
            return src[0]
        elif len(src) == 2:
            return src[0] + ' ' + src[1]

        raise ValueError("Invalid source {}. Supported format is "
                         "source can be 'any' or the MAC/Mask in "
                         "HHHH.HHHH.HHHH/mask or the host Mask in "
                         "HHHH.HHHH.HHHH.HHHH or host <name | ip >"
                         .format(src))

    def parse_vlan(self, **parameters):
        """
        parse the vlan param
        Args:
            parameters contains:
                vlan_id(integer): 1-4096
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'vlan_id' not in parameters:
            return None

        vlan = parameters['vlan_id']

        if not vlan:
            return None

        if vlan > 0 and vlan < 4096:
            return str(vlan)

        raise ValueError("The \'vlan\' value {} is invalid."
                         " Specify \'1-4095\' supported values")

    def parse_log(self, **parameters):
        """
        parse the log param
        Args:
            parameters contains:
                log(string): Enables the logging
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'log' in parameters:
            if parameters['log'] == 'True':
                return 'log'

        return None

    def parse_protocol(self, **parameters):
        """
        parse the protocol param
        Args:
            parameters contains:
                protocol_type: (string) Type of IP packets to be filtered
                    based on protocol. Valid values are <0-255> or
                    key words tcp, udp, icmp or ip
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'protocol_type' not in parameters:
            return None

        protocol_type = parameters['protocol_type']

        if not protocol_type:
            return None

        if protocol_type.isdigit():
            if int(protocol_type) < 0 or int(protocol_type) > 255:
                raise ValueError("The \'protocol\' value {} is invalid."
                                 " Specify \'0-255\' supported values"
                                 .format(protocol_type))

        return str(protocol_type)

    def parse_destination(self, **parameters):
        """
        parse the destination param.
        Args:
            parameters contains:
                destination (string): destination filter, can be 'any' or
                    the MAC/Mask in HHHH.HHHH.HHHH/mask or
                    the host Mask in HHHH.HHHH.HHHH or
                    host <name | ip >
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'destination' not in parameters:
            raise ValueError("\'destination\' is mandatory parameters arg")

        dst = parameters['destination']

        if not dst:
            raise ValueError("\'destination\' is mandatory parameters arg")

        dst = ' '.join(dst.split()).split()

        if dst[0] == "any":
            return "any"
        elif dst[0] == "host":
            return "host " + dst[1]
        elif '/' in dst[0]:
            return dst[0]

        raise ValueError("Invalid destination {}. Supported format is "
                         "destination can be 'any' or the MAC/Mask in "
                         "HHHH.HHHH.HHHH/mask or the host Mask in "
                         .format(dst))

    def parse_dscp_mapping(self, **parameters):
        """
        parse the dscp mapping param.
        Args:
            parameters contains:
                dscp: (string) Matches the specified value against the DSCP
                    value of the packet to filter.
                     Allowed values are 0 through 63.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'dscp' not in parameters:
            return None

        dscp_mapping = parameters['dscp']
        dscp_mapping = ' '.join(dscp_mapping.split())

        if dscp_mapping.isdigit():
            if int(dscp_mapping) >= 0 and int(dscp_mapping) <= 63:
                return 'dscp-mapping ' + dscp_mapping

        raise ValueError("Invalid dscp_mapping {}. Supported range is "
                         "<0-63>".format(dscp_mapping))

    def parse_dscp_marking(self, **parameters):
        """
        parse the dscp mapping param.
        Args:
            parameters contains:
                dscp: (string) Matches the specified value against the DSCP
                    value of the packet to filter.
                     Allowed values are 0 through 63.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'dscp_marking' not in parameters:
            return None

        dscp_marking = parameters['dscp_marking']
        dscp_marking = ' '.join(dscp_marking.split())

        if dscp_marking.isdigit():
            if int(dscp_marking) >= 0 and int(dscp_marking) <= 63:
                return 'dscp-marking ' + dscp_marking

        raise ValueError("Invalid dscp_marking {}. Supported range is "
                         "<0-63>".format(dscp_marking))

    def parse_fragment(self, **parameters):
        """
        parse the dscp mapping param.
        Args:
            parameters contains:
                dscp: (string) Matches the specified value against the DSCP
                    value of the packet to filter.
                     Allowed values are 0 through 63.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'fragment' not in parameters:
            return None

        fragment = parameters['fragment']
        if not fragment:
            return None
        fragment = ' '.join(fragment.split())

        if fragment in ['fragment', 'non-fragment']:
            return fragment

        raise ValueError("Invalid fragment {}. Supported values are "
                         "fragment or non-fragment".format(fragment))

    def parse_precedence(self, **parameters):
        """
        parse the precedence mapping param.
        Args:
            parameters contains:
                precedence:
                  type: string
                  description: Match packets with given precedence value.
                      Allowed value { <0 to 7> | critical | flash |
                      flash-override | immediate | internet | network |
                      priority | routine  }
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'precedence' not in parameters:
            return None

        precedence = parameters['precedence']
        if not precedence:
            return None
        precedence = ' '.join(precedence.split())

        if precedence.isdigit():
            if int(precedence) >= 0 and int(precedence) <= 7:
                return 'precedence ' + precedence
        if precedence in ['critical' 'flash', 'flash-override',
                          'immediate', 'internet', 'network',
                          'priority', 'routine']:
                return 'precedence ' + precedence

        raise ValueError("Invalid precedence {}. Supported values are "
                         "<0 to 7> | critical | flash |"
                         "flash-override | immediate | internet | network |"
                         "priority | routine ".format(precedence))

    def parse_option(self, **parameters):
        """
        parse the option mapping param.
        Args:
            parameters contains:
                option (string): Match match IP option packets.
                    supported values are -
                        any, eol, extended-security, ignore, loose-source-route
                        no-op, record-route, router-alert, security, streamid,
                        strict-source-route, timestamp
                        Allowed value in decimal <0-255>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'option' not in parameters:
            return None

        option = parameters['option']
        if not option:
            return None
        option = ' '.join(option.split())

        if option.isdigit():
            if int(option) >= 0 and int(option) <= 255:
                return 'option ' + option
        if option in ['any', 'eol', 'extended-security',
                      'ignore', 'loose-source-route',
                      'no-op', 'record-route', 'router-alert',
                      'security', 'streamid',
                      'strict-source-route', 'timestamp']:
                return 'option ' + option

        raise ValueError("Invalid option {}. Supported values are "
                         "any, eol, extended-security, ignore, "
                         "loose-source-route no-op, record-route, "
                         "router-alert, security, streamid, "
                         "strict-source-route, timestamp "
                         "Allowed value in decimal <0-255>."
                         .format(option))

    def parse_suppress_rpf_drop(self, **parameters):
        """
        parse the suppress_rpf_drop mapping param.
        Args:
            parameters contains:
                suppress_rpf_drop (boolean):Permit packets that fail RPF check
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'suppress_rpf_drop' not in parameters:
            return None
        suppress_rpf_drop = parameters['suppress_rpf_drop']
        if not suppress_rpf_drop:
            return None

        return 'suppress-rpf-drop'

    def parse_priority(self, **parameters):
        """
        parse the priority param.
        Args:
            parameters contains:
                priority(integer): set priorityr. Allowed value is <0-7>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority' not in parameters:
            return None

        priority = parameters['priority']
        if not priority:
            return None

        if priority >= 0 and priority <= 7:
            return 'priority ' + str(priority)

        raise ValueError("Invalid priority {}. "
                         "Allowed value in decimal <0-7>."
                         .format(priority))

    def parse_priority_force(self, **parameters):
        """
        parse the priority_force mapping param.
        Args:
            parameters contains:
                priority_force(integer): set priority_forcer.
                    Allowed value is <0-7>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority_force' not in parameters:
            return None

        priority_force = parameters['priority_force']
        if not priority_force:
            return None

        if priority_force >= 0 and priority_force <= 7:
            return 'priority-force ' + str(priority_force)

        raise ValueError("Invalid priority_force {}. "
                         "Allowed value in decimal <0-7>."
                         .format(priority_force))

    def parse_priority_mapping(self, **parameters):
        """
        parse the priority_mapping mapping param.
        Args:
            parameters contains:
                priority_mapping(integer): set priority_mappingr.
                    Allowed value is <0-7>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'priority_mapping' not in parameters:
            return None

        priority_mapping = parameters['priority_mapping']
        if not priority_mapping:
            return None

        if priority_mapping >= 0 and priority_mapping <= 7:
            return 'priority-mapping ' + str(priority_mapping)

        raise ValueError("Invalid priority_mapping {}. "
                         "Allowed value in decimal <0-7>."
                         .format(priority_mapping))

    def parse_tos(self, **parameters):
        """
        parse the tos mapping param.
        Args:
            parameters contains:
                tos(integer): set tosr. Allowed value is <0-15>.
        Returns:
            Return None or parsed string on success
        Raise:
            Raise ValueError exception
        Examples:
        """
        if 'tos' not in parameters:
            return None

        tos = parameters['tos']
        if not tos:
            return None

        if tos >= 0 and tos <= 15:
            return 'tos ' + str(tos)

        raise ValueError("Invalid tos {}. "
                         "Allowed value in decimal <0-15>."
                         .format(tos))

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
        if 'mirror' not in parameters:
            return None

        mirror = parameters['mirror']

        if mirror == 'True':
            if 'log' not in parameters:
                return 'mirror'
            log = parameters['log']
            if log == 'False':
                return 'mirror'
        else:
            return None

        raise ValueError("The \'mirror\' value {} is invalid."
                         " mirror can not be configured along with log"
                         .format(mirror))
