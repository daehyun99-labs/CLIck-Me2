from click.testing import CliRunner
from devintro.cli import cli
from devintro.profile import load_profile


def test_load_profile_default():
    profile = load_profile()
    assert profile.name == "Jane Developer"
    assert "Python" in profile.skills


def test_cli_info():
    runner = CliRunner()
    result = runner.invoke(cli, ["info"])
    assert result.exit_code == 0
    assert "Jane" in result.output


def test_cli_skills():
    runner = CliRunner()
    result = runner.invoke(cli, ["skills"])
    assert result.exit_code == 0
    assert "Python" in result.output
