# my_cli_project/cli.py
import click
from .commands.greetings import ola
from .commands.strings import timeid

@click.group()
def cli():
    """Comando principal da CLI."""
    pass

cli.add_command(ola)
cli.add_command(timeid)

def main():
    cli()

if __name__ == "__main__":
    main()
