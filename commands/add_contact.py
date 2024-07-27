import click
import pandas as pd

@click.command()
@click.option('--token')
@click.option('--full_name')
@click.option('--phone_number')
def add_contact(token, full_name,phone_number):
    if token and full_name and phone_number:
        print(f'Building this repo into a docker image...')
    else:
        print(f'Token and full_name and phone_number are required')
