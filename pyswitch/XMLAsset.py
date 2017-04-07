import re
import json
from pyswitchlib.asset import Asset

class XMLAsset(Asset):
    def __init__(self, ip_addr='', auth=('admin', 'password'), fw_ver='', timeout=''):
        super(XMLAsset, self).__init__(ip_addr=ip_addr, auth=auth ,fw_ver=fw_ver, timeout=timeout)

    def _rest_operation(self, rest_commands=None, yang_list=None, timeout=None):
        auth = self._auth
        auth_retries = 0
        index = 0
        del self._overall_status[:]

        if isinstance(timeout, basestring):
            if timeout == '':
                timeout = self._session_timeout

        self._cleanup_timer_handle()
        self._create_timer_handle()

        while index < len(rest_commands):
            rest_cmd = rest_commands[index]

            if len(rest_cmd) < 4:
                rest_cmd.append("config")

            if rest_cmd[3] == "config":
                uri_prefix_path = self._rest_config_path
            elif rest_cmd[3] == "operational":
                uri_prefix_path = self._rest_operational_path
            elif rest_cmd[3] == "rpc":
                uri_prefix_path = self._rest_rpc_path
            elif rest_cmd[3] == "discover":
                uri_prefix_path = self._rest_discover_path

            header = {"Resource-Depth": str(rest_cmd[4])}
            url = "http://" + self._ip_addr + uri_prefix_path

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
                    self._response = self._session.patch(url + rest_cmd[1], auth=auth, data=rest_cmd[2],
                                                         timeout=timeout)
                else:
                    self._response = self._session.patch(url + rest_cmd[1], data=rest_cmd[2], timeout=timeout)
            elif rest_cmd[0] == "DELETE":
                if self._rest_session_auth_token == self._rest_session_auth_token_expired:
                    self._response = self._session.delete(url + rest_cmd[1], auth=auth, timeout=timeout)
                else:
                    self._response = self._session.delete(url + rest_cmd[1], timeout=timeout)

            if 'Authentication-Token' in self._response.headers:
                self._rest_session_auth_token = self._response.headers['Authentication-Token']


            text_response = self._response.text

            if self._response.status_code >= 200 and self._response.status_code <= 299:
                if re.match('^<', self._response.text):
                    if rest_cmd[3] != "rpc":
                        text_response = '<output>\r\n' + self._response.text + '</output>\r\n'

            else:
                self._auth_token_expiration()

                if self._response.status_code == 401 and auth_retries < self._rest_session_auth_max_retries:
                    auth_retries += 1
                    continue

            self._overall_status.append({self._ip_addr: {
                'request': {'op_code': rest_cmd[0], 'uri': rest_cmd[1], 'data': rest_cmd[2]},
                'response': {'status_code': self._response.status_code, 'url': self._response.url,
                             'text': self._response.text}}})

            index += 1

        if not self._rest_session_timer_handle.is_alive():
            self._rest_session_timer_handle.start()

        return self._get_results()



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
        xml_output = self.get_xml_output()
        print xml_output

        if not re.match('^<output', xml_output):
            xml_output = '<output>\r\n' + xml_output + '</output>\r\n'

        dict_output = json.loads(self._xml_to_json(xml_output))

        if dict_output and self._yang_list:
            self._format_dict_output(container=dict_output, keys=self._yang_list)

        return dict_output