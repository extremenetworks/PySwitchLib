conversation_property_create = """
<config>
      <host-table xmlns="urn:brocade.com:mgmt:brocade-arp">
         <aging-mode>
            <conversational></conversational>
         </aging-mode>
         <aging-time>
            <conversational-timeout>{{arp_aging_timeout}}</conversational-timeout>
         </aging-time>
      </host-table>
      <mac-address-table xmlns="urn:brocade.com:mgmt:brocade-mac-address-table">
         <learning-mode>conversational</learning-mode>
         <aging-time>
            <conversational-time-out>{{mac_aging_timeout}}</conversational-time-out>
            <legacy-time-out>{{mac_legacy_aging_timeout}}</legacy-time-out>
         </aging-time>
         <mac-move>
            <mac-move-detect-enable></mac-move-detect-enable>
            <mac-move-limit>{{mac_move_limit}}</mac-move-limit>
         </mac-move>
      </mac-address-table>
</config>
"""
mac_address_table_get = """
/mac-address-table
"""

host_table_get = """
/host-table
"""
