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

vlan_delete = """
            <vlan operation="remove">
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
            {vlan_list}
    </interface-vlan>
</config>
"""

vlan_bulk_delete = """
<config>
    <interface-vlan xmlns="urn:brocade.com:mgmt:brocade-interface">
            {vlan_list}
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
            <vlan-and-bd>
               <vni>
                  <auto></auto>
               </vni>
            </vlan-and-bd>
         </map>
"""
evpn_instance_create = """
<config>
   <routing-system xmlns="urn:brocade.com:mgmt:brocade-common-def">
         <evpn-config xmlns="urn:brocade.com:mgmt:brocade-bgp">
            <evpn>
               <evpn-instance>
                  <instance-name>{{evi_name}}</instance-name>
                  <route-target>
                     <both>
                        <target-community>auto</target-community>
                        <ignore-as></ignore-as>
                     </both>
                  </route-target>
                  <route-distinguisher>
                     <auto></auto>
                  </route-distinguisher>
                  <duplicate-mac-timer>
                     <duplicate-mac-timer-value>{{duplicate_mac_timer}}</duplicate-mac-timer-value>
                     <max-count>{{duplicate_mac_timer_max_count}}</max-count>
                  </duplicate-mac-timer>
               </evpn-instance>
            </evpn>
         </evpn-config>
      </routing-system>
</config>
"""

overlay_gateway_get = """
/overlay-gateway
"""

evpn_instance_get = """
/routing-system/evpn-config/evpn/evpn-instance
"""

enable_intf_admin_state = """
         <{int_type}>
            <name>{name}</name>
            <shutdown operation = "remove"> </shutdown>
         </{int_type}>
"""

disable_intf_admin_state = """
         <{int_type}>
            <name>{name}</name>
            <shutdown></shutdown>
         </{int_type}>
"""

set_intf_admin_state = """
<config>
    <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
          {intf_list}
      </interface>
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

      <mtu>{{mtu}}</mtu>
      <switchport-basic operation="remove"><basic></basic></switchport-basic>

      <ipv6>
        <ipv6-config xmlns="urn:brocade.com:mgmt:brocade-ipv6-config">
          <mtu>{{ipv6_mtu}}</mtu>
        </ipv6-config>
      </ipv6>

      <ip>
        <ip-config xmlns="urn:brocade.com:mgmt:brocade-ip-config">
          <address>
            <address>{{ip}}</address>
          </address>

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
  <routing-system xmlns="urn:brocade.com:mgmt:brocade-common-def">

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

  </routing-system>
</config>
"""

interfaces_loopback_noshut_config_set = """
<config>
  <routing-system xmlns="urn:brocade.com:mgmt:brocade-common-def">

    <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
        <loopback xmlns="urn:brocade.com:mgmt:brocade-intf-loopback">

          <id>{{port}}</id>
          <shutdown operation="remove"></shutdown>

        </loopback>
    </interface>

  </routing-system>
</config>
"""
