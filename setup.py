"""setup.py file."""

import uuid

from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="pyswitchlib",
    version="0.1.19",
    packages=find_packages(),
    author="Brocade Comm",
    description="pySwitchLib Library for Brocade switches (SLXOS/NOS)",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/shivharis/pySwitchLib",
    include_package_data=True,
    install_requires=reqs,
)
