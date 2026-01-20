import click

@click.command()
@click.argument('name')
def ola(name):
    click.echo(f"Olá, {name}!")
