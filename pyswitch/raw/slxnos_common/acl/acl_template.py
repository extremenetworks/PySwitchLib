
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

acl_rule_ip = """
<config>
  <{{address_type}}-acl
    xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
    <{{address_type}}>
      <access-list>
        <{{acl_type}}>
          <name>{{acl_name}}</name>
          <hide-{{address_type}}-acl-{{acl_type[:3] }}>
              <seq>
                <seq-id>{{seq_id}}</seq-id>
                <action>{{action}}</action>
                <src-host-any-sip>{{source.host_any}}</src-host-any-sip>
                {% if source.host_any != "any" %}
                  {% if source.host_any == "host" %}
                    <src-host-ip>{{source.host_ip}}</src-host-ip>
                  {% else %}
                    <src-mask>{{source.mask}}</src-mask>
                  {% endif %}
                {% endif %}

                {% if acl_type == "extended" %}
                  <protocol-type>{{protocol_type}}</protocol-type>

                  <dst-host-any-dip>{{destination.host_any}}</dst-host-any-dip>
                  {% if destination.host_any != "any" %}
                    {% if destination.host_any == "host" %}
                      <dst-host-ip>{{destination.host_ip}}</dst-host-ip>
                    {% else %}
                      <dst-mask>{{destination.mask}}</dst-mask>
                    {% endif %}
                  {% endif %}

                  {% if drop_precedence_force is not none %}
                    <drop-precedence-force>{{drop_precedence_force}}
                    </drop-precedence-force>
                  {% endif %}

                  {% if dscp is not none %} <dscp>{{dscp}}</dscp> {% endif %}

                  {% if vlan_id is not none %}
                    <vlan-id>{{vlan_id}}</vlan-id>
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
              </seq>
          </hide-{{address_type}}-acl-{{acl_type[:3] }}>
        </{{acl_type}}>
      </access-list>
    </{{address_type}}>
  </{{address_type}}-acl>
</config>
"""


acl_rule_ip_delete = """
<config>
  <{{address_type}}-acl
    xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
    <{{address_type}}>
      <access-list>
        <{{acl_type}}>
          <name>{{acl_name}}</name>
          <hide-{{address_type}}-acl-{{acl_type[:3] }}>
            <seq operation="delete">
              <seq-id>{{seq_id}}</seq-id>
            </seq>
          </hide-{{address_type}}-acl-{{acl_type[:3] }}>
        </{{acl_type}}>
      </access-list>
    </{{address_type}}>
  </{{address_type}}-acl>
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

tmp_acl_rule_ip = """
<config>
   <{{address_type}}-acl
        xmlns="urn:brocade.com:mgmt:brocade-{{address_type}}-access-list">
      <{{address_type}}>
         <access-list>
            <{{acl_type}}>
               <name>{{acl_name}}</name>
               {{sequences}}

               <seq operation=\'delete\'> {{seq_id}} </seq>
               sequences = "<hide-ip-acl-std>\n{}</hide-ip-acl-std>\n".format(sequences)

            </{{acl_type}}>
         </access-list>
      </{{address_type}}>
   </{{address_type}}-acl>
</config>
"""
