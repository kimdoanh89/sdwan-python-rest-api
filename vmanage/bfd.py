import requests
import urllib3
import click
from rich.console import Console
from rich.table import Table
import datetime
from vmanage.constants import vmanage
from vmanage.authenticate import authentication
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group(name="bfd")
def cli_bfd():
    """Commands to monitor bfd sessions: link --state, summary, session
    """
    pass


@cli_bfd.command(
    name="link", help="Get list of bfd links with status: up or down")
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
        # breakpoint()
        time_date = datetime.datetime.fromtimestamp(
            int(item["lastupdated"])/1000).strftime('%c')
        table.add_row(f'[green]{item["asystem-ip"]}[/green]',
                      f'[blue]{item["ahost-name"]}[/blue]',
                      f'[magenta]{item["bsystem-ip"]}[/magenta]',
                      f'[cyan]{item["bhost-name"]}[/cyan]',
                      f'[orange1]{item["linkKeyDisplay"]}[/orange1]',
                      f'[bright_green]{item["state"]}[/bright_green]',
                      f'[yellow]{time_date}[/yellow]')
    console.print(table)


@cli_bfd.command(name="summary", help="Show BFD summary of a device")
@click.option("--system_ip", help="system ip of the device")
def summary_device(system_ip):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/device/bfd/summary?deviceId={system_ip}"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print(str(response.text))
        exit()
    console = Console()
    table = Table(
        "Sessions Total", "Sessions Up", "Sessions Max",
        "Sessions Flap", "App Route Poll Interval", "Last Updated")

    for item in items:
        time_date = datetime.datetime.fromtimestamp(
            int(item["lastupdated"])/1000).strftime('%c')
        table.add_row(f'[blue]{item["bfd-sessions-total"]}[/blue]',
                      f'[magenta]{item["bfd-sessions-up"]}[/magenta]',
                      f'[cyan]{item["bfd-sessions-max"]}[/cyan]',
                      f'[orange1]{item["bfd-sessions-flap"]}[/orange1]',
                      f'[bright_green]{item["poll-interval"]}[/bright_green]',
                      f'[yellow]{time_date}[/yellow]')
    console.print(table)


@cli_bfd.command(name="session", help="Show BFD sessions at a device")
@click.option("--system_ip", help="system ip of the device")
def session_device(system_ip):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/device/bfd/sessions?deviceId={system_ip}"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print(str(response.text))
        exit()
    console = Console()
    table = Table(
        "System IP", "Site ID", "State", "Source TLOC color",
        "Remote TLOC color", "Source IP", "Destination Public IP",
        "Destination Public Port", "Encapsulation", "Source Port",
        "Last Updated")

    for item in items:
        time_date = datetime.datetime.fromtimestamp(
            int(item["lastupdated"])/1000).strftime('%c')
        table.add_row(f'[green]{item["system-ip"]}[/green]',
                      f'[magenta]{item["site-id"]}[/magenta]',
                      f'[cyan]{item["state"]}[/cyan]',
                      f'[orange1]{item["local-color"]}[/orange1]',
                      f'[bright_green]{item["color"]}[/bright_green]',
                      f'[magenta]{item["src-ip"]}[/magenta]',
                      f'[cyan]{item["dst-ip"]}[/cyan]',
                      f'[orange1]{item["dst-port"]}[/orange1]',
                      f'[bright_green]{item["proto"]}[/bright_green]',
                      f'[magenta]{item["src-port"]}[/magenta]',
                      f'[yellow]{time_date}[/yellow]',)
    console.print(table)
