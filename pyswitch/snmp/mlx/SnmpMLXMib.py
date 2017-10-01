
from pyswitch.snmp.SnmpMib import SnmpMib as BaseSnmpMib


class SnmpMLXMib(BaseSnmpMib):
    """
    Class containing all the MLX proprietary SNMP MIB supported by Pyswitch
    Update the dictionary with MLX specific MIBs
    """
    BaseSnmpMib.mib_oid_map.update({
        'fdryLinkAggregationGroupTable': '1.3.6.1.4.1.1991.1.1.3.33.1.1',
        'fdryLinkAggregationGroupEntry': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1',
        'fdryLinkAggregationGroupName': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.1',
        'fdryLinkAggregationGroupType': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.2',
        'fdryLinkAggregationGroupAdminStatus': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.3',
        'fdryLinkAggregationGroupIfList': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.4',
        'fdryLinkAggregationGroupPrimaryPort': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.5',
        'fdryLinkAggregationGroupTrunkType': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.6',
        'fdryLinkAggregationGroupTrunkThreshold': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.7',
        'fdryLinkAggregationGroupLacpTimeout': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.8',
        'fdryLinkAggregationGroupIfIndex': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.9',
        'fdryLinkAggregationGroupPortCount': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.10',
        'fdryLinkAggregationGroupRowStatus': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.11',
        'fdryLinkAggregationGroupId': '1.3.6.1.4.1.1991.1.1.3.33.1.1.1.12',
    })
