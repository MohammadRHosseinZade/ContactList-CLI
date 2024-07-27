import click
from commands import(add_contact, get_contact_list, login, sign_up, delete_contact)

@click.group(help="CLI tool to manage full development cycle of projects")
def cli():
    pass

cli.add_command(sign_up.sign_up)
cli.add_command(login.login)
cli.add_command(add_contact.add_contact)
cli.add_command(get_contact_list.retrieve_contact_list)
cli.add_command(delete_contact.delete_contact)


if __name__ == '__main__':
    cli()