def activate_status_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: Please enter 'all' for activating all nodes in the logical-chassis or individual rbridge-ids of the form 1,2,3-6
		:type rbridge_id: (unicode)
		
		.. note::
			* pattern - [0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.activate_status.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.activate_status.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.activate_status.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.activate_status', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc.brocade_firmware', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def bna_config_cmd_rpc(self, src=None, dest=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param src: kwarg.
		:type src: (unicode)

		:param dest: kwarg.
		:type dest: (unicode)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_rpc.bna_config_cmd.input', 'pybind.nos.v6_0_2b.brocade_ras_rpc.brocade_ras', 'pybind.nos.v6_0_2b.brocade_ras_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_rpc.bna_config_cmd.input', 'pybind.nos.v7_0_1a.brocade_ras_rpc.brocade_ras', 'pybind.nos.v7_0_1a.brocade_ras_rpc'), ('pybind.nos.v7_1_0.brocade_ras_rpc.bna_config_cmd.input', 'pybind.nos.v7_1_0.brocade_ras_rpc.brocade_ras', 'pybind.nos.v7_1_0.brocade_ras_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_rpc.bna_config_cmd.input', 'pybind.slxos.v16r_1_00b.brocade_ras_rpc.brocade_ras', 'pybind.slxos.v16r_1_00b.brocade_ras_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, src=src, dest=dest)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def bna_config_cmd_status_rpc(self, session_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param session_id: kwarg.
		:type session_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_rpc.bna_config_cmd_status.input', 'pybind.nos.v6_0_2b.brocade_ras_rpc.brocade_ras', 'pybind.nos.v6_0_2b.brocade_ras_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_rpc.bna_config_cmd_status.input', 'pybind.nos.v7_0_1a.brocade_ras_rpc.brocade_ras', 'pybind.nos.v7_0_1a.brocade_ras_rpc'), ('pybind.nos.v7_1_0.brocade_ras_rpc.bna_config_cmd_status.input', 'pybind.nos.v7_1_0.brocade_ras_rpc.brocade_ras', 'pybind.nos.v7_1_0.brocade_ras_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_rpc.bna_config_cmd_status.input', 'pybind.slxos.v16r_1_00b.brocade_ras_rpc.brocade_ras', 'pybind.slxos.v16r_1_00b.brocade_ras_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, session_id=session_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_auto_bandwidth_sample_history_all_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_auto_bandwidth_sample_history_all', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_auto_bandwidth_sample_history_lsp_rpc(self, lsp_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param lsp_name: kwarg.
		:type lsp_name: (unicode)
		
		.. note::
			* length - [u'1..64']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_auto_bandwidth_sample_history_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, lsp_name=lsp_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_auto_bandwidth_statistics_all_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_auto_bandwidth_statistics_all', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_auto_bandwidth_statistics_lsp_rpc(self, lsp_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param lsp_name: kwarg.
		:type lsp_name: (unicode)
		
		.. note::
			* length - [u'1..64']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_auto_bandwidth_statistics_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, lsp_name=lsp_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_bypass_lsp_rpc(self, mpls_clear_bypass_lsp_name_in=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param mpls_clear_bypass_lsp_name_in: Bypass-lsp Name
		:type mpls_clear_bypass_lsp_name_in: (unicode)
		
		.. note::
			* length - [u'1..64']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_bypass_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_clear_bypass_lsp_name_in=mpls_clear_bypass_lsp_name_in)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_ldp_neighbor_rpc(self, mpls_clear_all_ldp_sessions=None, mpls_clear_one_ldp_sessions=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param mpls_clear_all_ldp_sessions: kwarg.
		:type mpls_clear_all_ldp_sessions: (YANGBool)

		:param mpls_clear_one_ldp_sessions: kwarg.
		:type mpls_clear_one_ldp_sessions: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_ldp_neighbor.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_clear_all_ldp_sessions=mpls_clear_all_ldp_sessions, mpls_clear_one_ldp_sessions=mpls_clear_one_ldp_sessions)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_ldp_statistics_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_ldp_statistics', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_rsvp_statistics_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_rsvp_statistics', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_rsvp_statistics_neighbor_rpc(self, clear_mpls_rsvp_statistics_neighbor_address=None, clear_mpls_rsvp_statistics_neighbor_all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param clear_mpls_rsvp_statistics_neighbor_address: kwarg.
		:type clear_mpls_rsvp_statistics_neighbor_address: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param clear_mpls_rsvp_statistics_neighbor_all: kwarg.
		:type clear_mpls_rsvp_statistics_neighbor_all: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_rsvp_statistics_neighbor.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, clear_mpls_rsvp_statistics_neighbor_address=clear_mpls_rsvp_statistics_neighbor_address, clear_mpls_rsvp_statistics_neighbor_all=clear_mpls_rsvp_statistics_neighbor_all)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_statistics_rpc(self, mpls_clear_statistics_type=None, mpls_clear_statistics_transit_ldp_fec_prefix=None, mpls_clear_statistics_transit_ldp_prefix_address=None, mpls_clear_statistics_transit_ldp_prefix_mask=None, mpls_clear_statistics_transit_label_id=None, mpls_clear_statistics_tunnel_ldp_id=None, mpls_clear_statistics_tunnel_rsvp_bypass=None, mpls_clear_statistics_tunnel_name=None, mpls_clear_statistics_tunnel_dest=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param mpls_clear_statistics_type: kwarg.
		:type mpls_clear_statistics_type: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param mpls_clear_statistics_transit_ldp_fec_prefix: kwarg.
		:type mpls_clear_statistics_transit_ldp_fec_prefix: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))

		:param mpls_clear_statistics_transit_ldp_prefix_address: kwarg.
		:type mpls_clear_statistics_transit_ldp_prefix_address: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param mpls_clear_statistics_transit_ldp_prefix_mask: kwarg.
		:type mpls_clear_statistics_transit_ldp_prefix_mask: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param mpls_clear_statistics_transit_label_id: kwarg.
		:type mpls_clear_statistics_transit_label_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param mpls_clear_statistics_tunnel_ldp_id: kwarg.
		:type mpls_clear_statistics_tunnel_ldp_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param mpls_clear_statistics_tunnel_rsvp_bypass: kwarg.
		:type mpls_clear_statistics_tunnel_rsvp_bypass: (int)
		
		.. note::
			* range - ['0..255']

		:param mpls_clear_statistics_tunnel_name: kwarg.
		:type mpls_clear_statistics_tunnel_name: (unicode)

		:param mpls_clear_statistics_tunnel_dest: kwarg.
		:type mpls_clear_statistics_tunnel_dest: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_statistics.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_clear_statistics_type=mpls_clear_statistics_type, mpls_clear_statistics_transit_ldp_fec_prefix=mpls_clear_statistics_transit_ldp_fec_prefix, mpls_clear_statistics_transit_ldp_prefix_address=mpls_clear_statistics_transit_ldp_prefix_address, mpls_clear_statistics_transit_ldp_prefix_mask=mpls_clear_statistics_transit_ldp_prefix_mask, mpls_clear_statistics_transit_label_id=mpls_clear_statistics_transit_label_id, mpls_clear_statistics_tunnel_ldp_id=mpls_clear_statistics_tunnel_ldp_id, mpls_clear_statistics_tunnel_rsvp_bypass=mpls_clear_statistics_tunnel_rsvp_bypass, mpls_clear_statistics_tunnel_name=mpls_clear_statistics_tunnel_name, mpls_clear_statistics_tunnel_dest=mpls_clear_statistics_tunnel_dest)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_statistics_ldp_transit_rpc(self, clear_statistics_ldp_transit_fec_prefix=None, clear_statistics_ldp_transit_fec_prefix_address=None, clear_statistics_ldp_transit_fec_prefix_mask=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param clear_statistics_ldp_transit_fec_prefix: kwarg.
		:type clear_statistics_ldp_transit_fec_prefix: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))

		:param clear_statistics_ldp_transit_fec_prefix_address: kwarg.
		:type clear_statistics_ldp_transit_fec_prefix_address: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param clear_statistics_ldp_transit_fec_prefix_mask: kwarg.
		:type clear_statistics_ldp_transit_fec_prefix_mask: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_statistics_ldp_transit.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, clear_statistics_ldp_transit_fec_prefix=clear_statistics_ldp_transit_fec_prefix, clear_statistics_ldp_transit_fec_prefix_address=clear_statistics_ldp_transit_fec_prefix_address, clear_statistics_ldp_transit_fec_prefix_mask=clear_statistics_ldp_transit_fec_prefix_mask)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def clear_mpls_statistics_ldp_tunnel_rpc(self, clear_statistics_ldp_tunnel_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param clear_statistics_ldp_tunnel_id: kwarg.
		:type clear_statistics_ldp_tunnel_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.clear_mpls_statistics_ldp_tunnel.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, clear_statistics_ldp_tunnel_id=clear_statistics_ldp_tunnel_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def dad_status_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.dad_status', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.dad_status', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.dad_status', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.dad_status', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc.brocade_firmware', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def fcoe_get_interface_rpc(self, fcoe_intf_name=None, fcoe_intf_rbridge_id=None, fcoe_intf_include_stats=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param fcoe_intf_name: kwarg.
		:type fcoe_intf_name: (unicode)
		
		.. note::
			* length - [u'3..32']

		:param fcoe_intf_rbridge_id: kwarg.
		:type fcoe_intf_rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param fcoe_intf_include_stats: kwarg.
		:type fcoe_intf_include_stats: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc.fcoe_get_interface.input', 'pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc.fcoe_get_interface.input', 'pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc'), ('pybind.nos.v7_1_0.brocade_fcoe_ext_rpc.fcoe_get_interface.input', 'pybind.nos.v7_1_0.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v7_1_0.brocade_fcoe_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc.fcoe_get_interface.input', 'pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, fcoe_intf_name=fcoe_intf_name, fcoe_intf_rbridge_id=fcoe_intf_rbridge_id, fcoe_intf_include_stats=fcoe_intf_include_stats)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def fcoe_get_login_rpc(self, fcoe_login_interface=None, fcoe_login_vfid=None, fcoe_login_vlan=None, fcoe_login_rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param fcoe_login_interface: kwarg.
		:type fcoe_login_interface: (unicode)
		
		.. note::
			* length - [u'3..32']

		:param fcoe_login_vfid: kwarg.
		:type fcoe_login_vfid: (long)
		
		.. note::
			* range - ['-2147483648..2147483647']

		:param fcoe_login_vlan: kwarg.
		:type fcoe_login_vlan: (long)
		
		.. note::
			* range - ['-2147483648..2147483647']

		:param fcoe_login_rbridge_id: kwarg.
		:type fcoe_login_rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc.fcoe_get_login.input', 'pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v6_0_2b.brocade_fcoe_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc.fcoe_get_login.input', 'pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v7_0_1a.brocade_fcoe_ext_rpc'), ('pybind.nos.v7_1_0.brocade_fcoe_ext_rpc.fcoe_get_login.input', 'pybind.nos.v7_1_0.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.nos.v7_1_0.brocade_fcoe_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc.fcoe_get_login.input', 'pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc.brocade_fcoe_ext', 'pybind.slxos.v16r_1_00b.brocade_fcoe_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, fcoe_login_interface=fcoe_login_interface, fcoe_login_vfid=fcoe_login_vfid, fcoe_login_vlan=fcoe_login_vlan, fcoe_login_rbridge_id=fcoe_login_rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def firmware_download_rpc(self, rbridge_id=None, auto_activate=None, coldboot=None, scp=None, usb=None, ftp=None, sftp=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: Please enter 'all' for activating all nodes in the logical-chassis or individual rbridge-ids of the form 1,2,3-6
		:type rbridge_id: (unicode)
		
		.. note::
			* pattern - [0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*

		:param auto_activate: To activate new firmware on all nodes
		:type auto_activate: (YANGBool)

		:param coldboot: Perform non ISSU firmware download.
		:type coldboot: (YANGBool)

	**Child Instance Keyword Arg Tuple(s)**:
		:param scp: kwarg tuple.
		:type scp: (user, password, host, directory, file).

		:param user: Username
		:type user: (unicode)

		:param password: Password
		:type password: (unicode)

		:param host: Host ipv4/ipv6 address
		:type host: (unicode)

		:param directory: Directory
		:type directory: (unicode)

		:param file: Package release file, example - release.plist
		:type file: (unicode)
		:param usb: kwarg tuple.
		:type usb: (directory).

		:param directory: Directory
		:type directory: (unicode)
		:param ftp: kwarg tuple.
		:type ftp: (user, password, host, directory, file).

		:param user: Username
		:type user: (unicode)

		:param password: Password
		:type password: (unicode)

		:param host: Host ipv4/ipv6 address
		:type host: (unicode)

		:param directory: Directory
		:type directory: (unicode)

		:param file: Package release file, example - release.plist
		:type file: (unicode)
		:param sftp: kwarg tuple.
		:type sftp: (user, password, host, directory, file, port, host_key_check).

		:param user: Username
		:type user: (unicode)

		:param password: Password
		:type password: (unicode)

		:param host: Host ipv4/ipv6 address
		:type host: (unicode)

		:param directory: Directory
		:type directory: (unicode)

		:param file: Package release file, example - release.plist
		:type file: (unicode)

		:param port: Server port number (default 22)
		:type port: (long)
		
		.. note::
			* range - ['-2147483648..2147483647']

		:param host_key_check: Enable strict host key check
		:type host_key_check: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc.brocade_firmware', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc')]
    composed_child_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', u'scp'), ('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', u'usb'), ('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', u'ftp'), ('pybind.nos.v6_0_2b.brocade_firmware_rpc.firmware_download.input', u'sftp'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', u'sftp'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', u'scp'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', u'ftp'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.firmware_download.input', u'usb'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', u'scp'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', u'sftp'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', u'ftp'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.firmware_download.input', u'usb'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', u'ftp'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', u'sftp'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', u'usb'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.firmware_download.input', u'scp')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'user, password, host, directory, file'}, {'leafval': 'directory'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'user, password, host, directory, file, port, host_key_check'}, {'leafval': 'user, password, host, directory, file, port, host_key_check'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'directory'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'user, password, host, directory, file, port, host_key_check'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'directory'}, {'leafval': 'user, password, host, directory, file'}, {'leafval': 'user, password, host, directory, file, port, host_key_check'}, {'leafval': 'directory'}, {'leafval': 'user, password, host, directory, file'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, auto_activate=auto_activate, coldboot=coldboot, scp=scp, usb=usb, ftp=ftp, sftp=sftp)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def fwdl_status_rpc(self, fwdl_tid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param fwdl_tid: kwarg.
		:type fwdl_tid: (long)
		
		.. note::
			* range - ['-2147483648..2147483647']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.fwdl_status.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.fwdl_status.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.fwdl_status.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_rpc.fwdl_status.input', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc.brocade_firmware', 'pybind.slxos.v16r_1_00b.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, fwdl_tid=fwdl_tid)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_arp_rpc(self, interface_type=None, interface_name=None, dynamic=None, static=None, ip_address=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param dynamic: kwarg.
		:type dynamic: (YANGBool)

		:param static: kwarg.
		:type static: (YANGBool)

		:param ip_address: kwarg.
		:type ip_address: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_arp_rpc.get_arp.input', 'pybind.nos.v6_0_2b.brocade_arp_rpc.brocade_arp', 'pybind.nos.v6_0_2b.brocade_arp_rpc'), ('pybind.nos.v7_0_1a.brocade_arp_rpc.get_arp.input', 'pybind.nos.v7_0_1a.brocade_arp_rpc.brocade_arp', 'pybind.nos.v7_0_1a.brocade_arp_rpc'), ('pybind.nos.v7_1_0.brocade_arp_rpc.get_arp.input', 'pybind.nos.v7_1_0.brocade_arp_rpc.brocade_arp', 'pybind.nos.v7_1_0.brocade_arp_rpc'), ('pybind.slxos.v16r_1_00b.brocade_arp_rpc.get_arp.input', 'pybind.slxos.v16r_1_00b.brocade_arp_rpc.brocade_arp', 'pybind.slxos.v16r_1_00b.brocade_arp_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, dynamic=dynamic, static=static, ip_address=ip_address)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_contained_in_id_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_entity_rpc.get_contained_in_ID', 'pybind.nos.v6_0_2b.brocade_entity_rpc.brocade_entity', 'pybind.nos.v6_0_2b.brocade_entity_rpc'), ('pybind.nos.v7_0_1a.brocade_entity_rpc.get_contained_in_ID', 'pybind.nos.v7_0_1a.brocade_entity_rpc.brocade_entity', 'pybind.nos.v7_0_1a.brocade_entity_rpc'), ('pybind.nos.v7_1_0.brocade_entity_rpc.get_contained_in_ID', 'pybind.nos.v7_1_0.brocade_entity_rpc.brocade_entity', 'pybind.nos.v7_1_0.brocade_entity_rpc'), ('pybind.slxos.v16r_1_00b.brocade_entity_rpc.get_contained_in_ID', 'pybind.slxos.v16r_1_00b.brocade_entity_rpc.brocade_entity', 'pybind.slxos.v16r_1_00b.brocade_entity_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_flexports_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_hardware_rpc.get_flexports', 'pybind.nos.v6_0_2b.brocade_hardware_rpc.brocade_hardware', 'pybind.nos.v6_0_2b.brocade_hardware_rpc'), ('pybind.nos.v7_0_1a.brocade_hardware_rpc.get_flexports', 'pybind.nos.v7_0_1a.brocade_hardware_rpc.brocade_hardware', 'pybind.nos.v7_0_1a.brocade_hardware_rpc'), ('pybind.nos.v7_1_0.brocade_hardware_rpc.get_flexports', 'pybind.nos.v7_1_0.brocade_hardware_rpc.brocade_hardware', 'pybind.nos.v7_1_0.brocade_hardware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_interface_detail_rpc(self, interface_type=None, interface_name=None, last_rcvd_interface=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

	**Child Instance Keyword Arg Tuple(s)**:
		:param last_rcvd_interface: kwarg tuple.
		:type last_rcvd_interface: (interface_type, interface_name).

		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_interface_detail.input', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_interface_detail.input', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_interface_detail.input', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_interface_detail.input', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = [('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_interface_detail.input', u'last_rcvd_interface'), ('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_interface_detail.input', u'last_rcvd_interface'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_interface_detail.input', u'last_rcvd_interface'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_interface_detail.input', u'last_rcvd_interface')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, last_rcvd_interface=last_rcvd_interface)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_interface_switchport_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_interface_switchport', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_interface_switchport', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_interface_switchport', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_interface_switchport', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_ip_interface_rpc(self, interface_type=None, interface_name=None, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_ip_interface.input', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_ip_interface.input', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_ip_interface.input', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_ip_interface.input', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_last_config_update_time_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.get_last_config_update_time', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.get_last_config_update_time', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.get_last_config_update_time', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.get_last_config_update_time', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_lldp_neighbor_detail_rpc(self, interface_type=None, interface_name=None, last_rcvd_ifindex=None, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param last_rcvd_ifindex: kwarg.
		:type last_rcvd_ifindex: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_lldp_ext_rpc.get_lldp_neighbor_detail.input', 'pybind.nos.v6_0_2b.brocade_lldp_ext_rpc.brocade_lldp_ext', 'pybind.nos.v6_0_2b.brocade_lldp_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_lldp_ext_rpc.get_lldp_neighbor_detail.input', 'pybind.nos.v7_0_1a.brocade_lldp_ext_rpc.brocade_lldp_ext', 'pybind.nos.v7_0_1a.brocade_lldp_ext_rpc'), ('pybind.nos.v7_1_0.brocade_lldp_ext_rpc.get_lldp_neighbor_detail.input', 'pybind.nos.v7_1_0.brocade_lldp_ext_rpc.brocade_lldp_ext', 'pybind.nos.v7_1_0.brocade_lldp_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_lldp_ext_rpc.get_lldp_neighbor_detail.input', 'pybind.slxos.v16r_1_00b.brocade_lldp_ext_rpc.brocade_lldp_ext', 'pybind.slxos.v16r_1_00b.brocade_lldp_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, last_rcvd_ifindex=last_rcvd_ifindex, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mac_acl_for_intf_rpc(self, interface_type=None, interface_name=None, direction=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param direction: kwarg.
		:type direction: (unicode)
		
		.. note::
			* enum - [u'all', u'in', u'out']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_mac_access_list_rpc.get_mac_acl_for_intf.input', 'pybind.nos.v6_0_2b.brocade_mac_access_list_rpc.brocade_mac_access_list', 'pybind.nos.v6_0_2b.brocade_mac_access_list_rpc'), ('pybind.nos.v7_0_1a.brocade_mac_access_list_rpc.get_mac_acl_for_intf.input', 'pybind.nos.v7_0_1a.brocade_mac_access_list_rpc.brocade_mac_access_list', 'pybind.nos.v7_0_1a.brocade_mac_access_list_rpc'), ('pybind.nos.v7_1_0.brocade_mac_access_list_rpc.get_mac_acl_for_intf.input', 'pybind.nos.v7_1_0.brocade_mac_access_list_rpc.brocade_mac_access_list', 'pybind.nos.v7_1_0.brocade_mac_access_list_rpc'), ('pybind.slxos.v16r_1_00b.brocade_mac_access_list_rpc.get_mac_acl_for_intf.input', 'pybind.slxos.v16r_1_00b.brocade_mac_access_list_rpc.brocade_mac_access_list', 'pybind.slxos.v16r_1_00b.brocade_mac_access_list_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, direction=direction)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mac_address_table_rpc(self, mac_address=None, last_mac_address_details=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param mac_address: kwarg.
		:type mac_address: (unicode)
		
		.. note::
			* pattern - [0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}

	**Child Instance Keyword Arg Tuple(s)**:
		:param last_mac_address_details: kwarg tuple.
		:type last_mac_address_details: (last_mac_address, last_vlan_id, last_mac_type).

		:param last_mac_address: tuple arg.
		:type last_mac_address: (unicode)
		
		.. note::
			* pattern - [0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}

		:param last_vlan_id: tuple arg.
		:type last_vlan_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param last_mac_type: tuple arg.
		:type last_mac_type: (unicode)
		
		.. note::
			* enum - [u'fpma', u'static', u'dynamic', u'system']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_mac_address_table_rpc.get_mac_address_table.input', 'pybind.nos.v6_0_2b.brocade_mac_address_table_rpc.brocade_mac_address_table', 'pybind.nos.v6_0_2b.brocade_mac_address_table_rpc'), ('pybind.nos.v7_0_1a.brocade_mac_address_table_rpc.get_mac_address_table.input', 'pybind.nos.v7_0_1a.brocade_mac_address_table_rpc.brocade_mac_address_table', 'pybind.nos.v7_0_1a.brocade_mac_address_table_rpc'), ('pybind.nos.v7_1_0.brocade_mac_address_table_rpc.get_mac_address_table.input', 'pybind.nos.v7_1_0.brocade_mac_address_table_rpc.brocade_mac_address_table', 'pybind.nos.v7_1_0.brocade_mac_address_table_rpc'), ('pybind.slxos.v16r_1_00b.brocade_mac_address_table_rpc.get_mac_address_table.input', 'pybind.slxos.v16r_1_00b.brocade_mac_address_table_rpc.brocade_mac_address_table', 'pybind.slxos.v16r_1_00b.brocade_mac_address_table_rpc')]
    composed_child_list = [('pybind.nos.v7_0_1a.brocade_mac_address_table_rpc.get_mac_address_table.input', u'last_mac_address_details'), ('pybind.nos.v6_0_2b.brocade_mac_address_table_rpc.get_mac_address_table.input', u'last_mac_address_details'), ('pybind.slxos.v16r_1_00b.brocade_mac_address_table_rpc.get_mac_address_table.input', u'last_mac_address_details'), ('pybind.nos.v7_1_0.brocade_mac_address_table_rpc.get_mac_address_table.input', u'last_mac_address_details'), ('pybind.nos.v7_1_0.brocade_mac_address_table_rpc.get_mac_address_table.input', u'forwarding_interface')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'last_mac_address, last_vlan_id, last_mac_type'}, {'leafval': 'last_mac_address, last_vlan_id, last_mac_type'}, {'leafval': 'last_mac_address, last_vlan_id, last_mac_type'}, {'leafval': 'last_mac_address, last_vlan_id, last_mac_type'}, {'leafval': 'interface_type, interface_name'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mac_address=mac_address, last_mac_address_details=last_mac_address_details)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_media_detail_rpc(self, interface_type=None, interface_name=None, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_media_detail.input', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_media_detail.input', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_media_detail.input', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_media_detail.input', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_autobw_template_brief_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_autobw_template_brief', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_autobw_template_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_autobw_template_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_neighbor_brief_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_neighbor_brief', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_neighbor_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_neighbor_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_session_brief_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_session_brief', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_mpls_ldp_session_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.get_mpls_ldp_session_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_nameserver_detail_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: <NUMBER:1-239>;;rbridge-id of switch to
retrieve info from
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_nameserver_rpc.get_nameserver_detail.input', 'pybind.nos.v6_0_2b.brocade_nameserver_rpc.brocade_nameserver', 'pybind.nos.v6_0_2b.brocade_nameserver_rpc'), ('pybind.nos.v7_0_1a.brocade_nameserver_rpc.get_nameserver_detail.input', 'pybind.nos.v7_0_1a.brocade_nameserver_rpc.brocade_nameserver', 'pybind.nos.v7_0_1a.brocade_nameserver_rpc'), ('pybind.nos.v7_1_0.brocade_nameserver_rpc.get_nameserver_detail.input', 'pybind.nos.v7_1_0.brocade_nameserver_rpc.brocade_nameserver', 'pybind.nos.v7_1_0.brocade_nameserver_rpc'), ('pybind.slxos.v16r_1_00b.brocade_nameserver_rpc.get_nameserver_detail.input', 'pybind.slxos.v16r_1_00b.brocade_nameserver_rpc.brocade_nameserver', 'pybind.slxos.v16r_1_00b.brocade_nameserver_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_netconf_client_capabilities_rpc(self, session_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param session_id: kwarg.
		:type session_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_netconf_ext_rpc.get_netconf_client_capabilities.input', 'pybind.nos.v6_0_2b.brocade_netconf_ext_rpc.brocade_netconf_ext', 'pybind.nos.v6_0_2b.brocade_netconf_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_netconf_ext_rpc.get_netconf_client_capabilities.input', 'pybind.nos.v7_0_1a.brocade_netconf_ext_rpc.brocade_netconf_ext', 'pybind.nos.v7_0_1a.brocade_netconf_ext_rpc'), ('pybind.nos.v7_1_0.brocade_netconf_ext_rpc.get_netconf_client_capabilities.input', 'pybind.nos.v7_1_0.brocade_netconf_ext_rpc.brocade_netconf_ext', 'pybind.nos.v7_1_0.brocade_netconf_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_netconf_ext_rpc.get_netconf_client_capabilities.input', 'pybind.slxos.v16r_1_00b.brocade_netconf_ext_rpc.brocade_netconf_ext', 'pybind.slxos.v16r_1_00b.brocade_netconf_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, session_id=session_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_port_channel_detail_rpc(self, aggregator_id=None, last_aggregator_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param aggregator_id: kwarg.
		:type aggregator_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param last_aggregator_id: kwarg.
		:type last_aggregator_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_lag_rpc.get_port_channel_detail.input', 'pybind.nos.v6_0_2b.brocade_lag_rpc.brocade_lag', 'pybind.nos.v6_0_2b.brocade_lag_rpc'), ('pybind.nos.v7_0_1a.brocade_lag_rpc.get_port_channel_detail.input', 'pybind.nos.v7_0_1a.brocade_lag_rpc.brocade_lag', 'pybind.nos.v7_0_1a.brocade_lag_rpc'), ('pybind.nos.v7_1_0.brocade_lag_rpc.get_port_channel_detail.input', 'pybind.nos.v7_1_0.brocade_lag_rpc.brocade_lag', 'pybind.nos.v7_1_0.brocade_lag_rpc'), ('pybind.slxos.v16r_1_00b.brocade_lag_rpc.get_port_channel_detail.input', 'pybind.slxos.v16r_1_00b.brocade_lag_rpc.brocade_lag', 'pybind.slxos.v16r_1_00b.brocade_lag_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, aggregator_id=aggregator_id, last_aggregator_id=last_aggregator_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_port_profile_for_intf_rpc(self, rbridge_id=None, interface_type=None, interface_name=None, last_received_interface_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

	**Child Instance Keyword Arg Tuple(s)**:
		:param last_received_interface_info: kwarg tuple.
		:type last_received_interface_info: (interface_type, interface_name).

		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', 'pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', 'pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc'), ('pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', 'pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v7_1_0.brocade_port_profile_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', 'pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc')]
    composed_child_list = [('pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', u'last_received_interface_info'), ('pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', u'last_received_interface_info'), ('pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', u'last_received_interface_info'), ('pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.get_port_profile_for_intf.input', u'last_received_interface_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}, {'leafval': 'interface_type, interface_name'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, interface_type=interface_type, interface_name=interface_name, last_received_interface_info=last_received_interface_info)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_port_profile_status_rpc(self, rbridge_id=None, port_profile_name=None, port_profile_status=None, last_received_port_profile_info=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param port_profile_name: kwarg.
		:type port_profile_name: (unicode)
		
		.. note::
			* pattern - [a-zA-Z]{1}([-a-zA-Z0-9\.\\\\@#\+\*\(\)=\{~\}%<>=$_\[\]\|]{0,63})

		:param port_profile_status: kwarg.
		:type port_profile_status: (unicode)
		
		.. note::
			* enum - [u'applied', u'activated', u'associated']

	**Child Instance Keyword Arg Tuple(s)**:
		:param last_received_port_profile_info: kwarg tuple.
		:type last_received_port_profile_info: (profile_name, profile_mac).

		:param profile_name: tuple arg.
		:type profile_name: (unicode)
		
		.. note::
			* pattern - [a-zA-Z]{1}([-a-zA-Z0-9\.\\\\@#\+\*\(\)=\{~\}%<>=$_\[\]\|]{0,63})

		:param profile_mac: tuple arg.
		:type profile_mac: (unicode)
		
		.. note::
			* pattern - [0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.get_port_profile_status.input', 'pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.get_port_profile_status.input', 'pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc'), ('pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.get_port_profile_status.input', 'pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.nos.v7_1_0.brocade_port_profile_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.get_port_profile_status.input', 'pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.brocade_port_profile_ext', 'pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc')]
    composed_child_list = [('pybind.nos.v6_0_2b.brocade_port_profile_ext_rpc.get_port_profile_status.input', u'last_received_port_profile_info'), ('pybind.slxos.v16r_1_00b.brocade_port_profile_ext_rpc.get_port_profile_status.input', u'last_received_port_profile_info'), ('pybind.nos.v7_0_1a.brocade_port_profile_ext_rpc.get_port_profile_status.input', u'last_received_port_profile_info'), ('pybind.nos.v7_1_0.brocade_port_profile_ext_rpc.get_port_profile_status.input', u'last_received_port_profile_info')]
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = [{'leafval': 'profile_name, profile_mac'}, {'leafval': 'profile_name, profile_mac'}, {'leafval': 'profile_name, profile_mac'}, {'leafval': 'profile_name, profile_mac'}]
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, port_profile_name=port_profile_name, port_profile_status=port_profile_status, last_received_port_profile_info=last_received_port_profile_info)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_portchannel_info_by_intf_rpc(self, interface_type=None, interface_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'l2vlan', u'gigabitethernet', u'hundredgigabitethernet', u'loopback', u'fortygigabitethernet', u'unknown', u'fibrechannel', u'port-channel', u'tengigabitethernet']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_lag_rpc.get_portchannel_info_by_intf.input', 'pybind.nos.v6_0_2b.brocade_lag_rpc.brocade_lag', 'pybind.nos.v6_0_2b.brocade_lag_rpc'), ('pybind.nos.v7_0_1a.brocade_lag_rpc.get_portchannel_info_by_intf.input', 'pybind.nos.v7_0_1a.brocade_lag_rpc.brocade_lag', 'pybind.nos.v7_0_1a.brocade_lag_rpc'), ('pybind.nos.v7_1_0.brocade_lag_rpc.get_portchannel_info_by_intf.input', 'pybind.nos.v7_1_0.brocade_lag_rpc.brocade_lag', 'pybind.nos.v7_1_0.brocade_lag_rpc'), ('pybind.slxos.v16r_1_00b.brocade_lag_rpc.get_portchannel_info_by_intf.input', 'pybind.slxos.v16r_1_00b.brocade_lag_rpc.brocade_lag', 'pybind.slxos.v16r_1_00b.brocade_lag_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_show_cfm_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_dot1ag_rpc.get_show_cfm', 'pybind.slxos.v16r_1_00b.brocade_dot1ag_rpc.brocade_dot1ag', 'pybind.slxos.v16r_1_00b.brocade_dot1ag_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_system_uptime_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_system_rpc.get_system_uptime.input', 'pybind.nos.v6_0_2b.brocade_system_rpc.brocade_system', 'pybind.nos.v6_0_2b.brocade_system_rpc'), ('pybind.nos.v7_0_1a.brocade_system_rpc.get_system_uptime.input', 'pybind.nos.v7_0_1a.brocade_system_rpc.brocade_system', 'pybind.nos.v7_0_1a.brocade_system_rpc'), ('pybind.nos.v7_1_0.brocade_system_rpc.get_system_uptime.input', 'pybind.nos.v7_1_0.brocade_system_rpc.brocade_system', 'pybind.nos.v7_1_0.brocade_system_rpc'), ('pybind.slxos.v16r_1_00b.brocade_system_rpc.get_system_uptime.input', 'pybind.slxos.v16r_1_00b.brocade_system_rpc.brocade_system', 'pybind.slxos.v16r_1_00b.brocade_system_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_tunnel_info_rpc(self, page_cursor=None, id=None, mode=None, gw_name=None, src_ip=None, dest_ip=None, config_src=None, site_name=None, admin_state=None, oper_state=None, bfd_state=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param page_cursor: kwarg.
		:type page_cursor: (unicode)

		:param id: kwarg.
		:type id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param mode: kwarg.
		:type mode: (unicode)
		
		.. note::
			* enum - [u'vxlan']

		:param gw_name: kwarg.
		:type gw_name: (unicode)
		
		.. note::
			* pattern - [-_a-zA-Z0-9]{1,32}

		:param src_ip: kwarg.
		:type src_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param dest_ip: kwarg.
		:type dest_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param config_src: kwarg.
		:type config_src: (unicode)
		
		.. note::
			* enum - [u'bgp-evpn', u'vtep-controller', u'site-config']

		:param site_name: kwarg.
		:type site_name: (unicode)
		
		.. note::
			* pattern - [-_a-zA-Z0-9]{1,63}

		:param admin_state: kwarg.
		:type admin_state: (unicode)
		
		.. note::
			* enum - [u'down', u'up']

		:param oper_state: kwarg.
		:type oper_state: (unicode)
		
		.. note::
			* enum - [u'down', u'up']

		:param bfd_state: kwarg.
		:type bfd_state: (unicode)
		
		.. note::
			* enum - [u'down', u'up']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc.get_tunnel_info.input', 'pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc.brocade_tunnels_ext', 'pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc'), ('pybind.nos.v7_1_0.brocade_tunnels_ext_rpc.get_tunnel_info.input', 'pybind.nos.v7_1_0.brocade_tunnels_ext_rpc.brocade_tunnels_ext', 'pybind.nos.v7_1_0.brocade_tunnels_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, page_cursor=page_cursor, id=id, mode=mode, gw_name=gw_name, src_ip=src_ip, dest_ip=dest_ip, config_src=config_src, site_name=site_name, admin_state=admin_state, oper_state=oper_state, bfd_state=bfd_state)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_tunnel_statistics_rpc(self, page_cursor=None, id=None, mode=None, gw_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param page_cursor: kwarg.
		:type page_cursor: (unicode)

		:param id: kwarg.
		:type id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param mode: kwarg.
		:type mode: (unicode)
		
		.. note::
			* enum - [u'vxlan']

		:param gw_name: kwarg.
		:type gw_name: (unicode)
		
		.. note::
			* pattern - [-_a-zA-Z0-9]{1,32}

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc.get_tunnel_statistics.input', 'pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc.brocade_tunnels_ext', 'pybind.nos.v7_0_1a.brocade_tunnels_ext_rpc'), ('pybind.nos.v7_1_0.brocade_tunnels_ext_rpc.get_tunnel_statistics.input', 'pybind.nos.v7_1_0.brocade_tunnels_ext_rpc.brocade_tunnels_ext', 'pybind.nos.v7_1_0.brocade_tunnels_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, page_cursor=page_cursor, id=id, mode=mode, gw_name=gw_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vcs_details_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.get_vcs_details', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.get_vcs_details', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.get_vcs_details', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.get_vcs_details', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vlan_brief_rpc(self, vlan_id=None, last_rcvd_vlan_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param vlan_id: kwarg.
		:type vlan_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param last_rcvd_vlan_id: kwarg.
		:type last_rcvd_vlan_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_interface_ext_rpc.get_vlan_brief.input', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v6_0_2b.brocade_interface_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_interface_ext_rpc.get_vlan_brief.input', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_0_1a.brocade_interface_ext_rpc'), ('pybind.nos.v7_1_0.brocade_interface_ext_rpc.get_vlan_brief.input', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.nos.v7_1_0.brocade_interface_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.get_vlan_brief.input', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc.brocade_interface_ext', 'pybind.slxos.v16r_1_00b.brocade_interface_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, vlan_id=vlan_id, last_rcvd_vlan_id=last_rcvd_vlan_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vmpolicy_macaddr_rpc(self, mac=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param mac: kwarg.
		:type mac: (unicode)
		
		.. note::
			* pattern - [0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}

		:param vcenter: kwarg.
		:type vcenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param datacenter: kwarg.
		:type datacenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param last_rcvd_instance: kwarg.
		:type last_rcvd_instance: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vmpolicy_macaddr.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vmpolicy_macaddr.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vmpolicy_macaddr.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vmpolicy_macaddr.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mac=mac, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_dvpgs_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param name: kwarg.
		:type name: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param vcenter: kwarg.
		:type vcenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param datacenter: kwarg.
		:type datacenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param last_rcvd_instance: kwarg.
		:type last_rcvd_instance: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_dvpgs.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_dvpgs.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_dvpgs.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_dvpgs.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_dvs_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param name: kwarg.
		:type name: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param vcenter: kwarg.
		:type vcenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param datacenter: kwarg.
		:type datacenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param last_rcvd_instance: kwarg.
		:type last_rcvd_instance: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_dvs.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_dvs.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_dvs.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_dvs.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_hosts_rpc(self, vcenter=None, datacenter=None, name=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param vcenter: kwarg.
		:type vcenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param datacenter: kwarg.
		:type datacenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param name: kwarg.
		:type name: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param last_rcvd_instance: kwarg.
		:type last_rcvd_instance: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_hosts.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_hosts.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_hosts.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_hosts.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, vcenter=vcenter, datacenter=datacenter, name=name, last_rcvd_instance=last_rcvd_instance)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_portgroups_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param name: kwarg.
		:type name: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param vcenter: kwarg.
		:type vcenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param datacenter: kwarg.
		:type datacenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param last_rcvd_instance: kwarg.
		:type last_rcvd_instance: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_portgroups.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_portgroups.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_portgroups.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_portgroups.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_vms_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param name: kwarg.
		:type name: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param vcenter: kwarg.
		:type vcenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param datacenter: kwarg.
		:type datacenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param last_rcvd_instance: kwarg.
		:type last_rcvd_instance: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_vms.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_vms.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_vms.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_vms.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def get_vnetwork_vswitches_rpc(self, name=None, vcenter=None, datacenter=None, last_rcvd_instance=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param name: kwarg.
		:type name: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param vcenter: kwarg.
		:type vcenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param datacenter: kwarg.
		:type datacenter: (unicode)
		
		.. note::
			* length - [u'1..80']

		:param last_rcvd_instance: kwarg.
		:type last_rcvd_instance: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vswitch_rpc.get_vnetwork_vswitches.input', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v6_0_2b.brocade_vswitch_rpc'), ('pybind.nos.v7_0_1a.brocade_vswitch_rpc.get_vnetwork_vswitches.input', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_0_1a.brocade_vswitch_rpc'), ('pybind.nos.v7_1_0.brocade_vswitch_rpc.get_vnetwork_vswitches.input', 'pybind.nos.v7_1_0.brocade_vswitch_rpc.brocade_vswitch', 'pybind.nos.v7_1_0.brocade_vswitch_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.get_vnetwork_vswitches.input', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc.brocade_vswitch', 'pybind.slxos.v16r_1_00b.brocade_vswitch_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, name=name, vcenter=vcenter, datacenter=datacenter, last_rcvd_instance=last_rcvd_instance)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_device_brief_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.1.0    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_device_brief', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_discovery_domain_rpc(self, isns_dd_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.1.0    

	**This Instance Arg(s)**:
		:param isns_dd_name: kwarg.
		:type isns_dd_name: (unicode)
		
		.. note::
			* length - [u'1..255']
			* pattern - [-_0-9a-zA-Z]{1,255}

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_discovery_domain.input', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, isns_dd_name=isns_dd_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_discovery_domain_set_rpc(self, isns_dds_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.1.0    

	**This Instance Arg(s)**:
		:param isns_dds_name: kwarg.
		:type isns_dds_name: (unicode)
		
		.. note::
			* length - [u'1..255']
			* pattern - [-_0-9a-zA-Z]{1,255}

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_discovery_domain_set.input', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, isns_dds_name=isns_dds_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_last_device_timestamp_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.1.0    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_last_device_timestamp', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_server_role_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.1.0    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_server_role', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def isns_get_vrf_forwarding_rpc(self, isns_vrf_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.1.0    

	**This Instance Arg(s)**:
		:param isns_vrf_id: kwarg.
		:type isns_vrf_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_1_0.brocade_isns_ext_rpc.isns_get_vrf_forwarding.input', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc.brocade_isns_ext', 'pybind.nos.v7_1_0.brocade_isns_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, isns_vrf_id=isns_vrf_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def l2traceroute_rpc(self, src_mac=None, dest_mac=None, vlan_id=None, rbridge_id=None, src_ip=None, dest_ip=None, l4protocol=None, l4_src_port=None, l4_dest_port=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param src_mac: kwarg.
		:type src_mac: (unicode)

		:param dest_mac: kwarg.
		:type dest_mac: (unicode)

		:param vlan_id: kwarg.
		:type vlan_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param rbridge_id: Syntax: rbridge-id [rbridge-id]
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param src_ip: kwarg.
		:type src_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param dest_ip: kwarg.
		:type dest_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param l4protocol: kwarg.
		:type l4protocol: (unicode)
		
		.. note::
			* enum - [u'UDP', u'TCP']

		:param l4_src_port: kwarg.
		:type l4_src_port: (int)
		
		.. note::
			* range - ['0..65535']

		:param l4_dest_port: kwarg.
		:type l4_dest_port: (int)
		
		.. note::
			* range - ['0..65535']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_trilloam_rpc.l2traceroute.input', 'pybind.nos.v6_0_2b.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v6_0_2b.brocade_trilloam_rpc'), ('pybind.nos.v7_0_1a.brocade_trilloam_rpc.l2traceroute.input', 'pybind.nos.v7_0_1a.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v7_0_1a.brocade_trilloam_rpc'), ('pybind.nos.v7_1_0.brocade_trilloam_rpc.l2traceroute.input', 'pybind.nos.v7_1_0.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v7_1_0.brocade_trilloam_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, src_mac=src_mac, dest_mac=dest_mac, vlan_id=vlan_id, rbridge_id=rbridge_id, src_ip=src_ip, dest_ip=dest_ip, l4protocol=l4protocol, l4_src_port=l4_src_port, l4_dest_port=l4_dest_port)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def l2traceroute_result_rpc(self, session_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param session_id: kwarg.
		:type session_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_trilloam_rpc.l2traceroute_result.input', 'pybind.nos.v6_0_2b.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v6_0_2b.brocade_trilloam_rpc'), ('pybind.nos.v7_0_1a.brocade_trilloam_rpc.l2traceroute_result.input', 'pybind.nos.v7_0_1a.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v7_0_1a.brocade_trilloam_rpc'), ('pybind.nos.v7_1_0.brocade_trilloam_rpc.l2traceroute_result.input', 'pybind.nos.v7_1_0.brocade_trilloam_rpc.brocade_trilloam', 'pybind.nos.v7_1_0.brocade_trilloam_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, session_id=session_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def logical_chassis_fwdl_sanity_rpc(self, user=None, password=None, host=None, directory=None, file=None, rbridge_id=None, auto_activate=None, coldboot=None, protocol=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param user: Username
		:type user: (unicode)

		:param password: Password
		:type password: (unicode)

		:param host: Host ipv4/ipv6 address
		:type host: (unicode)

		:param directory: Directory
		:type directory: (unicode)

		:param file: Package release file, example - release.plist
		:type file: (unicode)

		:param rbridge_id: Enter 'all' for firmware download on all nodes in the 
logical-chassis or comma seperated rbridge-ids like 'rbridge-id 3,4,7-9,20'
		:type rbridge_id: (unicode)
		
		.. note::
			* pattern - [0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*

		:param auto_activate: To activate new firmware on all nodes
		:type auto_activate: (YANGBool)

		:param coldboot: Perform non ISSU firmware download.
		:type coldboot: (YANGBool)

		:param protocol: Protocol type : ftp, scp or sftp
		:type protocol: (unicode)
		
		.. note::
			* enum - [u'ftp', u'scp', u'sftp']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.logical_chassis_fwdl_sanity.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.logical_chassis_fwdl_sanity.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.logical_chassis_fwdl_sanity.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, user=user, password=password, host=host, directory=directory, file=file, rbridge_id=rbridge_id, auto_activate=auto_activate, coldboot=coldboot, protocol=protocol)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def logical_chassis_fwdl_status_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param rbridge_id: Please enter 'all' for activating all nodes in the logical-chassis or individual rbridge-ids of the form 1,2,3-6
		:type rbridge_id: (unicode)
		
		.. note::
			* pattern - [0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_rpc.logical_chassis_fwdl_status.input', 'pybind.nos.v6_0_2b.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v6_0_2b.brocade_firmware_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_rpc.logical_chassis_fwdl_status.input', 'pybind.nos.v7_0_1a.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_0_1a.brocade_firmware_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_rpc.logical_chassis_fwdl_status.input', 'pybind.nos.v7_1_0.brocade_firmware_rpc.brocade_firmware', 'pybind.nos.v7_1_0.brocade_firmware_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def maps_get_all_policy_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_maps_ext_rpc.maps_get_all_policy.input', 'pybind.nos.v6_0_2b.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v6_0_2b.brocade_maps_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_maps_ext_rpc.maps_get_all_policy.input', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc'), ('pybind.nos.v7_1_0.brocade_maps_ext_rpc.maps_get_all_policy.input', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc.maps_get_all_policy.input', 'pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def maps_get_default_rules_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_maps_ext_rpc.maps_get_default_rules.input', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc'), ('pybind.nos.v7_1_0.brocade_maps_ext_rpc.maps_get_default_rules.input', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def maps_get_rules_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_maps_ext_rpc.maps_get_rules.input', 'pybind.nos.v6_0_2b.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v6_0_2b.brocade_maps_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc.maps_get_rules.input', 'pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.slxos.v16r_1_00b.brocade_maps_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def maps_re_apply_policy_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_maps_ext_rpc.maps_re_apply_policy.input', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_0_1a.brocade_maps_ext_rpc'), ('pybind.nos.v7_1_0.brocade_maps_ext_rpc.maps_re_apply_policy.input', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc.brocade_maps_ext', 'pybind.nos.v7_1_0.brocade_maps_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def mpls_adjust_bandwidth_lsp_rpc(self, lsp_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param lsp_name: kwarg.
		:type lsp_name: (unicode)
		
		.. note::
			* length - [u'1..64']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.mpls_adjust_bandwidth_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, lsp_name=lsp_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def mpls_adjust_bandwidth_lsp_all_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.mpls_adjust_bandwidth_lsp_all', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def mpls_reopt_lsp_rpc(self, mpls_reoptimize_lsp_name_in=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param mpls_reoptimize_lsp_name_in: kwarg.
		:type mpls_reoptimize_lsp_name_in: (unicode)
		
		.. note::
			* length - [u'1..64']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.mpls_reopt_lsp.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_reoptimize_lsp_name_in=mpls_reoptimize_lsp_name_in)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def redundancy_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 7.0.1a, 7.1.0    

	**This Instance Arg(s)**:
		:param rbridge_id: Please enter 'all' or an individual rbridge-id in the range 1-239
		:type rbridge_id: (unicode)
		
		.. note::
			* length - [u'1..3']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v7_0_1a.brocade_ha_rpc.redundancy.input', 'pybind.nos.v7_0_1a.brocade_ha_rpc.brocade_ha', 'pybind.nos.v7_0_1a.brocade_ha_rpc'), ('pybind.nos.v7_1_0.brocade_ha_rpc.redundancy.input', 'pybind.nos.v7_1_0.brocade_ha_rpc.brocade_ha', 'pybind.nos.v7_1_0.brocade_ha_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def reload_rpc(self, rbridge_id=None, system=None, standby=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: Rbridge-id (use only with  reload system)
		:type rbridge_id: (unicode)
		
		.. note::
			* length - [u'1..3']

		:param system: Reboots the chassis
		:type system: (YANGBool)

		:param standby: Reboots the standby MM
		:type standby: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ha_rpc.reload.input', 'pybind.nos.v6_0_2b.brocade_ha_rpc.brocade_ha', 'pybind.nos.v6_0_2b.brocade_ha_rpc'), ('pybind.nos.v7_0_1a.brocade_ha_rpc.reload.input', 'pybind.nos.v7_0_1a.brocade_ha_rpc.brocade_ha', 'pybind.nos.v7_0_1a.brocade_ha_rpc'), ('pybind.nos.v7_1_0.brocade_ha_rpc.reload.input', 'pybind.nos.v7_1_0.brocade_ha_rpc.brocade_ha', 'pybind.nos.v7_1_0.brocade_ha_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ha_rpc.reload.input', 'pybind.slxos.v16r_1_00b.brocade_ha_rpc.brocade_ha', 'pybind.slxos.v16r_1_00b.brocade_ha_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, system=system, standby=standby)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_bare_metal_state_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_preprovision_rpc.show_bare_metal_state', 'pybind.nos.v6_0_2b.brocade_preprovision_rpc.brocade_preprovision', 'pybind.nos.v6_0_2b.brocade_preprovision_rpc'), ('pybind.nos.v7_0_1a.brocade_preprovision_rpc.show_bare_metal_state', 'pybind.nos.v7_0_1a.brocade_preprovision_rpc.brocade_preprovision', 'pybind.nos.v7_0_1a.brocade_preprovision_rpc'), ('pybind.nos.v7_1_0.brocade_preprovision_rpc.show_bare_metal_state', 'pybind.nos.v7_1_0.brocade_preprovision_rpc.brocade_preprovision', 'pybind.nos.v7_1_0.brocade_preprovision_rpc'), ('pybind.slxos.v16r_1_00b.brocade_preprovision_rpc.show_bare_metal_state', 'pybind.slxos.v16r_1_00b.brocade_preprovision_rpc.brocade_preprovision', 'pybind.slxos.v16r_1_00b.brocade_preprovision_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_clock_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_clock_rpc.show_clock.input', 'pybind.nos.v6_0_2b.brocade_clock_rpc.brocade_clock', 'pybind.nos.v6_0_2b.brocade_clock_rpc'), ('pybind.nos.v7_0_1a.brocade_clock_rpc.show_clock.input', 'pybind.nos.v7_0_1a.brocade_clock_rpc.brocade_clock', 'pybind.nos.v7_0_1a.brocade_clock_rpc'), ('pybind.nos.v7_1_0.brocade_clock_rpc.show_clock.input', 'pybind.nos.v7_1_0.brocade_clock_rpc.brocade_clock', 'pybind.nos.v7_1_0.brocade_clock_rpc'), ('pybind.slxos.v16r_1_00b.brocade_clock_rpc.show_clock', 'pybind.slxos.v16r_1_00b.brocade_clock_rpc.brocade_clock', 'pybind.slxos.v16r_1_00b.brocade_clock_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_fabric_trunk_info_rpc(self, rbridge_id=None, all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: Syntax: rbridge-id [rbridge-id]
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param all: All rbridges in fabric
		:type all: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fabric_service_rpc.show_fabric_trunk_info.input', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc'), ('pybind.nos.v7_0_1a.brocade_fabric_service_rpc.show_fabric_trunk_info.input', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc'), ('pybind.nos.v7_1_0.brocade_fabric_service_rpc.show_fabric_trunk_info.input', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.show_fabric_trunk_info.input', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, all=all)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_fibrechannel_interface_info_rpc(self, all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param all: kwarg.
		:type all: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fabric_service_rpc.show_fibrechannel_interface_info.input', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc'), ('pybind.nos.v7_0_1a.brocade_fabric_service_rpc.show_fibrechannel_interface_info.input', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc'), ('pybind.nos.v7_1_0.brocade_fabric_service_rpc.show_fibrechannel_interface_info.input', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.show_fibrechannel_interface_info.input', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, all=all)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_firmware_version_rpc(self, switchid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param switchid: kwarg.
		:type switchid: (unicode)
		
		.. note::
			* length - [u'1..3']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_firmware_ext_rpc.show_firmware_version.input', 'pybind.nos.v6_0_2b.brocade_firmware_ext_rpc.brocade_firmware_ext', 'pybind.nos.v6_0_2b.brocade_firmware_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_firmware_ext_rpc.show_firmware_version.input', 'pybind.nos.v7_0_1a.brocade_firmware_ext_rpc.brocade_firmware_ext', 'pybind.nos.v7_0_1a.brocade_firmware_ext_rpc'), ('pybind.nos.v7_1_0.brocade_firmware_ext_rpc.show_firmware_version.input', 'pybind.nos.v7_1_0.brocade_firmware_ext_rpc.brocade_firmware_ext', 'pybind.nos.v7_1_0.brocade_firmware_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_firmware_ext_rpc.show_firmware_version', 'pybind.slxos.v16r_1_00b.brocade_firmware_ext_rpc.brocade_firmware_ext', 'pybind.slxos.v16r_1_00b.brocade_firmware_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, switchid=switchid)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_linkinfo_rpc(self, all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param all: kwarg.
		:type all: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fabric_service_rpc.show_linkinfo.input', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc'), ('pybind.nos.v7_0_1a.brocade_fabric_service_rpc.show_linkinfo.input', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc'), ('pybind.nos.v7_1_0.brocade_fabric_service_rpc.show_linkinfo.input', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.show_linkinfo.input', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, all=all)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bfd_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bfd', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_bypass_lsp_extensive_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_bypass_lsp_extensive', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_debug_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_debug', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_bypass_lsp_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_bypass_lsp_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_dynamic_bypass_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_dynamic_bypass', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_dynamic_bypass_interface_brief_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_dynamic_bypass_interface_brief', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_interface_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_interface', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_interface_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_interface_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_interface_one_interface_rpc(self, interface_type=None, interface_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: kwarg.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'ethernet', u've']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_interface_one_interface.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_filtered_rpc(self, ldp_fec_prefix_filtered=None, ldp_fec_prefix_filtered_in=None, ldp_fec_prefix_filtered_out=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_fec_prefix_filtered: kwarg.
		:type ldp_fec_prefix_filtered: (YANGBool)

		:param ldp_fec_prefix_filtered_in: kwarg.
		:type ldp_fec_prefix_filtered_in: (YANGBool)

		:param ldp_fec_prefix_filtered_out: kwarg.
		:type ldp_fec_prefix_filtered_out: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix_filtered.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_prefix_filtered=ldp_fec_prefix_filtered, ldp_fec_prefix_filtered_in=ldp_fec_prefix_filtered_in, ldp_fec_prefix_filtered_out=ldp_fec_prefix_filtered_out)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_prefix_rpc(self, ldp_fec_prefix=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_fec_prefix: kwarg.
		:type ldp_fec_prefix: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix_prefix.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_prefix=ldp_fec_prefix)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_prefix_filter_rpc(self, ldp_fec_prefix_filter=None, ldp_fec_prefix_filter_string=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_fec_prefix_filter: kwarg.
		:type ldp_fec_prefix_filter: (YANGBool)

		:param ldp_fec_prefix_filter_string: kwarg.
		:type ldp_fec_prefix_filter_string: (unicode)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix_prefix_filter.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_prefix_filter=ldp_fec_prefix_filter, ldp_fec_prefix_filter_string=ldp_fec_prefix_filter_string)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_prefix_prefix_longer_rpc(self, ldp_fec_prefix=None, ldp_fec_prefix_longer=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_fec_prefix: kwarg.
		:type ldp_fec_prefix: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))

		:param ldp_fec_prefix_longer: kwarg.
		:type ldp_fec_prefix_longer: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_prefix_prefix_longer.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_prefix=ldp_fec_prefix, ldp_fec_prefix_longer=ldp_fec_prefix_longer)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_summary_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_summary', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_vc_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_vc', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_fec_vc_id_rpc(self, ldp_fec_vc_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_fec_vc_id: kwarg.
		:type ldp_fec_vc_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_fec_vc_id.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_fec_vc_id=ldp_fec_vc_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_path_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_path', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_path_one_rpc(self, ldp_path_ip=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_path_ip: kwarg.
		:type ldp_path_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_path_one.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_path_ip=ldp_path_ip)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_peer_br_rpc(self, ldp_peer_brief=None, ldp_peer_detail=None, ldp_peer_ip=None, ldp_peer_ip_lblspid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_peer_brief: kwarg.
		:type ldp_peer_brief: (YANGBool)

		:param ldp_peer_detail: kwarg.
		:type ldp_peer_detail: (YANGBool)

		:param ldp_peer_ip: kwarg.
		:type ldp_peer_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param ldp_peer_ip_lblspid: kwarg.
		:type ldp_peer_ip_lblspid: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_peer_br.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_peer_brief=ldp_peer_brief, ldp_peer_detail=ldp_peer_detail, ldp_peer_ip=ldp_peer_ip, ldp_peer_ip_lblspid=ldp_peer_ip_lblspid)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_peer_det_rpc(self, ldp_peer_brief=None, ldp_peer_detail=None, ldp_peer_ip=None, ldp_peer_ip_lblspid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_peer_brief: kwarg.
		:type ldp_peer_brief: (YANGBool)

		:param ldp_peer_detail: kwarg.
		:type ldp_peer_detail: (YANGBool)

		:param ldp_peer_ip: kwarg.
		:type ldp_peer_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param ldp_peer_ip_lblspid: kwarg.
		:type ldp_peer_ip_lblspid: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_peer_det.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_peer_brief=ldp_peer_brief, ldp_peer_detail=ldp_peer_detail, ldp_peer_ip=ldp_peer_ip, ldp_peer_ip_lblspid=ldp_peer_ip_lblspid)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_peer_det_rec_rpc(self, ldp_peer_brief=None, ldp_peer_detail=None, ldp_peer_ip=None, ldp_peer_ip_lblspid=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_peer_brief: kwarg.
		:type ldp_peer_brief: (YANGBool)

		:param ldp_peer_detail: kwarg.
		:type ldp_peer_detail: (YANGBool)

		:param ldp_peer_ip: kwarg.
		:type ldp_peer_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param ldp_peer_ip_lblspid: kwarg.
		:type ldp_peer_ip_lblspid: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_peer_det_rec.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_peer_brief=ldp_peer_brief, ldp_peer_detail=ldp_peer_detail, ldp_peer_ip=ldp_peer_ip, ldp_peer_ip_lblspid=ldp_peer_ip_lblspid)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_statistics_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_statistics', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_targeted_peer_all_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_targeted_peer_all', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_ldp_targeted_peer_one_rpc(self, ldp_targeted_peer_ip=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_targeted_peer_ip: kwarg.
		:type ldp_targeted_peer_ip: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_ldp_targeted_peer_one.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_targeted_peer_ip=ldp_targeted_peer_ip)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_debug_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_debug', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_lsp_extensive_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_lsp_extensive', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_policy_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_policy', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_route_rpc(self, prefix_address_and_len=None, prefix_address=None, subnet_mask=None, longer=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param prefix_address_and_len: kwarg.
		:type prefix_address_and_len: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))

		:param prefix_address: kwarg.
		:type prefix_address: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param subnet_mask: kwarg.
		:type subnet_mask: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param longer: kwarg.
		:type longer: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_route.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, prefix_address_and_len=prefix_address_and_len, prefix_address=prefix_address, subnet_mask=subnet_mask, longer=longer)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_interface_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_interface', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_interface_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_interface_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_interface_one_interface_rpc(self, interface_type=None, interface_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param interface_type: kwarg.
		:type interface_type: (unicode)
		
		.. note::
			* enum - [u'ethernet', u've']

		:param interface_name: The Interface value.
		:type interface_name: (unicode)
		
		.. note::
			* length - [u'3..16']
			* pattern - ((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_interface_one_interface.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, interface_type=interface_type, interface_name=interface_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_neighbor_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_neighbor', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_neighbor_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_neighbor_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_neighbor_one_neighbor_rpc(self, mpls_rsvp_neighbor_peer_ip_addr=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param mpls_rsvp_neighbor_peer_ip_addr: kwarg.
		:type mpls_rsvp_neighbor_peer_ip_addr: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_neighbor_one_neighbor.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, mpls_rsvp_neighbor_peer_ip_addr=mpls_rsvp_neighbor_peer_ip_addr)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_detail_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session_detail', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_extensive_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session_extensive', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_name_rpc(self, session_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param session_name: kwarg.
		:type session_name: (unicode)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session_name.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, session_name=session_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_session_wide_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_session_wide', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_rsvp_statistics_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_rsvp_statistics', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_statistics_ldp_transit_rpc(self, ldp_transit_stats=None, ldp_transit_stats_fec_prefix=None, ldp_transit_stats_fec_prefix_longer=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_transit_stats: kwarg.
		:type ldp_transit_stats: (YANGBool)

		:param ldp_transit_stats_fec_prefix: kwarg.
		:type ldp_transit_stats_fec_prefix: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param ldp_transit_stats_fec_prefix_longer: kwarg.
		:type ldp_transit_stats_fec_prefix_longer: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_statistics_ldp_transit.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_transit_stats=ldp_transit_stats, ldp_transit_stats_fec_prefix=ldp_transit_stats_fec_prefix, ldp_transit_stats_fec_prefix_longer=ldp_transit_stats_fec_prefix_longer)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_statistics_ldp_tunnel_rpc(self, ldp_tunnel_stats=None, ldp_tunnel_stats_vif=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ldp_tunnel_stats: kwarg.
		:type ldp_tunnel_stats: (YANGBool)

		:param ldp_tunnel_stats_vif: kwarg.
		:type ldp_tunnel_stats_vif: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_statistics_ldp_tunnel.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ldp_tunnel_stats=ldp_tunnel_stats, ldp_tunnel_stats_vif=ldp_tunnel_stats_vif)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_statistics_oam_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_statistics_oam', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_summary_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_summary', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_mpls_te_path_rpc(self, ipAddr=None, bandwidth=None, cspfCompMode=None, excludeAny=None, hopLimit=None, includeAny=None, includeAll=None, tePathName=None, priority=None, tieBreaking=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param ipAddr: kwarg.
		:type ipAddr: (unicode)
		
		.. note::
			* pattern - (([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?

		:param bandwidth: kwarg.
		:type bandwidth: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param cspfCompMode: kwarg.
		:type cspfCompMode: (unicode)
		
		.. note::
			* enum - [u'use-igp-metric', u'use-te-metric']

		:param excludeAny: kwarg.
		:type excludeAny: (unicode)

		:param hopLimit: kwarg.
		:type hopLimit: (int)
		
		.. note::
			* range - ['0..255']

		:param includeAny: kwarg.
		:type includeAny: (unicode)

		:param includeAll: kwarg.
		:type includeAll: (unicode)

		:param tePathName: kwarg.
		:type tePathName: (unicode)

		:param priority: kwarg.
		:type priority: (int)
		
		.. note::
			* range - ['0..255']

		:param tieBreaking: kwarg.
		:type tieBreaking: (unicode)
		
		.. note::
			* enum - [u'most-fill', u'random', u'least-fill']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.slxos.v16r_1_00b.brocade_mpls_rpc.show_mpls_te_path.input', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc.brocade_mpls', 'pybind.slxos.v16r_1_00b.brocade_mpls_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, ipAddr=ipAddr, bandwidth=bandwidth, cspfCompMode=cspfCompMode, excludeAny=excludeAny, hopLimit=hopLimit, includeAny=includeAny, includeAll=includeAll, tePathName=tePathName, priority=priority, tieBreaking=tieBreaking)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_ntp_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ntp_rpc.show_ntp.input', 'pybind.nos.v6_0_2b.brocade_ntp_rpc.brocade_ntp', 'pybind.nos.v6_0_2b.brocade_ntp_rpc'), ('pybind.nos.v7_0_1a.brocade_ntp_rpc.show_ntp.input', 'pybind.nos.v7_0_1a.brocade_ntp_rpc.brocade_ntp', 'pybind.nos.v7_0_1a.brocade_ntp_rpc'), ('pybind.nos.v7_1_0.brocade_ntp_rpc.show_ntp.input', 'pybind.nos.v7_1_0.brocade_ntp_rpc.brocade_ntp', 'pybind.nos.v7_1_0.brocade_ntp_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ntp_rpc.show_ntp', 'pybind.slxos.v16r_1_00b.brocade_ntp_rpc.brocade_ntp', 'pybind.slxos.v16r_1_00b.brocade_ntp_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_portindex_interface_info_rpc(self, all=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param all: kwarg.
		:type all: (YANGBool)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_fabric_service_rpc.show_portindex_interface_info.input', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v6_0_2b.brocade_fabric_service_rpc'), ('pybind.nos.v7_0_1a.brocade_fabric_service_rpc.show_portindex_interface_info.input', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_0_1a.brocade_fabric_service_rpc'), ('pybind.nos.v7_1_0.brocade_fabric_service_rpc.show_portindex_interface_info.input', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.nos.v7_1_0.brocade_fabric_service_rpc'), ('pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.show_portindex_interface_info.input', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc.brocade_fabric_service', 'pybind.slxos.v16r_1_00b.brocade_fabric_service_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, all=all)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_raslog_rpc(self, rbridge_id=None, number_of_latest_events=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (unicode)
		
		.. note::
			* length - [u'1..3']

		:param number_of_latest_events: kwarg.
		:type number_of_latest_events: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_ext_rpc.show_raslog.input', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_ext_rpc.show_raslog.input', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc'), ('pybind.nos.v7_1_0.brocade_ras_ext_rpc.show_raslog.input', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.show_raslog.input', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id, number_of_latest_events=number_of_latest_events)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_support_save_status_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (unicode)
		
		.. note::
			* length - [u'1..3']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_ext_rpc.show_support_save_status.input', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_ext_rpc.show_support_save_status.input', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc'), ('pybind.nos.v7_1_0.brocade_ras_ext_rpc.show_support_save_status.input', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.show_support_save_status.input', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_system_info_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (unicode)
		
		.. note::
			* length - [u'1..3']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_ras_ext_rpc.show_system_info.input', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v6_0_2b.brocade_ras_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_ras_ext_rpc.show_system_info.input', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_0_1a.brocade_ras_ext_rpc'), ('pybind.nos.v7_1_0.brocade_ras_ext_rpc.show_system_info.input', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.nos.v7_1_0.brocade_ras_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.show_system_info.input', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc.brocade_ras_ext', 'pybind.slxos.v16r_1_00b.brocade_ras_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_system_monitor_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (long)
		
		.. note::
			* range - ['0..4294967295']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_system_monitor_ext_rpc.show_system_monitor.input', 'pybind.nos.v6_0_2b.brocade_system_monitor_ext_rpc.brocade_system_monitor_ext', 'pybind.nos.v6_0_2b.brocade_system_monitor_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_system_monitor_ext_rpc.show_system_monitor.input', 'pybind.nos.v7_0_1a.brocade_system_monitor_ext_rpc.brocade_system_monitor_ext', 'pybind.nos.v7_0_1a.brocade_system_monitor_ext_rpc'), ('pybind.nos.v7_1_0.brocade_system_monitor_ext_rpc.show_system_monitor.input', 'pybind.nos.v7_1_0.brocade_system_monitor_ext_rpc.brocade_system_monitor_ext', 'pybind.nos.v7_1_0.brocade_system_monitor_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_system_monitor_ext_rpc.show_system_monitor', 'pybind.slxos.v16r_1_00b.brocade_system_monitor_ext_rpc.brocade_system_monitor_ext', 'pybind.slxos.v16r_1_00b.brocade_system_monitor_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_vcs_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.show_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.show_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.show_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.show_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def show_zoning_enabled_configuration_rpc(self, zone_name_pattern=None, last_rcvd_zone_name=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param zone_name_pattern: <WORD>;;Enabled-Zone-Name
		:type zone_name_pattern: (unicode)

		:param last_rcvd_zone_name: <WORD>;;Enabled-Zone-Name
		:type last_rcvd_zone_name: (unicode)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_zone_rpc.show_zoning_enabled_configuration.input', 'pybind.nos.v6_0_2b.brocade_zone_rpc.brocade_zone', 'pybind.nos.v6_0_2b.brocade_zone_rpc'), ('pybind.nos.v7_0_1a.brocade_zone_rpc.show_zoning_enabled_configuration.input', 'pybind.nos.v7_0_1a.brocade_zone_rpc.brocade_zone', 'pybind.nos.v7_0_1a.brocade_zone_rpc'), ('pybind.nos.v7_1_0.brocade_zone_rpc.show_zoning_enabled_configuration.input', 'pybind.nos.v7_1_0.brocade_zone_rpc.brocade_zone', 'pybind.nos.v7_1_0.brocade_zone_rpc'), ('pybind.slxos.v16r_1_00b.brocade_zone_rpc.show_zoning_enabled_configuration.input', 'pybind.slxos.v16r_1_00b.brocade_zone_rpc.brocade_zone', 'pybind.slxos.v16r_1_00b.brocade_zone_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, zone_name_pattern=zone_name_pattern, last_rcvd_zone_name=last_rcvd_zone_name)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def user_session_info_rpc(self, output=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param output: kwarg.
		:type output: (output)

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_aaa_ext_rpc.user_session_info', 'pybind.nos.v6_0_2b.brocade_aaa_ext_rpc.brocade_aaa_ext', 'pybind.nos.v6_0_2b.brocade_aaa_ext_rpc'), ('pybind.nos.v7_0_1a.brocade_aaa_ext_rpc.user_session_info', 'pybind.nos.v7_0_1a.brocade_aaa_ext_rpc.brocade_aaa_ext', 'pybind.nos.v7_0_1a.brocade_aaa_ext_rpc'), ('pybind.nos.v7_1_0.brocade_aaa_ext_rpc.user_session_info', 'pybind.nos.v7_1_0.brocade_aaa_ext_rpc.brocade_aaa_ext', 'pybind.nos.v7_1_0.brocade_aaa_ext_rpc'), ('pybind.slxos.v16r_1_00b.brocade_aaa_ext_rpc.user_session_info', 'pybind.slxos.v16r_1_00b.brocade_aaa_ext_rpc.brocade_aaa_ext', 'pybind.slxos.v16r_1_00b.brocade_aaa_ext_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, output=output)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def vcs_rbridge_config_rpc(self, vcs_id=None, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param vcs_id: kwarg.
		:type vcs_id: (int)
		
		.. note::
			* range - ['0..65535']

		:param rbridge_id: kwarg.
		:type rbridge_id: (int)
		
		.. note::
			* range - ['0..65535']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.vcs_rbridge_config.input', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.vcs_rbridge_config.input', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.vcs_rbridge_config.input', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.vcs_rbridge_config.input', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, vcs_id=vcs_id, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

def vcs_rbridge_context_rpc(self, rbridge_id=None, api_timeout=''):
    """
    This is an auto-generated method for the PySwitchLib.

	**Supported Versions**:
		NOS: 6.0.2b, 7.0.1a, 7.1.0
		SLXOS: 16r.1.00b    

	**This Instance Arg(s)**:
		:param rbridge_id: kwarg.
		:type rbridge_id: (int)
		
		.. note::
			* range - ['0..65535']

		:param api_timeout: Timeout for connection and response in seconds.  If tuple specified, then first value is for connection timeout and second value is for response timeout.
		:type api_timeout: (long or tuple)

	:returns: (bool, list)
		Returns a tuple. First element (bool): The overall success or failure of the API. Second element (list): List of REST request/response dictionaries, keyed by the asset's ip address.

	:raises: AttributeError, ConnectionError
    """

    operation_type = 'rpc'
    compositions_list = []
    bindings_list = [('pybind.nos.v6_0_2b.brocade_vcs_rpc.vcs_rbridge_context.input', 'pybind.nos.v6_0_2b.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v6_0_2b.brocade_vcs_rpc'), ('pybind.nos.v7_0_1a.brocade_vcs_rpc.vcs_rbridge_context.input', 'pybind.nos.v7_0_1a.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_0_1a.brocade_vcs_rpc'), ('pybind.nos.v7_1_0.brocade_vcs_rpc.vcs_rbridge_context.input', 'pybind.nos.v7_1_0.brocade_vcs_rpc.brocade_vcs', 'pybind.nos.v7_1_0.brocade_vcs_rpc'), ('pybind.slxos.v16r_1_00b.brocade_vcs_rpc.vcs_rbridge_context.input', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc.brocade_vcs', 'pybind.slxos.v16r_1_00b.brocade_vcs_rpc')]
    composed_child_list = []
    compositions_keyval_list = []
    bindings_keyval = {'kwargs_key_name': '', 'keyval': '', 'extra_keyval': ''}
    composed_child_leafval_list = []
    pybind_object = self._get_pybind_object(compositions_list=compositions_list, bindings_list=bindings_list, composed_child_list=composed_child_list, compositions_keyval_list=compositions_keyval_list, bindings_keyval=bindings_keyval, composed_child_leafval_list=composed_child_leafval_list, rbridge_id=rbridge_id)

    return self._config_worker(operation_type=operation_type, pybind_object=pybind_object, resource_depth=1, timeout=api_timeout)

