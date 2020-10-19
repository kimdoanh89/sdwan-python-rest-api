import urllib3
import click
from vmanage.device import cli_device
from vmanage.template import cli_template
from vmanage.bfd import cli_bfd
from vmanage.sla import cli_sla
from vmanage.omp import cli_omp
from vmanage.ipsec import cli_ipsec
from vmanage.control import cli_control
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group()
def cli():
    """Command line tool to interact with CISCO SDWAN vManage.
    """
    pass


cli.add_command(cli_device)
cli.add_command(cli_template)
cli.add_command(cli_bfd)
cli.add_command(cli_sla)
cli.add_command(cli_omp)
cli.add_command(cli_ipsec)
cli.add_command(cli_control)


if __name__ == "__main__":
    cli()
