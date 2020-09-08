import requests
import urllib3
import click
from rich.console import Console
from rich.table import Table
from vmanage.constants import vmanage
from vmanage.authenticate import authentication
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group(name="device")
def cli_device():
    """Commands to manage device: list, show, create
    """
    pass


@cli_device.command(name="list", help="Get device list")
def device_list():
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
