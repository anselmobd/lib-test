from click.testing import CliRunner
from libtest.cli import cli

def test_greetings():
    runner = CliRunner()
    result = runner.invoke(cli, ['ola', 'Oxigenai'])
    assert result.exit_code == 0
    assert "Olá, Oxigenai!" in result.output
