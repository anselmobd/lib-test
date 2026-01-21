import click

from oxigenpy.strings import now_pid_tid_str


@click.command()
def timeid():
    click.echo(now_pid_tid_str())
