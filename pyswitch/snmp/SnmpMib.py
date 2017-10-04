

class SnmpMib:
    """
    Class containing all the standard SNMP MIBs supported by Pyswitch
    """
    mib_oid_map = {
        'sysObjectId': '1.3.6.1.2.1.1.2.0',
        'dot1qVlanStaticTable': '1.3.6.1.2.1.17.7.1.4.3.1',
        'dot1qVlanStaticEntry': '1.3.6.1.2.1.17.7.1.4.3.1.1',
        'dot1qVlanStaticName': '1.3.6.1.2.1.17.7.1.4.3.1.2',
        'dot1qVlanStaticEgressPorts': '1.3.6.1.2.1.17.7.1.4.3.1.3',
        'dot1qVlanForbiddenEgressPorts': '1.3.6.1.2.1.17.7.1.4.3.1.4',
        'dot1qVlanStaticRowStatus': '1.3.6.1.2.1.17.7.1.4.3.1.5',
        'dot3adAggTable': '1.2.840.10006.300.43.1.1.1.1',
        'dot3adAggIndex': '1.2.840.10006.300.43.1.1.1.1.1',
        'dot3adAggMACAddress': '1.2.840.10006.300.43.1.1.1.1.2',
        'dot3adAggActorSystemPriority': '1.2.840.10006.300.43.1.1.1.1.3',
        'dot3adAggActorSystemID': '1.2.840.10006.300.43.1.1.1.1.4',
        'dot3adAggAggregateOrIndividual': '1.2.840.10006.300.43.1.1.1.1.5',
        'dot3adAggActorAdminKey': '1.2.840.10006.300.43.1.1.1.1.6',
        'dot3adAggActorOperKey': '1.2.840.10006.300.43.1.1.1.1.7',
        'dot3adAggPartnerSystemID': '1.2.840.10006.300.43.1.1.1.1.8',
        'dot3adAggPartnerSystemPriority': '1.2.840.10006.300.43.1.1.1.1.9',
        'dot3adAggPartnerOperKey': '1.2.840.10006.300.43.1.1.1.1.10',
        'dot3adAggCollectorMaxDelay': '1.2.840.10006.300.43.1.1.1.1.11',
        'ifXTable': '1.3.6.1.2.1.31.1.1',
        'ifXEntry': '1.3.6.1.2.1.31.1.1.1',
        'ifAdminStatus': '1.3.6.1.2.1.2.2.1.7',
        'ifAlias': '1.3.6.1.2.1.31.1.1.1.18',
    }
