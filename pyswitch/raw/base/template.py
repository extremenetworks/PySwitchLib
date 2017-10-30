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

acl_get_config = """
<get-config>
    <source> <running/> </source>
    {filter}
</get-config>
"""

mac_fltr = "<nc:filter type='xpath' select='/mac/access-list/" + \
           "{acl_type}[name=\"{acl_name}\"]'></nc:filter>"
ipv4_fltr = "<nc:filter type='xpath' select='/ip-acl/ip/access-list/" + \
            "{acl_type}[name=\"{acl_name}\"]'></nc:filter>"
ipv6_fltr = "<nc:filter type='xpath' select='/ipv6-acl/ipv6/access-list/" + \
            "{acl_type}[name=\"{acl_name}\"]'></nc:filter>"

acl_create_mac = """
<config>
     <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
        <access-list>
           <{acl_type} {delete}>
              <name>{acl_name}</name>
           </{acl_type}>
        </access-list>
     </mac>
</config>
"""

acl_create_ip = """
<config>
    <{address_type}-acl xmlns="urn:brocade.com:mgmt:brocade-{address_type}-access-list">
         <{address_type}>
            <access-list>
               <{acl_type} {delete}>
                  <name>{acl_name}</name>
               </{acl_type}>
            </access-list>
         </{address_type}>
    </{address_type}-acl>
</config>
"""

acl_apply_mac = """
   <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
      <{intf_type}>
         <name>{intf}</name>
         <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
            <access-group {delete}>
               <mac-access-list>{acl_name}</mac-access-list>
               <mac-direction>{acl_direction}</mac-direction>
               {traffic_type}
            </access-group>
         </mac>
      </{intf_type}>
   </interface>
"""

acl_apply_ipv4 = """
   <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
      <{intf_type}>
         <name>{intf}</name>
         <ip-acl-interface xmlns="urn:brocade.com:mgmt:brocade-ip-access-list">
            <ip>
               <access-group {delete}>
                  <ip-access-list>{acl_name}</ip-access-list>
                  <ip-direction>{acl_direction}</ip-direction>
                  {traffic_type}
               </access-group>
            </ip>
         </ip-acl-interface>
      </{intf_type}>
   </interface>
"""

acl_apply_ipv6 = """
   <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
      <{intf_type}>
         <name>{intf}</name>
         <ipv6>
            <access-group xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list" {delete}>
               <ipv6-access-list>{acl_name}</ipv6-access-list>
               <ip-direction>{acl_direction}</ip-direction>
               {traffic_type}
            </access-group>
         </ipv6>
      </{intf_type}>
   </interface>
"""

rbridge_acl_apply = """
<config>
  <rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">
      <rbridge-id>{rbridge_id}</rbridge-id>
      {acl_apply}
  </rbridge-id>
</config>
"""


acl_rule_mac = """
<config>
   <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
      <access-list>
         <{acl_type}>
            <name>{acl_name}</name>
            {sequences}
         </standard>
      </access-list>
   </mac>
</config>
"""

acl_rule_ip = """
<config>
   <{address_type}-acl xmlns="urn:brocade.com:mgmt:brocade-{address_type}-access-list">
      <{address_type}>
         <access-list>
            <{acl_type}>
               <name>{acl_name}</name>
               {sequences}
            </{acl_type}>
         </access-list>
      </{address_type}>
   </{address_type}-acl>
</config>
"""
