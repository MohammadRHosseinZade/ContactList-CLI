import click
import pandas as pd
from datetime import datetime
from utils.utils_pandas.user import insert_user, search_user
from utils.random_token import random_token_generator

@click.command()
@click.option('--email')
@click.option('--password')
def sign_up(email, password):
    if email and password:
        if search_user(email=email) == None:
            insert_user(
                email=email,
                password=password,
                token=random_token_generator(),
                token_time= datetime.now()
            )
            print('Your account was registered')
        else:
            print("Account already exists")    
    else:
        print(f'Email and password are required')


def check_existance(email):
    csv_file_path = "./data/user.csv"
    df = pd.read_csv(csv_file_path)
    pass
