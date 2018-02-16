"""
Copyright 2015 Brocade Communications Systems, Inc.

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


class System(object):
    """
        System class containing all system level methods and attributes.
        """

    def __init__(self, callback):
        """System init method.
        Args:
            callback: Callback function that will be called for each action.
        Returns:
            System Object
        Raises:
            None
        """

        self._callback = callback

    def persist_config(self, **kwargs):
        raise ValueError('Use execute_cli action to perform persist configuration'
                         ' on this platform')

    def parse_persist_config_response(self, **kwargs):
        raise ValueError('Use execute_cli action to perform persist configuration'
                         ' on this platform')

    def persist_config_status(self, **kwargs):
        raise ValueError('Use execute_cli action to perform persist configuration'
                         ' on this platform')
