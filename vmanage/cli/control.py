import requests
import urllib3
import click
from rich.console import Console
from rich.table import Table
import datetime
from vmanage.constants import vmanage
from vmanage.api.authenticate import authentication
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group(name="control")
def cli_control():
    """Commands to monitor control plane: connections, connections-history
    """
    pass


@cli_control.command(
    name="connections", help="Display control connections information")
@click.option("--system_ip", help="System IP of the WAN Edge")
def control_connections(system_ip):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/device/control/connections?deviceId={system_ip}&&"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed: " + str(response.text))
        exit()
    console = Console()
    table = Table(
        "Peer Type", "Peer Protocol", "Peer System IP", "Site ID", "Domain ID",
        "Private IP", "Private Port", "Public IP", "Public Port", "Local Color",
        "Proxy", "State", "Uptime", "Control Group ID", "Last Updated")

    for item in items:
        # breakpoint()
        time_date = datetime.datetime.fromtimestamp(
            int(item["lastupdated"])/1000).strftime('%c')
        table.add_row(f'[green]{item["peer-type"]}[/green]',
                      f'[magenta]{item["protocol"]}[/magenta]',
                      f'[cyan]{item["system-ip"]}[/cyan]',
                      f'[orange1]{item["site-id"]}[/orange1]',
                      f'[bright_green]{item["domain-id"]}[/bright_green]',
                      f'[magenta]{item["private-ip"]}[/magenta]',
                      f'[cyan]{item["private-port"]}[/cyan]',
                      f'[orange1]{item["public-ip"]}[/orange1]',
                      f'[green]{item["public-port"]}[/green]',
                      f'[magenta]{item["local-color"]}[/magenta]',
                      f'[cyan]{item["behind-proxy"]}[/cyan]',
                      f'[orange1]{item["state"]}[/orange1]',
                      f'[bright_green]{item["uptime"]}[/bright_green]',
                      f'[magenta]{item["controller-group-id"]}[/magenta]',
                      f'[yellow]{time_date}[/yellow]',)
    console.print(table)


@cli_control.command(
    name="connections-history", help="Display control connection history")
@click.option("--system_ip", help="System IP of the WAN Edge")
def control_connections_history(system_ip):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/device/control/connectionshistory?deviceId={system_ip}&&&"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed: " + str(response.text))
        exit()
    console = Console()
    table = Table(
        "Peer Type", "Peer Protocol", "Peer System IP", "Site ID", "Domain ID",
        "Private IP", "Private Port", "Public IP", "Public Port", "Local Color",
        "State", "Local Error", "Remote Error", "Repeat Count", "Downtime")

    for item in items:
        # breakpoint()
        table.add_row(f'[green]{item["peer-type"]}[/green]',
                      f'[magenta]{item["protocol"]}[/magenta]',
                      f'[cyan]{item["system-ip"]}[/cyan]',
                      f'[orange1]{item["site-id"]}[/orange1]',
                      f'[bright_green]{item["domain-id"]}[/bright_green]',
                      f'[magenta]{item["private-ip"]}[/magenta]',
                      f'[cyan]{item["private-port"]}[/cyan]',
                      f'[orange1]{item["public-ip"]}[/orange1]',
                      f'[green]{item["public-port"]}[/green]',
                      f'[magenta]{item["local-color"]}[/magenta]',
                      f'[cyan]{item["state"]}[/cyan]',
                      f'[orange1]{item["local_enum"]}[/orange1]',
                      f'[bright_green]{item["remote_enum"]}[/bright_green]',
                      f'[magenta]{item["rep-count"]}[/magenta]',
                      f'[yellow]{item["downtime"]}[/yellow]',)
    console.print(table)
