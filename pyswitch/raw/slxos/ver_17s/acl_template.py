
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
                <vlan>{{vlan.vlan_id}}</vlan>
              {% endif %}

              {% if pcp is not none %}
                <pcp>{{pcp}}</pcp>
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

              {% if ud.vlan is not none %}
                <vlan>{{ud.vlan}}</vlan>
              {% endif %}

              {% if ud.pcp is not none %}
                <pcp>{{ud.pcp}}</pcp>
              {% endif %}

            {% endif %}

            {% if ud.count is not none %} <count></count> {% endif %}
            {% if ud.log is not none %}<log></log> {% endif %}
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
