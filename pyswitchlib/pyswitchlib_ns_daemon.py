import os
import sys
import time
import threading
import Pyro4
import Pyro4.naming
from pyswitchlib.util.configFile import ConfigFileUtil
from pyswitchlib.util.config import ConfigUtil
from daemon.runner import (DaemonRunner, DaemonRunnerStopFailureError)
from lockfile import LockTimeout

pyswitchlib_conf_file = os.path.join(os.sep, 'etc', 'pyswitchlib', 'pyswitchlib.conf')
pid_file = os.path.join(os.sep, 'etc', 'pyswitchlib', '.pyswitchlib_ns.pid')


class PySwitchLibNsDaemon(DaemonRunner):
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
        self.stdin_path = os.path.join(os.sep, 'dev', 'null')
        self.stdout_path = os.path.join(os.sep, 'dev', 'null')
        self.stderr_path = os.path.join(os.sep, 'dev', 'null')
        self.pidfile_path =  pid_file
        self.pidfile_timeout = 1
        super(PySwitchLibNsDaemon, self).__init__(self)

        if self._pyswitchlib_conf:
            if 'ns_port' in self._pyswitchlib_conf:
                self._pyro_ns_port = int(self._pyswitchlib_conf['ns_port'])

    def _restart(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        for key in self._pyswitchlib_conf:
            if 'api_daemon' in key:
                pyro_proxy_name = 'PySwitchLib.' + key

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

    def _start(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        super(PySwitchLibNsDaemon, self)._start()

    def _stop(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        super(PySwitchLibNsDaemon, self)._stop()

    action_funcs = {
        'start': _start,
        'stop': _stop,
        'restart': _restart,
        }

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

    def run(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """

        self._nameserver_thread.start()

        while True:
            time.sleep(5)

if __name__ == "__main__":
    pyswitchlib_conf = ConfigFileUtil().read(filename=pyswitchlib_conf_file)

    if len(sys.argv) >= 2:
        if sys.argv[1] == 'start':
            if os.path.exists(pid_file):
                with open(pid_file, 'r') as pid:
                    if os.path.isdir(os.path.join(os.sep, 'proc', pid.readline().rstrip())):
                        print(sys.argv[0].split('/')[-1] + ' is already started.')
                        sys.exit(0)
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

    pyswitchlib_runner = PySwitchLibNsDaemon(pyswitchlib_conf=pyswitchlib_conf)
    pyswitchlib_runner.parse_args(argv=sys.argv)

    try:
        pyswitchlib_runner.do_action()
    except (LockTimeout, DaemonRunnerStopFailureError) as e:
        sys.exit()

