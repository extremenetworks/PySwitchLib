
acl_rule_ip = """
<config>
  <{{address_type}}-acl
    xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
    <{{address_type}}>
      <access-list>
        <{{acl_type}}>
          <name>{{acl_name}}</name>
          {% if address_type == "ip" %}
            {% if acl_type == "extended" %}
              <hide-{{address_type}}-acl-ext>
            {% else %}
              <hide-{{address_type}}-acl-std>
            {% endif %}
          {% endif %}
              <seq>
                <seq-id>{{seq_id}}</seq-id>
                <action>{{action}}</action>

                <src-host-any-sip>{{source.host_any}}</src-host-any-sip>
                {% if source.host_any != "any" %}
                  {% if source.host_any == "host" %}
                    <src-host-ip>{{source.host_ip}}</src-host-ip>
                  {% elif source.mask is not none %}
                    <src-mask>{{source.mask}}</src-mask>
                  {% endif %}
                {% endif %}

                {% if acl_type == "extended" %}
                  <protocol-type>{{protocol_type}}</protocol-type>


                  {% if source.xport is not none %}
                    <sport>{{source.xport.op}}</sport>

                    {% if source.xport.op == "eq" or source.xport.op == "neq" %}
                      <sport-number-eq-neq-{{protocol_type}}>
                        {{source.xport.val[0]}}
                      </sport-number-eq-neq-{{protocol_type}}>
                    {% elif source.xport.op == "range" %}
                      <sport-number-range-lower-{{protocol_type}}>
                         {{source.xport.val[0]}}
                      </sport-number-range-lower-{{protocol_type}}>
                      <sport-number-range-higher-{{protocol_type}}>
                         {{source.xport.val[1]}}
                      </sport-number-range-higher-{{protocol_type}}>
                    {% else %}
                      <sport-number-{{source.xport.op}}-{{protocol_type}}>
                         {{source.xport.val[0]}}
                      </sport-number-{{source.xport.op}}-{{protocol_type}}>
                    {% endif %}
                  {% endif %}


                  <dst-host-any-dip>{{destination.host_any}}</dst-host-any-dip>
                  {% if destination.host_any != "any" %}
                    {% if destination.host_any == "host" %}
                      <dst-host-ip>{{destination.host_ip}}</dst-host-ip>
                    {% elif destination.mask is not none %}
                      <dst-mask>{{destination.mask}}</dst-mask>
                    {% endif %}
                  {% endif %}

                  {% if destination.xport is not none %}
                    <dport>{{destination.xport.op}}</dport>

                    {% if destination.xport.op == "eq" or
                          destination.xport.op == "neq" %}
                      <dport-number-eq-neq-{{protocol_type}}>
                        {{destination.xport.val[0]}}
                      </dport-number-eq-neq-{{protocol_type}}>
                    {% elif destination.xport.op == "range" %}
                      <dport-number-range-lower-{{protocol_type}}>
                         {{destination.xport.val[0]}}
                      </dport-number-range-lower-{{protocol_type}}>
                      <dport-number-range-higher-{{protocol_type}}>
                         {{destination.xport.val[1]}}
                      </dport-number-range-higher-{{protocol_type}}>
                    {% else %}
                      <dport-number-{{destination.xport.op}}-{{protocol_type}}>
                         {{destination.xport.val[0]}}
                      </dport-number-{{destination.xport.op}}-{{protocol_type}}>
                    {% endif %}
                  {% endif %}

                  {% if dscp is not none %} <dscp>{{dscp}}</dscp> {% endif %}
                  {% if dscp_force is not none %}
                    <dscp-force>{{dscp_force}}</dscp-force>
                  {% endif %}

                  {% if drop_precedence_force is not none %}
                    <drop-precedence-force>
                      {{drop_precedence_force}}
                    </drop-precedence-force>
                  {% endif %}

                  {% if vlan_id is not none %}
                    <vlan>{{vlan_id}}</vlan>
                  {% endif %}

                  {% if urg is not none %} <urg></urg> {% endif %}
                  {% if ack is not none %} <ack></ack> {% endif %}
                  {% if push is not none %} <push></push> {% endif %}
                  {% if fin is not none %} <fin></fin> {% endif %}
                  {% if rst is not none %} <rst></rst> {% endif %}
                  {% if sync is not none %} <sync></sync> {% endif %}
                  {% if mirror is not none %} <mirror></mirror> {% endif %}
                {% endif %}

                {% if count is not none %} <count></count> {% endif %}
                {% if log is not none %}<log></log> {% endif %}
                {% if copy_sflow is not none %}
                  <copy-sflow></copy-sflow>
                {% endif %}
              </seq>
          {% if address_type == "ip" %}
            {% if acl_type == "extended" %}
              </hide-{{address_type}}-acl-ext>
            {% else %}
              </hide-{{address_type}}-acl-std>
            {% endif %}
          {% endif %}
        </{{acl_type}}>
      </access-list>
    </{{address_type}}>
  </{{address_type}}-acl>
</config>
"""


