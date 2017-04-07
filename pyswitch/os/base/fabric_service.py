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

from pyswitch.utilities import Util


class FabricService(object):
    """
    FabricService class containing all VCS Fabric methods and attributes.
    """

    def __init__(self, callback):
        """FabricService init method.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            FabricService Object

        Raises:
            None
        """
        self._callback = callback

    @property
    def trill_links(self):
        """dict: trill link details
        """

        get_links_info = ('show_linkinfo_rpc', {})

        results = self._callback(get_links_info, handler='get')
        util = Util(results.data)

        result = []

        for item in util.findlist(util.root, './/show-link-info'):
            src_rbridge_id = util.find(item, './/linkinfo-rbridgeid')
            src_switch_wwn = util.find(item, './/linkinfo-wwn')
            for link in util.findlist(item, './/linkinfo-isl'):
                dest_rbridge_id = util.find(link,
                                            './/linkinfo-isllink-destdomain')
                src_interface = util.find(
                    link, './/linkinfo-isllink-srcport-interface')
                dest_interface = util.find(
                    link, './/linkinfo-isllink-destport-interface')
                link_cost = util.find(link,'.//linkinfo-isl-linkcost')
                link_cost_count = util.find(link,
                                            './/linkinfo-isllink-costcount')

                item_results = {'source-rbridgeid': src_rbridge_id,
                                'source-switch-wwn': src_switch_wwn,
                                'dest-rbridgeid': dest_rbridge_id,
                                'source-interface': src_interface,
                                'dest-interface': dest_interface,
                                'link-cost': link_cost,
                                'link-costcount': link_cost_count}

                result.append(item_results)

        return result
