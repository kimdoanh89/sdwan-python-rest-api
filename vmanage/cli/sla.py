import requests
import urllib3
import click
from rich.console import Console
from rich.table import Table
from rich.text import Text
import datetime
import json
from vmanage.constants import vmanage
from vmanage.api.authenticate import authentication
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group(name="sla")
def cli_sla():
    """Commands for managing SLA Class: list, create, edit, delete
    """
    pass


@cli_sla.command(name="list", help="Get list of SLA Classes")
def sla_list():
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/template/policy/list/sla"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Error:: " + str(response.text))
        exit()
    console = Console()
    table = Table(
        "Name", "Loss (%)", "Latency (ms)", "jitter (ms)", "Reference Count",
        "Updated by", "SLA ID", "Last Updated")

    for item in items:
        # breakpoint()
        time_date = datetime.datetime.fromtimestamp(
            item["lastUpdated"]/1000).strftime('%c')
        table.add_row(f'[green]{item["name"]}[/green]',
                      f'[blue]{item["entries"][0]["loss"]}[/blue]',
                      f'[magenta]{item["entries"][0]["latency"]}[/magenta]',
                      f'[cyan]{item["entries"][0]["jitter"]}[/cyan]',
                      f'[orange1]{item["referenceCount"]}[/orange1]',
                      f'[bright_green]{item["owner"]}[/bright_green]',
                      f'[magenta]{item["listId"]}[/magenta]',
                      f'[yellow]{time_date}[/yellow]')
    console.print(table)


@cli_sla.command(name="create", help="Create a SLA Class")
@click.option("--name", help="name of the SLA Class")
@click.option("--description", help="description of the SLA Class")
@click.option("--loss", help="loss 0 - 100 %")
@click.option("--latency", help="latency 1 - 1000 ms")
@click.option("--jitter", help="jitter 1 - 1000 ms")
def sla_create(name, description, loss, latency, jitter):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = "/template/policy/list/sla"
    url = base_url + api
    payload = {
        "name": name,
        "description": description,
        "entries": [
            {
                "latency": latency,
                "loss": loss,
                "jitter": jitter
            }
        ]
    }
    response = requests.post(
        url=url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        items = response.json()
        text = Text.assemble(
            ("Successful", "bold green"),
            " create SLA Class with listID = ",
            (items["listId"], "magenta"))
        console = Console()
        console.print(text)
    else:
        print(str(response.text))
        exit()


@cli_sla.command(name="delete", help="Delete a SLA with sla-id")
@click.option("--sla_id", help="SLA ID")
def summary_device(sla_id):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/template/policy/list/sla/{sla_id}"
    url = base_url + api
    response = requests.delete(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        text = Text.assemble(
            ("Successful", "bold green"),
            " delete SLA Class with listID = ",
            (sla_id, "magenta"))
        console = Console()
        console.print(text)
        exit()
    else:
        print(str(response.text))
        exit()


@cli_sla.command(name="edit", help="Edit a SLA Class")
@click.option("--name", help="name of the SLA Class")
@click.option("--sla_id", help="name of the SLA Class")
@click.option("--loss", help="loss 0 - 100 %")
@click.option("--latency", help="latency 1 - 1000 ms")
@click.option("--jitter", help="jitter 1 - 1000 ms")
def sla_edit(name, sla_id, loss, latency, jitter):
    headers = authentication(vmanage)
    base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
    api = f"/template/policy/list/sla/{sla_id}"
    url = base_url + api
    payload = {
        "name": name,
        "entries": [
            {
                "latency": latency,
                "loss": loss,
                "jitter": jitter
            }
        ]
    }
    response = requests.put(
        url=url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        text = Text.assemble(
            ("Successful", "bold green"),
            " edit the SLA class")
        console = Console()
        console.print(text)
    else:
        print(str(response.text))
        exit()