acl_rule_mac = """
<config>
  <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
    <access-list>
      <{{acl_type}}>
        <name>{{acl_name}}</name>
        {% if acl_type == "extended" %}
          <hide-mac-acl-ext>
        {% else %}
          <hide-mac-acl-std>
        {% endif %}
          <seq>
            <seq-id>{{seq_id}}</seq-id>
            <action>{{action}}</action>

            <source>{{source.source}}</source>
            {% if source.source != "any" %}
              {% if source.source == "host" %}
                <srchost>{{source.srchost}}</srchost>
              {% else %}
                <src-mac-addr-mask>{{source.mask}}</src-mac-addr-mask>
              {% endif %}
            {% endif %}

            {% if acl_type == "extended" %}

              <dst>{{dst.dst}}</dst>
              {% if dst.dst != "any" %}
                {% if dst.dst == "host" %}
                  <dsthost>{{dst.dsthost}}</dsthost>
                {% else %}
                  <dst-mac-addr-mask>{{dst.mask}}</dst-mac-addr-mask>
                {% endif %}
              {% endif %}

              {% if ethertype is not none %}
                <ethertype>{{ethertype}}</ethertype>
              {% endif %}

              {% if vlan_tag_format is not none %}
                <vlan-tag-format>{{vlan_tag_format}}</vlan-tag-format>
              {% endif %}

              {% if vlan is not none %}

                {% if vlan_tag_format is none %}
                  <vlan>{{vlan.vlan_id}}</vlan>

                {% elif vlan_tag_format == "untagged" %}
                  <vlan>{{vlan.vlan_id}}</vlan>

                  {% if vlan.mask is not none %}
                    <vlan-id-mask>{{vlan.mask}}</vlan-id-mask>
                  {% endif %}

                {% elif vlan_tag_format == "single-tagged" %}

                  <vlan>{{vlan.vlan_id}}</vlan>

                  {% if vlan.mask is not none %}
                    <vlan-id-mask>{{vlan.mask}}</vlan-id-mask>
                  {% endif %}

                {% elif vlan_tag_format == "double-tagged" %}

                  <outer-vlan>{{vlan.outervlan}}</outer-vlan>
                  {% if vlan.outermask is not none %}
                    <outer-vlan-id-mask>{{vlan.outermask}}</outer-vlan-id-mask>
                  {% endif %}

                  <inner-vlan>{{vlan.innervlan}}</inner-vlan>
                  {% if vlan.innermask is not none %}
                    <inner-vlan-id-mask>{{vlan.innermask}}</inner-vlan-id-mask>
                  {% endif %}

                {% endif %}
              {% endif %}

              {% if arp_guard is not none %}
                <arp-guard></arp-guard>
              {% endif %}

              {% if pcp is not none %} <pcp>{{pcp}}</pcp> {% endif %}
              {% if pcp_force is not none %}
                <pcp-force>{{pcp_force}}</pcp-force>
              {% endif %}

              {% if drop_precedence_force is not none %}
                <drop-precedence-force>
                  {{drop_precedence_force}}
                </drop-precedence-force>
              {% endif %}

              {% if mirror is not none %} <mirror></mirror> {% endif %}
            {% endif %}

            {% if count is not none %} <count></count> {% endif %}
            {% if log is not none %}<log></log> {% endif %}
            {% if copy_sflow is not none %}
              <copy-sflow></copy-sflow>
            {% endif %}
          </seq>
        {% if acl_type == "extended" %}
          </hide-mac-acl-ext>
        {% else %}
          </hide-mac-acl-std>
        {% endif %}
      </{{acl_type}}>
    </access-list>
  </mac>
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

acl_rule_ip_bulk = """
<config>
  <{{address_type}}-acl
    xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
    <{{address_type}}>
      <access-list>
        <{{acl_type}}>
          <name>{{acl_name}}</name>
          {% if address_type == "ip" %}
            {% if acl_type == "extended" %}
              <hide-{{address_type}}-acl-ext>
            {% else %}
              <hide-{{address_type}}-acl-std>
            {% endif %}
          {% endif %}
          {% for ud in user_data_list %}
              <seq>
                <seq-id>{{ud.seq_id}}</seq-id>
                <action>{{ud.action}}</action>

                <src-host-any-sip>{{ud.source.host_any}}</src-host-any-sip>
                {% if ud.source.host_any != "any" %}
                  {% if ud.source.host_any == "host" %}
                    <src-host-ip>{{ud.source.host_ip}}</src-host-ip>
                  {% elif ud.source.mask is not none %}
                    <src-mask>{{ud.source.mask}}</src-mask>
                  {% endif %}
                {% endif %}

                {% if acl_type == "extended" %}
                  <protocol-type>{{ud.protocol_type}}</protocol-type>


                  {% if ud.source.xport is not none %}
                    <sport>{{ud.source.xport.op}}</sport>

                    {% if ud.source.xport.op == "eq" or ud.source.xport.op == "neq" %}
                      <sport-number-eq-neq-{{ud.protocol_type}}>
                        {{ud.source.xport.val[0]}}
                      </sport-number-eq-neq-{{ud.protocol_type}}>
                    {% elif ud.source.xport.op == "range" %}
                      <sport-number-range-lower-{{ud.protocol_type}}>
                         {{ud.source.xport.val[0]}}
                      </sport-number-range-lower-{{ud.protocol_type}}>
                      <sport-number-range-higher-{{ud.protocol_type}}>
                         {{ud.source.xport.val[1]}}
                      </sport-number-range-higher-{{ud.protocol_type}}>
                    {% else %}
                      <sport-number-{{ud.source.xport.op}}-{{ud.protocol_type}}>
                         {{ud.source.xport.val[0]}}
                      </sport-number-{{ud.source.xport.op}}-{{ud.protocol_type}}>
                    {% endif %}
                  {% endif %}


                  <dst-host-any-dip>{{ud.destination.host_any}}</dst-host-any-dip>
                  {% if ud.destination.host_any != "any" %}
                    {% if ud.destination.host_any == "host" %}
                      <dst-host-ip>{{ud.destination.host_ip}}</dst-host-ip>
                    {% elif ud.destination.mask is not none %}
                      <dst-mask>{{ud.destination.mask}}</dst-mask>
                    {% endif %}
                  {% endif %}

                  {% if ud.destination.xport is not none %}
                    <dport>{{ud.destination.xport.op}}</dport>

                    {% if ud.destination.xport.op == "eq" or
                          ud.destination.xport.op == "neq" %}
                      <dport-number-eq-neq-{{ud.protocol_type}}>
                        {{ud.destination.xport.val[0]}}
                      </dport-number-eq-neq-{{ud.protocol_type}}>
                    {% elif ud.destination.xport.op == "range" %}
                      <dport-number-range-lower-{{ud.protocol_type}}>
                         {{ud.destination.xport.val[0]}}
                      </dport-number-range-lower-{{ud.protocol_type}}>
                      <dport-number-range-higher-{{ud.protocol_type}}>
                         {{ud.destination.xport.val[1]}}
                      </dport-number-range-higher-{{ud.protocol_type}}>
                    {% else %}
                      <dport-number-{{ud.destination.xport.op}}-{{ud.protocol_type}}>
                         {{ud.destination.xport.val[0]}}
                      </dport-number-{{ud.destination.xport.op}}-{{ud.protocol_type}}>
                    {% endif %}
                  {% endif %}

                  {% if ud.dscp is not none %} <dscp>{{ud.dscp}}</dscp> {% endif %}
                  {% if ud.drop_precedence_force is not none %}
                    <drop-precedence-force>
                      {{ud.drop_precedence_force}}
                    </drop-precedence-force>
                  {% endif %}

                  {% if ud.vlan_id is not none %}
                    <vlan>{{ud.vlan_id}}</vlan>
                  {% endif %}

                  {% if ud.urg is not none %} <urg></urg> {% endif %}
                  {% if ud.ack is not none %} <ack></ack> {% endif %}
                  {% if ud.push is not none %} <push></push> {% endif %}
                  {% if ud.fin is not none %} <fin></fin> {% endif %}
                  {% if ud.rst is not none %} <rst></rst> {% endif %}
                  {% if ud.sync is not none %} <sync></sync> {% endif %}
                  {% if ud.mirror is not none %} <mirror></mirror> {% endif %}
                {% endif %}

                {% if ud.count is not none %} <count></count> {% endif %}
                {% if ud.log is not none %}<log></log> {% endif %}
                {% if ud.copy_sflow is not none %}
                  <copy-sflow></copy-sflow>
                {% endif %}
              </seq>
          {% endfor %}
          {% if address_type == "ip" %}
            {% if acl_type == "extended" %}
              </hide-{{address_type}}-acl-ext>
            {% else %}
              </hide-{{address_type}}-acl-std>
            {% endif %}
          {% endif %}
        </{{acl_type}}>
      </access-list>
    </{{address_type}}>
  </{{address_type}}-acl>
