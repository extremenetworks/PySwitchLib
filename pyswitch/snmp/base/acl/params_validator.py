
def validate_params_mlx_add_ipv4_rule_acl(**parameters):

    required_params = ['source', 'acl_name', 'action']
    accepted_params = ['precedence', 'dscp_marking', 'copy_sflow', 'mirror',
                       'drop_precedence_force', 'vlan_id',
                       'log', 'priority_mapping', 'seq_id', 'destination',
                       'suppress_rpf_drop', 'priority', 'source',
                       'priority_force', 'option', 'acl_name',
                       'drop_precedence', 'fragment', 'dscp', 'protocol_type',
                       'tos', 'action', 'icmp_filter', 'tcp_operator']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_add_std_ipv4_rule_acl(**parameters):

    required_params = ['source', 'acl_name', 'action']
    accepted_params = ['acl_name', 'seq_id', 'action', 'source',
                       'vlan_id', 'log']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_add_ipv6_rule_acl(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['tcp_operator', 'acl_name', 'fragment', 'dscp',
                       'dscp_marking', 'copy_sflow', 'mirror',
                       'drop_precedence_force', 'vlan_id', 'drop_precedence',
                       'log', 'seq_id', 'destination', 'source',
                       'protocol_type', 'action', 'icmp_filter']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_add_or_remove_l2_acl_rule(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['dsthost', 'priority_force', 'acl_name', 'vlan',
                       'dst_mac_addr_mask', 'arp_guard', 'mirror',
                       'drop_precedence_force', 'count', 'drop_precedence',
                       'log', 'priority_mapping', 'seq_id', 'dst', 'priority',
                       'source', 'src_mac_addr_mask', 'ethertype', 'action',
                       'delete']
    st2_specific_params = ['copy_sflow']

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    if 'copy_sflow' in received_params and parameters['copy_sflow'] != 'False':
        raise ValueError("unaccepted parameters provided: copy_sflow")

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_apply_acl(**parameters):

    required_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    accepted_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_create_acl(**parameters):

    required_params = ['address_type', 'acl_name']
    accepted_params = ['address_type', 'acl_type', 'acl_name']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_delete_acl(**parameters):

    required_params = ['acl_name']
    accepted_params = ['acl_name']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_delete_ipv4_rule_acl(**parameters):

    required_params = ['seq_id', 'acl_name']
    accepted_params = ['seq_id', 'acl_name']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_delete_ipv6_rule_acl(**parameters):

    required_params = ['seq_id', 'acl_name']
    accepted_params = ['seq_id', 'acl_name']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_remove_acl(**parameters):

    required_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    accepted_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    received_params = list(set(received_params) - set(st2_specific_params))
    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))


def validate_params_mlx_delete_l2_acl_rule(**parameters):

    required_params = ['acl_name', 'seq_id', 'delete']
    accepted_params = ['dsthost', 'acl_name', 'srchost', 'vlan',
                       'dst_mac_addr_mask', 'count', 'log', 'seq_id', 'dst',
                       'source', 'src_mac_addr_mask', 'ethertype', 'action']
    st2_specific_params = ['arp_guard', 'copy_sflow', 'mirror', 'delete']

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    if 'arp_guard' in received_params and parameters['arp_guard'] != 'False':
        raise ValueError("unaccepted parameters provided: arp_guard")

    if 'copy_sflow' in received_params and parameters['copy_sflow'] != 'False':
        raise ValueError("unaccepted parameters provided: copy_sflow")

    if 'mirror' in received_params and parameters['mirror'] != 'False':
        raise ValueError("unaccepted parameters provided: mirror")

    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        if set(unaccepted_params) != set(st2_specific_params):
            raise ValueError("unaccepted parameters provided: {}"
                             .format(unaccepted_params))


def validate_params_mlx_get_acl_rules(**parameters):
    required_params = ['acl_name']
    accepted_params = ['acl_name', 'seq_id']
    st2_specific_params = []

    received_params = [k for k, v in parameters.iteritems() if v]

    absent_required = list(set(required_params) - set(received_params))
    if len(absent_required) > 0:
        raise ValueError("missing required parameters: {}"
                         .format(absent_required))

    unaccepted_params = list(set(received_params) - set(accepted_params))
    if len(unaccepted_params) > 0:
        if set(unaccepted_params) != set(st2_specific_params):
            raise ValueError("unaccepted parameters provided: {}"
                             .format(unaccepted_params))
