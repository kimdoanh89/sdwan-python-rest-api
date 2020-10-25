import requests
import urllib3
import click
from rich.console import Console
from rich.table import Table
import datetime
from vmanage.constants import vmanage
from vmanage.api.authenticate import authentication
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group(name="ipsec")
def cli_ipsec():
    """Commands to monitor ipsec: outbound-connections, inbound-connections
    """
    pass


@cli_ipsec.command(
    name="inbound-connections", help="Show Received TLOCS of a WAN Edge")
@click.option("--system_ip", help="System IP of the WAN Edge")
def inbound_connections(system_ip):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/device/omp/tlocs/received?deviceId={system_ip}"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed: " + str(response.text))
        exit()
    console = Console()
    table = Table(
        "IP", "Color", "Encap", "From Peer", "Tloc Spi",
        "Public IP", "Public Port", "Private IP", "Private Port", "Site ID",
        "BFD Status", "Preference", "Weight", "Originator", "Last Updated")

    for item in items:
        # breakpoint()
        time_date = datetime.datetime.fromtimestamp(
            int(item["lastupdated"])/1000).strftime('%c')
        table.add_row(f'[green]{item["ip"]}[/green]',
                      f'[magenta]{item["color"]}[/magenta]',
                      f'[cyan]{item["encap"]}[/cyan]',
                      f'[orange1]{item["from-peer"]}[/orange1]',
                      f'[bright_green]{item["tloc-spi"]}[/bright_green]',
                      f'[magenta]{item["tloc-public-ip"]}[/magenta]',
                      f'[cyan]{item["tloc-public-port"]}[/cyan]',
                      f'[orange1]{item["tloc-private-ip"]}[/orange1]',
                      f'[green]{item["tloc-private-port"]}[/green]',
                      f'[magenta]{item["site-id"]}[/magenta]',
                      f'[cyan]{item["bfd-status"]}[/cyan]',
                      f'[orange1]{item["preference"]}[/orange1]',
                      f'[bright_green]{item["weight"]}[/bright_green]',
                      f'[magenta]{item["originator"]}[/magenta]',
                      f'[yellow]{time_date}[/yellow]',)
    console.print(table)


@cli_ipsec.command(
    name="outbound-connections", help="Display TLOC paths of a WAN Edge")
@click.option("--system_ip", help="System IP of the WAN Edge")
def outbound_connections(system_ip):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/device/omp/tlocs/received?deviceId={system_ip}"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed: " + str(response.text))
        exit()
    for item in items:
        print("tloc-paths entries", item["ip"], item["color"], item["encap"])
