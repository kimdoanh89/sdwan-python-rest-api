import requests
import urllib3
import click
from rich.console import Console
from rich.table import Table
from vmanage.constants import vmanage
from vmanage.authenticate import authentication
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group(name="bfd")
def cli_bfd():
    """Commands monitor bfd sessions: link --state, summary
    """
    pass


@cli_bfd.command(name="link", help="Get list of links with status: up or down")
@click.option("--state", help="State of BFD connections")
def connection_status(state):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/device/bfd/links?state={state}"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed to get list of devices " + str(response.text))
        exit()
    console = Console()
    table = Table(
        "System IP 1", "Host-Name 1", "System IP 2", "Host-Name 2",
        "Link", "Status", "Last Updated")

    for item in items:
        table.add_row(f'[green]{item["asystem-ip"]}[/green]',
                      f'[blue]{item["ahost-name"]}[/blue]',
                      f'[magenta]{item["bsystem-ip"]}[/magenta]',
                      f'[cyan]{item["bhost-name"]}[/cyan]',
                      f'[orange1]{item["linkKeyDisplay"]}[/orange1]',
                      f'[bright_green]{item["state"]}[/bright_green]',
                      f'[yellow]{item["lastupdated"]}[/yellow]')
    console.print(table)
