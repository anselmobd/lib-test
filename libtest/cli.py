# my_cli_project/cli.py
import click
from commands.greetings import ola
from commands.command2 import command2

@click.group()
def cli():
    """Comando principal da CLI."""
    pass

cli.add_command(ola)
cli.add_command(command2)

if __name__ == '__main__':
    cli()
