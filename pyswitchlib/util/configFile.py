import os
import re
import fasteners

lock_file = os.path.join(os.sep, 'etc', 'pyswitchlib', '.pyswitchlib_config_file.lock')

class ConfigFileUtil(object):
    """
    This is an auto-generated class for the PySwitchLib device asset.
    Asset provides connection information for PySwitchLib APIs.
    """

    def __init__(self):
        """
        This is an auto-generated method for the PySwitchLib.
        """
        if not os.path.exists(lock_file):
            original_mask = os.umask(0o111)

            try:
                with os.fdopen(os.open(lock_file, os.O_WRONLY | os.O_CREAT, 0o666), 'w') as fd:
                    pass
            except:
                pass
            finally:
                os.umask(original_mask)

    def read(self, filename=None):
        """
        This is an auto-generated method for the PySwitchLib.
        """
        conf_dict = {}
        conf_pattern = re.compile('\s*(\w+)\s*=\s*(\S+)\s*')

        with fasteners.InterProcessLock(lock_file):
            if os.path.exists(filename):
                with open(filename, 'r') as conf_file:
                    for conf_line in conf_file:
                        line = conf_line.strip()

                        if not re.match('^#', line):
                            match = conf_pattern.match(line)

                            if match:
                                conf_dict[match.group(1)] = match.group(2)

        return conf_dict

    def write(self, filename=None, conf_dict=None, do_merge=True):
        """
        This is an auto-generated method for the PySwitchLib.
        """
        if do_merge:
            merged_conf = self.read(filename=filename)
        else:
            merged_conf = {}

        if conf_dict != None:
            merged_conf.update(conf_dict)

            with fasteners.InterProcessLock(lock_file):
                with open(filename, 'w') as conf_file:
                    for key in merged_conf:
                        conf_file.write(key + ' = ' + str(merged_conf[key]) + '\n')


