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

vlan_delete = """
            <vlan operation="remove">
               <name>{vlan_id}</name>
            </vlan>
"""

vlan_bulk_delete = """
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


interfaces_config_get = """
<get-config> <source> <running/> </source>
  <nc:filter type="xpath" select="//{{intf_type}}[{{interface_names}}]"></nc:filter>
</get-config>
"""


interfaces_config_set = """
<config>
  <interface xmlns="urn:brocade.com:mgmt:brocade-interface">

    <{{intf_type}}>
      <name>{{port}}</name>


      {% if bfd_tx is not none %}
        <bfd>
                <interval>
                    <min-tx>{{bfd_tx}}</min-tx>
                    <min-rx>{{bfd_rx}}</min-rx>
                    <multiplier>{{bfd_multiplier}}</multiplier>
                </interval>
        </bfd>
      {% endif %}

      <fabric xmlns="urn:brocade.com:mgmt:brocade-fcoe">
          <fabric-isl>
            <fabric-isl-enable operation="remove"></fabric-isl-enable>
          </fabric-isl>

          <neighbor-discovery> <disable></disable> </neighbor-discovery>

          <fabric-trunk>
            <fabric-trunk-enable operation="remove"></fabric-trunk-enable>
          </fabric-trunk>
      </fabric>

      <mtu>{{mtu}}</mtu>
      <switchport-basic operation="remove"><basic></basic></switchport-basic>

      <ip>
        <ip-config xmlns="urn:brocade.com:mgmt:brocade-ip-config">
          {% if "unnumbered" == ip %}
            <unnumbered>
              <ip-donor-interface-type>{{donor_type}}</ip-donor-interface-type>
              <ip-donor-interface-name>{{donor_name}}</ip-donor-interface-name>
            </unnumbered>
          {% else %}
            <address>
              <address>{{ip}}</address>
            </address>
          {% endif %}

          <mtu>{{ip_mtu}}</mtu>
          <proxy-arp></proxy-arp>
          </ip-config>
      </ip>
      <shutdown operation="remove"></shutdown>
    </{{intf_type}}>

  </interface>
</config>
"""

interfaces_loopback_ip_config_set = """
<config>
  <rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">
    <rbridge-id>{{rbridge_id}}</rbridge-id>

    <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
      <loopback xmlns="urn:brocade.com:mgmt:brocade-intf-loopback">
        <id>{{port}}</id>
        <ip xmlns="urn:brocade.com:mgmt:brocade-ip-config">
          <ip-config >
            <address> <address>{{ip}}</address> </address>
          </ip-config>
        </ip>

      </loopback>
    </interface>
  </rbridge-id>
</config>
"""

interfaces_loopback_noshut_config_set = """
<config>
  <rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">
    <rbridge-id>{{rbridge_id}}</rbridge-id>

    <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
      <loopback xmlns="urn:brocade.com:mgmt:brocade-intf-loopback">

        <id>{{port}}</id>

        <intf-loopback>
            <shutdown operation="remove"></shutdown>
        </intf-loopback>

      </loopback>
    </interface>
  </rbridge-id>
</config>
"""
