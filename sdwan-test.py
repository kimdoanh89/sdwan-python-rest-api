import urllib3
import click
from vmanage.constants import vmanage
from vmanage.utils import device_list, template_list
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group()
def cli():
    """Command line tool for deploying templates to CISCO SDWAN.
    """
    pass


@click.command()
def sdwan_device_list():
    device_list(vmanage)


@click.command()
def sdwan_template_list():
    template_list(vmanage)


cli.add_command(sdwan_device_list)
cli.add_command(sdwan_template_list)

if __name__ == "__main__":
    cli()
