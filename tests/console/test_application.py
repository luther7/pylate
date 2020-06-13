# import pytest

from click.testing import CliRunner
from pylate.console.application import main


def test_example():
    command = ["example"]

    runner = CliRunner()
    result = runner.invoke(main, command)

    assert "pylate example" in result.output
    assert result.exit_code == 0
