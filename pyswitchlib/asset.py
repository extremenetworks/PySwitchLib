import requests
import weakref
import re
import os
import sys
import threading
import xml.etree.ElementTree as ElementTree
import xmltodict
import json
import atexit
import Pyro4
import Pyro4.util
import Pyro4.errors
from distutils.sysconfig import get_python_lib
import time

from requests.packages.urllib3.exceptions import SubjectAltNameWarning
requests.packages.urllib3.disable_warnings(SubjectAltNameWarning)

from pyswitchlib.util.configFile import ConfigFileUtil
import pyswitchlib.exceptions
locals().update(pyswitchlib.exceptions.__dict__)

sys.excepthook = Pyro4.util.excepthook


class Asset(object):
    """
    This is an auto-generated class for the PySwitchLib device asset.
    Asset provides connection information for PySwitchLib APIs.
    """

    def __init__(self, ip_addr='', auth=('admin', 'password'), rest_proto=None, cacert=None, fw_ver='', timeout='', api_port=None):
        def on_deletion (killed_ref):
            self._cleanup_timer_handle()
            self._session.close()
            self._response.close()

        atexit.register(self._cleanup_timer_handle)
        self._weakref = weakref.ref(self, on_deletion)

        self._ip_addr = ip_addr
        self._auth = auth
        self._rest_proto_input = ''
        self._rest_protocol = 'http'
        self._attempted_rest_protocols = []
        self._enabled_rest_protocols = []
        self._cacert_input = ''
        self._os_type = 'unknown'
        self._os_ver = fw_ver
        self._os_full_ver = fw_ver
        self._default_connection_timeout = 60
        self._default_response_timeout = 1800
        self._default_session_verify = False
        self._session_timeout = (self._default_connection_timeout, self._default_response_timeout)
        self._session = requests.Session()
        self._response = requests.Response()
        self._overall_success = True
        self._overall_status = []
        self._exc_info = None

        self._rest_session_auth_max_retries = 1
        self._rest_session_auth_token_expiration = 160
        self._rest_session_auth_token_expired = '_EXPIRED_'
        self._rest_session_auth_token = self._rest_session_auth_token_expired
        self._rest_session_timer_handle = None
        self._rest_config_path = '/rest/config/running'
        self._rest_operational_path = '/rest/operational-state'
        self._rest_rpc_path = '/rest/operational-state'
        self._rest_discover_path = '/rest'
        self._yang_list = None
        self._module_obj = None

        self._pyro_ns_port = None
        self._pyro_proxy_name = ''
        self._pyro_daemon_id = 'default'
        self._pyro_bind_max_retries = 30
        self._ns_pid_file = os.path.join(os.sep, 'etc', 'pyswitchlib', '.pyswitchlib_ns.pid')
        self._pyswitchlib_conf_filename = os.path.join(os.sep, 'etc', 'pyswitchlib', 'pyswitchlib.conf')
        self._pyswitchlib_ns_daemon_filename = os.path.join(os.sep, 'etc', 'pyswitchlib', '.pyswitchlib_ns_daemon.uri')
        self._pyswitchlib_conf = ConfigFileUtil().read(filename=self._pyswitchlib_conf_filename)
        self._pyswitchlib_ns_daemon = ConfigFileUtil().read(filename=self._pyswitchlib_ns_daemon_filename)

        for key in self._pyswitchlib_conf:
            if 'ns_port' == key:
                self._pyro_ns_port = int(self._pyswitchlib_conf[key])
            elif 'api_daemon_' in key:
                if sys.prefix in self._pyswitchlib_conf[key]:
                    self._pyro_daemon_id = key
            elif 'cacert' == key:
                if cacert is None:
                    cacert = self._pyswitchlib_conf[key]

        if api_port:
            self._pyro_ns_port = api_port

        if os.path.exists(self._ns_pid_file):
            self._pyro_proxy_name = 'PYRONAME:PySwitchLib.' + self._pyro_daemon_id

            if self._pyro_ns_port:
                self._pyro_proxy_name += '@localhost:' + str(self._pyro_ns_port)
        else:
            if self._pyswitchlib_ns_daemon:
                if self._pyro_daemon_id in self._pyswitchlib_ns_daemon:
                    self._pyro_proxy_name = self._pyswitchlib_ns_daemon[self._pyro_daemon_id]

        if rest_proto is not None:
            if rest_proto.lower() == 'http' or rest_proto.lower() == 'https' or rest_proto.lower() == 'auto':
                self._rest_proto_input = rest_proto.lower()

                if self._rest_proto_input == 'http' or self._rest_proto_input == 'https':
                    self._rest_protocol = self._rest_proto_input
            else:
                raise RestProtocolTypeError("Rest protocol type must be 'http', 'https', or 'auto'.  '" + rest_proto + "' was specified.")

        if cacert is not None:
            self._cacert_input = cacert

            if cacert:
                if self._rest_protocol == 'https' or self._rest_proto_input == 'auto':
                    if os.path.isfile(cacert):
                        self._default_session_verify = cacert
                    else:
                        raise CACertificateNotFoundError("The CA certificate file '" + cacert + "' could not be found.")
                else:
                    self._default_session_verify = False
            elif cacert is False:
                self._default_session_verify = False
            else:
                raise CACertificateNotSpecifiedError("The path to the CA certificate file is not specified.")
        else:
            self._default_session_verify = False

        if timeout != '':
            self._session_timeout = timeout

        self._create_timer_handle()
        self._discover_rest_protocol_and_paths()
        self._update_fw_version()
        self._supported_module_name = self._get_supported_module()

        with Pyro4.Proxy(self._pyro_proxy_name) as pyro_proxy:
            for n in range(self._pyro_bind_max_retries):
                try:
                    pyro_proxy._pyroBind()
                except (Pyro4.errors.NamingError, Pyro4.errors.CommunicationError) as e:
                    if n == 0:
                        if self._pyswitchlib_conf and 'ns_port' in self._pyswitchlib_conf:
                            bound_api_port = int(self._pyswitchlib_conf['ns_port'])

                            if bound_api_port and self._pyro_ns_port and bound_api_port != self._pyro_ns_port:
                                raise ExistingApiPortBound("API port: " + str(bound_api_port) + " is already bound.")

                        pyswitchlib_api_daemon = os.path.join(get_python_lib(), 'pyswitchlib', 'pyswitchlib_api_daemon.py')
                        pyswitchlib_api_start_string = 'python ' + pyswitchlib_api_daemon + ' start'

                        if self._pyro_ns_port:
                            pyswitchlib_api_start_string += ' ' + str(self._pyro_ns_port)

                        os.system(pyswitchlib_api_start_string)
                else:
                    break

                time.sleep(1)

            else:
                raise ApiDaemonConnectionError("Cannot connect to pyswitchlib_api_daemon.py.")

            self._proxied = pyro_proxy

    def __getattr__(self, name):
        if hasattr(self._proxied, name):
            def getattr_wrapper(*args, **kwargs):
                self._proxied.api_acquire()
                self._proxied.module_name(module_name=self._supported_module_name)
                rest_operation_tuple = ()

                try:
                    rest_operation_tuple = getattr(self._proxied, name)(*args, **kwargs)
                except Exception as e:
                    raise e
                finally:
                    self._proxied.api_release()

                return self._rest_operation(rest_commands=rest_operation_tuple[0], yang_list=rest_operation_tuple[1], timeout=rest_operation_tuple[2])
            return getattr_wrapper
        else:
            raise AttributeError(name)

    def _rest_operation(self, rest_commands=None, yang_list=None, rest_proto=None, cacert=None, timeout=None):
        auth = self._auth
        auth_retries = 0
        index = 0
        rest_protocol = None
        del self._overall_status[:]

        if rest_proto is not None:
            rest_protocol = rest_proto
        else:
            rest_protocol = self._rest_protocol

        if cacert is not None:
            self._session.verify = cacert
        else:
            self._session.verify = self._default_session_verify

        if isinstance(timeout, basestring):
            if timeout == '':
                timeout = self._session_timeout

        self._cleanup_timer_handle()
        self._create_timer_handle()

        while index < len(rest_commands):
            rest_cmd = rest_commands[index]

            if len(rest_cmd) < 4:
                rest_cmd.append ("config")

            if rest_cmd[3] == "config":
                uri_prefix_path = self._rest_config_path
            elif rest_cmd[3] == "operational":
                uri_prefix_path = self._rest_operational_path
            elif rest_cmd[3] == "rpc":
                uri_prefix_path = self._rest_rpc_path
            elif rest_cmd[3] == "discover":
                uri_prefix_path = self._rest_discover_path

            header = {"Resource-Depth" : str(rest_cmd[4])}
            url = rest_protocol+"://"+self._ip_addr+uri_prefix_path

            self._session.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})

            if self._rest_session_auth_token != self._rest_session_auth_token_expired:
                self._session.headers.update({'Authentication-Token': self._rest_session_auth_token})
            else:
                if 'Authentication-Token' in self._session.headers:
                    self._session.headers.pop('Authentication-Token')

            if rest_cmd[0] == "GET":
                if self._rest_session_auth_token == self._rest_session_auth_token_expired:
                    self._response = self._session.get(url + rest_cmd[1], headers=header, auth=auth, timeout=timeout)
                else:
                    self._response = self._session.get(url + rest_cmd[1], headers=header, timeout=timeout)
            elif rest_cmd[0] == "POST":
                if self._rest_session_auth_token == self._rest_session_auth_token_expired:
                    self._response = self._session.post(url + rest_cmd[1], auth=auth, data=rest_cmd[2], timeout=timeout)
                else:
                    self._response = self._session.post(url + rest_cmd[1], data=rest_cmd[2], timeout=timeout)
            elif rest_cmd[0] == "PUT":
                if self._rest_session_auth_token == self._rest_session_auth_token_expired:
                    self._response = self._session.put(url + rest_cmd[1], auth=auth, data=rest_cmd[2], timeout=timeout)
                else:
                    self._response = self._session.put(url + rest_cmd[1], data=rest_cmd[2], timeout=timeout)
            elif rest_cmd[0] == "PATCH":
                if self._rest_session_auth_token == self._rest_session_auth_token_expired:
                    self._response = self._session.patch(url + rest_cmd[1], auth=auth, data=rest_cmd[2], timeout=timeout)
                else:
                    self._response = self._session.patch(url + rest_cmd[1], data=rest_cmd[2], timeout=timeout)
            elif rest_cmd[0] == "DELETE":
                if self._rest_session_auth_token == self._rest_session_auth_token_expired:
                    self._response = self._session.delete(url + rest_cmd[1], auth=auth, timeout=timeout)
                else:
                    self._response = self._session.delete(url + rest_cmd[1], timeout=timeout)

            if 'Authentication-Token' in self._response.headers:
                self._rest_session_auth_token = self._response.headers['Authentication-Token']

            json_output = json.loads('{"output": ""}')
            text_response = self._response.text

            if self._response.status_code >= 200 and self._response.status_code <= 299:
                if re.match('^<', self._response.text):
                    if rest_cmd[3] != "rpc":
                        text_response = '<output>\r\n' + self._response.text + '</output>\r\n'

                    json_output = json.loads(self._xml_to_json(text_response))
            else:
                self._auth_token_expiration()

                if self._response.status_code == 401 and auth_retries < self._rest_session_auth_max_retries:
                    auth_retries += 1
                    continue

                if re.match('^<', self._response.text):
                    if re.match('^<output', self._response.text):
                        json_output = json.loads(self._xml_to_json(text_response))
                    else:
                        json_output = json.loads('{"output": ' + self._xml_to_json(text_response) + '}')
                else:
                    json_output = json.loads('{"output": ' + json.dumps(str(self._response.text)) + '}')

            if yang_list:
                self._format_dict_output(container=json_output, keys=yang_list)

            self._overall_status.append({self._ip_addr : {'request': {'op_code': rest_cmd[0], 'uri': rest_cmd[1], 'data': rest_cmd[2]}, 'response': {'status_code': self._response.status_code, 'url': self._response.url, 'text': self._response.text, 'json': json_output}}})

            index += 1

        if not self._rest_session_timer_handle.is_alive():
            self._rest_session_timer_handle.start()

        return self._get_results()

    def _get_results(self):
        self._overall_success = True

        if self._overall_status:
            for status in self._overall_status:
                for key in status:
                    if (status[key]['response']['status_code'] < 200) or (status[key]['response']['status_code'] > 299):
                        self._overall_success = False
        else:
            self._overall_success = False

        return self._overall_success, self._overall_status

    def _discover_rest_protocol_and_paths(self):
        status, result = self._do_rest_protocol_discovery(self._rest_proto_input)

        if status == False:
            self._raise_rest_validation_exception(result)

        self._update_uri_prefix_paths(result)

    def _update_fw_version(self):
        rest_command = (
            ["POST", "/show-firmware-version", "", "rpc", 1],
        )

        self._rest_operation(rest_command, timeout=(self._default_connection_timeout, self._default_connection_timeout*2))

        status, result = self._get_results()

        if status == False:                                                                                                                                                         
            self._raise_rest_validation_exception(result)

        try:
            rest_root = ElementTree.fromstring(re.sub(' xmlns[^ \t\n\r\f\v>]+', '', result[0][self._ip_addr]['response']['text']))

            if rest_root.find('show-firmware-version').find('os-name') is not None:
                if 'Network Operating System' in rest_root.find('show-firmware-version').find('os-name').text:
                    self._os_type = 'nos'
                elif 'SLX' in rest_root.find('show-firmware-version').find('os-name').text:
                    self._os_type = 'slxos'

            if 'Server' in self._response.headers:
                if 'NOS' in self._response.headers['Server']:
                    self._os_type = 'nos'
                elif 'SLX' in self._response.headers['Server']:
                    self._os_type = 'slxos'

            if rest_root.find('show-firmware-version').find('firmware-full-version') is not None:
                self._os_full_ver = rest_root.find('show-firmware-version').find('firmware-full-version').text

            if rest_root.find('show-firmware-version').find('os-version') is not None:
                self._os_ver = rest_root.find('show-firmware-version').find('os-version').text

                if self._os_type == 'slxos':
                    slxos_ver = self._os_ver.split('.')

                    if len(slxos_ver) >= 2:
                        slxos_pattern_string = '^({0}[rs]{{1}})\.{1}\.'.format(slxos_ver[0], slxos_ver[1])
                    elif len(slxos_ver) == 1:
                        slxos_pattern_string = '^({0}[rs]{{1}})\.'.format(slxos_ver[0])
                    else:
                        slxos_pattern_string = '^(\d+[rs]{1})\.'

                    slxos_pattern = re.compile(slxos_pattern_string)

                    match = slxos_pattern.match(self._os_full_ver)

                    if match:
                        slxos_ver[0] = match.group(1)
                        self._os_ver = '.'.join(slxos_ver)

        except:
            pass

    def _do_rest_protocol_discovery(self, rest_proto_input):
        rest_command = (
            ["GET", "", "", "discover", 1],
        )

        overall_status = None
        overall_result = None

        if rest_proto_input == 'auto':
            self._attempted_rest_protocols.append('http')

            try:
                self._rest_operation(rest_command, rest_proto='http', timeout=(self._default_connection_timeout, self._default_connection_timeout*2))
            except:
                pass
            finally:
                overall_status, overall_result = self._get_results()

                if (overall_status == True):
                    self._enabled_rest_protocols.append('http')

            self._attempted_rest_protocols.append('https')

            try:
                self._rest_operation(rest_command, rest_proto='https', cacert=False, timeout=(self._default_connection_timeout, self._default_connection_timeout*2))
            except:
                pass
            finally:
                status, result = self._get_results()

                if (status == True):
                    self._session.close()
                    self._session = requests.Session()
                    self._session.verify = self._default_session_verify

                    self._enabled_rest_protocols.append('https')
                    self._rest_protocol = 'https'

                    overall_status = status
                    overall_result = result
        else:
            self._attempted_rest_protocols.append(self._rest_protocol)

            try:
                self._rest_operation(rest_command, timeout=(self._default_connection_timeout, self._default_connection_timeout*2))
            except:
                self._exc_info = sys.exc_info()
            finally:
                overall_status, overall_result = self._get_results()

                if (overall_status == True):
                    self._enabled_rest_protocols.append(self._rest_protocol)

        return overall_status, overall_result

    def _update_uri_prefix_paths(self, result):
        try:
            rest_root = ElementTree.fromstring(re.sub(' xmlns[^ \t\n\r\f\v>]+|y:', '', result[0][self._ip_addr]['response']['text']))

            if rest_root.find('config').find('running') is not None:
                self._rest_config_path = rest_root.find('config').find('running').get('self')

            if rest_root.find('operational-state') is not None:
                self._rest_rpc_path = rest_root.find('operational-state').get('self')
                self._rest_operational_path = rest_root.find('operational-state').get('self')

            if rest_root.find('operations') is not None:
                self._rest_rpc_path = rest_root.find('operations').get('self')
        except:
            pass

    def _raise_rest_validation_exception(self, result):
        if result:
            if result[0][self._ip_addr]['response']['status_code'] == 401:
                raise InvalidAuthenticationCredentialsError('Status Code: ' + str(result[0][self._ip_addr]['response']['status_code']) + ', Error: Invalid Authentication Credentials.')
            elif result[0][self._ip_addr]['response']['status_code'] == 404:
                raise RestInterfaceError('Status Code: ' + str(result[0][self._ip_addr]['response']['status_code']) + ', Error: Not Found.')
        else:
            try:
                if self._exc_info:
                    raise self._exc_info[0], self._exc_info[1], self._exc_info[2]
            except Exception as e:
                raise RestInterfaceError('Could not establish a connection to ' + self._ip_addr + ' using ' + str(self._attempted_rest_protocols) + '. Reason: ' + str(e))

    def _update_max_keep_alive_requests(self, max_requests=0):
        return self.run_command(command="unhide foscmd;fibranne;foscmd sed \\'s/MaxKeepAliveRequests [0-9]*/MaxKeepAliveRequests " + str(max_requests) + "/\\' /fabos/webtools/bin/httpd.conf > /fabos/webtools/bin/httpd.conf.temp&&mv /fabos/webtools/bin/httpd.conf.temp /fabos/webtools/bin/httpd.conf&&/usr/apache/bin/apachectl -k restart &")

    def _xml_to_json(self, xml=''):
        return json.dumps(xmltodict.parse(xml))

    def _get_supported_module(self):
        pybind_dir = ''
        site_dir = sys.path

        for site_path in site_dir:
            pybind_dir = os.path.join(site_path, 'pybind')
            if os.path.isdir(pybind_dir):
                pybind_dir = os.path.join(pybind_dir, self._os_type)
                break

        pybind_ver_tree = {}

        max_depth = 1
        cur_depth = pybind_dir.count(os.sep)
        max_os_walk_depth = cur_depth + max_depth

        for (dirpath, dirs, files) in os.walk(pybind_dir):
            if dirpath.count(os.sep) >= max_os_walk_depth:
                del dirs[:]

            submodule = dirpath.partition(pybind_dir)[2].lstrip('/').replace(os.sep, '.')

            if submodule:
                tuple = submodule.strip('v_').split('_')

                for index, elem in enumerate(tuple):
                    if index == 0:
                        if elem not in pybind_ver_tree:
                            pybind_ver_tree[elem] = {}
                    elif index == 1:
                        if elem not in pybind_ver_tree[tuple[0]]:
                            pybind_ver_tree[tuple[0]][elem] = {}
                    elif index == 2:
                        if elem not in pybind_ver_tree[tuple[0]][tuple[1]]:
                            pybind_ver_tree[tuple[0]][tuple[1]][elem] = {}
                    elif index == 3:
                        if elem not in pybind_ver_tree[tuple[0]][tuple[1]][tuple[2]]:
                            pybind_ver_tree[tuple[0]][tuple[1]][tuple[2]][elem] = {}

        os_version_tuple = self._os_ver.strip('.').split('.')
        supported_os_version = []

        if os_version_tuple[0] in pybind_ver_tree:
            supported_os_version.append(os_version_tuple[0])
        else:
            for major in sorted(pybind_ver_tree, reverse=True):
                if os_version_tuple[0] >= re.sub('\D', '', major):
                    supported_os_version.append(major)
                    break;

        if len(supported_os_version) < 1:
            raise UnsupportedOSError("OS Version: " + self._os_type + " " + self._os_ver + " is unsupported.")

        if supported_os_version[0] == os_version_tuple[0] and os_version_tuple[1] in pybind_ver_tree[supported_os_version[0]]:
            supported_os_version.append(os_version_tuple[1])
        else:
            for minor in sorted(pybind_ver_tree[supported_os_version[0]], reverse=True):
                if supported_os_version[0] == os_version_tuple[0]:
                    if os_version_tuple[1] >= minor:
                        supported_os_version.append(minor)
                        break;
                else:
                    supported_os_version.append(minor)
                    break;

        if len(supported_os_version) >= 2:
            if supported_os_version[0] == os_version_tuple[0] and supported_os_version[1] == os_version_tuple[1] and os_version_tuple[2] in pybind_ver_tree[supported_os_version[0]][supported_os_version[1]]:
                supported_os_version.append(os_version_tuple[2])
            else:
                for patch in sorted(pybind_ver_tree[supported_os_version[0]][supported_os_version[1]], reverse=True):
                    if supported_os_version[0] == os_version_tuple[0] and supported_os_version[1] == os_version_tuple[1]:
                        if os_version_tuple[2] >= patch or len(pybind_ver_tree[supported_os_version[0]][supported_os_version[1]]) == 1:
                            supported_os_version.append(patch)
                            break;
                    else:
                        supported_os_version.append(patch)
                        break;
        else:
            for minor in sorted(pybind_ver_tree[supported_os_version[0]], reverse=True):
                supported_os_version.append(minor)
                break;

            for patch in sorted(pybind_ver_tree[supported_os_version[0]][supported_os_version[1]], reverse=True):
                supported_os_version.append(patch)
                break;

        safe_os_version = 'v'+'_'.join(supported_os_version)
        package_name = '.'.join(['pybind', self._os_type, safe_os_version])

        return package_name

    def _load_module(self, supported_module_name=''):
        if supported_module_name:
            self._module_obj =  __import__(supported_module_name, fromlist=['*'])

    def _auth_token_expiration(self):
        self._rest_session_auth_token = self._rest_session_auth_token_expired
        self._cleanup_timer_handle()
        self._create_timer_handle()

    def _create_timer_handle(self):
        self._rest_session_timer_handle = threading.Timer(self._rest_session_auth_token_expiration, self._auth_token_expiration)
        self._rest_session_timer_handle.daemon = True

    def _cleanup_timer_handle(self):
        if self._rest_session_timer_handle:
            if self._rest_session_timer_handle.is_alive():
                self._rest_session_timer_handle.cancel()
                self._rest_session_timer_handle = None

    def _format_dict_output(self, container=None, keys=None):
        if keys and container:
            if isinstance(container, dict):
                for k in container:
                    if isinstance(container[k], dict):
                        if k.lower() in keys:
                            keys.remove(k.lower())
                            container[k] = [container[k]]
                            self._format_dict_output(container=container[k], keys=keys)
                        else:
                            self._format_dict_output(container=container[k], keys=keys)
                    elif isinstance(container[k], list):
                        for elem in container[k]:
                            self._format_dict_output(container=elem, keys=keys)
            elif isinstance(container, list):
                for elem in container:
                    self._format_dict_output(container=elem, keys=keys)

    def get_os_type(self):
        """
        This is an auto-generated method for the PySwitchLib.

        :rtype: *string*
        :returns: Returns "nos" or "slxos" of the approprate switch type.
        """
        return self._os_type

    def get_os_version(self):
        """
        This is an auto-generated method for the PySwitchLib.

        :rtype: *string*
        :returns: Returns "os-version" value from the show-firmware-version RPC call.
        """
        return self._os_ver

    def get_os_full_version(self):
        """
        This is an auto-generated method for the PySwitchLib.

        :rtype: *string*
        :returns: Returns "full-firmware-version" value from the show-firmware-version RPC call.
        """
        return self._os_full_ver

    def get_xml_output(self):
        """
        This is an auto-generated method for the PySwitchLib.

        :rtype: *string*
        :returns: Returns the xml output response from the last api call.
        """
        return self._overall_status[0][self._ip_addr]['response']['text']

    def get_dict_output(self):
        """
        This is an auto-generated method for the PySwitchLib.

        :rtype: *dict*
        :returns: Returns the json output response from the last api call.
        """
        return self._overall_status[0][self._ip_addr]['response']['json']['output']

    def get_supported_module_name(self):
        """
        This is an auto-generated method for the PySwitchLib.

        :rtype: *string*
        :returns: Returns the path name of the selected pybind module.
        """
        return self._supported_module_name

    def get_enabled_rest_protocols(self):
        """
        This is an auto-generated method for the PySwitchLib.

        :rtype: *list*
        :returns: Returns the enabled rest protocols for the asset.
        """
        return self._enabled_rest_protocols

    def run_command(self, command=''):
        """
        This is an auto-generated method for the PySwitchLib.

        :rtype: (*bool, list*)
        :returns: Returns a tuple.

            #. **api_success** (*bool*) - The success or failure of the API.
            #. **details** (*list*) - List of REST request/response dictionaries, keyed by the asset's ip address.
        """

        rest_command = (
            ["POST", "/runcmd", command, "discover", 1],
        )

        self._rest_operation(rest_command)

        return self._get_results()


