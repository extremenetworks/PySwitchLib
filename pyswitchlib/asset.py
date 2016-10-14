import pyswitchlib
import requests
import weakref

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
        self._proxied = pyswitchlib.PySwitchLib(ver=fw_ver, rest_operation=self._rest_operation)

        def on_deletion (killed_ref):
            self._session.close()

        self._weakref = weakref.ref(self, on_deletion)

    def __getattr__(self, name):
        return getattr(self._proxied, name)

    def _rest_operation(self, rest_commands):
        url = "http://"+self._ip_addr+"/rest/config/running"
        header = {"Resource-Depth" : "2"}
        auth = self._auth
        del self._overall_status[:]

        response = self._response

        for rest_cmd in rest_commands:
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

