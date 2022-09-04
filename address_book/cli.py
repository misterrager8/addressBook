import click

from address_book import config, create_app


@click.group()
def cli():
    """Address Book"""
    pass


@cli.command()
def web():
    """Address Book"""
    app = create_app(config)
    app.run()
