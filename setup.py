"""setup.py file."""

import os
import sys
import atexit
import uuid
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install
from pip.req import parse_requirements
from distutils.sysconfig import get_python_lib

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

class PostInstallCommand(install):
    def run(self):
        def _get_latest_lib_path():
            return sorted(os.path.join(x, 'pyswitchlib') for x in sys.path if os.path.isdir(os.path.join(x, 'pyswitchlib')))[0]

        def _post_install():
            pyswitchlib_init_scriptname = 'pyswitchlib-api-daemon'
            pyswitchlib_daemon_scriptname = 'pyswitchlib_api_daemon.py'

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

            rc = os.WEXITSTATUS(os.system(python_prefix + ' ' + pyswitchlib_api_daemon + ' status'))

            if rc == 0:
                os.system(python_prefix + ' ' + pyswitchlib_api_daemon + ' stop')

            os.system(python_prefix + ' ' + pyswitchlib_api_daemon + ' start')

        atexit.register(_post_install)
        install.run(self)

setup(
    name="pyswitchlib",
    version="0.1.87",
    packages=find_packages(),
    author="Brocade Communications Inc",
    description="pySwitchLib Library for Brocade switches (SLXOS/NOS)",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/StackStorm/PySwitchLib",
    include_package_data=True,
    install_requires=reqs,
    cmdclass={
        'install': PostInstallCommand,
    },
    data_files=[('/etc/init.d', ['pyswitchlib-api-daemon'])]
)