</config>
"""

acl_apply = """
<config>
   {% if intf_type == 've' %}
      <routing-system xmlns="urn:brocade.com:mgmt:brocade-common-def">
       <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
   {% elif intf_type == 'vlan' %}
      <interface-vlan xmlns="urn:brocade.com:mgmt:brocade-interface">
   {% else %}
         <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
   {% endif %}
            <{{intf_type}}>
               <name>{{intf}}</name>
               {% if intf_type == 'management' %}
                  <{{address_type}}>
                     <access-group
                        xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
                        <mgmt-{{address_type}}-access-list>{{acl_name}}</mgmt-{{address_type}}-access-list>
                        <mgmt-ip-direction>{{acl_direction}}</mgmt-ip-direction>
                     </access-group>
                  </{{address_type}}>
               {% elif address_type == 'mac' %}
                  <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
                     <access-group>
                        <mac-access-list>{{acl_name}}</mac-access-list>
                        <mac-direction>{{acl_direction}}</mac-direction>
                        {% if traffic_type is not none %}
                           <traffic-type>{{traffic_type}}</traffic-type>
                        {% endif %}
                     </access-group>
                  </mac>
               {% elif address_type == 'ip' %}
                  <ip-acl-interface
                    xmlns="urn:brocade.com:mgmt:brocade-ip-access-list">
                     <ip>
                        <access-group>
                           <ip-access-list>{{acl_name}}</ip-access-list>
                           <ip-direction>{{acl_direction}}</ip-direction>
                           {% if traffic_type is not none %}
                              <traffic-type>{{traffic_type}}</traffic-type>
                           {% endif %}
                        </access-group>
                     </ip>
                  </ip-acl-interface>
               {% elif address_type == 'ipv6' %}
                  {% if intf_type == 've' %}
                   <ipv6 xmlns="urn:brocade.com:mgmt:brocade-ipv6-config">
                  {% else %}
                   <ipv6>
                  {% endif %}
                     <access-group
                        xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list">
                        <ipv6-access-list>{{acl_name}}</ipv6-access-list>
                        <ip-direction>{{acl_direction}}</ip-direction>
                        {% if traffic_type is not none %}
                           <traffic-type>{{traffic_type}}</traffic-type>
                        {% endif %}
                     </access-group>
                  </ipv6>
               {% endif %}
            </{{intf_type}}>

   {% if intf_type == 've' %}
       </interface>
      </routing-system>
   {% elif intf_type == 'vlan' %}
      </interface-vlan>
   {% else %}
      </interface>
   {% endif %}
