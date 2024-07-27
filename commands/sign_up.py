import click
import pandas as pd

@click.command()
@click.option('--email')
@click.option('--password')
def sign_up(email, password):
    if email and password:
        print(f'Building this repo into a docker image...')
    else:
        print(f'Email and password are required')


def check_existance(email):
    csv_file_path = "./data/user.csv"
    df = pd.read_csv(csv_file_path)
    pass
