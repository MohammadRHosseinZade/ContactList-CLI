import click
import pandas as pd

@click.command()
@click.option('--email')
@click.option('--password')
def login(email, password):
    if email and password:
        print(f'Building this repo into a docker image...')
    else:
        print(f'Email and password are required')
