import requests
import urllib3
import click
import json
from rich.console import Console
from rich.table import Table
# from rich.text import Text
from vmanage.api.authenticate import authentication
from vmanage.constants import vmanage
from vmanage.api.vpn import generate_dict_vpn_ip_nexthops
import ast
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group(name="template")
def cli_template():
    """Commands to manage Device and Feature Templates: list, show, create, delete
    """


@click.group()
def device():
    """
    Manage Device Templates: list, show, create, delete
    """


@click.group()
def feature():
    """
    Manage Feature Templates: list, show, create, delete
    """


@click.group(name="create")
def feature_create():
    """
    Create Feature Template: banner, system, vpn, vpn-int, ...
    """


@device.command(name="list", help="Get Device Template List")
@click.option('--default/--no-default', help="Print system default templates", default=False)
def template_list(default):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/template/device"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed to get list of devices " + str(response.text))
        exit()

    console = Console()
    table = Table(
        "Template Name", "Device Model", "Template ID",
        "Attached devices", "Template version")

    for item in items:
        if not default and item["factoryDefault"]:
            continue
        table.add_row(
            f'[green]{item["templateName"]}[/green]',
            f'[blue]{item["deviceType"]}[/blue]',
            f'[magenta]{item["templateId"]}[/magenta]',
            f'[orange1]{item["devicesAttached"]}[/orange1]',
            f'[bright_yellow]{item["templateAttached"]}[/bright_yellow]')
    console.print(table)


@device.command(name="delete", help="Delete a Device Template")
@click.option("--template_id", help="ID of the template you wish to delete")
def delete_template(template_id):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/template/device/{template_id}?api_key=/template/device"
    url = base_url + api
    response = requests.delete(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        print("Succed to delete the template " + str(template_id))
    else:
        print("Failed to delete the template " + str(template_id))
        exit()


@device.command(name="show", help="Show details of a Device Template")
@click.argument('template_id')
def show_template(template_id):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/template/device/object/{template_id}?api_key=/template/device"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print("Failed to show the template " + str(template_id))
        exit()


@feature.command(name="list", help="Get Feature Template list")
@click.option('--default/--no-default', help="Print system default templates", default=False)
def feature_list(default):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/template/feature"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed to get list of devices " + str(response.text))
        exit()

    console = Console()
    table = Table(
        "Template Name", "Template Type")
    table.add_column("Device Model", width=15)
    table.add_column("Template ID", width=36)
    table.add_column("Attached devices", width=10)
    table.add_column("Device Templates", width=10)

    for item in items:
        if not default and item["factoryDefault"]:
            continue
        table.add_row(
            f'[green]{item["templateName"]}[/green]',
            f'[blue]{item["templateType"]}[/blue]',
            f'[blue]{item["deviceType"]}[/blue]',
            f'[magenta]{item["templateId"]}[/magenta]',
            f'[orange1]{item["devicesAttached"]}[/orange1]',
            f'[bright_green]{item["attachedMastersCount"]}[/bright_green]')
    console.print(table)


