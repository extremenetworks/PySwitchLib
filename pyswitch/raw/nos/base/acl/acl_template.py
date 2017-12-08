
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
                  {% elif address_type == "ip" %}
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
                    {% elif address_type == "ip" %}
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

                  {% if vlan_id is not none %}
                    <vlan>{{vlan_id}}</vlan>
                  {% endif %}

                  {% if urg is not none %} <urg></urg> {% endif %}
                  {% if ack is not none %} <ack></ack> {% endif %}
                  {% if push is not none %} <push></push> {% endif %}
                  {% if fin is not none %} <fin></fin> {% endif %}
                  {% if rst is not none %} <rst></rst> {% endif %}
                  {% if sync is not none %} <sync></sync> {% endif %}
                {% endif %}

                {% if count is not none %} <count></count> {% endif %}
                {% if log is not none %}<log></log> {% endif %}
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

              {% if vlan is not none %}
                <vlan>{{vlan}}</vlan>
              {% endif %}

            {% endif %}

            {% if count is not none %} <count></count> {% endif %}
            {% if log is not none %}<log></log> {% endif %}
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
'''
acl_apply_intf = """
<interface xmlns="urn:brocade.com:mgmt:brocade-interface">
  <{{intf_type}}>
    <name>{{intf}}</name>
    <{{address_type}}
      xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
      <access-group>
        <{{address_type}}-access-list>{{acl_name}} </{{address_type}}-access-list>
               <{{address_type}}-direction>
                {acl_direction}</mac-direction>
               {traffic_type}
            </access-group>
         </mac>
      </{intf_type}>
   </interface>
"""
'''

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