</config>
"""

acl_remove = """
<config>
   {% if intf_type == 've' %}
      <routing-system xmlns="urn:brocade.com:mgmt:brocade-common-def">
       <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
   {% elif intf_type == 'vlan' %}
      <interface-vlan xmlns="urn:brocade.com:mgmt:brocade-interface">
   {% else %}
         <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
   {% endif %}
            <{{intf_type}}>
               <name>{{intf}}</name>
               {% if intf_type == 'management' %}
                  <{{address_type}}>
                     <access-group
                        xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list"
                        operation="delete">
                        <mgmt-{{address_type}}-access-list>{{acl_name}}</mgmt-{{address_type}}-access-list>
                        <mgmt-ip-direction>{{acl_direction}}</mgmt-ip-direction>
                     </access-group>
                  </{{address_type}}>
               {% elif address_type == 'mac' %}
                  <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
                     <access-group operation="delete">
                        <mac-access-list>{{acl_name}}</mac-access-list>
                        <mac-direction>{{acl_direction}}</mac-direction>
                        {% if traffic_type is not none %}
                           <traffic-type>{{traffic_type}}</traffic-type>
                        {% endif %}
                     </access-group>
                  </mac>
               {% elif address_type == 'ip' %}
                  <ip-acl-interface
                    xmlns="urn:brocade.com:mgmt:brocade-ip-access-list">
                     <ip>
                        <access-group operation="delete">
                           <ip-access-list>{{acl_name}}</ip-access-list>
                           <ip-direction>{{acl_direction}}</ip-direction>
                           {% if traffic_type is not none %}
                              <traffic-type>{{traffic_type}}</traffic-type>
                           {% endif %}
                        </access-group>
                     </ip>
                  </ip-acl-interface>
               {% elif address_type == 'ipv6' %}
                  {% if intf_type == 've' %}
                   <ipv6 xmlns="urn:brocade.com:mgmt:brocade-ipv6-config">
                  {% else %}
                   <ipv6>
                  {% endif %}
                     <access-group
                        xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list"
                        operation="delete">
                        <ipv6-access-list>{{acl_name}}</ipv6-access-list>
                        <ip-direction>{{acl_direction}}</ip-direction>
                        {% if traffic_type is not none %}
                           <traffic-type>{{traffic_type}}</traffic-type>
                        {% endif %}
                     </access-group>
                  </ipv6>
               {% endif %}
            </{{intf_type}}>

   {% if intf_type == 've' %}
       </interface>
      </routing-system>
   {% elif intf_type == 'vlan' %}
      </interface-vlan>
   {% else %}
      </interface>
   {% endif %}
