rbridge_id_interface_loopback_create = """
   <config>
     <rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">
         <rbridge-id>{rbridge_id}</rbridge-id>
         <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
            <loopback xmlns="urn:brocade.com:mgmt:brocade-intf-loopback">
               <id>{loopback}</id>
            </loopback>
         </interface>
      </rbridge-id>
   </config>

"""
vlan_id = """
            <vlan>
               <name>{vlan_id}</name>
            </vlan>
"""

vlan_id_desc = """
            <vlan>
               <name>{vlan_id}</name>
               <description>{desc}</description>
            </vlan>
"""

vlan_create = """
<config>
    <interface-vlan xmlns="urn:brocade.com:mgmt:brocade-interface">
         <interface>
            {vlan_list}
           </interface>
    </interface-vlan>
</config>
"""

rbridge_id_interface_loopback_get = """
  /rbridge-id/interface/loopback
"""

interface_switchport_get = """
/interface/{int_type}[name='{int_name}']
"""

overlay_gateway_create = """
<config>
    <overlay-gateway xmlns="urn:brocade.com:mgmt:brocade-tunnels">
         <name>{gw_name}</name>
         <gw-type>{gw_type}</gw-type>
         <ip>
            <interface>
               <loopback>
                  <loopback-id>{loopback_id}</loopback-id>
               </loopback>
            </interface>
         </ip>
         {vni_auto_data}
         <activate></activate>
    </overlay-gateway>
</config>

"""
overlay_gateway_vni_auto = """
         <map>
            <vlan>
               <vni>
                  <auto></auto>
               </vni>
            </vlan>
         </map>
"""

overlay_gateway_attach_rb = """
<config>
    <overlay-gateway xmlns="urn:brocade.com:mgmt:brocade-tunnels">
         <name>{gw_name}</name>
         <gw-type>{gw_type}</gw-type>
         <attach>
            <rbridge-id>
               <rb-add>{rbridge_id}</rb-add>
            </rbridge-id>
         </attach>
    </overlay-gateway>
</config>
"""
overlay_gateway_get = """
/overlay-gateway
"""

evpn_instance_create = """
<config>
     <rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">
         <rbridge-id>{{rbridge_id}}</rbridge-id>
         <evpn-instance xmlns="urn:brocade.com:mgmt:brocade-bgp">
            <instance-name>{{evi_name}}</instance-name>
            <route-distinguisher>
               <auto></auto>
            </route-distinguisher>
            <duplicate-mac-timer>
               <duplicate-mac-timer-value>{{duplicate_mac_timer}}</duplicate-mac-timer-value>
               <max-count>{{duplicate_mac_timer_max_count}}</max-count>
            </duplicate-mac-timer>
         </evpn-instance>
      </rbridge-id>
</config>
"""

evpn_instance_router_target_auto = """
<config>
     <rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">
         <rbridge-id>{{rbridge_id}}</rbridge-id>
         <evpn-instance xmlns="urn:brocade.com:mgmt:brocade-bgp">
            <instance-name>{{evi_name}}</instance-name>
            <route-target>
               <both>
                  <target-community>auto</target-community>
                  <ignore-as></ignore-as>
               </both>
            </route-target>
         </evpn-instance>
      </rbridge-id>
</config>
"""

evpn_instance_get = """
/rbridge-id[rbridge-id={rbridge_id}]/evpn-instance
"""
