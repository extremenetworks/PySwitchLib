"""
Copyright 2017 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import abc
import logging


class Acl(object):
    """
    The Acl class holds all the functions assocaiated with the Access Control list.

    Attributes:
        None
    """
    __metaclass__ = abc.ABCMeta

    os_type = None

    @abc.abstractmethod
    def __init__(self, callback):
        """
        ACL init function.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            ACL Object
        """
        logging.basicConfig(format='pyswitch.raw.base.acl.Acl: %(levelname)s  %(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self._callback = callback

    @abc.abstractmethod
    def get_acl_type(self, acl_name):
        """
        Return acl-type as dict {'type':'standard'/'ectended;, 'protocol':'mac'/'ip'/'ipv6'}.
        """
        return

    @abc.abstractmethod
    def get_seq(self, acl_name, seq_id, acl_type, address_type):
        """
        Return ACL rule sequence as dict() with given 'seq_id'
        or last sequence if 'seq_id' not given.
        """
        return

    @abc.abstractmethod
    def get_seq_id(self, acl_name, acl_type, address_type=None):
        """
        Return new sequence id for the given ACL.
        """
        return

    @abc.abstractmethod
    def create_acl(self, **kwargs):
        """
        Create an Access Control List.
        """
        return

    @abc.abstractmethod
    def delete_acl(self, **kwargs):
        """
        Delete Access Control List.
        """
        return

    @abc.abstractmethod
    def apply_acl(self, **kwargs):
        """
        Apply an ACL to a physical port, port channel, VE or management interface.
        """
        return

    @abc.abstractmethod
    def remove_acl(self, **kwargs):
        """
        Remove ACL from a physical port, port channel, VE or management interface.
        """
        return

    @abc.abstractmethod
    def add_mac_acl_rule(self, **kwargs):
        """
        Add ACL rule to an existing L2 ACL.
        """
        return

    @abc.abstractmethod
    def add_ip_acl_rule(self, **kwargs):
        """
        Add ACL rule to an existing ACL.
        """
        return

    @abc.abstractmethod
    def remove_acl_rule(self, **kwargs):
        """
        Remove ACL rule from an existing ACL..
        """
        return
