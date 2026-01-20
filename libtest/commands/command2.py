import click

@click.command()
@click.argument('name')
def command2(name):
    click.echo(f"Olá, {name} 2!")
