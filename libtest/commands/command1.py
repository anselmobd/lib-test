# my_cli_project/commands/command1.py
import click

@click.command()
@click.argument('name')
def command1(name):
    click.echo(f"Olá, {name}!")