@feature.command(name="delete", help="Delete a Feature Template")
@click.argument("template_id")
def delete_feature_template(template_id):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/template/feature/{template_id}?api_key=/template/feature"
    url = base_url + api
    response = requests.delete(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        print("Succeed to delete the template " + str(template_id))
    else:
        print("Failed to delete the template " + str(template_id))
        exit()


@feature.command(name="show", help="Show details of a Feature Template")
@click.argument('template_id')
def show_feature_template(template_id):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/template/feature/object/{template_id}?api_key=/template/feature"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print("Failed to show the template " + str(template_id))
        exit()


class PythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


@feature_create.command(name="banner", help="Create a Banner Feature Template")
@click.option(
    "--types", "-t", cls=PythonLiteralOption, default=[],
    help="List of device types, ex. '[\"vedge-cloud\", \"vedge-1000\"]'",
    )
@click.option("--name", "-n", help="Name of the Template']")
def create_feature_template(types, name):
    """ Usage: sdwancli template feature create banner -t '["vedge-cloud",
    "vedge-1000"]' -n VE-banner-2
    """
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/template/feature"
    url = base_url + api
    payload = {
        "deviceType": types,
        "templateType": "banner",
        "templateMinVersion": "15.0.0",
        "templateDefinition": {
            "login": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": "This is vEdge Cloud Login banner",
                "vipVariableName": "banner_login"
            },
            "motd": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": "This is vEdge Cloud MOTD banner",
                "vipVariableName": "banner_motd"
            }
        },
        "factoryDefault": "false",
        "templateName": name,
        "templateDescription": "VE-Banner"
    }
    response = requests.post(
        url=url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print("Failed to create the template ")
        exit()


@feature_create.command(name="system", help="Create a Feature Template System")
@click.option(
    "--types", "-t", cls=PythonLiteralOption, default=[],
    help="List of device types, ex. '[\"vedge-cloud\", \"vedge-1000\"]'",
    )
@click.option("--name", "-n", help="Name of the Template']")
@click.option("--time_zone", "-time", help="Timezone setting of the System']")
def create_system_feature_template(types, name, time_zone):
    """ Usage: sdwancli template feature create banner -t '["vedge-cloud",
    "vedge-1000"]' -n VE-banner-2
    """
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/template/feature"
    url = base_url + api
    payload = {
        "deviceType": types,
        "templateType": "system-vedge",
        "templateMinVersion": "15.0.0",
        "templateDefinition": {
            "clock": {
                "timezone": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": time_zone,
                    "vipVariableName": "system_timezone"
                }
            },
            "site-id": {
                "vipObjectType": "object",
                "vipType": "variableName",
                "vipValue": "",
                "vipVariableName": "system_site_id"
            },
            "system-ip": {
                "vipObjectType": "object",
                "vipType": "variableName",
                "vipValue": "",
                "vipVariableName": "system_system_ip"
            },
            "host-name": {
                "vipObjectType": "object",
                "vipType": "variableName",
                "vipValue": "",
                "vipVariableName": "system_host_name"
            },
            "console-baud-rate": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": "_empty",
                "vipVariableName": "system_console_baud_rate"
            }
        },
        "factoryDefault": "false",
        "templateName": name,
        "templateDescription": "VE-System"
    }
    response = requests.post(
        url=url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print("Failed to create the template ")
        exit()


@feature_create.command(name="vpn", help="Create a Feature Template System")
@click.option(
    "--types", "-t", cls=PythonLiteralOption, default=[],
    help="List of device types, ex. '[\"vedge-cloud\", \"vedge-1000\"]'",
    )
@click.option("--name", "-n", help="Name of the Template']")
@click.option("--vpn_id", "-id", help="VPN ID of the VPN Template']")
@click.option("--description", "-d", help="Description of the VPN Template']")
@click.option("--prefix", "-p", help="Description of the VPN Template']", required=False)
@click.option(
    "--nexthops", "-nh", required=False, cls=PythonLiteralOption, default=[],
    help="List of nexthops ip address names, ex. '[\"vpn_g2_if\", \"vpn_g1_if\"]'")
def create_vpn_feature_template(types, name, vpn_id, description, prefix, nexthops):
    """ Usage: sdwancli template feature create banner -t '["vedge-cloud",
    "vedge-1000"]' -n VE-banner-2
    """
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/template/feature"
    url = base_url + api
    if nexthops:
        payload = {
            "deviceType": types,
            "templateType": "vpn-vedge",
            "templateMinVersion": "15.0.0",
            "templateDefinition": {
                "vpn-id": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": vpn_id
                },
                "name": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": description,
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
                                    "vipValue": prefix,
                                    "vipVariableName": "vpn_ipv4_ip_prefix"
                                },
                                "vipOptional": "false",
                                "next-hop": {
                                    "vipType": "constant",
                                    "vipValue": generate_dict_vpn_ip_nexthops(nexthops),
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
            "factoryDefault": "false",
            "templateName": name,
            "templateDescription": "VPN feature template"
        }
    else:
        payload = {
            "deviceType": types,
            "templateType": "vpn-vedge",
            "templateMinVersion": "15.0.0",
            "templateDefinition": {
                "vpn-id": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": vpn_id
                },
                "name": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": description,
                    "vipVariableName": "vpn_name"
                },
            },
            "factoryDefault": "false",
            "templateName": name,
            "templateDescription": "VPN feature template"
        }
    response = requests.post(
        url=url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print("Failed to create the template ")
        exit()


@feature_create.command(name="vpn-int", help="Create a Feature Template System")
@click.option(
    "--types", "-t", cls=PythonLiteralOption, default=[],
    help="List of device types, ex. '[\"vedge-cloud\", \"vedge-1000\"]'",
    )
@click.option("--name", "-n", help="Name of the Template']")
@click.option("--if_name", "-i", help="Interface Name of the VPN INT Template']")
@click.option("--description", "-d", help="Description of the VPN INT']", required=False)
@click.option("--ip_addr_name", "-ip", help="IPv4 variable name']", required=False)
@click.option("--color", "-c", help="Color of the interface']", required=False)
def create_vpn_int_feature_template(types, name, if_name, description, ip_addr_name, color):
    """ Usage: sdwancli template feature create banner -t '["vedge-cloud",
    "vedge-1000"]' -n VE-banner-2
    """
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/template/feature"
    url = base_url + api
    if ip_addr_name:
        payload = {
            "deviceType": types,
            "templateType": "vpn-vedge-interface",
            "templateMinVersion": "15.0.0",
            "templateDefinition": {
                "if-name": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": if_name,
                    "vipVariableName": "vpn_if_name"
                },
                "description": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": description,
                    "vipVariableName": "vpn_if_description"
                },
                "ip": {
                    "address": {
                        "vipObjectType": "object",
                        "vipType": "variableName",
                        "vipValue": "",
                        "vipVariableName": ip_addr_name
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
                            "vipValue": color,
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
                        "sshd": {
                            "vipObjectType": "object",
                            "vipType": "constant",
                            "vipValue": "true",
                            "vipVariableName": "vpn_if_tunnel_sshd"
                        },
                        "all": {
                            "vipObjectType": "object",
                            "vipType": "constant",
                            "vipValue": "true",
                            "vipVariableName": "vpn_if_tunnel_all"
                        },
                        "netconf": {
                            "vipObjectType": "object",
                            "vipType": "constant",
                            "vipValue": "true",
                            "vipVariableName": "vpn_if_tunnel_netconf"
                        }
                    }
                }
            },
            "factoryDefault": "false",
            "templateName": name,
            "templateDescription": "VPN Interface Ethernet feature template"
        }
    else:
        payload = {
            "deviceType": types,
            "templateType": "vpn-vedge-interface",
            "templateMinVersion": "15.0.0",
            "templateDefinition": {
                "if-name": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": if_name,
                    "vipVariableName": "vpn_if_name"
                },
                "description": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": description,
                    "vipVariableName": "vpn_if_description"
                }
            },
            "factoryDefault": "false",
            "templateName": name,
            "templateDescription": "VPN Interface Ethernet feature template"
        }

    response = requests.post(
        url=url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print("Failed to create the template ")
        exit()


cli_template.add_command(device)
cli_template.add_command(feature)
feature.add_command(feature_create)
