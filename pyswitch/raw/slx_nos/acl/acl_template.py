
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


acl_rule_ipx_delete_bulk = """
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
              <seq operation="delete">
                <seq-id>{{ud.seq_id}}</seq-id>
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

acl_rule_mac_delete_bulk = """
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
          <seq operation="delete">
            <seq-id>{{ud.seq_id}}</seq-id>
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