</config>
"""

get_interface_by_name = """
<get-config>
  <source> <running/> </source>
    {% if intf_type == "ve" %}
        <nc:filter type="xpath" select="/routing-system/interface/\
{{intf_type}}/name[text()=\'{{intf}}\']"></nc:filter>
      {% elif intf_type == "vlan" %}
          <nc:filter type="xpath" select="/interface-vlan/\
  {{intf_type}}/name[text()=\'{{intf}}\']"></nc:filter>
    {% else %}
        <nc:filter type="xpath" select="/interface/{{intf_type}}/\
name[text()=\'{{intf}}\']"></nc:filter>
    {% endif %}
</get-config>
"""

acl_rule_mac_bulk = """
<config>
  <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
    <access-list>
      <{{acl_type}}>
        <name>{{acl_name}}</name>
        {% if acl_type == "extended" %}
          <hide-mac-acl-ext>
        {% else %}
          <hide-mac-acl-std>
        {% endif %}

        {% for ud in user_data_list %}
            <seq>
              <seq-id>{{ud.seq_id}}</seq-id>
              <action>{{ud.action}}</action>

              <source>{{ud.source.source}}</source>
              {% if ud.source.source != "any" %}
                {% if ud.source.source == "host" %}
                  <srchost>{{ud.source.srchost}}</srchost>
                {% else %}
                  <src-mac-addr-mask>{{ud.source.mask}}</src-mac-addr-mask>
                {% endif %}
              {% endif %}

              {% if acl_type == "extended" %}

                <dst>{{ud.dst.dst}}</dst>
                {% if ud.dst.dst != "any" %}
                  {% if ud.dst.dst == "host" %}
                    <dsthost>{{ud.dst.dsthost}}</dsthost>
                  {% else %}
                    <dst-mac-addr-mask>{{ud.dst.mask}}</dst-mac-addr-mask>
                  {% endif %}
                {% endif %}

                {% if ud.ethertype is not none %}
                  <ethertype>{{ud.ethertype}}</ethertype>
                {% endif %}

                {% if ud.vlan_tag_format is not none %}
                  <vlan-tag-format>{{ud.vlan_tag_format}}</vlan-tag-format>
                {% endif %}

                {% if ud.vlan is not none %}

                  {% if ud.vlan_tag_format is none %}
                    <vlan>{{ud.vlan.vlan_id}}</vlan>

                  {% elif ud.vlan_tag_format == "untagged" %}
                    <vlan>{{ud.vlan.vlan_id}}</vlan>

                  {% elif ud.vlan_tag_format == "single-tagged" %}

                    <vlan>{{ud.vlan.vlan_id}}</vlan>

                    {% if ud.vlan.mask is not none %}
                      <vlan-id-mask>{{ud.vlan.mask}}</vlan-id-mask>
                    {% endif %}

                  {% elif ud.vlan_tag_format == "double-tagged" %}

                    <outer-vlan>{{ud.vlan.outervlan}}</outer-vlan>
                    {% if ud.vlan.outermask is not none %}
                      <outer-vlan-id-mask>{{ud.vlan.outermask}}</outer-vlan-id-mask>
                    {% endif %}

                    <inner-vlan>{{ud.vlan.innervlan}}</inner-vlan>
                    {% if ud.vlan.innermask is not none %}
                      <inner-vlan-id-mask>{{ud.vlan.innermask}}</inner-vlan-id-mask>
                    {% endif %}

                  {% endif %}
                {% endif %}

                {% if ud.arp_guard is not none %}
                  <arp-guard></arp-guard>
                {% endif %}

                {% if ud.pcp is not none %} <pcp>{{ud.pcp}}</pcp> {% endif %}
                {% if ud.pcp_force is not none %}
                  <pcp-force>{{ud.pcp_force}}</pcp-force>
                {% endif %}

                {% if ud.drop_precedence_force is not none %}
                  <drop-precedence-force>
                    {{ud.drop_precedence_force}}
                  </drop-precedence-force>
                {% endif %}

                {% if ud.mirror is not none %} <mirror></mirror> {% endif %}
              {% endif %}

              {% if ud.count is not none %} <count></count> {% endif %}
              {% if ud.log is not none %}<log></log> {% endif %}
              {% if ud.copy_sflow is not none %}
                <copy-sflow></copy-sflow>
              {% endif %}
            </seq>
        {% endfor %}

        {% if acl_type == "extended" %}
          </hide-mac-acl-ext>
        {% else %}
          </hide-mac-acl-std>
        {% endif %}
      </{{acl_type}}>
    </access-list>
  </mac>
</config>
"""
