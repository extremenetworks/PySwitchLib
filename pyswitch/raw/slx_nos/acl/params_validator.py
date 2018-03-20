# NOS validation code comes here


def validate_params_nos_add_ipv4_rule_acl(**parameters):

    required_params = ['source', 'acl_name', 'action']
    accepted_params = ['sync', 'vlan_id', 'log', 'seq_id', 'destination',
                       'source', 'fin', 'acl_name', 'dscp', 'push', 'rst',
                       'protocol_type', 'count', 'urg', 'ack', 'action',
                       'device']
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


def validate_params_nos_add_std_ipv4_rule_acl(**parameters):

    required_params = ['source', 'acl_name', 'action']
    accepted_params = ['log', 'seq_id', 'source', 'acl_name', 'count',
                       'action', 'device']
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


def validate_params_nos_add_or_remove_l2_acl_rule(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['dsthost', 'acl_name', 'srchost', 'vlan',
                       'dst_mac_addr_mask', 'count', 'log', 'seq_id', 'dst',
                       'source', 'src_mac_addr_mask', 'ethertype', 'action',
                       'device']
    st2_specific_params = ['arp_guard', 'copy_sflow', 'mirror']

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


def validate_params_slxos_17s_add_or_remove_l2_acl_rule(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['dsthost', 'acl_name', 'srchost', 'vlan',
                       'dst_mac_addr_mask', 'count', 'log', 'seq_id', 'dst',
                       'source', 'src_mac_addr_mask', 'ethertype', 'action',
                       'pcp', 'device']
    st2_specific_params = ['arp_guard', 'copy_sflow', 'mirror']

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


def validate_params_nos_delete_add_or_remove_l2_acl_rule(**parameters):

    required_params = ['acl_name', 'seq_id', 'delete']
    accepted_params = ['dsthost', 'acl_name', 'srchost', 'vlan',
                       'dst_mac_addr_mask', 'count', 'log', 'seq_id', 'dst',
                       'source', 'src_mac_addr_mask', 'ethertype', 'action',
                       'device']
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


def validate_params_nos_apply_acl(**parameters):

    required_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    accepted_params = ['intf_type', 'rbridge_id', 'acl_name', 'intf_name',
                       'traffic_type', 'acl_direction', 'device']
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


def validate_params_slx_nos_create_acl(**parameters):

    required_params = ['address_type', 'acl_type', 'acl_name']
    accepted_params = ['address_type', 'acl_type', 'acl_name', 'device']
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


def validate_params_slx_nos_delete_acl(**parameters):

    required_params = ['acl_name']
    accepted_params = ['acl_name', 'device']
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


def validate_params_slx_nos_delete_acl_rule(**parameters):

    required_params = ['seq_id', 'acl_name']
    accepted_params = ['seq_id', 'acl_name', 'device']
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


def validate_params_nos_remove_acl(**parameters):

    required_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    accepted_params = ['intf_type', 'rbridge_id', 'acl_name', 'intf_name',
                       'traffic_type', 'acl_direction', 'device']
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

# SLX validation code comes here


def validate_params_slx_add_ipv4_rule_acl(**parameters):

    required_params = ['source', 'acl_name', 'action']
    accepted_params = ['sync', 'copy_sflow', 'mirror', 'drop_precedence_force',
                       'vlan_id', 'log', 'seq_id', 'destination', 'source',
                       'fin', 'acl_name', 'dscp', 'push', 'rst',
                       'protocol_type', 'count', 'urg', 'ack', 'action',
                       'device']
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


def validate_params_slx_add_std_ipv4_rule_acl(**parameters):

    required_params = ['source', 'acl_name', 'action']
    accepted_params = ['log', 'seq_id', 'source', 'acl_name', 'count',
                       'action', 'device', 'copy_sflow']
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


def validate_params_slx_add_ipv6_rule_acl(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['acl_name', 'sync', 'dscp', 'push', 'copy_sflow',
                       'mirror', 'rst', 'drop_precedence_force', 'vlan_id',
                       'count', 'log', 'ack', 'seq_id', 'destination',
                       'source', 'protocol_type', 'action', 'fin', 'urg',
                       'device']
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


def validate_params_slx_add_ipv6_std_rule_acl(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['acl_name', 'count', 'log', 'seq_id', 'source',
                       'action', 'device']
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


def validate_params_slx_add_or_remove_l2_acl_rule(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['dsthost', 'vlan_tag_format', 'acl_name', 'srchost',
                       'vlan', 'dst_mac_addr_mask', 'arp_guard', 'copy_sflow',
                       'mirror', 'drop_precedence_force', 'count',
                       'log', 'seq_id', 'dst', 'source',
                       'src_mac_addr_mask', 'ethertype', 'action', 'pcp',
                       'device']
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


def validate_params_slx_std_add_or_remove_l2_acl_rule(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['acl_name', 'srchost', 'count', 'log', 'seq_id',
                       'source', 'src_mac_addr_mask', 'action', 'arp_guard',
                       'dst', 'mirror', 'copy_sflow', 'device']
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


def validate_params_slx_apply_acl(**parameters):

    required_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    accepted_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction',
                       'device']
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


def validate_params_slx_ver17s_apply_acl(**parameters):

    required_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    accepted_params = ['intf_type', 'acl_name', 'intf_name', 'traffic_type',
                       'acl_direction', 'device']
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


def validate_params_slx_remove_acl(**parameters):

    required_params = ['intf_type', 'acl_name', 'intf_name', 'acl_direction']
    accepted_params = ['intf_type', 'acl_name', 'intf_name', 'traffic_type',
                       'acl_direction', 'device']
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


def validate_params_nos_add_ipv6_rule_acl(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['acl_name', 'sync', 'dscp', 'push', 'rst', 'vlan_id',
                       'count', 'log', 'ack', 'seq_id', 'destination',
                       'source', 'protocol_type', 'action', 'fin', 'urg',
                       'device']
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


def validate_params_nos_add_ipv6_std_rule_acl(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['acl_name', 'count', 'log', 'seq_id', 'source',
                       'action', 'device']
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


def validate_params_nos_add_or_remove_l2_acl_std_rule(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['acl_name', 'srchost', 'count', 'log', 'seq_id',
                       'source', 'src_mac_addr_mask', 'action', 'device']
    st2_specific_params = ['arp_guard', 'copy_sflow', 'mirror']

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


def validate_params_get_acl_rules(**parameters):
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
