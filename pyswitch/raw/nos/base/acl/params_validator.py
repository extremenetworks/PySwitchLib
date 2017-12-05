
def validate_params_add_or_remove_l2_acl_rule(**parameters):

    required_params = ['acl_name', 'source', 'action']
    accepted_params = ['dsthost', 'acl_name', 'srchost', 'vlan',
                       'dst_mac_addr_mask', 'arp_guard', 'copy_sflow',
                       'mirror', 'count', 'log', 'seq_id', 'dst', 'source',
                       'src_mac_addr_mask', 'ethertype', 'action']

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
        raise ValueError("unaccepted parameters provided: {}"
                         .format(unaccepted_params))

