from click.testing import CliRunner
from libtest.cli import cli

def test_command1():
    runner = CliRunner()
    result = runner.invoke(cli, ['command1', 'Lucas'])
    assert result.exit_code == 0
    assert "Olá, Lucas!" in result.output
