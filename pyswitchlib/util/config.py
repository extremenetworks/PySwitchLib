import os
import sys

class ConfigUtil(object):
    """
    This is an auto-generated class for the PySwitchLib device asset.
    Asset provides connection information for PySwitchLib APIs.
    """

    def get_daemon_id_for_prefix(self, prefix='', conf_dict=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """
        daemon_id = ''

        if conf_dict:
            for key in conf_dict:
                if 'api_daemon_' in key:
                    if prefix in conf_dict[key]:
                        daemon_id = key
                        break

        return daemon_id

    def get_prefix_for_daemon_id(self, daemon_id='', conf_dict=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """
        prefix = sys.prefix

        if conf_dict:
            if daemon_id in conf_dict:
                prefixes = conf_dict[daemon_id].split(':')

                if sys.prefix in prefixes:
                    prefix = sys.prefix
                else:
                    prefix = prefixes[0]

        return prefix

    def get_prefix_lib_path(self, prefix='', package=''):
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

    def get_pidfilename_for_daemon_id(self, daemon_id=None, conf_dict=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """
        pidfilename = ''

        if conf_dict and daemon_id:
            if daemon_id in conf_dict:
                pidfilename = '.pyswitchlib_' + daemon_id + '.pid'

        if not pidfilename:
            pidfilename = '.pyswitchlib_default.pid'

        pidfilename = os.path.join(os.sep, 'etc', 'pyswitchlib', pidfilename)

        return pidfilename


