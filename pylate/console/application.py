import click


@click.group()
def main():
    """pylate console"""


@main.command()
def example():
    """pylate example"""
    print("pylate example")
