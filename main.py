import click

@click.group(help="CLI tool to manage full development cycle of projects")
def cli():
    pass

if __name__ == '__main__':
    cli()