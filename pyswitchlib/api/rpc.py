def activate_status_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: unicode
    :param rbridge_id: Please enter 'all' for activating all nodes in the logical-chassis or individual rbridge-ids of the form 1,2,3-6

        * pattern restriction: ::

            '[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.activate_status.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.activate_status.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.activate_status.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.activate_status', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc.brocade_firmware', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def bna_config_cmd_rpc(self, src=None, dest=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type src: unicode
    :param src: Keyword argument.

    :type dest: unicode
    :param dest: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_rpc.bna_config_cmd.input', 'pybind.nos.v6_0_2b.brocade_ras_rpc.brocade_ras', 'pybind.nos.v6_0_2b.brocade_ras_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_rpc.bna_config_cmd.input', 'pybind.nos.v7_0_1a.brocade_ras_rpc.brocade_ras', 'pybind.nos.v7_0_1a.brocade_ras_rpc'), ('pybind.nos.v7_1_0.brocade_ras_rpc.bna_config_cmd.input', 'pybind.nos.v7_1_0.brocade_ras_rpc.brocade_ras', 'pybind.nos.v7_1_0.brocade_ras_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_rpc.bna_config_cmd.input', 'pybind.slxos.v16r_1_00b.brocade_ras_rpc.brocade_ras', 'pybind.slxos.v16r_1_00b.brocade_ras_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, src=src, dest=dest)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def bna_config_cmd_status_rpc(self, session_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type session_id: long
    :param session_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_rpc.bna_config_cmd_status.input', 'pybind.nos.v6_0_2b.brocade_ras_rpc.brocade_ras', 'pybind.nos.v6_0_2b.brocade_ras_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_rpc.bna_config_cmd_status.input', 'pybind.nos.v7_0_1a.brocade_ras_rpc.brocade_ras', 'pybind.nos.v7_0_1a.brocade_ras_rpc'), ('pybind.nos.v7_1_0.brocade_ras_rpc.bna_config_cmd_status.input', 'pybind.nos.v7_1_0.brocade_ras_rpc.brocade_ras', 'pybind.nos.v7_1_0.brocade_ras_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_rpc.bna_config_cmd_status.input', 'pybind.slxos.v16r_1_00b.brocade_ras_rpc.brocade_ras', 'pybind.slxos.v16r_1_00b.brocade_ras_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, session_id=session_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_auto_bandwidth_sample_history_all_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_auto_bandwidth_sample_history_all', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_auto_bandwidth_sample_history_lsp_rpc(self, lsp_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type lsp_name: unicode
    :param lsp_name: Keyword argument.

        * length restriction: ::

            ['1..64']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_auto_bandwidth_sample_history_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, lsp_name=lsp_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_auto_bandwidth_statistics_all_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_auto_bandwidth_statistics_all', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_auto_bandwidth_statistics_lsp_rpc(self, lsp_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type lsp_name: unicode
    :param lsp_name: Keyword argument.

        * length restriction: ::

            ['1..64']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_auto_bandwidth_statistics_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, lsp_name=lsp_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_bypass_lsp_rpc(self, mpls_clear_bypass_lsp_name_in=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type mpls_clear_bypass_lsp_name_in: unicode
    :param mpls_clear_bypass_lsp_name_in: Bypass-lsp Name

        * length restriction: ::

            ['1..64']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_bypass_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_clear_bypass_lsp_name_in=mpls_clear_bypass_lsp_name_in)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_ldp_neighbor_rpc(self, mpls_clear_all_ldp_sessions=None, mpls_clear_one_ldp_sessions=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type mpls_clear_all_ldp_sessions: YANGBool
    :param mpls_clear_all_ldp_sessions: Keyword argument.

    :type mpls_clear_one_ldp_sessions: unicode
    :param mpls_clear_one_ldp_sessions: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_ldp_neighbor.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_clear_all_ldp_sessions=mpls_clear_all_ldp_sessions, mpls_clear_one_ldp_sessions=mpls_clear_one_ldp_sessions)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_ldp_statistics_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_ldp_statistics', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_lsp_rpc(self, clear_mpls_lsp_option=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type clear_mpls_lsp_option: mpls_clear_lsp_name_in, primary, secondary
    :param clear_mpls_lsp_option: Keyword argument tuple.

    :type mpls_clear_lsp_name_in: unicode
    :param mpls_clear_lsp_name_in: **clear_mpls_lsp_option** tuple argument:  LSP Name

        * length restriction: ::

            ['1..64']

    :type primary: YANGBool
    :param primary: **clear_mpls_lsp_option** tuple argument:  Reset LSP's primary path

    :type secondary: YANGBool
    :param secondary: **clear_mpls_lsp_option** tuple argument:  Reset LSP's secondary path

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_lsp.input', u'clear_mpls_lsp_option')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'mpls_clear_lsp_name_in, primary, secondary'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, clear_mpls_lsp_option=clear_mpls_lsp_option)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_rsvp_statistics_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_rsvp_statistics', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_rsvp_statistics_neighbor_rpc(self, clear_mpls_rsvp_statistics_neighbor_address=None, clear_mpls_rsvp_statistics_neighbor_all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type clear_mpls_rsvp_statistics_neighbor_address: unicode
    :param clear_mpls_rsvp_statistics_neighbor_address: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type clear_mpls_rsvp_statistics_neighbor_all: YANGBool
    :param clear_mpls_rsvp_statistics_neighbor_all: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_rsvp_statistics_neighbor.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, clear_mpls_rsvp_statistics_neighbor_address=clear_mpls_rsvp_statistics_neighbor_address, clear_mpls_rsvp_statistics_neighbor_all=clear_mpls_rsvp_statistics_neighbor_all)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_statistics_rpc(self, mpls_clear_statistics_type=None, mpls_clear_statistics_transit_ldp_fec_prefix=None, mpls_clear_statistics_transit_ldp_prefix_address=None, mpls_clear_statistics_transit_ldp_prefix_mask=None, mpls_clear_statistics_transit_label_id=None, mpls_clear_statistics_tunnel_ldp_id=None, mpls_clear_statistics_tunnel_rsvp_bypass=None, mpls_clear_statistics_tunnel_name=None, mpls_clear_statistics_tunnel_dest=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type mpls_clear_statistics_type: long
    :param mpls_clear_statistics_type: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type mpls_clear_statistics_transit_ldp_fec_prefix: unicode
    :param mpls_clear_statistics_transit_ldp_fec_prefix: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'

    :type mpls_clear_statistics_transit_ldp_prefix_address: unicode
    :param mpls_clear_statistics_transit_ldp_prefix_address: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type mpls_clear_statistics_transit_ldp_prefix_mask: unicode
    :param mpls_clear_statistics_transit_ldp_prefix_mask: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type mpls_clear_statistics_transit_label_id: long
    :param mpls_clear_statistics_transit_label_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type mpls_clear_statistics_tunnel_ldp_id: long
    :param mpls_clear_statistics_tunnel_ldp_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type mpls_clear_statistics_tunnel_rsvp_bypass: int
    :param mpls_clear_statistics_tunnel_rsvp_bypass: Keyword argument.

        * range restriction: ::

            ['0..255']

    :type mpls_clear_statistics_tunnel_name: unicode
    :param mpls_clear_statistics_tunnel_name: Keyword argument.

    :type mpls_clear_statistics_tunnel_dest: unicode
    :param mpls_clear_statistics_tunnel_dest: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_statistics.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_clear_statistics_type=mpls_clear_statistics_type, mpls_clear_statistics_transit_ldp_fec_prefix=mpls_clear_statistics_transit_ldp_fec_prefix, mpls_clear_statistics_transit_ldp_prefix_address=mpls_clear_statistics_transit_ldp_prefix_address, mpls_clear_statistics_transit_ldp_prefix_mask=mpls_clear_statistics_transit_ldp_prefix_mask, mpls_clear_statistics_transit_label_id=mpls_clear_statistics_transit_label_id, mpls_clear_statistics_tunnel_ldp_id=mpls_clear_statistics_tunnel_ldp_id, mpls_clear_statistics_tunnel_rsvp_bypass=mpls_clear_statistics_tunnel_rsvp_bypass, mpls_clear_statistics_tunnel_name=mpls_clear_statistics_tunnel_name, mpls_clear_statistics_tunnel_dest=mpls_clear_statistics_tunnel_dest)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_statistics_ldp_transit_rpc(self, clear_statistics_ldp_transit_fec_prefix=None, clear_statistics_ldp_transit_fec_prefix_address=None, clear_statistics_ldp_transit_fec_prefix_mask=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type clear_statistics_ldp_transit_fec_prefix: unicode
    :param clear_statistics_ldp_transit_fec_prefix: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'

    :type clear_statistics_ldp_transit_fec_prefix_address: unicode
    :param clear_statistics_ldp_transit_fec_prefix_address: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type clear_statistics_ldp_transit_fec_prefix_mask: unicode
    :param clear_statistics_ldp_transit_fec_prefix_mask: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_statistics_ldp_transit.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, clear_statistics_ldp_transit_fec_prefix=clear_statistics_ldp_transit_fec_prefix, clear_statistics_ldp_transit_fec_prefix_address=clear_statistics_ldp_transit_fec_prefix_address, clear_statistics_ldp_transit_fec_prefix_mask=clear_statistics_ldp_transit_fec_prefix_mask)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_statistics_ldp_tunnel_rpc(self, clear_statistics_ldp_tunnel_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type clear_statistics_ldp_tunnel_id: long
    :param clear_statistics_ldp_tunnel_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_statistics_ldp_tunnel.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, clear_statistics_ldp_tunnel_id=clear_statistics_ldp_tunnel_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def dad_status_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.dad_status', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.dad_status', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.dad_status', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.dad_status', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc.brocade_firmware', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def fcoe_get_interface_rpc(self, fcoe_intf_name=None, fcoe_intf_rbridge_id=None, fcoe_intf_include_stats=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type fcoe_intf_name: unicode
    :param fcoe_intf_name: Keyword argument.

        * length restriction: ::

            ['3..32']

    :type fcoe_intf_rbridge_id: long
    :param fcoe_intf_rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type fcoe_intf_include_stats: YANGBool
    :param fcoe_intf_include_stats: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc.fcoe_get_interface.input', 'pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc.fcoe_get_interface.input', 'pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc'), ('pybind.nos.v7_1_0.brocade_fcoe_ext_rpc.fcoe_get_interface.input', 'pybind.nos.v7_1_0.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v7_1_0.brocade_fcoe_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc.fcoe_get_interface.input', 'pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, fcoe_intf_name=fcoe_intf_name, fcoe_intf_rbridge_id=fcoe_intf_rbridge_id, fcoe_intf_include_stats=fcoe_intf_include_stats)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def fcoe_get_login_rpc(self, fcoe_login_interface=None, fcoe_login_vfid=None, fcoe_login_vlan=None, fcoe_login_rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type fcoe_login_interface: unicode
    :param fcoe_login_interface: Keyword argument.

        * length restriction: ::

            ['3..32']

    :type fcoe_login_vfid: long
    :param fcoe_login_vfid: Keyword argument.

        * range restriction: ::

            ['-2147483648..2147483647']

    :type fcoe_login_vlan: long
    :param fcoe_login_vlan: Keyword argument.

        * range restriction: ::

            ['-2147483648..2147483647']

    :type fcoe_login_rbridge_id: long
    :param fcoe_login_rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc.fcoe_get_login.input', 'pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc.fcoe_get_login.input', 'pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc'), ('pybind.nos.v7_1_0.brocade_fcoe_ext_rpc.fcoe_get_login.input', 'pybind.nos.v7_1_0.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v7_1_0.brocade_fcoe_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc.fcoe_get_login.input', 'pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, fcoe_login_interface=fcoe_login_interface, fcoe_login_vfid=fcoe_login_vfid, fcoe_login_vlan=fcoe_login_vlan, fcoe_login_rbridge_id=fcoe_login_rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def firmware_download_rpc(self, rbridge_id=None, auto_activate=None, coldboot=None, scp=None, usb=None, ftp=None, sftp=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: unicode
    :param rbridge_id: Please enter 'all' for activating all nodes in the logical-chassis or individual rbridge-ids of the form 1,2,3-6

        * pattern restriction: ::

            '[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'

    :type auto_activate: YANGBool
    :param auto_activate: To activate new firmware on all nodes

    :type coldboot: YANGBool
    :param coldboot: Perform non ISSU firmware download.

    **Child Instance Keyword Argument Tuple(s)**:

    :type scp: user, password, host, directory, file
    :param scp: Keyword argument tuple.

    :type user: unicode
    :param user: **scp** tuple argument:  Username

    :type password: unicode
    :param password: **scp** tuple argument:  Password

    :type host: unicode
    :param host: **scp** tuple argument:  Host ipv4/ipv6 address

    :type directory: unicode
    :param directory: **scp** tuple argument:  Directory

    :type file: unicode
    :param file: **scp** tuple argument:  Package release file, example - release.plist
    :type usb: directory
    :param usb: Keyword argument tuple.

    :type directory: unicode
    :param directory: **usb** tuple argument:  Directory
    :type ftp: user, password, host, directory, file
    :param ftp: Keyword argument tuple.

    :type user: unicode
    :param user: **ftp** tuple argument:  Username

    :type password: unicode
    :param password: **ftp** tuple argument:  Password

    :type host: unicode
    :param host: **ftp** tuple argument:  Host ipv4/ipv6 address

    :type directory: unicode
    :param directory: **ftp** tuple argument:  Directory

    :type file: unicode
    :param file: **ftp** tuple argument:  Package release file, example - release.plist
    :type sftp: user, password, host, directory, file, port, host_key_check
    :param sftp: Keyword argument tuple.

    :type user: unicode
    :param user: **sftp** tuple argument:  Username

    :type password: unicode
    :param password: **sftp** tuple argument:  Password

    :type host: unicode
    :param host: **sftp** tuple argument:  Host ipv4/ipv6 address

    :type directory: unicode
    :param directory: **sftp** tuple argument:  Directory

    :type file: unicode
    :param file: **sftp** tuple argument:  Package release file, example - release.plist

    :type port: long
    :param port: **sftp** tuple argument:  Server port number (default 22)

        * range restriction: ::

            ['-2147483648..2147483647']

    :type host_key_check: YANGBool
    :param host_key_check: **sftp** tuple argument:  Enable strict host key check

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc.brocade_firmware', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc')]
    composed_child_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', u'scp'), ('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', u'usb'), ('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', u'ftp'), ('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', u'sftp'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', u'sftp'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', u'scp'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', u'ftp'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', u'usb'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', u'scp'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', u'sftp'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', u'ftp'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', u'usb'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', u'ftp'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', u'sftp'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', u'usb'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', u'scp')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'user, password, host, directory, file'}, {'leafval': 'directory'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'user, password, host, directory, file, port, host_key_check'}, {'leafval': 'user, password, host, directory, file, port, host_key_check'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'directory'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'user, password, host, directory, file, port, host_key_check'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'directory'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'user, password, host, directory, file, port, host_key_check'}, {'leafval': 'directory'}, {'leafval': 'user, password, host, directory, file'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, auto_activate=auto_activate, coldboot=coldboot, scp=scp, usb=usb, ftp=ftp, sftp=sftp)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def fwdl_status_rpc(self, fwdl_tid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type fwdl_tid: long
    :param fwdl_tid: Keyword argument.

        * range restriction: ::

            ['-2147483648..2147483647']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.fwdl_status.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.fwdl_status.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.fwdl_status.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.fwdl_status.input', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc.brocade_firmware', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, fwdl_tid=fwdl_tid)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_arp_rpc(self, interface_type=None, interface_name=None, dynamic=None, static=None, ip_address=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    :type dynamic: YANGBool
    :param dynamic: Keyword argument.

    :type static: YANGBool
    :param static: Keyword argument.

    :type ip_address: unicode
    :param ip_address: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_arp_rpc.get_arp.input', 'pybind.nos.v6_0_2b.brocade_arp_rpc.brocade_arp', 'pybind.nos.v6_0_2b.brocade_arp_rpc'), ('pybind.nos.v7_0_1a.brocade_arp_rpc.get_arp.input', 'pybind.nos.v7_0_1a.brocade_arp_rpc.brocade_arp', 'pybind.nos.v7_0_1a.brocade_arp_rpc'), ('pybind.nos.v7_1_0.brocade_arp_rpc.get_arp.input', 'pybind.nos.v7_1_0.brocade_arp_rpc.brocade_arp', 'pybind.nos.v7_1_0.brocade_arp_rpc'), ('pybind.slxos.v16r_1_00b.brocade_arp_rpc.get_arp.input', 'pybind.slxos.v16r_1_00b.brocade_arp_rpc.brocade_arp', 'pybind.slxos.v16r_1_00b.brocade_arp_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, dynamic=dynamic, static=static, ip_address=ip_address)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_contained_in_id_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_entity_rpc.get_contained_in_ID', 'pybind.nos.v6_0_2b.brocade_entity_rpc.brocade_entity', 'pybind.nos.v6_0_2b.brocade_entity_rpc'), ('pybind.nos.v7_0_1a.brocade_entity_rpc.get_contained_in_ID', 'pybind.nos.v7_0_1a.brocade_entity_rpc.brocade_entity', 'pybind.nos.v7_0_1a.brocade_entity_rpc'), ('pybind.nos.v7_1_0.brocade_entity_rpc.get_contained_in_ID', 'pybind.nos.v7_1_0.brocade_entity_rpc.brocade_entity', 'pybind.nos.v7_1_0.brocade_entity_rpc'), ('pybind.slxos.v16r_1_00b.brocade_entity_rpc.get_contained_in_ID', 'pybind.slxos.v16r_1_00b.brocade_entity_rpc.brocade_entity', 'pybind.slxos.v16r_1_00b.brocade_entity_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_flexports_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_hardware_rpc.get_flexports', 'pybind.nos.v6_0_2b.brocade_hardware_rpc.brocade_hardware', 'pybind.nos.v6_0_2b.brocade_hardware_rpc'), ('pybind.nos.v7_0_1a.brocade_hardware_rpc.get_flexports', 'pybind.nos.v7_0_1a.brocade_hardware_rpc.brocade_hardware', 'pybind.nos.v7_0_1a.brocade_hardware_rpc'), ('pybind.nos.v7_1_0.brocade_hardware_rpc.get_flexports', 'pybind.nos.v7_1_0.brocade_hardware_rpc.brocade_hardware', 'pybind.nos.v7_1_0.brocade_hardware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_interface_detail_rpc(self, interface_type=None, interface_name=None, last_rcvd_interface=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    **Child Instance Keyword Argument Tuple(s)**:

    :type last_rcvd_interface: interface_type, interface_name
    :param last_rcvd_interface: Keyword argument tuple.

    :type interface_type: unicode
    :param interface_type: **last_rcvd_interface** tuple argument:  The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: **last_rcvd_interface** tuple argument:  The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_interface_detail.input', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_interface_detail.input', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_interface_detail.input', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_interface_detail.input', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = [('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_interface_detail.input', u'last_rcvd_interface'), ('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_interface_detail.input', u'last_rcvd_interface'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_interface_detail.input', u'last_rcvd_interface'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_interface_detail.input', u'last_rcvd_interface')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, last_rcvd_interface=last_rcvd_interface)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_interface_switchport_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_interface_switchport', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_interface_switchport', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_interface_switchport', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_interface_switchport', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_ip_interface_rpc(self, interface_type=None, interface_name=None, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_ip_interface.input', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_ip_interface.input', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_ip_interface.input', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_ip_interface.input', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_last_config_update_time_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.get_last_config_update_time', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.get_last_config_update_time', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.get_last_config_update_time', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.get_last_config_update_time', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_last_config_update_time_for_xpaths_rpc(self, xpath_strings=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type xpath_strings: xpath_string
    :param xpath_strings: Keyword argument tuple.

    :type xpath_string: unicode
    :param xpath_string: **xpath_strings** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.get_last_config_update_time_for_xpaths.input', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.get_last_config_update_time_for_xpaths.input', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.get_last_config_update_time_for_xpaths.input', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.get_last_config_update_time_for_xpaths.input', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.get_last_config_update_time_for_xpaths.input', u'xpath_strings'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.get_last_config_update_time_for_xpaths.input', u'xpath_strings'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.get_last_config_update_time_for_xpaths.input', u'xpath_strings'), ('pybind.nos.v6_0_2b.brocade_vcs_rpc.get_last_config_update_time_for_xpaths.input', u'xpath_strings')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'xpath_string'}, {'leafval': 'xpath_string'}, {'leafval': 'xpath_string'}, {'leafval': 'xpath_string'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, xpath_strings=xpath_strings)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_lldp_neighbor_detail_rpc(self, interface_type=None, interface_name=None, last_rcvd_ifindex=None, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    :type last_rcvd_ifindex: long
    :param last_rcvd_ifindex: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_lldp_ext_rpc.get_lldp_neighbor_detail.input', 'pybind.nos.v6_0_2b.brocade_lldp_ext_rpc.brocade_lldp_ext', 'pybind.nos.v6_0_2b.brocade_lldp_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_lldp_ext_rpc.get_lldp_neighbor_detail.input', 'pybind.nos.v7_0_1a.brocade_lldp_ext_rpc.brocade_lldp_ext', 'pybind.nos.v7_0_1a.brocade_lldp_ext_rpc'), ('pybind.nos.v7_1_0.brocade_lldp_ext_rpc.get_lldp_neighbor_detail.input', 'pybind.nos.v7_1_0.brocade_lldp_ext_rpc.brocade_lldp_ext', 'pybind.nos.v7_1_0.brocade_lldp_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_lldp_ext_rpc.get_lldp_neighbor_detail.input', 'pybind.slxos.v16r_1_00b.brocade_lldp_ext_rpc.brocade_lldp_ext', 'pybind.slxos.v16r_1_00b.brocade_lldp_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, last_rcvd_ifindex=last_rcvd_ifindex, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mac_acl_for_intf_rpc(self, interface_type=None, interface_name=None, direction=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    :type direction: unicode
    :param direction: Keyword argument.

        * enumeration restriction: ::

            ['all', 'in', 'out']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_mac_access_list_rpc.get_mac_acl_for_intf.input', 'pybind.nos.v6_0_2b.brocade_mac_access_list_rpc.brocade_mac_access_list', 'pybind.nos.v6_0_2b.brocade_mac_access_list_rpc'), ('pybind.nos.v7_0_1a.brocade_mac_access_list_rpc.get_mac_acl_for_intf.input', 'pybind.nos.v7_0_1a.brocade_mac_access_list_rpc.brocade_mac_access_list', 'pybind.nos.v7_0_1a.brocade_mac_access_list_rpc'), ('pybind.nos.v7_1_0.brocade_mac_access_list_rpc.get_mac_acl_for_intf.input', 'pybind.nos.v7_1_0.brocade_mac_access_list_rpc.brocade_mac_access_list', 'pybind.nos.v7_1_0.brocade_mac_access_list_rpc'), ('pybind.slxos.v16r_1_00b.brocade_mac_access_list_rpc.get_mac_acl_for_intf.input', 'pybind.slxos.v16r_1_00b.brocade_mac_access_list_rpc.brocade_mac_access_list', 'pybind.slxos.v16r_1_00b.brocade_mac_access_list_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, direction=direction)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mac_address_table_rpc(self, mac_address=None, last_mac_address_details=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type mac_address: unicode
    :param mac_address: Keyword argument.

        * pattern restriction: ::

            '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'

    **Child Instance Keyword Argument Tuple(s)**:

    :type last_mac_address_details: last_mac_address, last_vlan_id, last_mac_type
    :param last_mac_address_details: Keyword argument tuple.

    :type last_mac_address: unicode
    :param last_mac_address: **last_mac_address_details** tuple argument.

        * pattern restriction: ::

            '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'

    :type last_vlan_id: long
    :param last_vlan_id: **last_mac_address_details** tuple argument.

        * range restriction: ::

            ['0..4294967295']

    :type last_mac_type: unicode
    :param last_mac_type: **last_mac_address_details** tuple argument.

        * enumeration restriction: ::

            ['fpma', 'static', 'dynamic', 'system']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_mac_address_table_rpc.get_mac_address_table.input', 'pybind.nos.v6_0_2b.brocade_mac_address_table_rpc.brocade_mac_address_table', 'pybind.nos.v6_0_2b.brocade_mac_address_table_rpc'), ('pybind.nos.v7_0_1a.brocade_mac_address_table_rpc.get_mac_address_table.input', 'pybind.nos.v7_0_1a.brocade_mac_address_table_rpc.brocade_mac_address_table', 'pybind.nos.v7_0_1a.brocade_mac_address_table_rpc'), ('pybind.nos.v7_1_0.brocade_mac_address_table_rpc.get_mac_address_table.input', 'pybind.nos.v7_1_0.brocade_mac_address_table_rpc.brocade_mac_address_table', 'pybind.nos.v7_1_0.brocade_mac_address_table_rpc'), ('pybind.slxos.v16r_1_00b.brocade_mac_address_table_rpc.get_mac_address_table.input', 'pybind.slxos.v16r_1_00b.brocade_mac_address_table_rpc.brocade_mac_address_table', 'pybind.slxos.v16r_1_00b.brocade_mac_address_table_rpc')]
    composed_child_list = [('pybind.nos.v7_0_1a.brocade_mac_address_table_rpc.get_mac_address_table.input', u'last_mac_address_details'), ('pybind.nos.v6_0_2b.brocade_mac_address_table_rpc.get_mac_address_table.input', u'last_mac_address_details'), ('pybind.slxos.v16r_1_00b.brocade_mac_address_table_rpc.get_mac_address_table.input', u'last_mac_address_details'), ('pybind.nos.v7_1_0.brocade_mac_address_table_rpc.get_mac_address_table.input', u'last_mac_address_details'), ('pybind.nos.v7_1_0.brocade_mac_address_table_rpc.get_mac_address_table.input', u'forwarding_interface')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'last_mac_address, last_vlan_id, last_mac_type'}, {'leafval': 'last_mac_address, last_vlan_id, last_mac_type'}, {'leafval': 'last_mac_address, last_vlan_id, last_mac_type'}, {'leafval': 'last_mac_address, last_vlan_id, last_mac_type'}, {'leafval': 'interface_type, interface_name'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mac_address=mac_address, last_mac_address_details=last_mac_address_details)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_media_detail_rpc(self, interface_type=None, interface_name=None, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_media_detail.input', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_media_detail.input', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_media_detail.input', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_media_detail.input', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_autobw_template_brief_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_autobw_template_brief', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_autobw_template_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_autobw_template_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_autobw_template_one_rpc(self, mpls_autobw_template_one=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type mpls_autobw_template_one: autobwTemplateName
    :param mpls_autobw_template_one: Keyword argument tuple.

    :type autobwTemplateName: unicode
    :param autobwTemplateName: **mpls_autobw_template_one** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_autobw_template_one.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_autobw_template_one.input', u'mpls_autobw_template_one')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'autobwTemplateName'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_autobw_template_one=mpls_autobw_template_one)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_neighbor_brief_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_neighbor_brief', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_neighbor_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_neighbor_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_neighbor_one_rpc(self, mpls_ldp_neighbor_one_input=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type mpls_ldp_neighbor_one_input: ldpid, labelspaceId
    :param mpls_ldp_neighbor_one_input: Keyword argument tuple.

    :type ldpid: unicode
    :param ldpid: **mpls_ldp_neighbor_one_input** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type labelspaceId: int
    :param labelspaceId: **mpls_ldp_neighbor_one_input** tuple argument.

        * range restriction: ::

            ['0..255']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_neighbor_one.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_neighbor_one.input', u'mpls_ldp_neighbor_one_input')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'ldpid, labelspaceId'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_ldp_neighbor_one_input=mpls_ldp_neighbor_one_input)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_session_brief_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_session_brief', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_session_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_session_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_session_one_rpc(self, mpls_ldp_session_one=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type mpls_ldp_session_one: ldpid, labelspaceId, debug, out, in_
    :param mpls_ldp_session_one: Keyword argument tuple.

    :type ldpid: unicode
    :param ldpid: **mpls_ldp_session_one** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type labelspaceId: int
    :param labelspaceId: **mpls_ldp_session_one** tuple argument.

        * range restriction: ::

            ['0..255']

    :type debug: YANGBool
    :param debug: **mpls_ldp_session_one** tuple argument.

    :type out: YANGBool
    :param out: **mpls_ldp_session_one** tuple argument.

    :type in_: YANGBool
    :param in_: **mpls_ldp_session_one** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_session_one.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_session_one.input', u'mpls_ldp_session_one')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'ldpid, labelspaceId, debug, out, in_'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_ldp_session_one=mpls_ldp_session_one)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_nameserver_detail_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: <NUMBER:1-239>;;rbridge-id of switch toretrieve info from

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_nameserver_rpc.get_nameserver_detail.input', 'pybind.nos.v6_0_2b.brocade_nameserver_rpc.brocade_nameserver', 'pybind.nos.v6_0_2b.brocade_nameserver_rpc'), ('pybind.nos.v7_0_1a.brocade_nameserver_rpc.get_nameserver_detail.input', 'pybind.nos.v7_0_1a.brocade_nameserver_rpc.brocade_nameserver', 'pybind.nos.v7_0_1a.brocade_nameserver_rpc'), ('pybind.nos.v7_1_0.brocade_nameserver_rpc.get_nameserver_detail.input', 'pybind.nos.v7_1_0.brocade_nameserver_rpc.brocade_nameserver', 'pybind.nos.v7_1_0.brocade_nameserver_rpc'), ('pybind.slxos.v16r_1_00b.brocade_nameserver_rpc.get_nameserver_detail.input', 'pybind.slxos.v16r_1_00b.brocade_nameserver_rpc.brocade_nameserver', 'pybind.slxos.v16r_1_00b.brocade_nameserver_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_netconf_client_capabilities_rpc(self, session_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type session_id: long
    :param session_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_netconf_ext_rpc.get_netconf_client_capabilities.input', 'pybind.nos.v6_0_2b.brocade_netconf_ext_rpc.brocade_netconf_ext', 'pybind.nos.v6_0_2b.brocade_netconf_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_netconf_ext_rpc.get_netconf_client_capabilities.input', 'pybind.nos.v7_0_1a.brocade_netconf_ext_rpc.brocade_netconf_ext', 'pybind.nos.v7_0_1a.brocade_netconf_ext_rpc'), ('pybind.nos.v7_1_0.brocade_netconf_ext_rpc.get_netconf_client_capabilities.input', 'pybind.nos.v7_1_0.brocade_netconf_ext_rpc.brocade_netconf_ext', 'pybind.nos.v7_1_0.brocade_netconf_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_netconf_ext_rpc.get_netconf_client_capabilities.input', 'pybind.slxos.v16r_1_00b.brocade_netconf_ext_rpc.brocade_netconf_ext', 'pybind.slxos.v16r_1_00b.brocade_netconf_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, session_id=session_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_port_channel_detail_rpc(self, aggregator_id=None, last_aggregator_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type aggregator_id: long
    :param aggregator_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type last_aggregator_id: long
    :param last_aggregator_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_lag_rpc.get_port_channel_detail.input', 'pybind.nos.v6_0_2b.brocade_lag_rpc.brocade_lag', 'pybind.nos.v6_0_2b.brocade_lag_rpc'), ('pybind.nos.v7_0_1a.brocade_lag_rpc.get_port_channel_detail.input', 'pybind.nos.v7_0_1a.brocade_lag_rpc.brocade_lag', 'pybind.nos.v7_0_1a.brocade_lag_rpc'), ('pybind.nos.v7_1_0.brocade_lag_rpc.get_port_channel_detail.input', 'pybind.nos.v7_1_0.brocade_lag_rpc.brocade_lag', 'pybind.nos.v7_1_0.brocade_lag_rpc'), ('pybind.slxos.v16r_1_00b.brocade_lag_rpc.get_port_channel_detail.input', 'pybind.slxos.v16r_1_00b.brocade_lag_rpc.brocade_lag', 'pybind.slxos.v16r_1_00b.brocade_lag_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, aggregator_id=aggregator_id, last_aggregator_id=last_aggregator_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_port_profile_for_intf_rpc(self, rbridge_id=None, interface_type=None, interface_name=None, last_received_interface_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type interface_type: unicode
    :param interface_type: The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    **Child Instance Keyword Argument Tuple(s)**:

    :type last_received_interface_info: interface_type, interface_name
    :param last_received_interface_info: Keyword argument tuple.

    :type interface_type: unicode
    :param interface_type: **last_received_interface_info** tuple argument:  The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: **last_received_interface_info** tuple argument:  The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', 'pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', 'pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc'), ('pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', 'pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v7_1_0.brocade_port_profile_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', 'pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc')]
    composed_child_list = [('pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', u'last_received_interface_info'), ('pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', u'last_received_interface_info'), ('pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', u'last_received_interface_info'), ('pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', u'last_received_interface_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, interface_type=interface_type, interface_name=interface_name, last_received_interface_info=last_received_interface_info)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_port_profile_status_rpc(self, rbridge_id=None, port_profile_name=None, port_profile_status=None, last_received_port_profile_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type port_profile_name: unicode
    :param port_profile_name: Keyword argument.

        * pattern restriction: ::

            '[a-zA-Z]{1}([-a-zA-Z0-9\.\\\\@#\+\*\(\)=\{~\}%<>'
            '=$_\[\]\|]{0,63})'

    :type port_profile_status: unicode
    :param port_profile_status: Keyword argument.

        * enumeration restriction: ::

            ['applied', 'activated', 'associated']

    **Child Instance Keyword Argument Tuple(s)**:

    :type last_received_port_profile_info: profile_name, profile_mac
    :param last_received_port_profile_info: Keyword argument tuple.

    :type profile_name: unicode
    :param profile_name: **last_received_port_profile_info** tuple argument.

        * pattern restriction: ::

            '[a-zA-Z]{1}([-a-zA-Z0-9\.\\\\@#\+\*\(\)=\{~\}%<>'
            '=$_\[\]\|]{0,63})'

    :type profile_mac: unicode
    :param profile_mac: **last_received_port_profile_info** tuple argument.

        * pattern restriction: ::

            '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.get_port_profile_status.input', 'pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.get_port_profile_status.input', 'pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc'), ('pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.get_port_profile_status.input', 'pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v7_1_0.brocade_port_profile_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.get_port_profile_status.input', 'pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc')]
    composed_child_list = [('pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.get_port_profile_status.input', u'last_received_port_profile_info'), ('pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.get_port_profile_status.input', u'last_received_port_profile_info'), ('pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.get_port_profile_status.input', u'last_received_port_profile_info'), ('pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.get_port_profile_status.input', u'last_received_port_profile_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'profile_name, profile_mac'}, {'leafval': 'profile_name, profile_mac'}, {'leafval': 'profile_name, profile_mac'}, {'leafval': 'profile_name, profile_mac'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, port_profile_name=port_profile_name, port_profile_status=port_profile_status, last_received_port_profile_info=last_received_port_profile_info)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_portchannel_info_by_intf_rpc(self, interface_type=None, interface_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: The type of the interface. An 'unknown' type represents error scenario and should not be used.

        * enumeration restriction: ::

            ['l2vlan',
            'gigabitethernet',
            'hundredgigabitethernet',
            'loopback',
            'fortygigabitethernet',
            'unknown',
            'fibrechannel',
            'port-channel',
            'tengigabitethernet']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['3..16']

        * pattern restriction: ::

            '((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?('
            '([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0'
            '-9])(:[1-4])?)'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_lag_rpc.get_portchannel_info_by_intf.input', 'pybind.nos.v6_0_2b.brocade_lag_rpc.brocade_lag', 'pybind.nos.v6_0_2b.brocade_lag_rpc'), ('pybind.nos.v7_0_1a.brocade_lag_rpc.get_portchannel_info_by_intf.input', 'pybind.nos.v7_0_1a.brocade_lag_rpc.brocade_lag', 'pybind.nos.v7_0_1a.brocade_lag_rpc'), ('pybind.nos.v7_1_0.brocade_lag_rpc.get_portchannel_info_by_intf.input', 'pybind.nos.v7_1_0.brocade_lag_rpc.brocade_lag', 'pybind.nos.v7_1_0.brocade_lag_rpc'), ('pybind.slxos.v16r_1_00b.brocade_lag_rpc.get_portchannel_info_by_intf.input', 'pybind.slxos.v16r_1_00b.brocade_lag_rpc.brocade_lag', 'pybind.slxos.v16r_1_00b.brocade_lag_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_show_cfm_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_dot1ag_rpc.get_show_cfm', 'pybind.slxos.v16r_1_00b.brocade_dot1ag_rpc.brocade_dot1ag', 'pybind.slxos.v16r_1_00b.brocade_dot1ag_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_stp_brief_info_rpc(self, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type last_rcvd_instance: instance_id
    :param last_rcvd_instance: Keyword argument tuple.

    :type instance_id: long
    :param instance_id: **last_rcvd_instance** tuple argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_xstp_ext_rpc.get_stp_brief_info.input', 'pybind.nos.v6_0_2b.brocade_xstp_ext_rpc.brocade_xstp_ext', 'pybind.nos.v6_0_2b.brocade_xstp_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_xstp_ext_rpc.get_stp_brief_info.input', 'pybind.nos.v7_0_1a.brocade_xstp_ext_rpc.brocade_xstp_ext', 'pybind.nos.v7_0_1a.brocade_xstp_ext_rpc'), ('pybind.nos.v7_1_0.brocade_xstp_ext_rpc.get_stp_brief_info.input', 'pybind.nos.v7_1_0.brocade_xstp_ext_rpc.brocade_xstp_ext', 'pybind.nos.v7_1_0.brocade_xstp_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_xstp_ext_rpc.get_stp_brief_info.input', 'pybind.slxos.v16r_1_00b.brocade_xstp_ext_rpc.brocade_xstp_ext', 'pybind.slxos.v16r_1_00b.brocade_xstp_ext_rpc')]
    composed_child_list = [('pybind.nos.v7_0_1a.brocade_xstp_ext_rpc.get_stp_brief_info.input', u'last_rcvd_instance'), ('pybind.nos.v6_0_2b.brocade_xstp_ext_rpc.get_stp_brief_info.input', u'last_rcvd_instance'), ('pybind.slxos.v16r_1_00b.brocade_xstp_ext_rpc.get_stp_brief_info.input', u'last_rcvd_instance'), ('pybind.nos.v7_1_0.brocade_xstp_ext_rpc.get_stp_brief_info.input', u'last_rcvd_instance')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'instance_id'}, {'leafval': 'instance_id'}, {'leafval': 'instance_id'}, {'leafval': 'instance_id'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_stp_mst_detail_rpc(self, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type last_rcvd_instance: instance_id
    :param last_rcvd_instance: Keyword argument tuple.

    :type instance_id: long
    :param instance_id: **last_rcvd_instance** tuple argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_xstp_ext_rpc.get_stp_mst_detail.input', 'pybind.nos.v6_0_2b.brocade_xstp_ext_rpc.brocade_xstp_ext', 'pybind.nos.v6_0_2b.brocade_xstp_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_xstp_ext_rpc.get_stp_mst_detail.input', 'pybind.nos.v7_0_1a.brocade_xstp_ext_rpc.brocade_xstp_ext', 'pybind.nos.v7_0_1a.brocade_xstp_ext_rpc'), ('pybind.nos.v7_1_0.brocade_xstp_ext_rpc.get_stp_mst_detail.input', 'pybind.nos.v7_1_0.brocade_xstp_ext_rpc.brocade_xstp_ext', 'pybind.nos.v7_1_0.brocade_xstp_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_xstp_ext_rpc.get_stp_mst_detail.input', 'pybind.slxos.v16r_1_00b.brocade_xstp_ext_rpc.brocade_xstp_ext', 'pybind.slxos.v16r_1_00b.brocade_xstp_ext_rpc')]
    composed_child_list = [('pybind.nos.v7_1_0.brocade_xstp_ext_rpc.get_stp_mst_detail.input', u'last_rcvd_instance'), ('pybind.slxos.v16r_1_00b.brocade_xstp_ext_rpc.get_stp_mst_detail.input', u'last_rcvd_instance'), ('pybind.nos.v7_0_1a.brocade_xstp_ext_rpc.get_stp_mst_detail.input', u'last_rcvd_instance'), ('pybind.nos.v6_0_2b.brocade_xstp_ext_rpc.get_stp_mst_detail.input', u'last_rcvd_instance')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'instance_id'}, {'leafval': 'instance_id'}, {'leafval': 'instance_id'}, {'leafval': 'instance_id'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_system_uptime_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_system_rpc.get_system_uptime.input', 'pybind.nos.v6_0_2b.brocade_system_rpc.brocade_system', 'pybind.nos.v6_0_2b.brocade_system_rpc'), ('pybind.nos.v7_0_1a.brocade_system_rpc.get_system_uptime.input', 'pybind.nos.v7_0_1a.brocade_system_rpc.brocade_system', 'pybind.nos.v7_0_1a.brocade_system_rpc'), ('pybind.nos.v7_1_0.brocade_system_rpc.get_system_uptime.input', 'pybind.nos.v7_1_0.brocade_system_rpc.brocade_system', 'pybind.nos.v7_1_0.brocade_system_rpc'), ('pybind.slxos.v16r_1_00b.brocade_system_rpc.get_system_uptime.input', 'pybind.slxos.v16r_1_00b.brocade_system_rpc.brocade_system', 'pybind.slxos.v16r_1_00b.brocade_system_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_tunnel_info_rpc(self, page_cursor=None, id=None, mode=None, gw_name=None, src_ip=None, dest_ip=None, config_src=None, site_name=None, admin_state=None, oper_state=None, bfd_state=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type page_cursor: unicode
    :param page_cursor: Keyword argument.

    :type id: long
    :param id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type mode: unicode
    :param mode: Keyword argument.

        * enumeration restriction: ::

            ['vxlan']

    :type gw_name: unicode
    :param gw_name: Keyword argument.

        * pattern restriction: ::

            '[-_a-zA-Z0-9]{1,32}'

    :type src_ip: unicode
    :param src_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type dest_ip: unicode
    :param dest_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type config_src: unicode
    :param config_src: Keyword argument.

        * enumeration restriction: ::

            ['bgp-evpn', 'vtep-controller', 'site-config']

    :type site_name: unicode
    :param site_name: Keyword argument.

        * pattern restriction: ::

            '[-_a-zA-Z0-9]{1,63}'

    :type admin_state: unicode
    :param admin_state: Keyword argument.

        * enumeration restriction: ::

            ['down', 'up']

    :type oper_state: unicode
    :param oper_state: Keyword argument.

        * enumeration restriction: ::

            ['down', 'up']

    :type bfd_state: unicode
    :param bfd_state: Keyword argument.

        * enumeration restriction: ::

            ['down', 'up']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc.get_tunnel_info.input', 'pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc.brocade_tunnels_ext', 'pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc'), ('pybind.nos.v7_1_0.brocade_tunnels_ext_rpc.get_tunnel_info.input', 'pybind.nos.v7_1_0.brocade_tunnels_ext_rpc.brocade_tunnels_ext', 'pybind.nos.v7_1_0.brocade_tunnels_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, page_cursor=page_cursor, id=id, mode=mode, gw_name=gw_name, src_ip=src_ip, dest_ip=dest_ip, config_src=config_src, site_name=site_name, admin_state=admin_state, oper_state=oper_state, bfd_state=bfd_state)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_tunnel_statistics_rpc(self, page_cursor=None, id=None, mode=None, gw_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type page_cursor: unicode
    :param page_cursor: Keyword argument.

    :type id: long
    :param id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type mode: unicode
    :param mode: Keyword argument.

        * enumeration restriction: ::

            ['vxlan']

    :type gw_name: unicode
    :param gw_name: Keyword argument.

        * pattern restriction: ::

            '[-_a-zA-Z0-9]{1,32}'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc.get_tunnel_statistics.input', 'pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc.brocade_tunnels_ext', 'pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc'), ('pybind.nos.v7_1_0.brocade_tunnels_ext_rpc.get_tunnel_statistics.input', 'pybind.nos.v7_1_0.brocade_tunnels_ext_rpc.brocade_tunnels_ext', 'pybind.nos.v7_1_0.brocade_tunnels_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, page_cursor=page_cursor, id=id, mode=mode, gw_name=gw_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vcs_details_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.get_vcs_details', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.get_vcs_details', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.get_vcs_details', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.get_vcs_details', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vlan_brief_rpc(self, vlan_id=None, last_rcvd_vlan_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type vlan_id: long
    :param vlan_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type last_rcvd_vlan_id: long
    :param last_rcvd_vlan_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_vlan_brief.input', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_vlan_brief.input', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_vlan_brief.input', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_vlan_brief.input', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, vlan_id=vlan_id, last_rcvd_vlan_id=last_rcvd_vlan_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vmpolicy_macaddr_rpc(self, mac=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type mac: unicode
    :param mac: Keyword argument.

        * pattern restriction: ::

            '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'

    :type vcenter: unicode
    :param vcenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type datacenter: unicode
    :param datacenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type last_rcvd_instance: long
    :param last_rcvd_instance: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vmpolicy_macaddr.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vmpolicy_macaddr.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vmpolicy_macaddr.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vmpolicy_macaddr.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mac=mac, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_dvpgs_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type name: unicode
    :param name: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type vcenter: unicode
    :param vcenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type datacenter: unicode
    :param datacenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type last_rcvd_instance: long
    :param last_rcvd_instance: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_dvpgs.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_dvpgs.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_dvpgs.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_dvpgs.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_dvs_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type name: unicode
    :param name: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type vcenter: unicode
    :param vcenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type datacenter: unicode
    :param datacenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type last_rcvd_instance: long
    :param last_rcvd_instance: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_dvs.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_dvs.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_dvs.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_dvs.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_hosts_rpc(self, vcenter=None, datacenter=None, name=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type vcenter: unicode
    :param vcenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type datacenter: unicode
    :param datacenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type name: unicode
    :param name: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type last_rcvd_instance: long
    :param last_rcvd_instance: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_hosts.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_hosts.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_hosts.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_hosts.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, vcenter=vcenter, datacenter=datacenter, name=name, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_portgroups_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type name: unicode
    :param name: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type vcenter: unicode
    :param vcenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type datacenter: unicode
    :param datacenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type last_rcvd_instance: long
    :param last_rcvd_instance: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_portgroups.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_portgroups.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_portgroups.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_portgroups.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_vms_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type name: unicode
    :param name: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type vcenter: unicode
    :param vcenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type datacenter: unicode
    :param datacenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type last_rcvd_instance: long
    :param last_rcvd_instance: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_vms.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_vms.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_vms.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_vms.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_vswitches_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type name: unicode
    :param name: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type vcenter: unicode
    :param vcenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type datacenter: unicode
    :param datacenter: Keyword argument.

        * length restriction: ::

            ['1..80']

    :type last_rcvd_instance: long
    :param last_rcvd_instance: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_vswitches.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_vswitches.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_vswitches.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_vswitches.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_device_brief_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.1.0    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_device_brief', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_discovery_domain_rpc(self, isns_dd_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.1.0    

    **Instance Argument(s)**:

    :type isns_dd_name: unicode
    :param isns_dd_name: Keyword argument.

        * length restriction: ::

            ['1..255']

        * pattern restriction: ::

            '[-_0-9a-zA-Z]{1,255}'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_discovery_domain.input', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, isns_dd_name=isns_dd_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_discovery_domain_set_rpc(self, isns_dds_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.1.0    

    **Instance Argument(s)**:

    :type isns_dds_name: unicode
    :param isns_dds_name: Keyword argument.

        * length restriction: ::

            ['1..255']

        * pattern restriction: ::

            '[-_0-9a-zA-Z]{1,255}'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_discovery_domain_set.input', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, isns_dds_name=isns_dds_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_last_device_timestamp_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.1.0    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_last_device_timestamp', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_server_role_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.1.0    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_server_role', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_vrf_forwarding_rpc(self, isns_vrf_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.1.0    

    **Instance Argument(s)**:

    :type isns_vrf_id: long
    :param isns_vrf_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_vrf_forwarding.input', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, isns_vrf_id=isns_vrf_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def l2traceroute_rpc(self, src_mac=None, dest_mac=None, vlan_id=None, rbridge_id=None, src_ip=None, dest_ip=None, l4protocol=None, l4_src_port=None, l4_dest_port=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type src_mac: unicode
    :param src_mac: Keyword argument.

    :type dest_mac: unicode
    :param dest_mac: Keyword argument.

    :type vlan_id: long
    :param vlan_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type rbridge_id: long
    :param rbridge_id: Syntax: rbridge-id [rbridge-id]

        * range restriction: ::

            ['0..4294967295']

    :type src_ip: unicode
    :param src_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type dest_ip: unicode
    :param dest_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type l4protocol: unicode
    :param l4protocol: Keyword argument.

        * enumeration restriction: ::

            ['UDP', 'TCP']

    :type l4_src_port: int
    :param l4_src_port: Keyword argument.

        * range restriction: ::

            ['0..65535']

    :type l4_dest_port: int
    :param l4_dest_port: Keyword argument.

        * range restriction: ::

            ['0..65535']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_trilloam_rpc.l2traceroute.input', 'pybind.nos.v6_0_2b.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v6_0_2b.brocade_trilloam_rpc'), ('pybind.nos.v7_0_1a.brocade_trilloam_rpc.l2traceroute.input', 'pybind.nos.v7_0_1a.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v7_0_1a.brocade_trilloam_rpc'), ('pybind.nos.v7_1_0.brocade_trilloam_rpc.l2traceroute.input', 'pybind.nos.v7_1_0.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v7_1_0.brocade_trilloam_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, src_mac=src_mac, dest_mac=dest_mac, vlan_id=vlan_id, rbridge_id=rbridge_id, src_ip=src_ip, dest_ip=dest_ip, l4protocol=l4protocol, l4_src_port=l4_src_port, l4_dest_port=l4_dest_port)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def l2traceroute_result_rpc(self, session_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type session_id: long
    :param session_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_trilloam_rpc.l2traceroute_result.input', 'pybind.nos.v6_0_2b.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v6_0_2b.brocade_trilloam_rpc'), ('pybind.nos.v7_0_1a.brocade_trilloam_rpc.l2traceroute_result.input', 'pybind.nos.v7_0_1a.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v7_0_1a.brocade_trilloam_rpc'), ('pybind.nos.v7_1_0.brocade_trilloam_rpc.l2traceroute_result.input', 'pybind.nos.v7_1_0.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v7_1_0.brocade_trilloam_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, session_id=session_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def logical_chassis_fwdl_sanity_rpc(self, user=None, password=None, host=None, directory=None, file=None, rbridge_id=None, auto_activate=None, coldboot=None, protocol=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type user: unicode
    :param user: Username

    :type password: unicode
    :param password: Password

    :type host: unicode
    :param host: Host ipv4/ipv6 address

    :type directory: unicode
    :param directory: Directory

    :type file: unicode
    :param file: Package release file, example - release.plist

    :type rbridge_id: unicode
    :param rbridge_id: Enter 'all' for firmware download on all nodes in the logical-chassis or comma seperated rbridge-ids like 'rbridge-id 3,4,7-9,20'

        * pattern restriction: ::

            '[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'

    :type auto_activate: YANGBool
    :param auto_activate: To activate new firmware on all nodes

    :type coldboot: YANGBool
    :param coldboot: Perform non ISSU firmware download.

    :type protocol: unicode
    :param protocol: Protocol type : ftp, scp or sftp

        * enumeration restriction: ::

            ['ftp', 'scp', 'sftp']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.logical_chassis_fwdl_sanity.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.logical_chassis_fwdl_sanity.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.logical_chassis_fwdl_sanity.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, user=user, password=password, host=host, directory=directory, file=file, rbridge_id=rbridge_id, auto_activate=auto_activate, coldboot=coldboot, protocol=protocol)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def logical_chassis_fwdl_status_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type rbridge_id: unicode
    :param rbridge_id: Please enter 'all' for activating all nodes in the logical-chassis or individual rbridge-ids of the form 1,2,3-6

        * pattern restriction: ::

            '[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.logical_chassis_fwdl_status.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.logical_chassis_fwdl_status.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.logical_chassis_fwdl_status.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def maps_get_all_policy_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_maps_ext_rpc.maps_get_all_policy.input', 'pybind.nos.v6_0_2b.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v6_0_2b.brocade_maps_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_maps_ext_rpc.maps_get_all_policy.input', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc'), ('pybind.nos.v7_1_0.brocade_maps_ext_rpc.maps_get_all_policy.input', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc.maps_get_all_policy.input', 'pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def maps_get_default_rules_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_maps_ext_rpc.maps_get_default_rules.input', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc'), ('pybind.nos.v7_1_0.brocade_maps_ext_rpc.maps_get_default_rules.input', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def maps_get_rules_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_maps_ext_rpc.maps_get_rules.input', 'pybind.nos.v6_0_2b.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v6_0_2b.brocade_maps_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc.maps_get_rules.input', 'pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def maps_re_apply_policy_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_maps_ext_rpc.maps_re_apply_policy.input', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc'), ('pybind.nos.v7_1_0.brocade_maps_ext_rpc.maps_re_apply_policy.input', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def mpls_adjust_bandwidth_lsp_rpc(self, lsp_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type lsp_name: unicode
    :param lsp_name: Keyword argument.

        * length restriction: ::

            ['1..64']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.mpls_adjust_bandwidth_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, lsp_name=lsp_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def mpls_adjust_bandwidth_lsp_all_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.mpls_adjust_bandwidth_lsp_all', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def mpls_reopt_lsp_rpc(self, mpls_reoptimize_lsp_name_in=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type mpls_reoptimize_lsp_name_in: unicode
    :param mpls_reoptimize_lsp_name_in: Keyword argument.

        * length restriction: ::

            ['1..64']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.mpls_reopt_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_reoptimize_lsp_name_in=mpls_reoptimize_lsp_name_in)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def no_vcs_rbridge_context_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.no_vcs_rbridge_context', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.no_vcs_rbridge_context', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.no_vcs_rbridge_context', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.no_vcs_rbridge_context', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def ping_mpls_rpc(self, oam_params=None, ping_mpls_input=None, traceroute_params=None, ping_params=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type oam_params: destination, reply_mode, reply_tos, size, source, timeout
    :param oam_params: Keyword argument tuple.

    :type destination: unicode
    :param destination: **oam_params** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type reply_mode: unicode
    :param reply_mode: **oam_params** tuple argument.

        * enumeration restriction: ::

            ['router-alert']

    :type reply_tos: int
    :param reply_tos: **oam_params** tuple argument.

        * range restriction: ::

            ['0..255']

    :type size: long
    :param size: **oam_params** tuple argument.

        * range restriction: ::

            ['0..4294967295']

    :type source: unicode
    :param source: **oam_params** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type timeout: long
    :param timeout: **oam_params** tuple argument.

        * range restriction: ::

            ['0..4294967295']
    :type ping_mpls_input: ping_mpls_rsvp_lsp, ping_mpls_rsvp_session_src, ping_mpls_rsvp_session_dst, ping_mpls_rsvp_session_id, ping_mpls_ldp_prefix, ping_mpls_ldp_prefix_address
    :param ping_mpls_input: Keyword argument tuple.

    :type ping_mpls_rsvp_lsp: unicode
    :param ping_mpls_rsvp_lsp: **ping_mpls_input** tuple argument.

        * length restriction: ::

            ['1..64']

    :type ping_mpls_rsvp_session_src: unicode
    :param ping_mpls_rsvp_session_src: **ping_mpls_input** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type ping_mpls_rsvp_session_dst: unicode
    :param ping_mpls_rsvp_session_dst: **ping_mpls_input** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type ping_mpls_rsvp_session_id: long
    :param ping_mpls_rsvp_session_id: **ping_mpls_input** tuple argument.

        * range restriction: ::

            ['0..4294967295']

    :type ping_mpls_ldp_prefix: unicode
    :param ping_mpls_ldp_prefix: **ping_mpls_input** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'

    :type ping_mpls_ldp_prefix_address: unicode
    :param ping_mpls_ldp_prefix_address: **ping_mpls_input** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'
    :type traceroute_params: dsmap, min_ttl, max_ttl, nexthop
    :param traceroute_params: Keyword argument tuple.

    :type dsmap: YANGBool
    :param dsmap: **traceroute_params** tuple argument.

    :type min_ttl: int
    :param min_ttl: **traceroute_params** tuple argument.

        * range restriction: ::

            ['0..255']

    :type max_ttl: int
    :param max_ttl: **traceroute_params** tuple argument.

        * range restriction: ::

            ['0..255']

    :type nexthop: unicode
    :param nexthop: **traceroute_params** tuple argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'
    :type ping_params: count, detail, detour, standby
    :param ping_params: Keyword argument tuple.

    :type count: long
    :param count: **ping_params** tuple argument.

        * range restriction: ::

            ['0..4294967295']

    :type detail: YANGBool
    :param detail: **ping_params** tuple argument.

    :type detour: YANGBool
    :param detour: **ping_params** tuple argument.

    :type standby: YANGBool
    :param standby: **ping_params** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.ping_mpls.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.ping_mpls.input.ping_mpls_input', u'oam_params'), ('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.ping_mpls.input', u'ping_mpls_input'), ('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.ping_mpls.input.ping_mpls_input', u'traceroute_params'), ('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.ping_mpls.input.ping_mpls_input', u'ping_params')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'destination, reply_mode, reply_tos, size, source, timeout'}, {'leafval': 'ping_mpls_rsvp_lsp, ping_mpls_rsvp_session_src, ping_mpls_rsvp_session_dst, ping_mpls_rsvp_session_id, ping_mpls_ldp_prefix, ping_mpls_ldp_prefix_address'}, {'leafval': 'dsmap, min_ttl, max_ttl, nexthop'}, {'leafval': 'count, detail, detour, standby'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, oam_params=oam_params, ping_mpls_input=ping_mpls_input, traceroute_params=traceroute_params, ping_params=ping_params)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def redundancy_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 7.0.1a, 7.1.0    

    **Instance Argument(s)**:

    :type rbridge_id: unicode
    :param rbridge_id: Please enter 'all' or an individual rbridge-id in the range 1-239

        * length restriction: ::

            ['1..3']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_ha_rpc.redundancy.input', 'pybind.nos.v7_0_1a.brocade_ha_rpc.brocade_ha', 'pybind.nos.v7_0_1a.brocade_ha_rpc'), ('pybind.nos.v7_1_0.brocade_ha_rpc.redundancy.input', 'pybind.nos.v7_1_0.brocade_ha_rpc.brocade_ha', 'pybind.nos.v7_1_0.brocade_ha_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def reload_rpc(self, rbridge_id=None, system=None, standby=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: unicode
    :param rbridge_id: Rbridge-id (use only with  reload system)

        * length restriction: ::

            ['1..3']

    :type system: YANGBool
    :param system: Reboots the chassis

    :type standby: YANGBool
    :param standby: Reboots the standby MM

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ha_rpc.reload.input', 'pybind.nos.v6_0_2b.brocade_ha_rpc.brocade_ha', 'pybind.nos.v6_0_2b.brocade_ha_rpc'), ('pybind.nos.v7_0_1a.brocade_ha_rpc.reload.input', 'pybind.nos.v7_0_1a.brocade_ha_rpc.brocade_ha', 'pybind.nos.v7_0_1a.brocade_ha_rpc'), ('pybind.nos.v7_1_0.brocade_ha_rpc.reload.input', 'pybind.nos.v7_1_0.brocade_ha_rpc.brocade_ha', 'pybind.nos.v7_1_0.brocade_ha_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ha_rpc.reload.input', 'pybind.slxos.v16r_1_00b.brocade_ha_rpc.brocade_ha', 'pybind.slxos.v16r_1_00b.brocade_ha_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, system=system, standby=standby)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def set_http_application_url_rpc(self, config_http_app_url=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type config_http_app_url: url, op_type
    :param config_http_app_url: Keyword argument tuple.

    :type url: unicode
    :param url: **config_http_app_url** tuple argument.

        * length restriction: ::

            ['0..512']

    :type op_type: long
    :param op_type: **config_http_app_url** tuple argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_http_redirect_rpc.set_http_application_url.input', 'pybind.nos.v6_0_2b.brocade_http_redirect_rpc.brocade_http_redirect', 'pybind.nos.v6_0_2b.brocade_http_redirect_rpc'), ('pybind.nos.v7_0_1a.brocade_http_redirect_rpc.set_http_application_url.input', 'pybind.nos.v7_0_1a.brocade_http_redirect_rpc.brocade_http_redirect', 'pybind.nos.v7_0_1a.brocade_http_redirect_rpc'), ('pybind.nos.v7_1_0.brocade_http_redirect_rpc.set_http_application_url.input', 'pybind.nos.v7_1_0.brocade_http_redirect_rpc.brocade_http_redirect', 'pybind.nos.v7_1_0.brocade_http_redirect_rpc'), ('pybind.slxos.v16r_1_00b.brocade_http_redirect_rpc.set_http_application_url.input', 'pybind.slxos.v16r_1_00b.brocade_http_redirect_rpc.brocade_http_redirect', 'pybind.slxos.v16r_1_00b.brocade_http_redirect_rpc')]
    composed_child_list = [('pybind.nos.v7_1_0.brocade_http_redirect_rpc.set_http_application_url.input', u'config_http_app_url'), ('pybind.slxos.v16r_1_00b.brocade_http_redirect_rpc.set_http_application_url.input', u'config_http_app_url'), ('pybind.nos.v7_0_1a.brocade_http_redirect_rpc.set_http_application_url.input', u'config_http_app_url'), ('pybind.nos.v6_0_2b.brocade_http_redirect_rpc.set_http_application_url.input', u'config_http_app_url')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'url, op_type'}, {'leafval': 'url, op_type'}, {'leafval': 'url, op_type'}, {'leafval': 'url, op_type'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, config_http_app_url=config_http_app_url)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_bare_metal_state_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_preprovision_rpc.show_bare_metal_state', 'pybind.nos.v6_0_2b.brocade_preprovision_rpc.brocade_preprovision', 'pybind.nos.v6_0_2b.brocade_preprovision_rpc'), ('pybind.nos.v7_0_1a.brocade_preprovision_rpc.show_bare_metal_state', 'pybind.nos.v7_0_1a.brocade_preprovision_rpc.brocade_preprovision', 'pybind.nos.v7_0_1a.brocade_preprovision_rpc'), ('pybind.nos.v7_1_0.brocade_preprovision_rpc.show_bare_metal_state', 'pybind.nos.v7_1_0.brocade_preprovision_rpc.brocade_preprovision', 'pybind.nos.v7_1_0.brocade_preprovision_rpc'), ('pybind.slxos.v16r_1_00b.brocade_preprovision_rpc.show_bare_metal_state', 'pybind.slxos.v16r_1_00b.brocade_preprovision_rpc.brocade_preprovision', 'pybind.slxos.v16r_1_00b.brocade_preprovision_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_clock_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_clock_rpc.show_clock.input', 'pybind.nos.v6_0_2b.brocade_clock_rpc.brocade_clock', 'pybind.nos.v6_0_2b.brocade_clock_rpc'), ('pybind.nos.v7_0_1a.brocade_clock_rpc.show_clock.input', 'pybind.nos.v7_0_1a.brocade_clock_rpc.brocade_clock', 'pybind.nos.v7_0_1a.brocade_clock_rpc'), ('pybind.nos.v7_1_0.brocade_clock_rpc.show_clock.input', 'pybind.nos.v7_1_0.brocade_clock_rpc.brocade_clock', 'pybind.nos.v7_1_0.brocade_clock_rpc'), ('pybind.slxos.v16r_1_00b.brocade_clock_rpc.show_clock', 'pybind.slxos.v16r_1_00b.brocade_clock_rpc.brocade_clock', 'pybind.slxos.v16r_1_00b.brocade_clock_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_fabric_trunk_info_rpc(self, rbridge_id=None, all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Syntax: rbridge-id [rbridge-id]

        * range restriction: ::

            ['0..4294967295']

    :type all: YANGBool
    :param all: All rbridges in fabric

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fabric_service_rpc.show_fabric_trunk_info.input', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc'), ('pybind.nos.v7_0_1a.brocade_fabric_service_rpc.show_fabric_trunk_info.input', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc'), ('pybind.nos.v7_1_0.brocade_fabric_service_rpc.show_fabric_trunk_info.input', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.show_fabric_trunk_info.input', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, all=all)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_fibrechannel_interface_info_rpc(self, all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type all: YANGBool
    :param all: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fabric_service_rpc.show_fibrechannel_interface_info.input', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc'), ('pybind.nos.v7_0_1a.brocade_fabric_service_rpc.show_fibrechannel_interface_info.input', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc'), ('pybind.nos.v7_1_0.brocade_fabric_service_rpc.show_fibrechannel_interface_info.input', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.show_fibrechannel_interface_info.input', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, all=all)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_firmware_version_rpc(self, switchid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type switchid: unicode
    :param switchid: Keyword argument.

        * length restriction: ::

            ['1..3']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_ext_rpc.show_firmware_version.input', 'pybind.nos.v6_0_2b.brocade_firmware_ext_rpc.brocade_firmware_ext', 'pybind.nos.v6_0_2b.brocade_firmware_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_ext_rpc.show_firmware_version.input', 'pybind.nos.v7_0_1a.brocade_firmware_ext_rpc.brocade_firmware_ext', 'pybind.nos.v7_0_1a.brocade_firmware_ext_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_ext_rpc.show_firmware_version.input', 'pybind.nos.v7_1_0.brocade_firmware_ext_rpc.brocade_firmware_ext', 'pybind.nos.v7_1_0.brocade_firmware_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_ext_rpc.show_firmware_version', 'pybind.slxos.v16r_1_00b.brocade_firmware_ext_rpc.brocade_firmware_ext', 'pybind.slxos.v16r_1_00b.brocade_firmware_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, switchid=switchid)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_linkinfo_rpc(self, all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type all: YANGBool
    :param all: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fabric_service_rpc.show_linkinfo.input', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc'), ('pybind.nos.v7_0_1a.brocade_fabric_service_rpc.show_linkinfo.input', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc'), ('pybind.nos.v7_1_0.brocade_fabric_service_rpc.show_linkinfo.input', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.show_linkinfo.input', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, all=all)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bfd_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bfd', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_bypass_lsp_extensive_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_bypass_lsp_extensive', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_debug_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_debug', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_name_debug_rpc(self, show_lsp_input_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type show_lsp_input_info: lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more
    :param show_lsp_input_info: Keyword argument tuple.

    :type lsp: unicode
    :param lsp: **show_lsp_input_info** tuple argument.

    :type lsp_wide: YANGBool
    :param lsp_wide: **show_lsp_input_info** tuple argument.

    :type lsp_detail: YANGBool
    :param lsp_detail: **show_lsp_input_info** tuple argument.

    :type lsp_extensive: YANGBool
    :param lsp_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_debug: YANGBool
    :param lsp_debug: **show_lsp_input_info** tuple argument.

    :type lsp_name: unicode
    :param lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_name_extensive: YANGBool
    :param lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_name_debug: YANGBool
    :param lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp: unicode
    :param bypass_lsp: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_wide: YANGBool
    :param bypass_lsp_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_detail: YANGBool
    :param bypass_lsp_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_extensive: YANGBool
    :param bypass_lsp_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_debug: YANGBool
    :param bypass_lsp_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name: unicode
    :param bypass_lsp_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_extensive: YANGBool
    :param bypass_lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_debug: YANGBool
    :param bypass_lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static: unicode
    :param bypass_lsp_static: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_wide: YANGBool
    :param bypass_lsp_static_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_detail: YANGBool
    :param bypass_lsp_static_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_extensive: YANGBool
    :param bypass_lsp_static_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_debug: YANGBool
    :param bypass_lsp_static_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name: unicode
    :param bypass_lsp_static_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_extensive: YANGBool
    :param bypass_lsp_static_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_debug: YANGBool
    :param bypass_lsp_static_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic: unicode
    :param bypass_lsp_dynamic: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_wide: YANGBool
    :param bypass_lsp_dynamic_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_detail: YANGBool
    :param bypass_lsp_dynamic_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_extensive: YANGBool
    :param bypass_lsp_dynamic_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_debug: YANGBool
    :param bypass_lsp_dynamic_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name: unicode
    :param bypass_lsp_dynamic_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_extensive: YANGBool
    :param bypass_lsp_dynamic_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_debug: YANGBool
    :param bypass_lsp_dynamic_name_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_lsp_name: unicode
    :param lsp_input_lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_input_bypass: YANGBool
    :param lsp_input_bypass: **show_lsp_input_info** tuple argument.

    :type lsp_input_dynamic: YANGBool
    :param lsp_input_dynamic: **show_lsp_input_info** tuple argument.

    :type lsp_input_brief: YANGBool
    :param lsp_input_brief: **show_lsp_input_info** tuple argument.

    :type lsp_input_wide: YANGBool
    :param lsp_input_wide: **show_lsp_input_info** tuple argument.

    :type lsp_input_detail: YANGBool
    :param lsp_input_detail: **show_lsp_input_info** tuple argument.

    :type lsp_input_extensive: YANGBool
    :param lsp_input_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_input_debug: YANGBool
    :param lsp_input_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_one: YANGBool
    :param lsp_input_one: **show_lsp_input_info** tuple argument.

    :type lsp_input_all: YANGBool
    :param lsp_input_all: **show_lsp_input_info** tuple argument.

    :type lsp_input_more: YANGBool
    :param lsp_input_more: **show_lsp_input_info** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_name_debug.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_name_debug.input', u'show_lsp_input_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, show_lsp_input_info=show_lsp_input_info)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_name_detail_rpc(self, show_lsp_input_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type show_lsp_input_info: lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more
    :param show_lsp_input_info: Keyword argument tuple.

    :type lsp: unicode
    :param lsp: **show_lsp_input_info** tuple argument.

    :type lsp_wide: YANGBool
    :param lsp_wide: **show_lsp_input_info** tuple argument.

    :type lsp_detail: YANGBool
    :param lsp_detail: **show_lsp_input_info** tuple argument.

    :type lsp_extensive: YANGBool
    :param lsp_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_debug: YANGBool
    :param lsp_debug: **show_lsp_input_info** tuple argument.

    :type lsp_name: unicode
    :param lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_name_extensive: YANGBool
    :param lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_name_debug: YANGBool
    :param lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp: unicode
    :param bypass_lsp: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_wide: YANGBool
    :param bypass_lsp_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_detail: YANGBool
    :param bypass_lsp_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_extensive: YANGBool
    :param bypass_lsp_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_debug: YANGBool
    :param bypass_lsp_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name: unicode
    :param bypass_lsp_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_extensive: YANGBool
    :param bypass_lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_debug: YANGBool
    :param bypass_lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static: unicode
    :param bypass_lsp_static: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_wide: YANGBool
    :param bypass_lsp_static_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_detail: YANGBool
    :param bypass_lsp_static_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_extensive: YANGBool
    :param bypass_lsp_static_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_debug: YANGBool
    :param bypass_lsp_static_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name: unicode
    :param bypass_lsp_static_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_extensive: YANGBool
    :param bypass_lsp_static_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_debug: YANGBool
    :param bypass_lsp_static_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic: unicode
    :param bypass_lsp_dynamic: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_wide: YANGBool
    :param bypass_lsp_dynamic_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_detail: YANGBool
    :param bypass_lsp_dynamic_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_extensive: YANGBool
    :param bypass_lsp_dynamic_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_debug: YANGBool
    :param bypass_lsp_dynamic_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name: unicode
    :param bypass_lsp_dynamic_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_extensive: YANGBool
    :param bypass_lsp_dynamic_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_debug: YANGBool
    :param bypass_lsp_dynamic_name_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_lsp_name: unicode
    :param lsp_input_lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_input_bypass: YANGBool
    :param lsp_input_bypass: **show_lsp_input_info** tuple argument.

    :type lsp_input_dynamic: YANGBool
    :param lsp_input_dynamic: **show_lsp_input_info** tuple argument.

    :type lsp_input_brief: YANGBool
    :param lsp_input_brief: **show_lsp_input_info** tuple argument.

    :type lsp_input_wide: YANGBool
    :param lsp_input_wide: **show_lsp_input_info** tuple argument.

    :type lsp_input_detail: YANGBool
    :param lsp_input_detail: **show_lsp_input_info** tuple argument.

    :type lsp_input_extensive: YANGBool
    :param lsp_input_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_input_debug: YANGBool
    :param lsp_input_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_one: YANGBool
    :param lsp_input_one: **show_lsp_input_info** tuple argument.

    :type lsp_input_all: YANGBool
    :param lsp_input_all: **show_lsp_input_info** tuple argument.

    :type lsp_input_more: YANGBool
    :param lsp_input_more: **show_lsp_input_info** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_name_detail.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_name_detail.input', u'show_lsp_input_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, show_lsp_input_info=show_lsp_input_info)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_name_extensive_rpc(self, show_lsp_input_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type show_lsp_input_info: lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more
    :param show_lsp_input_info: Keyword argument tuple.

    :type lsp: unicode
    :param lsp: **show_lsp_input_info** tuple argument.

    :type lsp_wide: YANGBool
    :param lsp_wide: **show_lsp_input_info** tuple argument.

    :type lsp_detail: YANGBool
    :param lsp_detail: **show_lsp_input_info** tuple argument.

    :type lsp_extensive: YANGBool
    :param lsp_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_debug: YANGBool
    :param lsp_debug: **show_lsp_input_info** tuple argument.

    :type lsp_name: unicode
    :param lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_name_extensive: YANGBool
    :param lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_name_debug: YANGBool
    :param lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp: unicode
    :param bypass_lsp: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_wide: YANGBool
    :param bypass_lsp_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_detail: YANGBool
    :param bypass_lsp_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_extensive: YANGBool
    :param bypass_lsp_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_debug: YANGBool
    :param bypass_lsp_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name: unicode
    :param bypass_lsp_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_extensive: YANGBool
    :param bypass_lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_debug: YANGBool
    :param bypass_lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static: unicode
    :param bypass_lsp_static: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_wide: YANGBool
    :param bypass_lsp_static_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_detail: YANGBool
    :param bypass_lsp_static_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_extensive: YANGBool
    :param bypass_lsp_static_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_debug: YANGBool
    :param bypass_lsp_static_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name: unicode
    :param bypass_lsp_static_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_extensive: YANGBool
    :param bypass_lsp_static_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_debug: YANGBool
    :param bypass_lsp_static_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic: unicode
    :param bypass_lsp_dynamic: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_wide: YANGBool
    :param bypass_lsp_dynamic_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_detail: YANGBool
    :param bypass_lsp_dynamic_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_extensive: YANGBool
    :param bypass_lsp_dynamic_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_debug: YANGBool
    :param bypass_lsp_dynamic_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name: unicode
    :param bypass_lsp_dynamic_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_extensive: YANGBool
    :param bypass_lsp_dynamic_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_debug: YANGBool
    :param bypass_lsp_dynamic_name_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_lsp_name: unicode
    :param lsp_input_lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_input_bypass: YANGBool
    :param lsp_input_bypass: **show_lsp_input_info** tuple argument.

    :type lsp_input_dynamic: YANGBool
    :param lsp_input_dynamic: **show_lsp_input_info** tuple argument.

    :type lsp_input_brief: YANGBool
    :param lsp_input_brief: **show_lsp_input_info** tuple argument.

    :type lsp_input_wide: YANGBool
    :param lsp_input_wide: **show_lsp_input_info** tuple argument.

    :type lsp_input_detail: YANGBool
    :param lsp_input_detail: **show_lsp_input_info** tuple argument.

    :type lsp_input_extensive: YANGBool
    :param lsp_input_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_input_debug: YANGBool
    :param lsp_input_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_one: YANGBool
    :param lsp_input_one: **show_lsp_input_info** tuple argument.

    :type lsp_input_all: YANGBool
    :param lsp_input_all: **show_lsp_input_info** tuple argument.

    :type lsp_input_more: YANGBool
    :param lsp_input_more: **show_lsp_input_info** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_name_extensive.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_name_extensive.input', u'show_lsp_input_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, show_lsp_input_info=show_lsp_input_info)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_dynamic_bypass_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_dynamic_bypass', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_dynamic_bypass_interface_brief_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_dynamic_bypass_interface_brief', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_interface_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_interface', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_interface_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_interface_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_interface_one_interface_rpc(self, interface_type=None, interface_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: Keyword argument.

        * enumeration restriction: ::

            ['ethernet', 've']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['1..16']

        * pattern restriction: ::

            '((([0-9]|[1][0-6])/([1-9]|[1-9][0-9]|[1-9][0-9]['
            '0-9])(:[1-4])?)|([0-9]([0-9])?([0-9])?([0-9])?))'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_interface_one_interface.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_filtered_rpc(self, ldp_fec_prefix_filtered=None, ldp_fec_prefix_filtered_in=None, ldp_fec_prefix_filtered_out=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_fec_prefix_filtered: YANGBool
    :param ldp_fec_prefix_filtered: Keyword argument.

    :type ldp_fec_prefix_filtered_in: YANGBool
    :param ldp_fec_prefix_filtered_in: Keyword argument.

    :type ldp_fec_prefix_filtered_out: YANGBool
    :param ldp_fec_prefix_filtered_out: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix_filtered.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_prefix_filtered=ldp_fec_prefix_filtered, ldp_fec_prefix_filtered_in=ldp_fec_prefix_filtered_in, ldp_fec_prefix_filtered_out=ldp_fec_prefix_filtered_out)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_prefix_rpc(self, ldp_fec_prefix=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_fec_prefix: unicode
    :param ldp_fec_prefix: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix_prefix.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_prefix=ldp_fec_prefix)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_prefix_filter_rpc(self, ldp_fec_prefix_filter=None, ldp_fec_prefix_filter_string=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_fec_prefix_filter: YANGBool
    :param ldp_fec_prefix_filter: Keyword argument.

    :type ldp_fec_prefix_filter_string: unicode
    :param ldp_fec_prefix_filter_string: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix_prefix_filter.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_prefix_filter=ldp_fec_prefix_filter, ldp_fec_prefix_filter_string=ldp_fec_prefix_filter_string)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_prefix_longer_rpc(self, ldp_fec_prefix=None, ldp_fec_prefix_longer=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_fec_prefix: unicode
    :param ldp_fec_prefix: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'

    :type ldp_fec_prefix_longer: YANGBool
    :param ldp_fec_prefix_longer: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix_prefix_longer.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_prefix=ldp_fec_prefix, ldp_fec_prefix_longer=ldp_fec_prefix_longer)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_summary_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_summary', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_vc_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_vc', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_vc_id_rpc(self, ldp_fec_vc_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_fec_vc_id: long
    :param ldp_fec_vc_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_vc_id.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_vc_id=ldp_fec_vc_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_path_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_path', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_path_one_rpc(self, ldp_path_ip=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_path_ip: unicode
    :param ldp_path_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_path_one.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_path_ip=ldp_path_ip)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_peer_br_rpc(self, ldp_peer_brief=None, ldp_peer_detail=None, ldp_peer_ip=None, ldp_peer_ip_lblspid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_peer_brief: YANGBool
    :param ldp_peer_brief: Keyword argument.

    :type ldp_peer_detail: YANGBool
    :param ldp_peer_detail: Keyword argument.

    :type ldp_peer_ip: unicode
    :param ldp_peer_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type ldp_peer_ip_lblspid: long
    :param ldp_peer_ip_lblspid: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_peer_br.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_peer_brief=ldp_peer_brief, ldp_peer_detail=ldp_peer_detail, ldp_peer_ip=ldp_peer_ip, ldp_peer_ip_lblspid=ldp_peer_ip_lblspid)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_peer_det_rpc(self, ldp_peer_brief=None, ldp_peer_detail=None, ldp_peer_ip=None, ldp_peer_ip_lblspid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_peer_brief: YANGBool
    :param ldp_peer_brief: Keyword argument.

    :type ldp_peer_detail: YANGBool
    :param ldp_peer_detail: Keyword argument.

    :type ldp_peer_ip: unicode
    :param ldp_peer_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type ldp_peer_ip_lblspid: long
    :param ldp_peer_ip_lblspid: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_peer_det.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_peer_brief=ldp_peer_brief, ldp_peer_detail=ldp_peer_detail, ldp_peer_ip=ldp_peer_ip, ldp_peer_ip_lblspid=ldp_peer_ip_lblspid)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_peer_det_rec_rpc(self, ldp_peer_brief=None, ldp_peer_detail=None, ldp_peer_ip=None, ldp_peer_ip_lblspid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_peer_brief: YANGBool
    :param ldp_peer_brief: Keyword argument.

    :type ldp_peer_detail: YANGBool
    :param ldp_peer_detail: Keyword argument.

    :type ldp_peer_ip: unicode
    :param ldp_peer_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type ldp_peer_ip_lblspid: long
    :param ldp_peer_ip_lblspid: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_peer_det_rec.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_peer_brief=ldp_peer_brief, ldp_peer_detail=ldp_peer_detail, ldp_peer_ip=ldp_peer_ip, ldp_peer_ip_lblspid=ldp_peer_ip_lblspid)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_statistics_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_statistics', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_targeted_peer_all_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_targeted_peer_all', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_targeted_peer_one_rpc(self, ldp_targeted_peer_ip=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_targeted_peer_ip: unicode
    :param ldp_targeted_peer_ip: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_targeted_peer_one.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_targeted_peer_ip=ldp_targeted_peer_ip)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_debug_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_debug', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_extensive_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_extensive', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_name_debug_rpc(self, show_lsp_input_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type show_lsp_input_info: lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more
    :param show_lsp_input_info: Keyword argument tuple.

    :type lsp: unicode
    :param lsp: **show_lsp_input_info** tuple argument.

    :type lsp_wide: YANGBool
    :param lsp_wide: **show_lsp_input_info** tuple argument.

    :type lsp_detail: YANGBool
    :param lsp_detail: **show_lsp_input_info** tuple argument.

    :type lsp_extensive: YANGBool
    :param lsp_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_debug: YANGBool
    :param lsp_debug: **show_lsp_input_info** tuple argument.

    :type lsp_name: unicode
    :param lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_name_extensive: YANGBool
    :param lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_name_debug: YANGBool
    :param lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp: unicode
    :param bypass_lsp: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_wide: YANGBool
    :param bypass_lsp_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_detail: YANGBool
    :param bypass_lsp_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_extensive: YANGBool
    :param bypass_lsp_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_debug: YANGBool
    :param bypass_lsp_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name: unicode
    :param bypass_lsp_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_extensive: YANGBool
    :param bypass_lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_debug: YANGBool
    :param bypass_lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static: unicode
    :param bypass_lsp_static: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_wide: YANGBool
    :param bypass_lsp_static_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_detail: YANGBool
    :param bypass_lsp_static_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_extensive: YANGBool
    :param bypass_lsp_static_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_debug: YANGBool
    :param bypass_lsp_static_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name: unicode
    :param bypass_lsp_static_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_extensive: YANGBool
    :param bypass_lsp_static_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_debug: YANGBool
    :param bypass_lsp_static_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic: unicode
    :param bypass_lsp_dynamic: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_wide: YANGBool
    :param bypass_lsp_dynamic_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_detail: YANGBool
    :param bypass_lsp_dynamic_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_extensive: YANGBool
    :param bypass_lsp_dynamic_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_debug: YANGBool
    :param bypass_lsp_dynamic_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name: unicode
    :param bypass_lsp_dynamic_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_extensive: YANGBool
    :param bypass_lsp_dynamic_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_debug: YANGBool
    :param bypass_lsp_dynamic_name_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_lsp_name: unicode
    :param lsp_input_lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_input_bypass: YANGBool
    :param lsp_input_bypass: **show_lsp_input_info** tuple argument.

    :type lsp_input_dynamic: YANGBool
    :param lsp_input_dynamic: **show_lsp_input_info** tuple argument.

    :type lsp_input_brief: YANGBool
    :param lsp_input_brief: **show_lsp_input_info** tuple argument.

    :type lsp_input_wide: YANGBool
    :param lsp_input_wide: **show_lsp_input_info** tuple argument.

    :type lsp_input_detail: YANGBool
    :param lsp_input_detail: **show_lsp_input_info** tuple argument.

    :type lsp_input_extensive: YANGBool
    :param lsp_input_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_input_debug: YANGBool
    :param lsp_input_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_one: YANGBool
    :param lsp_input_one: **show_lsp_input_info** tuple argument.

    :type lsp_input_all: YANGBool
    :param lsp_input_all: **show_lsp_input_info** tuple argument.

    :type lsp_input_more: YANGBool
    :param lsp_input_more: **show_lsp_input_info** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_name_debug.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_name_debug.input', u'show_lsp_input_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, show_lsp_input_info=show_lsp_input_info)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_name_detail_rpc(self, show_lsp_input_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type show_lsp_input_info: lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more
    :param show_lsp_input_info: Keyword argument tuple.

    :type lsp: unicode
    :param lsp: **show_lsp_input_info** tuple argument.

    :type lsp_wide: YANGBool
    :param lsp_wide: **show_lsp_input_info** tuple argument.

    :type lsp_detail: YANGBool
    :param lsp_detail: **show_lsp_input_info** tuple argument.

    :type lsp_extensive: YANGBool
    :param lsp_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_debug: YANGBool
    :param lsp_debug: **show_lsp_input_info** tuple argument.

    :type lsp_name: unicode
    :param lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_name_extensive: YANGBool
    :param lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_name_debug: YANGBool
    :param lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp: unicode
    :param bypass_lsp: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_wide: YANGBool
    :param bypass_lsp_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_detail: YANGBool
    :param bypass_lsp_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_extensive: YANGBool
    :param bypass_lsp_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_debug: YANGBool
    :param bypass_lsp_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name: unicode
    :param bypass_lsp_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_extensive: YANGBool
    :param bypass_lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_debug: YANGBool
    :param bypass_lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static: unicode
    :param bypass_lsp_static: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_wide: YANGBool
    :param bypass_lsp_static_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_detail: YANGBool
    :param bypass_lsp_static_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_extensive: YANGBool
    :param bypass_lsp_static_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_debug: YANGBool
    :param bypass_lsp_static_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name: unicode
    :param bypass_lsp_static_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_extensive: YANGBool
    :param bypass_lsp_static_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_debug: YANGBool
    :param bypass_lsp_static_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic: unicode
    :param bypass_lsp_dynamic: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_wide: YANGBool
    :param bypass_lsp_dynamic_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_detail: YANGBool
    :param bypass_lsp_dynamic_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_extensive: YANGBool
    :param bypass_lsp_dynamic_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_debug: YANGBool
    :param bypass_lsp_dynamic_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name: unicode
    :param bypass_lsp_dynamic_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_extensive: YANGBool
    :param bypass_lsp_dynamic_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_debug: YANGBool
    :param bypass_lsp_dynamic_name_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_lsp_name: unicode
    :param lsp_input_lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_input_bypass: YANGBool
    :param lsp_input_bypass: **show_lsp_input_info** tuple argument.

    :type lsp_input_dynamic: YANGBool
    :param lsp_input_dynamic: **show_lsp_input_info** tuple argument.

    :type lsp_input_brief: YANGBool
    :param lsp_input_brief: **show_lsp_input_info** tuple argument.

    :type lsp_input_wide: YANGBool
    :param lsp_input_wide: **show_lsp_input_info** tuple argument.

    :type lsp_input_detail: YANGBool
    :param lsp_input_detail: **show_lsp_input_info** tuple argument.

    :type lsp_input_extensive: YANGBool
    :param lsp_input_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_input_debug: YANGBool
    :param lsp_input_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_one: YANGBool
    :param lsp_input_one: **show_lsp_input_info** tuple argument.

    :type lsp_input_all: YANGBool
    :param lsp_input_all: **show_lsp_input_info** tuple argument.

    :type lsp_input_more: YANGBool
    :param lsp_input_more: **show_lsp_input_info** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_name_detail.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_name_detail.input', u'show_lsp_input_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, show_lsp_input_info=show_lsp_input_info)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_name_extensive_rpc(self, show_lsp_input_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Child Instance Keyword Argument Tuple(s)**:

    :type show_lsp_input_info: lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more
    :param show_lsp_input_info: Keyword argument tuple.

    :type lsp: unicode
    :param lsp: **show_lsp_input_info** tuple argument.

    :type lsp_wide: YANGBool
    :param lsp_wide: **show_lsp_input_info** tuple argument.

    :type lsp_detail: YANGBool
    :param lsp_detail: **show_lsp_input_info** tuple argument.

    :type lsp_extensive: YANGBool
    :param lsp_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_debug: YANGBool
    :param lsp_debug: **show_lsp_input_info** tuple argument.

    :type lsp_name: unicode
    :param lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_name_extensive: YANGBool
    :param lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_name_debug: YANGBool
    :param lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp: unicode
    :param bypass_lsp: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_wide: YANGBool
    :param bypass_lsp_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_detail: YANGBool
    :param bypass_lsp_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_extensive: YANGBool
    :param bypass_lsp_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_debug: YANGBool
    :param bypass_lsp_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name: unicode
    :param bypass_lsp_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_extensive: YANGBool
    :param bypass_lsp_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_name_debug: YANGBool
    :param bypass_lsp_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static: unicode
    :param bypass_lsp_static: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_wide: YANGBool
    :param bypass_lsp_static_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_detail: YANGBool
    :param bypass_lsp_static_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_extensive: YANGBool
    :param bypass_lsp_static_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_debug: YANGBool
    :param bypass_lsp_static_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name: unicode
    :param bypass_lsp_static_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_extensive: YANGBool
    :param bypass_lsp_static_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_static_name_debug: YANGBool
    :param bypass_lsp_static_name_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic: unicode
    :param bypass_lsp_dynamic: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_wide: YANGBool
    :param bypass_lsp_dynamic_wide: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_detail: YANGBool
    :param bypass_lsp_dynamic_detail: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_extensive: YANGBool
    :param bypass_lsp_dynamic_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_debug: YANGBool
    :param bypass_lsp_dynamic_debug: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name: unicode
    :param bypass_lsp_dynamic_name: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_extensive: YANGBool
    :param bypass_lsp_dynamic_name_extensive: **show_lsp_input_info** tuple argument.

    :type bypass_lsp_dynamic_name_debug: YANGBool
    :param bypass_lsp_dynamic_name_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_lsp_name: unicode
    :param lsp_input_lsp_name: **show_lsp_input_info** tuple argument.

    :type lsp_input_bypass: YANGBool
    :param lsp_input_bypass: **show_lsp_input_info** tuple argument.

    :type lsp_input_dynamic: YANGBool
    :param lsp_input_dynamic: **show_lsp_input_info** tuple argument.

    :type lsp_input_brief: YANGBool
    :param lsp_input_brief: **show_lsp_input_info** tuple argument.

    :type lsp_input_wide: YANGBool
    :param lsp_input_wide: **show_lsp_input_info** tuple argument.

    :type lsp_input_detail: YANGBool
    :param lsp_input_detail: **show_lsp_input_info** tuple argument.

    :type lsp_input_extensive: YANGBool
    :param lsp_input_extensive: **show_lsp_input_info** tuple argument.

    :type lsp_input_debug: YANGBool
    :param lsp_input_debug: **show_lsp_input_info** tuple argument.

    :type lsp_input_one: YANGBool
    :param lsp_input_one: **show_lsp_input_info** tuple argument.

    :type lsp_input_all: YANGBool
    :param lsp_input_all: **show_lsp_input_info** tuple argument.

    :type lsp_input_more: YANGBool
    :param lsp_input_more: **show_lsp_input_info** tuple argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_name_extensive.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_name_extensive.input', u'show_lsp_input_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'lsp, lsp_wide, lsp_detail, lsp_extensive, lsp_debug, lsp_name, lsp_name_extensive, lsp_name_debug, bypass_lsp, bypass_lsp_wide, bypass_lsp_detail, bypass_lsp_extensive, bypass_lsp_debug, bypass_lsp_name, bypass_lsp_name_extensive, bypass_lsp_name_debug, bypass_lsp_static, bypass_lsp_static_wide, bypass_lsp_static_detail, bypass_lsp_static_extensive, bypass_lsp_static_debug, bypass_lsp_static_name, bypass_lsp_static_name_extensive, bypass_lsp_static_name_debug, bypass_lsp_dynamic, bypass_lsp_dynamic_wide, bypass_lsp_dynamic_detail, bypass_lsp_dynamic_extensive, bypass_lsp_dynamic_debug, bypass_lsp_dynamic_name, bypass_lsp_dynamic_name_extensive, bypass_lsp_dynamic_name_debug, lsp_input_lsp_name, lsp_input_bypass, lsp_input_dynamic, lsp_input_brief, lsp_input_wide, lsp_input_detail, lsp_input_extensive, lsp_input_debug, lsp_input_one, lsp_input_all, lsp_input_more'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, show_lsp_input_info=show_lsp_input_info)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_policy_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_policy', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_route_rpc(self, prefix_address_and_len=None, prefix_address=None, subnet_mask=None, longer=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type prefix_address_and_len: unicode
    :param prefix_address_and_len: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'

    :type prefix_address: unicode
    :param prefix_address: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type subnet_mask: unicode
    :param subnet_mask: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type longer: YANGBool
    :param longer: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_route.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, prefix_address_and_len=prefix_address_and_len, prefix_address=prefix_address, subnet_mask=subnet_mask, longer=longer)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_interface_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_interface', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_interface_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_interface_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_interface_one_interface_rpc(self, interface_type=None, interface_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type interface_type: unicode
    :param interface_type: Keyword argument.

        * enumeration restriction: ::

            ['ethernet', 've']

    :type interface_name: unicode
    :param interface_name: The Interface value.

        * length restriction: ::

            ['1..16']

        * pattern restriction: ::

            '((([0-9]|[1][0-6])/([1-9]|[1-9][0-9]|[1-9][0-9]['
            '0-9])(:[1-4])?)|([0-9]([0-9])?([0-9])?([0-9])?))'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_interface_one_interface.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_neighbor_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_neighbor', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_neighbor_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_neighbor_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_neighbor_one_neighbor_rpc(self, mpls_rsvp_neighbor_peer_ip_addr=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type mpls_rsvp_neighbor_peer_ip_addr: unicode
    :param mpls_rsvp_neighbor_peer_ip_addr: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_neighbor_one_neighbor.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_rsvp_neighbor_peer_ip_addr=mpls_rsvp_neighbor_peer_ip_addr)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_detail_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_extensive_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session_extensive', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_name_rpc(self, session_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type session_name: unicode
    :param session_name: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session_name.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, session_name=session_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_wide_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session_wide', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_statistics_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_statistics', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_statistics_ldp_transit_rpc(self, ldp_transit_stats=None, ldp_transit_stats_fec_prefix=None, ldp_transit_stats_fec_prefix_longer=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_transit_stats: YANGBool
    :param ldp_transit_stats: Keyword argument.

    :type ldp_transit_stats_fec_prefix: unicode
    :param ldp_transit_stats_fec_prefix: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type ldp_transit_stats_fec_prefix_longer: YANGBool
    :param ldp_transit_stats_fec_prefix_longer: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_statistics_ldp_transit.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_transit_stats=ldp_transit_stats, ldp_transit_stats_fec_prefix=ldp_transit_stats_fec_prefix, ldp_transit_stats_fec_prefix_longer=ldp_transit_stats_fec_prefix_longer)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_statistics_ldp_tunnel_rpc(self, ldp_tunnel_stats=None, ldp_tunnel_stats_vif=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ldp_tunnel_stats: YANGBool
    :param ldp_tunnel_stats: Keyword argument.

    :type ldp_tunnel_stats_vif: long
    :param ldp_tunnel_stats_vif: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_statistics_ldp_tunnel.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_tunnel_stats=ldp_tunnel_stats, ldp_tunnel_stats_vif=ldp_tunnel_stats_vif)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_statistics_oam_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_statistics_oam', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_summary_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_summary', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_te_path_rpc(self, ipAddr=None, bandwidth=None, cspfCompMode=None, excludeAny=None, hopLimit=None, includeAny=None, includeAll=None, tePathName=None, priority=None, tieBreaking=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type ipAddr: unicode
    :param ipAddr: Keyword argument.

        * pattern restriction: ::

            '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-'
            '5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-'
            '9]|25[0-5])(%[\p{N}\p{L}]+)?'

    :type bandwidth: long
    :param bandwidth: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type cspfCompMode: unicode
    :param cspfCompMode: Keyword argument.

        * enumeration restriction: ::

            ['use-igp-metric', 'use-te-metric']

    :type excludeAny: unicode
    :param excludeAny: Keyword argument.

    :type hopLimit: int
    :param hopLimit: Keyword argument.

        * range restriction: ::

            ['0..255']

    :type includeAny: unicode
    :param includeAny: Keyword argument.

    :type includeAll: unicode
    :param includeAll: Keyword argument.

    :type tePathName: unicode
    :param tePathName: Keyword argument.

    :type priority: int
    :param priority: Keyword argument.

        * range restriction: ::

            ['0..255']

    :type tieBreaking: unicode
    :param tieBreaking: Keyword argument.

        * enumeration restriction: ::

            ['most-fill', 'random', 'least-fill']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_te_path.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ipAddr=ipAddr, bandwidth=bandwidth, cspfCompMode=cspfCompMode, excludeAny=excludeAny, hopLimit=hopLimit, includeAny=includeAny, includeAll=includeAll, tePathName=tePathName, priority=priority, tieBreaking=tieBreaking)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_ntp_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ntp_rpc.show_ntp.input', 'pybind.nos.v6_0_2b.brocade_ntp_rpc.brocade_ntp', 'pybind.nos.v6_0_2b.brocade_ntp_rpc'), ('pybind.nos.v7_0_1a.brocade_ntp_rpc.show_ntp.input', 'pybind.nos.v7_0_1a.brocade_ntp_rpc.brocade_ntp', 'pybind.nos.v7_0_1a.brocade_ntp_rpc'), ('pybind.nos.v7_1_0.brocade_ntp_rpc.show_ntp.input', 'pybind.nos.v7_1_0.brocade_ntp_rpc.brocade_ntp', 'pybind.nos.v7_1_0.brocade_ntp_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ntp_rpc.show_ntp', 'pybind.slxos.v16r_1_00b.brocade_ntp_rpc.brocade_ntp', 'pybind.slxos.v16r_1_00b.brocade_ntp_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_portindex_interface_info_rpc(self, all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type all: YANGBool
    :param all: Keyword argument.

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fabric_service_rpc.show_portindex_interface_info.input', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc'), ('pybind.nos.v7_0_1a.brocade_fabric_service_rpc.show_portindex_interface_info.input', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc'), ('pybind.nos.v7_1_0.brocade_fabric_service_rpc.show_portindex_interface_info.input', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.show_portindex_interface_info.input', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, all=all)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_raslog_rpc(self, rbridge_id=None, number_of_latest_events=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: unicode
    :param rbridge_id: Keyword argument.

        * length restriction: ::

            ['1..3']

    :type number_of_latest_events: long
    :param number_of_latest_events: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_ext_rpc.show_raslog.input', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_ext_rpc.show_raslog.input', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc'), ('pybind.nos.v7_1_0.brocade_ras_ext_rpc.show_raslog.input', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.show_raslog.input', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, number_of_latest_events=number_of_latest_events)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_support_save_status_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: unicode
    :param rbridge_id: Keyword argument.

        * length restriction: ::

            ['1..3']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_ext_rpc.show_support_save_status.input', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_ext_rpc.show_support_save_status.input', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc'), ('pybind.nos.v7_1_0.brocade_ras_ext_rpc.show_support_save_status.input', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.show_support_save_status.input', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_system_info_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: unicode
    :param rbridge_id: Keyword argument.

        * length restriction: ::

            ['1..3']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_ext_rpc.show_system_info.input', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_ext_rpc.show_system_info.input', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc'), ('pybind.nos.v7_1_0.brocade_ras_ext_rpc.show_system_info.input', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.show_system_info.input', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_system_monitor_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: long
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..4294967295']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_system_monitor_ext_rpc.show_system_monitor.input', 'pybind.nos.v6_0_2b.brocade_system_monitor_ext_rpc.brocade_system_monitor_ext', 'pybind.nos.v6_0_2b.brocade_system_monitor_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_system_monitor_ext_rpc.show_system_monitor.input', 'pybind.nos.v7_0_1a.brocade_system_monitor_ext_rpc.brocade_system_monitor_ext', 'pybind.nos.v7_0_1a.brocade_system_monitor_ext_rpc'), ('pybind.nos.v7_1_0.brocade_system_monitor_ext_rpc.show_system_monitor.input', 'pybind.nos.v7_1_0.brocade_system_monitor_ext_rpc.brocade_system_monitor_ext', 'pybind.nos.v7_1_0.brocade_system_monitor_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_system_monitor_ext_rpc.show_system_monitor', 'pybind.slxos.v16r_1_00b.brocade_system_monitor_ext_rpc.brocade_system_monitor_ext', 'pybind.slxos.v16r_1_00b.brocade_system_monitor_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_vcs_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.show_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.show_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.show_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.show_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_zoning_enabled_configuration_rpc(self, zone_name_pattern=None, last_rcvd_zone_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type zone_name_pattern: unicode
    :param zone_name_pattern: <WORD>;;Enabled-Zone-Name

    :type last_rcvd_zone_name: unicode
    :param last_rcvd_zone_name: <WORD>;;Enabled-Zone-Name

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_zone_rpc.show_zoning_enabled_configuration.input', 'pybind.nos.v6_0_2b.brocade_zone_rpc.brocade_zone', 'pybind.nos.v6_0_2b.brocade_zone_rpc'), ('pybind.nos.v7_0_1a.brocade_zone_rpc.show_zoning_enabled_configuration.input', 'pybind.nos.v7_0_1a.brocade_zone_rpc.brocade_zone', 'pybind.nos.v7_0_1a.brocade_zone_rpc'), ('pybind.nos.v7_1_0.brocade_zone_rpc.show_zoning_enabled_configuration.input', 'pybind.nos.v7_1_0.brocade_zone_rpc.brocade_zone', 'pybind.nos.v7_1_0.brocade_zone_rpc'), ('pybind.slxos.v16r_1_00b.brocade_zone_rpc.show_zoning_enabled_configuration.input', 'pybind.slxos.v16r_1_00b.brocade_zone_rpc.brocade_zone', 'pybind.slxos.v16r_1_00b.brocade_zone_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, zone_name_pattern=zone_name_pattern, last_rcvd_zone_name=last_rcvd_zone_name)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def user_session_info_rpc(self, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_aaa_ext_rpc.user_session_info', 'pybind.nos.v6_0_2b.brocade_aaa_ext_rpc.brocade_aaa_ext', 'pybind.nos.v6_0_2b.brocade_aaa_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_aaa_ext_rpc.user_session_info', 'pybind.nos.v7_0_1a.brocade_aaa_ext_rpc.brocade_aaa_ext', 'pybind.nos.v7_0_1a.brocade_aaa_ext_rpc'), ('pybind.nos.v7_1_0.brocade_aaa_ext_rpc.user_session_info', 'pybind.nos.v7_1_0.brocade_aaa_ext_rpc.brocade_aaa_ext', 'pybind.nos.v7_1_0.brocade_aaa_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_aaa_ext_rpc.user_session_info', 'pybind.slxos.v16r_1_00b.brocade_aaa_ext_rpc.brocade_aaa_ext', 'pybind.slxos.v16r_1_00b.brocade_aaa_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def vcs_rbridge_config_rpc(self, vcs_id=None, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type vcs_id: int
    :param vcs_id: Keyword argument.

        * range restriction: ::

            ['0..65535']

    :type rbridge_id: int
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..65535']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.vcs_rbridge_config.input', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.vcs_rbridge_config.input', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.vcs_rbridge_config.input', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.vcs_rbridge_config.input', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, vcs_id=vcs_id, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def vcs_rbridge_context_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

    **Supported Versions**:

        * NOS: 6.0.2b, 7.0.1a, 7.1.0
        * SLXOS: 16r.1.00b    

    **Instance Argument(s)**:

    :type rbridge_id: int
    :param rbridge_id: Keyword argument.

        * range restriction: ::

            ['0..65535']

    :type api_timeout: long or tuple(long, long)
    :param api_timeout: Timeout for connection and response in seconds.  If a tuple is specified, then the first value is for the connection timeout and the second value is for the response timeout.

    :rtype: (*bool, list*)
    :returns: Returns a tuple.

        #. **api_success** (*bool*) - The success or failure of the API.
        #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.

    :raises ValueError: If the argument value does not meet type requirements or value restrictions.
    :raises ConnectionError: If requests module connection or response timeout occurs.
    :raises RestInterfaceError: If requests module does not get a successful response from the rest URI.
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.vcs_rbridge_context.input', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.vcs_rbridge_context.input', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.vcs_rbridge_context.input', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.vcs_rbridge_context.input', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._rpc_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

