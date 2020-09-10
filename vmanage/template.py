import requests
import urllib3
import click
import json
from rich.console import Console
from rich.table import Table
# from rich.text import Text
from vmanage.authenticate import authentication
from vmanage.constants import vmanage
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group(name="template")
def cli_template():
    """Commands to manage template: create, delete, list, show
    """
    pass


@cli_template.command(name="list", help="Get template list")
def template_list():
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
        table.add_row(
            f'[green]{item["templateName"]}[/green]',
            f'[blue]{item["deviceType"]}[/blue]',
            f'[magenta]{item["templateId"]}[/magenta]',
            f'[orange1]{item["devicesAttached"]}[/orange1]',
            f'[bright_yellow]{item["templateAttached"]}[/bright_yellow]')
    console.print(table)


# @cli_template.command(name="create", help="Create a feature template")
# @click.option("--name", help="ID of the template you wish to delete")
# @click.option("--description", help="ID of the template you wish to delete")
# @click.option("--device_type", help="ID of the template you wish to delete")
# def create_template(name, description, device_type):
#     headers = authentication(vmanage)
#     base_url = "https://"+f'{vmanage["host"]}:{vmanage["port"]}/dataservice'
#     api = "/template/device/feature?api_key=/template/device"
#     url = base_url + api
#     payload = {
#         "templateName": name,
#         "templateDescription": description,
#         "deviceType": device_type,
#         "configType": "template",
#         "factoryDefault": "true",
#         "policyId": "",
#         "featureTemplateUidRange": [],
#         "generalTemplates": [
#             {
#                 "templateId": "70fd00fe-cc5e-4e19-a730-538a77e758d5",
#                 "templateType": "aaa"
#             },
#             {
#                 "templateId": "99f10289-4795-4512-8955-007902bea884",
#                 "templateType": "bfd-vedge"
#             },
#             {
#                 "templateId": "1327de66-2eff-4e83-8787-0060675dc498",
#                 "templateType": "omp-vedge"
#             },
#             {
#                 "templateId": "24fb3c60-f4a5-4daf-9910-be477a046b9e",
#                 "templateType": "security-vedge"
#             },
#             {
#                 "templateId": "5fb744ed-3bbd-47d8-bec2-19b46c158fb5",
#                 "templateType": "system-vedge",
#                 "subTemplates": [
#                     {
#                         "templateId": "7eb31a03-0ad1-4bac-b89c-5b3012b6d09d",
#                         "templateType": "logging"
#                     }
#                 ]
#             },
#             {
#                 "templateId": "71294ac3-0aaa-4115-8995-476a91eac976",
#                 "templateType": "vpn-vedge"
#             },
#             {
#                 "templateId": "bbc09a4e-c91f-4dcf-a3ca-654a2f3bd135",
#                 "templateType": "vpn-vedge"
#             }
#         ],
#         "templateClass": "vedge"
#     }
#     response = requests.post(
#         url=url, data=json.dumps(payload), headers=headers, verify=False)
#     if response.status_code == 200:
#         items = response.json()
#         text = Text.assemble(
#             ("Successful", "bold green"),
#             " create template with templateID = ",
#             (items["templateId"], "magenta"))
#         console = Console()
#         console.print(text)
#     else:
#         print(str(response.text))
#         exit()


@cli_template.command(name="delete", help="Delete a feature template")
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


@cli_template.command(name="show", help="Show details of a feature template")
@click.option("--template_id", help="ID of the template to show details")
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
