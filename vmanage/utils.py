import requests
import urllib3
from rich.console import Console
from rich.table import Table
from vmanage.authenticate import authentication
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def device_list(vmanage):
    """
    Get device lists
    """
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/device"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed to get list of devices " + str(response.text))
        exit()
    console = Console()
    table = Table(
        "Host-Name", "Device Type", "Device ID", "System IP",
        "Site ID", "Version", "Device Model")

    for item in items:
        table.add_row(f'[green]{item["host-name"]}[/green]',
                      f'[blue]{item["device-type"]}[/blue]',
                      f'[magenta]{item["uuid"]}[/magenta]',
                      f'[cyan]{item["system-ip"]}[/cyan]',
                      f'[orange1]{item["site-id"]}[/orange1]',
                      f'[bright_green]{item["version"]}[/bright_green]',
                      f'[yellow]{item["device-model"]}[/yellow]')
    console.print(table)


def template_list(vmanage):
    """
    Get device lists
    """
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
        "Template Name", "Device Type", "Template ID",
        "Attached devices", "Template version")

    for item in items:
        table.add_row(f'[green]{item["templateName"]}[/green]',
                      f'[blue]{item["deviceType"]}[/blue]',
                      f'[magenta]{item["templateId"]}[/magenta]',
                      f'[orange1]{item["devicesAttached"]}[/orange1]',
                      f'[bright_yellow]{item["templateAttached"]}[/bright_yellow]')
    console.print(table)
