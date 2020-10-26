def generate_dict_vpn_ip_nexthops(nexthops):
    """
    This function generates the block of configurtion for the VPN IP
    nexthops that will be used in CLI template to generate VPN Feature
    Template
    """
    vipValue = []
    for nexthop in nexthops:
        vipValue.append(
            {
                "address": {
                    "vipObjectType": "object",
                    "vipType": "variableName",
                    "vipValue": "",
                    "vipVariableName": nexthop
                }
            }
        )
    return vipValue
    pass

