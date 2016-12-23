import pyangbind.lib.pybindJSON as pybindJSON
from collections import OrderedDict
from dicttoxml import dicttoxml
import json
import re


class PySwitchLib(object):
    """
    This is an auto-generated class for the PySwitchLib.
    Providing python bindings to configure a switch through the REST interface.
    """
    import api.create
    import api.update
    import api.delete
    import api.get
    import api.rpc

    locals().update(api.create.__dict__)
    locals().update(api.update.__dict__)                                                                                                                                            
    locals().update(api.delete.__dict__)                                                                                                                                            
    locals().update(api.get.__dict__)                                                                                                                                               
    locals().update(api.rpc.__dict__) 


    def __init__(self, module_name='', module_obj=None, rest_operation=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        self._module_name = module_name
        self._module_obj = module_obj
        self._rest_operation = rest_operation

    def _get_pybind_object(self, compositions_list=None, bindings_list=None, composed_child_list=None, compositions_keyval_list=None, bindings_keyval=None, composed_child_leafval_list=None, **kwargs):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        pybind_obj = None

        for index, value in enumerate(bindings_list):
            if self._module_name in value[2]:
                class_name = value[1].replace(value[2] + '.', '', 1)  
                pybind_module_path = value[0].replace(value[2] + '.', '', 1)  
                pybind_paths = pybind_module_path.split('.')

                module_name = value[2]
                module_obj = None

                if self._module_obj is not None:
                    module_obj = self._module_obj
                else:
                    module_obj =  __import__(module_name, fromlist=[class_name])

                pybind_base_class = getattr(module_obj, class_name)
                pybind_obj = pybind_base_class()
                pybind_module = pybind_obj
                pybind_class_module_name = value[2]
                kwargs_exclusion_list = []
                
                for module in pybind_paths:
                    pybind_class_module_name = pybind_class_module_name + '.' + module
                    pybind_module = getattr(pybind_module, module)

                    for composition_index, composition_tuple in enumerate(compositions_list):
                        if pybind_class_module_name == composition_tuple[0]:
                            kwargs_exclusion_list.append(composition_tuple[1])

                            pybind_module = getattr(pybind_module, 'add')

                            if compositions_keyval_list[composition_index]['extra_keyval']:
                                parent_kwargs_map = {}
                                parent_key_instance = []

                                for parent_key_index, parent_key in enumerate(compositions_keyval_list[composition_index]['extra_keyval'].split(', ')):
                                    if parent_key_index < len(kwargs[composition_tuple[1]]):
                                        parent_kwargs_map[parent_key] = kwargs[composition_tuple[1]][parent_key_index]

                                for key in compositions_keyval_list[composition_index]['keyval'].split(', '):
                                    if key in parent_kwargs_map:
                                        parent_key_instance.append(parent_kwargs_map[key])
                                        parent_kwargs_map.pop(key)

                                pybind_module = pybind_module(' '.join(map(str, parent_key_instance)))

                                for key in parent_kwargs_map:
                                    if parent_kwargs_map[key] is not None:
                                        pybind_parent_extra_key_assignment = getattr(pybind_parent_obj, '_set_' + key)
                                        pybind_parent_extra_key_assignment(parent_kwargs_map[key])
                            else:
                                if type(kwargs[composition_tuple[1]]) == 'tuple':
                                    pybind_module = pybind_module(' '.join(kwargs[composition_tuple[1]]))
                                else:
                                    pybind_module = pybind_module(kwargs[composition_tuple[1]])
                                
                if bindings_keyval['kwargs_key_name']:
                    pybind_obj = getattr(pybind_module, 'add')
                else:
                    pybind_obj = pybind_module

                for kwarg in kwargs:
                    if kwarg in bindings_keyval['kwargs_key_name']:
                        if bindings_keyval['extra_keyval']:
                            kwargs_map = {}
                            key_instance = []

                            for key_index, key in enumerate(bindings_keyval['extra_keyval'].split(', ')):
                                if key_index < len(kwargs[kwarg]):
                                    kwargs_map[key] = kwargs[kwarg][key_index]

                            for key in bindings_keyval['keyval'].split(', '):
                                if key in kwargs_map:
                                    key_instance.append(kwargs_map[key])
                                    kwargs_map.pop(key)

                            pybind_obj = pybind_obj(' '.join(map(str, key_instance)))

                            for key in kwargs_map:
                                if kwargs_map[key] is not None:
                                    pybind_extra_key_assignment = getattr(pybind_obj, '_set_' + key)
                                    pybind_extra_key_assignment(kwargs_map[key])
                        else:
                            if type(kwargs[kwarg]) == 'tuple':
                                pybind_obj = pybind_obj(' '.join(kwargs[kwarg]))
                            elif kwargs[kwarg] is not None:
                                pybind_obj = pybind_obj(kwargs[kwarg])
                            else:
                                pybind_obj = pybind_module

                for child_index, child_tuple in enumerate(composed_child_list):
                    if pybind_class_module_name in child_tuple[0]:
                        if child_tuple[1] in kwargs and kwargs[child_tuple[1]] != None:
                            kwargs_exclusion_list.append(child_tuple[1])
                            pybind_update_child_obj = pybind_obj

                            if pybind_class_module_name != child_tuple[0]:
                                pybind_update_child_path = child_tuple[0].replace(pybind_class_module_name + '.', '', 1)
                                pybind_update_child_paths = pybind_update_child_path.split('.')

                                for module in pybind_update_child_paths:
                                    pybind_update_child_obj = getattr(pybind_update_child_obj, module)

                            pybind_update_child_obj = getattr(pybind_update_child_obj, child_tuple[1])

                            for leaf_index, leaf_name in enumerate(composed_child_leafval_list[child_index]['leafval'].split(', ')):
                                if kwargs[child_tuple[1]][leaf_index] is not None:
                                    pybind_update_child_assignment = getattr(pybind_update_child_obj, '_set_' + leaf_name) 
                                    pybind_update_child_assignment(kwargs[child_tuple[1]][leaf_index])

                for kwarg in kwargs:
                    if kwarg not in kwargs_exclusion_list and kwargs[kwarg] != None:
                        if kwarg not in bindings_keyval['kwargs_key_name']:
                            if kwargs[kwarg] is not None:
                                pybind_update_key_assignment = getattr(pybind_obj, '_set_' + kwarg)
                                pybind_update_key_assignment(kwargs[kwarg])

                break

        return pybind_obj

    def _config_worker(self, operation_type=None, pybind_object=None, resource_depth=None, timeout=''):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        rest_operation = ''
        rest_uri = ''
        rest_data = ''
        rest_commands = []

        if operation_type == 'create':
            rest_operation = 'POST'
            rest_uri = pybind_object._rest_uri_for_post()
        elif operation_type == 'update_patch':
            rest_operation = 'PATCH'
            rest_uri = pybind_object._rest_uri()
        elif operation_type == 'update_put':
            rest_operation = 'PUT'
            rest_uri = pybind_object._rest_uri()
        elif operation_type == 'delete':
            rest_operation = 'DELETE'
            rest_uri = pybind_object._rest_uri()

        label_list_items = lambda x: x

        if 'update' in operation_type:
            rest_data =  dicttoxml(json.loads(pybindJSON.dumps(pybind_object, mode='rest'), object_pairs_hook=OrderedDict), root=False, attr_type=False, item_func=label_list_items)

            for key in pybind_object.elements():
                update_object_name = getattr(pybind_object, '_get_' + key)
                update_object = update_object_name()
                rest_uri = update_object._rest_uri()
                rest_uri_end_element = rest_uri.split('/')[-1]

                if update_object._is_keyval == False and update_object._changed() == True:
                    rest_name = update_object.rest_name()
                    yang_leaf_name = update_object.yang_name()
                    temp_pybind_obj = update_object

                    while(temp_pybind_obj._parent and (rest_name == '' or rest_name != rest_uri_end_element)):
                        rest_name = temp_pybind_obj.rest_name()
                        yang_leaf_name = temp_pybind_obj.yang_name()
                        temp_pybind_obj = temp_pybind_obj._parent

                    if hasattr(temp_pybind_obj, '_pyangbind_elements'):
                        rest_data = dicttoxml(json.loads(pybindJSON.dumps(temp_pybind_obj, mode='rest'), object_pairs_hook=OrderedDict), root=False, attr_type=False, item_func=label_list_items)

                    update_object_rest_data = rest_data

                    match = re.match(r'.*(<{0}.*{0}>).*'.format(yang_leaf_name), update_object_rest_data)

                    if match:
                        update_object_rest_data = match.group(1)

                    if temp_pybind_obj == False:                                                                                                                                    
                        rest_operation = 'DELETE'                                                                                                                                   
                        update_object_rest_data = '' 
                    else:                                                                                                                                                           
                        if operation_type == 'update_patch':                                                                                                                        
                            rest_operation = 'PATCH'                                                                                                                                
                        elif operation_type == 'update_put':                                                                                                                        
                            rest_operation = 'PUT' 
                    
                    rest_commands.append([rest_operation, rest_uri, update_object_rest_data, 'config', resource_depth])

            rest_commands.reverse()
        else:
            pybind_object = pybind_object._parent
            
            rest_data = dicttoxml(json.loads(pybindJSON.dumps(pybind_object, mode='rest'), object_pairs_hook=OrderedDict), root=False, attr_type=False, item_func=label_list_items)

            if rest_data:
                end_marker = rest_data.rsplit('<', 1)[1].strip('/')

                rest_data = rest_data.rsplit('<', 1)[0]
                rest_data = rest_data.split(end_marker, 1)[-1]
            
            rest_commands.append([rest_operation, rest_uri, rest_data, 'config', resource_depth])

        return self._rest_operation(rest_commands=rest_commands, timeout=timeout)

    def _config_get_worker(self, operation_type=None, pybind_object=None, bindings_list=None, composed_child_list=None, resource_depth=None, timeout=''):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        rest_operation = 'GET'
        rest_uri = pybind_object._rest_uri()
        rest_data = ''
        rest_commands = []
        yang_list = []

        rest_commands.append([rest_operation, rest_uri, rest_data, 'config', resource_depth])

        yang_list.extend(self._get_bindings_list_yang_name(bindings_list=bindings_list))
        yang_list.extend(self._get_child_list_yang_name(composed_child_list=composed_child_list))

        return self._rest_operation(rest_commands=rest_commands, yang_list=yang_list, timeout=timeout)

    def _rpc_worker(self, operation_type=None, pybind_object=None, resource_depth=None, timeout=''):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        rest_operation = 'POST'
        rest_uri = pybind_object._rest_uri_for_post()
        rest_data = ''
        rest_commands = []

        if rest_uri == '/':
            rest_uri = pybind_object._rest_uri()

        label_list_items = lambda x: x

        pybind_object = pybind_object._parent
        
        rest_data = dicttoxml(json.loads(pybindJSON.dumps(pybind_object, mode='rest'), object_pairs_hook=OrderedDict), root=False, attr_type=False, item_func=label_list_items)

        rest_commands.append([rest_operation, rest_uri, rest_data, 'rpc', resource_depth])

        return self._rest_operation(rest_commands=rest_commands, timeout=timeout)

    def _get_bindings_list_yang_name(self, bindings_list=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        yang_name_list = []

        for bindings_tuple in bindings_list:
            if self._module_name == bindings_tuple[2]:
                yang_name_list.append(bindings_tuple[0].split('.')[-1].replace('_', '-'))
        
        return yang_name_list

    def _get_child_list_yang_name(self, composed_child_list=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        yang_name_list = []

        for child_tuple in composed_child_list:
            if self._module_name in child_tuple[0]:
                yang_name_list.append(child_tuple[1])

        return yang_name_list

