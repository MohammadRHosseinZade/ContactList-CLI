import click
import pandas as pd

df = pd.read_csv('./data/user.csv')

@click.command()
@click.option('--token')
@click.option('--full_name')
@click.option('--phone_number')
def add_contact(token, full_name,phone_number):
    if token and full_name and phone_number:
        entry_exists = df[df['token'] == token]
        if not entry_exists.empty:
            return entry_exists
        return None
    else:
        print(f'Token and full_name and phone_number are required')
