import click
import pandas as pd

@click.command()
@click.option('--token')
def retrieve_contact_list(token):
    if token:
        print(f'Building this repo into a docker image...')
    else:
        print(f'Token is required required')