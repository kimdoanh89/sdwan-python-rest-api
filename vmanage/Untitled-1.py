{
    "deviceType": [
        "vedge-cloud"
    ],
    "templateType": "vpn-vedge",
    "templateMinVersion": "15.0.0",
    "templateDefinition": {
            "vpn-id": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": 0
            },
            "name": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": "Transport VPN",
                "vipVariableName": "vpn_name"
            },
            "ip": {
                "route": {
                    "vipType": "constant",
                    "vipValue": [
                        {
                            "prefix": {
                                "vipObjectType": "object",
                                "vipType": "constant",
                                "vipValue": "0.0.0.0/0",
                                "vipVariableName": "vpn_ipv4_ip_prefix"
                            },
                            "vipOptional": "false",
                            "next-hop": {
                                "vipType": "constant",
                                "vipValue": [
                                    {
                                        "address": {
                                            "vipObjectType": "object",
                                            "vipType": "variableName",
                                            "vipValue": "",
                                            "vipVariableName": "vpn0_g0_next_hop_ip_address_0"
                                        }
                                    },
                                    {
                                        "address": {
                                            "vipObjectType": "object",
                                            "vipType": "variableName",
                                            "vipValue": "",
                                            "vipVariableName": "vpn0_g1_next_hop_ip_address_1"
                                        }
                                    },
                                    {
                                        "address": {
                                            "vipObjectType": "object",
                                            "vipType": "variableName",
                                            "vipValue": "",
                                            "vipVariableName": "vpn0_g2_next_hop_ip_address_2"
                                        }
                                    }
                                ],
                                "vipObjectType": "tree",
                                "vipPrimaryKey": [
                                    "address"
                                ]
                            },
                            "priority-order": [
                                "prefix",
                                "next-hop"
                            ]
                        }
                    ],
                    "vipObjectType": "tree",
                    "vipPrimaryKey": [
                        "prefix"
                    ]
                },
                "gre-route": {},
                "ipsec-route": {},
                "service-route": {}
            }
    },
    "configType": "xml",
    "attachedMastersCount": 1,
    "templateId": "8b28af80-58c6-4773-90e0-43aeabdc843f",
    "createdOn": 1603564206774,
    "@rid": 635,
    "factoryDefault": false,
    "feature": "vmanage-default",
    "createdBy": "admin",
    "templateName": "VE-BR-VPN0",
    "devicesAttached": 2,
    "templateDescription": "VE-BR-VPN0",
    "lastUpdatedOn": 1603564206774
}