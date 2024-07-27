import click

@click.command()
@click.option('--email')
@click.option('--password')
def sign_up(email, password):
    if docker:
        print(f'Building this repo into a docker image...')
    else:
        print(f'Building this repo using default method...')


def check_existance(email):
    pass
