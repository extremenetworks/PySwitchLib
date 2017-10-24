import os
import sys
import signal
import time
import threading
import multiprocessing
import json
import re
import Pyro4
import Pyro4.naming
import pyangbind.lib.pybindJSON as pybindJSON
from  pyswitchlib.util.config import ConfigFileUtil
from pyswitchlib.exceptions import (MultipleChoicesSetError)
from collections import OrderedDict
from dicttoxml import dicttoxml
from daemon.runner import (DaemonRunner, DaemonRunnerStopFailureError)
from lockfile import LockTimeout

pid_file = os.path.join(os.sep, 'tmp', '.pyswitchlib_api.pid')
daemon_pid_file = os.path.join(os.sep, 'tmp', '.pyswitchlib_api_daemon.pid')
pyswitchlib_conf_file = os.path.join(os.sep, 'etc', 'pyswitchlib', 'pyswitchlib.conf')

@Pyro4.behavior(instance_mode="single")
class PySwitchLibApiDaemon(object):
    """
    This is an auto-generated class for the PySwitchLib.
    Providing python bindings to configure a switch through the REST interface.
    """

    def __init__(self, module_name='', module_obj=None, pyro_daemon=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        self._module_name = module_name
        self._module_obj = module_obj
        self._api_lock = threading.Lock()
        self._pyro_daemon = pyro_daemon

    def shutdown(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        if self._pyro_daemon:
            self._pyro_daemon.shutdown()

    def module_name(self, module_name=''):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        self._module_name = module_name

    def api_acquire(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        self._api_lock.acquire()

    def api_release(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        self._api_lock.release()

    def _api_validation(self, choices_kwargs_map=None, leaf_os_support_map=None, **kwargs):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        if choices_kwargs_map:
            for choice_ver_key in choices_kwargs_map:
                if self._module_name in choice_ver_key:
                    choice_kwargs_set_list = []

                    for kwarg in kwargs:
                        if kwarg.rstrip('_') in choices_kwargs_map[choice_ver_key]:
                            if kwargs[kwarg] != None:
                                choice_kwargs_set_list.append(kwarg)

                    if len(choice_kwargs_set_list) >= 2:
                        raise MultipleChoicesSetError("Only one choice type kwarg is allowed per API invocation.  Multiple choice kwargs set: " + ', '.join(choice_kwargs_set_list))

                    break

        if leaf_os_support_map:
            pass

    def _get_pybind_object(self, operation_type=None, compositions_list=None, bindings_list=None, composed_child_list=None, compositions_keyval_list=None, bindings_keyval=None, composed_child_leafval_list=None, leafval_map=None, **kwargs):
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
                                        mapped_key = key

                                        if leafval_map and pybind_class_module_name in leafval_map and key in leafval_map[pybind_class_module_name]:
                                            mapped_key = leafval_map[pybind_class_module_name][key]

                                        pybind_parent_extra_key_assignment = getattr(pybind_parent_obj, '_set_' + mapped_key)
                                        pybind_parent_extra_key_assignment(parent_kwargs_map[key])
                            else:
                                if isinstance(kwargs[composition_tuple[1]], tuple):
                                    pybind_module = pybind_module(' '.join(kwargs[composition_tuple[1]]))
                                else:
                                    pybind_module = pybind_module(kwargs[composition_tuple[1]])
                                
                if bindings_keyval['kwargs_key_name']:
                    pybind_obj = getattr(pybind_module, 'add')
                else:
                    pybind_obj = pybind_module

                for kwarg in kwargs:
                    if kwarg == bindings_keyval['kwargs_key_name']:
                        if bindings_keyval['extra_keyval'] and kwargs[kwarg] is not None:
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
                                    mapped_key = key

                                    if leafval_map and pybind_class_module_name in leafval_map and key in leafval_map[pybind_class_module_name]:
                                        mapped_key = leafval_map[pybind_class_module_name][key]

                                    pybind_extra_key_assignment = getattr(pybind_obj, '_set_' + mapped_key)
                                    pybind_extra_key_assignment(kwargs_map[key])
                        else:
                            if isinstance(kwargs[kwarg], tuple):
                                pybind_obj = pybind_obj(' '.join(kwargs[kwarg]))
                            elif kwargs[kwarg] is not None:
                                pybind_obj = pybind_obj(kwargs[kwarg])
                            else:
                                pybind_obj = pybind_module

                if operation_type != 'get':
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
                    if kwarg not in kwargs_exclusion_list:
                        if kwarg != bindings_keyval['kwargs_key_name']:
                            if kwargs[kwarg] is not None:
                                mapped_kwarg = kwarg

                                if leafval_map and pybind_class_module_name in leafval_map and kwarg in leafval_map[pybind_class_module_name]:
                                    mapped_kwarg = leafval_map[pybind_class_module_name][kwarg]

                                pybind_update_key_assignment = getattr(pybind_obj, '_set_' + mapped_kwarg)
                                pybind_update_key_assignment(kwargs[kwarg])

                break

        return pybind_obj

    def _config_worker(self, operation_type=None, pybind_object=None, rest_leaf_name=None, resource_depth=None, timeout=''):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        rest_operation = ''
        rest_uri = ''
        rest_data = ''
        rest_commands = []

        if 'create' == operation_type:
            rest_operation = 'POST'
            rest_uri = pybind_object._rest_uri_for_post()
        elif 'update_patch' in operation_type:
            rest_operation = 'PATCH'
            rest_uri = pybind_object._rest_uri()
        elif 'update_put' in operation_type:
            rest_operation = 'PUT'
            rest_uri = pybind_object._rest_uri()
        elif 'delete' == operation_type:
            rest_operation = 'DELETE'
            rest_uri = pybind_object._rest_uri()

        label_list_items = lambda x: x

        if 'update' in operation_type:
            update_object_rest_data = ''
            rest_data =  dicttoxml(json.loads(pybindJSON.dumps(pybind_object, mode='rest'), object_pairs_hook=OrderedDict), root=False, attr_type=False, item_func=label_list_items)

            for key in pybind_object.elements():
                update_object_name = getattr(pybind_object, '_get_' + key)
                update_object = update_object_name()
                rest_uri = update_object._rest_uri()
                rest_uri_end_element = rest_uri.split('/')[-1]

                if update_object._is_keyval == False and (update_object._changed() == True or (update_object.default() and update_object == update_object.default())):
                    rest_name = update_object.rest_name()
                    yang_leaf_name = update_object.yang_name()
                    temp_pybind_obj = update_object

                    while(temp_pybind_obj._parent and (rest_name == '' or rest_name != rest_uri_end_element)):
                        rest_name = temp_pybind_obj.rest_name()
                        yang_leaf_name = temp_pybind_obj.yang_name()
                        temp_pybind_obj = temp_pybind_obj._parent

                    if hasattr(temp_pybind_obj, '_pyangbind_elements'):
                        rest_data = dicttoxml(json.loads(pybindJSON.dumps(temp_pybind_obj, mode='rest'), object_pairs_hook=OrderedDict), root=False, attr_type=False, item_func=label_list_items)
                    elif update_object.default() and update_object == update_object.default():
                        rest_data += '<{0}>{1}</{0}>'.format(rest_name, update_object)

                    match = re.match(r'.*(<{0}>.*</{0}>).*'.format(rest_name), rest_data)

                    if match:
                        update_object_rest_data = match.group(1)

                    if repr(temp_pybind_obj) is 'False':
                        rest_operation = 'DELETE'
                    else:
                        if 'update_patch' in operation_type:
                            rest_operation = 'PATCH'
                        elif 'update_put' in operation_type:
                            rest_operation = 'PUT' 

                    if rest_operation == 'DELETE':
                        rest_commands.append([rest_operation, rest_uri, '', 'config', resource_depth])
                    elif 'bulk' not in operation_type:
                        rest_commands.append([rest_operation, rest_uri, update_object_rest_data, 'config', resource_depth])
                        
            if 'bulk' in operation_type:
                if 'update_patch' in operation_type:
                    rest_operation = 'PATCH'
                elif 'update_put' in operation_type:
                    rest_operation = 'PUT'

                update_object = update_object._parent
                rest_uri = update_object._rest_uri()
                rest_uri_end_element = rest_uri.split('/')[-1]
                update_object_rest_data = '<{0}>{1}</{0}>'.format(rest_uri_end_element, rest_data)

                rest_commands.append([rest_operation, rest_uri, update_object_rest_data, 'config', resource_depth])

            rest_commands.reverse()
        else:
            uri = pybind_object._rest_uri() 

            pybind_object = pybind_object._parent
            
            rest_data = dicttoxml(json.loads(pybindJSON.dumps(pybind_object, mode='rest'), object_pairs_hook=OrderedDict), root=False, attr_type=False, item_func=label_list_items)

            if rest_data:
                end_marker = rest_data.rsplit('<', 1)[1].strip('/')

                rest_data = rest_data.rsplit('<', 1)[0]
                rest_data = rest_data.split(end_marker, 1)[-1]

                if operation_type == 'create' and end_marker[:-1] + '/' in uri:
                    rest_uri = uri.rsplit(end_marker[:-1] + '/', 1)[0]

                    if len(rest_uri) > 1:
                        rest_uri = rest_uri.rstrip('/')
            else:
                if operation_type == 'create':
                    uri = uri.split('/')[-1]
                    rest_data = '<' + uri + '> </' + uri + '>'
            
            if operation_type == 'delete' and rest_leaf_name:
                rest_uri += '/' + rest_leaf_name

                rest_commands.append([rest_operation, rest_uri, '', 'config', resource_depth])
            else:
                rest_commands.append([rest_operation, rest_uri, rest_data, 'config', resource_depth])

        return(rest_commands, '', timeout)

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

        return(rest_commands, yang_list, timeout)

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

        return(rest_commands, '', timeout)

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


class PySwitchLibApiRunner(DaemonRunner):
    """
    This is an auto-generated class for the PySwitchLib.
    Providing python bindings to configure a switch through the REST interface.
    """

    def __init__(self, pyswitchlib_conf=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        self._pyswitchlib_conf = pyswitchlib_conf
        self._pyro_ns_port = None
        self._nameserver_thread = threading.Thread(target=self._nameserver_loop)
        self._nameserver_thread.setDaemon(True)
        self._daemon_processes = {}
        self._daemon_id = 'default'
        self.stdin_path = os.path.join(os.sep, 'dev', 'null')
        self.stdout_path = os.path.join(os.sep, 'dev', 'null')
        self.stderr_path = os.path.join(os.sep, 'dev', 'null')
        self.pidfile_path =  pid_file
        self.pidfile_timeout = 1
        super(PySwitchLibApiRunner, self).__init__(self)

        self.daemon_context.detach_process = False

        if self._pyswitchlib_conf:
            if 'ns_port' in self._pyswitchlib_conf:
                self._pyro_ns_port = int(self._pyswitchlib_conf['ns_port'])

            for key in self._pyswitchlib_conf:
                if 'api_daemon_' in key:
                    prefixes = self._pyswitchlib_conf[key].split(':')
                    daemon_prefix = ''

                    for prefix in prefixes:
                        if os.path.exists(prefix):
                            daemon_prefix = prefix
                            break

                    if daemon_prefix:
                        daemon_process = multiprocessing.Process(target=self._daemon_loop, kwargs={'daemon_id': key, 'daemon_prefix':daemon_prefix, 'pyro_ns_port': self._pyro_ns_port})
                        daemon_process.daemon = True
                        self._daemon_processes[key] = daemon_process

        if len(self._daemon_processes) == 0:
            daemon_process = multiprocessing.Process(target=self._daemon_loop, kwargs={'daemon_id': self._daemon_id, 'daemon_prefix':sys.prefix, 'pyro_ns_port': self._pyro_ns_port})
            daemon_process.daemon = True
            self._daemon_processes[self._daemon_id] = daemon_process

    def _restart(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        daemon_id = self._get_daemon_id_for_prefix(prefix=sys.prefix)
        if daemon_id in self._daemon_processes:
            pyro_proxy_name = 'PySwitchLib.' + daemon_id

            with Pyro4.locateNS(host='localhost', port=self._pyro_ns_port) as ns:
                uri = None

                try:
                    uri = ns.lookup(pyro_proxy_name)
                except:
                    pass

                if uri:
                    with Pyro4.Proxy(uri) as pyro_proxy:
                        pyro_proxy.shutdown()
                        pyro_proxy._pyroRelease()

                    ns.remove(pyro_proxy_name)

                    daemon_thread = threading.Thread(target=self._daemon_loop, kwargs={'daemon_id': daemon_id, 'daemon_prefix':sys.prefix, 'pyro_ns_port': self._pyro_ns_port})
                    daemon_thread.setDaemon (True)
                    self._daemon_processes[daemon_id] = daemon_thread
                    self._daemon_processes[daemon_id].start()

                    api_deamon_pids = {}
                    api_deamon_pids[daemon_id] = os.getpid()
                    ConfigFileUtil().write(filename=daemon_pid_file, conf_dict=api_deamon_pids)

                    while True:
                        if self._daemon_processes[daemon_id].is_alive() == False:
                            self._daemon_processes[daemon_id].join()
                        time.sleep(5)

    def _start(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        super(PySwitchLibApiRunner, self)._start()

    def _stop(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        api_deamon_pids = ConfigFileUtil().read(filename=daemon_pid_file)

        for daemon_id in api_deamon_pids:
            try:
                os.kill(int(api_deamon_pids[daemon_id]), signal.SIGTERM)
            except:
                pass

        try:
            os.unlink(daemon_pid_file)
        except:
            pass

        super(PySwitchLibApiRunner, self)._stop()

    action_funcs = {
        'start': _start,
        'stop': _stop,
        'restart': _restart,
        }

    def _get_daemon_id_for_prefix(self, prefix=''):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        daemon_id = ''

        if self._pyswitchlib_conf:
            for key in self._pyswitchlib_conf:
                if 'api_daemon_' in key:
                    if prefix in self._pyswitchlib_conf[key]:
                        daemon_id = key
                        break

        return daemon_id

    def _get_prefix_lib_path(self, prefix='', package=''):                                                                                                                          
        """
        This is an auto-generated method for the PySwitchLib.
        """

        prefix_lib_path = ''                                                                                                                                                        
                                                                                                                                                                                    
        python_version = sys.version_info                                                                                                                                           
        python_lib_ver = 'python' + str(python_version[0]) + '.' + str(python_version[1])                                                                                           
                                                                                                                                                                                    
        lib_path = os.path.join(prefix, 'lib', python_lib_ver, 'site-packages', package)                                                                                            
                                                                                                                                                                                    
        if os.path.exists(lib_path):                                                                                                                                                
            prefix_lib_path = lib_path                                                                                                                                              
                                                                                                                                                                                    
        return prefix_lib_path

    def _get_configured_daemon(self, daemon_id='', daemon_prefix=''):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        pyro_daemon = Pyro4.Daemon()

        Pyro4.config.THREADPOOL_SIZE_MIN = 10
        Pyro4.config.THREADPOOL_SIZE = 200

        daemon_lib_path = self._get_prefix_lib_path(prefix=daemon_prefix, package='pyswitchlib')

        if daemon_lib_path:
            sys.prefix = daemon_prefix
            sys.exec_prefix = daemon_prefix
            sys.path.insert(0, daemon_lib_path)


        pyswitchlib_api_create = __import__('pyswitchlib.api.create', fromlist=['*'])
        pyswitchlib_api_update = __import__('pyswitchlib.api.update', fromlist=['*'])
        pyswitchlib_api_delete = __import__('pyswitchlib.api.delete', fromlist=['*'])
        pyswitchlib_api_get = __import__('pyswitchlib.api.get', fromlist=['*'])
        pyswitchlib_api_rpc = __import__('pyswitchlib.api.rpc', fromlist=['*'])

        map(lambda filtered_api: setattr(PySwitchLibApiDaemon, filtered_api[0], filtered_api[1]), filter(lambda api: '__' not in api[0], pyswitchlib_api_create.__dict__.items()))
        map(lambda filtered_api: setattr(PySwitchLibApiDaemon, filtered_api[0], filtered_api[1]), filter(lambda api: '__' not in api[0], pyswitchlib_api_update.__dict__.items()))
        map(lambda filtered_api: setattr(PySwitchLibApiDaemon, filtered_api[0], filtered_api[1]), filter(lambda api: '__' not in api[0], pyswitchlib_api_delete.__dict__.items()))
        map(lambda filtered_api: setattr(PySwitchLibApiDaemon, filtered_api[0], filtered_api[1]), filter(lambda api: '__' not in api[0], pyswitchlib_api_get.__dict__.items()))
        map(lambda filtered_api: setattr(PySwitchLibApiDaemon, filtered_api[0], filtered_api[1]), filter(lambda api: '__' not in api[0], pyswitchlib_api_rpc.__dict__.items()))

        api_exposed_class = Pyro4.expose(PySwitchLibApiDaemon)
        daemon_obj = api_exposed_class(pyro_daemon=pyro_daemon)

        uri = pyro_daemon.register(daemon_obj, force=True)

        return pyro_daemon, uri

    def _nameserver_loop(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        if self._pyro_ns_port:
            Pyro4.config.NS_PORT = self._pyro_ns_port

        try:
            Pyro4.locateNS(host='localhost')
        except Pyro4.errors.NamingError:
            Pyro4.naming.startNSloop(host='localhost', enableBroadcast=False)

    def _daemon_loop(self, daemon_id='', daemon_prefix='', pyro_ns_port=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        if daemon_id:
            pyro_daemon, pyro_uri = self._get_configured_daemon(daemon_id=daemon_id, daemon_prefix=daemon_prefix)

            with Pyro4.locateNS(host='localhost', port=pyro_ns_port) as ns:
                ns.register("PySwitchLib." + daemon_id, pyro_uri)
                pyro_daemon.requestLoop()
                pyro_daemon.close()

    def run(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        self._nameserver_thread.start()

        while True:
            for daemon_id in self._daemon_processes:
                if self._daemon_processes[daemon_id].ident == None and self._nameserver_thread.is_alive() == True:
                    self._daemon_processes[daemon_id].start()

            time.sleep(5)

if __name__ == "__main__":
    pyswitchlib_conf = ConfigFileUtil().read(filename=pyswitchlib_conf_file)

    if len(sys.argv) >= 2:
        if sys.argv[1] == 'start':
            if os.path.exists(pid_file):
                with open(pid_file, 'r') as pid:
                    if os.path.isdir(os.path.join(os.sep, 'proc', pid.readline().rstrip())):
                        print(sys.argv[0].split('/')[-1] + ' is already started.')
                        sys.exit(1)
        elif sys.argv[1] == 'restart':
            if not os.path.exists(pid_file):
                print(sys.argv[0].split('/')[-1] + ' is not started.')
                sys.exit(2)
        elif sys.argv[1] == 'status':
            if os.path.exists(pid_file):
                with open(pid_file, 'r') as pid:
                    proc_pid = pid.readline().rstrip()

                    if os.path.isdir(os.path.join(os.sep, 'proc', proc_pid)):
                        print(sys.argv[0].split('/')[-1] + ' (pid ' + proc_pid + ') is running...')
                        sys.exit(0)
                    else:
                        print(sys.argv[0].split('/')[-1] + ' is stopped.')
                        sys.exit(3)
            else:
                print(sys.argv[0].split('/')[-1] + ' is stopped.')
                sys.exit(3)

    if len(sys.argv) == 3 and sys.argv[1] != 'stop':
        pyswitchlib_conf['ns_port'] = sys.argv[2]

        ConfigFileUtil().write(filename=pyswitchlib_conf_file, conf_dict=pyswitchlib_conf)

    pyswitchlib_runner = PySwitchLibApiRunner(pyswitchlib_conf=pyswitchlib_conf)
    pyswitchlib_runner.parse_args(argv=sys.argv)

    try:
        pyswitchlib_runner.do_action()
    except (LockTimeout, DaemonRunnerStopFailureError) as e:
        sys.exit()

