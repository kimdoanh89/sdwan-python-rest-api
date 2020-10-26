{
    "deviceType": [
        "vedge-cloud"
    ],
    "templateType": "vpn-vedge-interface",
    "templateMinVersion": "15.0.0",
    "templateDefinition": {
            "if-name": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": "ge0/1",
                "vipVariableName": "vpn_if_name"
            },
            "description": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": "Internet",
                "vipVariableName": "vpn_if_description"
            },
            "ip": {
                "address": {
                    "vipObjectType": "object",
                    "vipType": "variableName",
                    "vipValue": "",
                    "vipVariableName": "vpn0_g1_if_ipv4_address"
                }
            },
            "shutdown": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": "false",
                "vipVariableName": "vpn_if_shutdown"
            },
            "tunnel-interface": {
                "color": {
                    "value": {
                        "vipObjectType": "object",
                        "vipType": "constant",
                        "vipValue": "biz-internet",
                        "vipVariableName": "vpn_if_tunnel_color_value"
                    },
                    "restrict": {
                        "vipObjectType": "node-only",
                        "vipType": "ignore",
                        "vipValue": "false",
                        "vipVariableName": "vpn_if_tunnel_color_restrict"
                    }
                },
                "allow-service": {
                    "dhcp": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "true",
                        "vipVariableName": "vpn_if_tunnel_dhcp"
                    },
                    "dns": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "true",
                        "vipVariableName": "vpn_if_tunnel_dns"
                    },
                    "icmp": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "true",
                        "vipVariableName": "vpn_if_tunnel_icmp"
                    },
                    "sshd": {
                        "vipObjectType": "object",
                        "vipType": "constant",
                        "vipValue": "true",
                        "vipVariableName": "vpn_if_tunnel_sshd"
                    },
                    "ntp": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "false",
                        "vipVariableName": "vpn_if_tunnel_ntp"
                    },
                    "stun": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "false",
                        "vipVariableName": "vpn_if_tunnel_stun"
                    },
                    "all": {
                        "vipObjectType": "object",
                        "vipType": "constant",
                        "vipValue": "true",
                        "vipVariableName": "vpn_if_tunnel_all"
                    },
                    "bgp": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "false",
                        "vipVariableName": "vpn_if_tunnel_bgp"
                    },
                    "ospf": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "false",
                        "vipVariableName": "vpn_if_tunnel_ospf"
                    },
                    "netconf": {
                        "vipObjectType": "object",
                        "vipType": "constant",
                        "vipValue": "true",
                        "vipVariableName": "vpn_if_tunnel_netconf"
                    },
                    "snmp": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "false"
                    },
                    "https": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "true",
                        "vipVariableName": "vpn_if_tunnel_https"
                    }
                },
            "max-control-connections": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipVariableName": "vpn_if_tunnel_max_control_connections"
            },
            "vbond-as-stun-server": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": "false",
                "vipVariableName": "vpn_if_tunnel_vbond_as_stun_server"
            },
            "exclude-controller-group-list": {
                "vipObjectType": "list",
                "vipType": "ignore",
                "vipVariableName": "vpn_if_tunnel_exclude_controller_group_list"
            },
            "vmanage-connection-preference": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": 5,
                "vipVariableName": "vpn_if_tunnel_vmanage_connection_preference"
            },
            "port-hop": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": "true",
                "vipVariableName": "vpn_if_tunnel_port_hop"
            },
            "low-bandwidth-link": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": "false",
                "vipVariableName": "vpn_if_tunnel_low_bandwidth_link"
            },
            "last-resort-circuit": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": "false",
                "vipVariableName": "vpn_if_tunnel_last_resort_circuit"
            },
            "hold-time": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": 7000,
                "vipVariableName": "hold-time"
            },
            "nat-refresh-interval": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": 5,
                "vipVariableName": "vpn_if_tunnel_nat_refresh_interval"
            },
            "hello-interval": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": 1000,
                "vipVariableName": "vpn_if_tunnel_hello_interval"
            },
            "hello-tolerance": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": 12,
                "vipVariableName": "vpn_if_tunnel_hello_tolerance"
            },
            "tloc-extension-gre-to": {
                "dst-ip": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_tunnel_tloc_ext_gre_to_dst_ip"
                }
            },
            "control-connections": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": "true",
                "vipVariableName": "control_connections"
            }
        },
        "ip-directed-broadcast": {
            "vipObjectType": "object",
            "vipType": "ignore",
            "vipValue": "false",
            "vipVariableName": "vpn_if_ip-directed-broadcast"
        },
        "ipv6": {
            "access-list": {
                "vipType": "ignore",
                "vipValue": [],
                "vipObjectType": "tree",
                "vipPrimaryKey": [
                    "direction"
                ]
            },
            "address": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": "",
                "vipVariableName": "vpn_if_ipv6_ipv6_address"
            },
            "dhcp-helper-v6": {
                "vipType": "ignore",
                "vipValue": [],
                "vipObjectType": "tree",
                "vipPrimaryKey": [
                    "address"
                ]
            },
            "secondary-address": {
                "vipType": "ignore",
                "vipValue": [],
                "vipObjectType": "tree",
                "vipPrimaryKey": [
                    "address"
                ]
            }
        },
        "arp": {
            "ip": {
                "vipType": "ignore",
                "vipValue": [],
                "vipObjectType": "tree",
                "vipPrimaryKey": [
                    "addr"
                ]
            }
        },
        "vrrp": {
            "vipType": "ignore",
            "vipValue": [],
            "vipObjectType": "tree",
            "vipPrimaryKey": [
                "grp-id"
            ]
        },
        "ipv6-vrrp": {
            "vipType": "ignore",
            "vipValue": [],
            "vipObjectType": "tree",
            "vipPrimaryKey": [
                "grp-id"
            ]
        },
        "dot1x": {
            "vipType": "ignore",
            "vipObjectType": "node-only"
        }
    },
    "configType": "xml",
    "attachedMastersCount": 3,
    "templateId": "beabf169-c9d3-4cdd-a3bf-382cce7db82b",
    "createdOn": 1603564859732,
    "@rid": 324,
    "factoryDefault": false,
    "feature": "vmanage-default",
    "createdBy": "admin",
    "templateName": "VE-VPN0-G1",
    "devicesAttached": 4,
    "templateDescription": "VE-VPN0-G1",
    "lastUpdatedOn": 1603565327215
}