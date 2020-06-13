# import pytest

from click.testing import CliRunner
from {{ cookiecutter.package_name }}.console.application import main


def test_example():
    command = ["example"]

    runner = CliRunner()
    result = runner.invoke(main, command)

    assert "{{ cookiecutter.package_name }} example" in result.output
    assert result.exit_code == 0
