
acl_create = """
<config>
  {% if address_type != "mac" %}
    <{{address_type}}-acl
      xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
      <{{address_type}}>
  {% else %}
    <{{address_type}}
      xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
  {% endif %}

        <access-list>
          <{{acl_type}}>
            <name>{{acl_name}}</name>
          </{{acl_type}}>
        </access-list>

  {% if address_type != "mac" %}
      </{{address_type}}>
    </{{address_type}}-acl>
  {% else %}
    </{{address_type}}>
  {% endif %}

</config>
"""

acl_delete = """
<config>
  {% if address_type != "mac" %}
    <{{address_type}}-acl
      xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
      <{{address_type}}>
  {% else %}
    <{{address_type}}
      xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
  {% endif %}

        <access-list>
          <{{acl_type}} operation="delete" >
            <name>{{acl_name}}</name>
          </{{acl_type}}>
        </access-list>

  {% if address_type != "mac" %}
      </{{address_type}}>
    </{{address_type}}-acl>
  {% else %}
    </{{address_type}}>
  {% endif %}

</config>
"""


acl_get_config = """
<get-config>
  <source> <running/> </source>

  {% if acl_type == "standard" -%}

    <nc:filter type='xpath' select='/{{address_type}}-acl/{{address_type}}/\
access-list/{{acl_type}}[name=\"{{acl_name}}\"]/\
hide-{{address_type}}-acl-std/seq/seq-id'></nc:filter>

  {% else -%}

    <nc:filter type='xpath' select='/{{address_type}}-acl/{{address_type}}/\
access-list/{{acl_type}}[name=\"{{acl_name}}\"]/\
hide-{{address_type}}-acl-ext/seq/seq-id'></nc:filter>

  {% endif %}

</get-config>
"""

acl_get_config_name = """
<get-config>
  <source> <running/> </source>

  {% if address_type != "mac" -%}

    <nc:filter type='xpath' select='/{{address_type}}-acl/{{address_type}}/\
access-list/{{acl_type}}[name=\"{{acl_name}}\"]'>

  {% else -%}

    <nc:filter type='xpath' select='/{{address_type}}/access-list/\
{{acl_type}}[name=\"{{acl_name}}\"]'>

  {% endif %}
    </nc:filter>
</get-config>
"""

acl_rule_ipx_delete = """
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
              <seq operation="delete">
                <seq-id>{{seq_id}}</seq-id>
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

acl_rule_mac_delete = """
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
          <seq operation="delete">
            <seq-id>{{seq_id}}</seq-id>
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
   {% if rbridge_id is defined and rbridge_id is not none %}
      <rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">
         <rbridge-id>{{rbridge_id}}</rbridge-id>
   {% elif intf_type == 've' %}
      <routing-system xmlns="urn:brocade.com:mgmt:brocade-common-def">
   {% elif intf_type == 'vlan' %}
      <interface-vlan xmlns="urn:brocade.com:mgmt:brocade-interface">
   {% endif %}
         <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
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
         </interface>
   {% if rbridge_id is defined and rbridge_id is not none %}
      </rbridge-id>
   {% elif intf_type == 've' %}
      </routing-system>
   {% elif intf_type == 'vlan' %}
      </interface-vlan>
   {% endif %}
</config>
"""

acl_remove = """
<config>
   {% if rbridge_id is defined and rbridge_id is not none %}
      <rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">
         <rbridge-id>{{rbridge_id}}</rbridge-id>
   {% elif intf_type == 've' %}
      <routing-system xmlns="urn:brocade.com:mgmt:brocade-common-def">
   {% elif intf_type == 'vlan' %}
      <interface-vlan xmlns="urn:brocade.com:mgmt:brocade-interface">
   {% endif %}
         <interface xmlns="urn:brocade.com:mgmt:brocade-interface">
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
         </interface>
   {% if rbridge_id is defined and rbridge_id is not none %}
      </rbridge-id>
   {% elif intf_type == 've' %}
      </routing-system>
   {% elif intf_type == 'vlan' %}
      </interface-vlan>
   {% endif %}
</config>
"""

get_interface_by_name = """
<get-config>
  <source> <running/> </source>
  <nc:filter type='xpath' select='/interface/{{intf_type}}[name=\"{{intf_name}}\"]'> </nc:filter>
</get-config>
"""
