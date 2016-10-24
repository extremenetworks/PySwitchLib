import pyswitchlib
import requests
import weakref
import re
import xml.etree.ElementTree as ElementTree

class Asset(object):
    """
    This is an auto-generated class for the PySwitchLib device asset.
    Asset provides connection information for PySwitchLib APIs.    """


    def __init__(self, ip_addr='', auth=('admin', 'password'), fw_ver=''):
        self._ip_addr = ip_addr
        self._auth = auth
        self._fw_ver = fw_ver
        self._session = requests.Session()
        self._response = requests.Response()
        self._overall_success = True
        self._overall_status = []

        def on_deletion (killed_ref):
            self._session.close()

        self._weakref = weakref.ref(self, on_deletion)

        self._rest_config_path = '/rest/config/running'
        self._rest_operational_path = '/rest/operational-state'
        self._rest_rpc_path = '/rest/operations'
        self._rest_discover_path = '/rest'

        self._update_uri_prefix_paths()
        self._update_fw_version()

        self._proxied = pyswitchlib.PySwitchLib(ver=self._fw_ver, rest_operation=self._rest_operation)

    def __getattr__(self, name):
        return getattr(self._proxied, name)

    def _rest_operation(self, rest_commands):
        header = {"Resource-Depth" : "2"}
        auth = self._auth
        del self._overall_status[:]

        response = self._response

        for rest_cmd in rest_commands:
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

            url = "http://"+self._ip_addr+uri_prefix_path

            if rest_cmd[0] == "GET":
                self._response = self._session.get(url + rest_cmd[1], headers=header, auth=auth)
            elif rest_cmd[0] == "POST":
                self._response = self._session.post(url + rest_cmd[1], auth=auth, data=rest_cmd[2])
            elif rest_cmd[0] == "PUT":
                self._response = self._session.put(url + rest_cmd[1], auth=auth, data=rest_cmd[2])
            elif rest_cmd[0] == "PATCH":
                self._response = self._session.patch(url + rest_cmd[1], auth=auth, data=rest_cmd[2])
            elif rest_cmd[0] == "DELETE":
                self._response = self._session.delete(url + rest_cmd[1], auth=auth)

            self._overall_status.append({self._ip_addr : {'request': {'op_code': rest_cmd[0], 'uri': rest_cmd[1], 'data': rest_cmd[2]}, 'response': {'status_code': self._response.status_code, 'url': self._response.url, 'text': self._response.text}}})

        return self._get_results()

    def _get_results(self):
        self._overall_success = True

        for status in self._overall_status:
            for key in status:
                if (status[key]['response']['status_code'] < 200) or (status[key]['response']['status_code'] > 299):
                    self._overall_success = False

        return self._overall_success, self._overall_status
    def _update_fw_version(self):
        rest_command = (
            ["POST", "/show-firmware-version", "", "rpc"],
        )

        self._rest_operation(rest_command)

        status, result = self._get_results()

        try:
            rest_root = ElementTree.fromstring(re.sub(" xmlns*='[^']+'", '', result[0][self._ip_addr]['response']['text']))

            if rest_root.find('show-firmware-version').find('os-name') is not None:
                if 'Network Operating System' in rest_root.find('show-firmware-version').find('os-name').text:
                    self._fw_ver = 'nos'
                elif 'SLX' in rest_root.find('show-firmware-version').find('os-name').text:
                    self._fw_ver = 'slxos'

            if rest_root.find('show-firmware-version').find('os-version') is not None:
                self._fw_ver += rest_root.find('show-firmware-version').find('os-version').text
        except:
            pass

    def _update_uri_prefix_paths(self):
        rest_command = (
            ["GET", "", "", "discover"],
        )

        self._rest_operation(rest_command)

        status, result = self._get_results()

        try:
            rest_root = ElementTree.fromstring(re.sub(' xmlns[:y]*="[^"]+"|y:', '', result[0][self._ip_addr]['response']['text']))

            if rest_root.find('config').find('running') is not None:
                self._rest_config_path = rest_root.find('config').find('running').get('self')

            if rest_root.find('operational-state') is not None:
                self._rest_rpc_path = rest_root.find('operational-state').get('self')
                self._rest_operational_path = rest_root.find('operational-state').get('self')

            if rest_root.find('operations') is not None:
                self._rest_rpc_path = rest_root.find('operations').get('self')
        except:
            pass


