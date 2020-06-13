import click


@click.group()
def main():
    """{{ cookiecutter.package_name }} console"""


@main.command()
def example():
    """{{ cookiecutter.package_name }} example"""
    print("{{ cookiecutter.package_name }} example")
