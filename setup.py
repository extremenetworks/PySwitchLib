"""setup.py file."""

import atexit
import os
import subprocess
import sys
import uuid
from setuptools import setup, find_packages
from setuptools.command.install import install

try:
    from pip.req import parse_requirements
except:
    from pip._internal.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]


class PostInstallCommand(install):
    def run(self):
        def _get_latest_lib_path():
            return sorted(os.path.join(x, 'pyswitchlib') for x in sys.path if os.path.isdir(os.path.join(x, 'pyswitchlib')))[0]

        def _post_install():
            pyswitchlib_init_scriptname = 'pyswitchlib-api-daemon'
            pyswitchlib_daemon_scriptname = 'pyswitchlib_api_daemon.py'
            pyswitchlib_default_conf_filename = 'pyswitchlib.conf.default'
            pyswitchlib_conf_filename = 'pyswitchlib.conf'
            pyswitchlib_default_cacert_filename = 'cacert.pem'
            pyswitchlib_default_conf_path = os.path.join(os.sep, 'etc', 'pyswitchlib', pyswitchlib_default_conf_filename)
            pyswitchlib_conf_path = os.path.join(os.sep, 'etc', 'pyswitchlib', pyswitchlib_conf_filename)
            pyswitchlib_default_cacert_path = os.path.join(os.sep, 'etc', 'pyswitchlib', pyswitchlib_default_cacert_filename)

            ubuntu_init_script_cmd = 'update-rc.d ' + pyswitchlib_init_scriptname + ' defaults 95 05'
            centos_init_script_cmd = 'chkconfig --add ' + pyswitchlib_init_scriptname

            python_prefix = os.path.join(sys.prefix, 'bin', 'python')
            pyswitchlib_api_daemon = os.path.join(_get_latest_lib_path(), pyswitchlib_daemon_scriptname)

            try:
                subprocess.check_call(ubuntu_init_script_cmd, shell=True)
            except:
                try:
                    subprocess.check_call(centos_init_script_cmd, shell=True)
                except:
                    pass

            if not os.path.exists(pyswitchlib_conf_path):
                os.system('cp ' + pyswitchlib_default_conf_path + ' ' + pyswitchlib_conf_path)

            if not os.path.exists(pyswitchlib_default_cacert_path):
                os.system('touch ' + pyswitchlib_default_cacert_path)

            rc = os.WEXITSTATUS(os.system(python_prefix + ' ' + pyswitchlib_api_daemon + ' status'))

            if rc == 3:
                subprocess.Popen([python_prefix, pyswitchlib_api_daemon, 'start'], close_fds=True)
            else:
                subprocess.Popen([python_prefix, pyswitchlib_api_daemon, 'restart'], close_fds=True)

        atexit.register(_post_install)
        install.run(self)

setup(
    name="pyswitchlib",
    version="1.2.0",
    packages=find_packages(),
    author="Extreme Networks Inc",
    description="pySwitchLib Library for Extreme switches (SLXOS/NOS/NI)",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://stackstorm.github.io/PySwitchLib/",
    include_package_data=True,
    install_requires=reqs,
    cmdclass={
        'install': PostInstallCommand,
    },
    data_files=[('/etc/pyswitchlib', ['pyswitchlib.conf.default']),
                ('/etc/init.d', ['pyswitchlib-api-daemon'])]
)
