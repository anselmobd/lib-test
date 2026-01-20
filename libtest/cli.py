# my_cli_project/cli.py
import click
from libtest.commands.command1 import command1
from libtest.commands.command2 import command2

@click.group()
def cli():
    """Comando principal da CLI."""
    pass

cli.add_command(command1)
cli.add_command(command2)

if __name__ == '__main__':
    cli()
