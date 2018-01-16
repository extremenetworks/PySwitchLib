
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
