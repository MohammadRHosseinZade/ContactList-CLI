import click
import pandas as pd
from utils.utils_pandas.user import check_token_expiration
from utils.utils_pandas.contact import insert_phone_number, insert_contact_info
df = pd.read_csv('./data/user.csv')

@click.command()
@click.option('--token')
@click.option('--full_name')
@click.option('--phone_number')
@click.option('--description')
def add_contact(token, full_name,phone_number, description):
    if token and full_name and phone_number:
        entry_exists = df[df['token'] == token]
        if not entry_exists.empty:
           validated = check_token_expiration(user= entry_exists, input_token=token, expire_minutes=300)
           if validated == False:
               print('Your token is expired')
           else:
               phone = insert_phone_number(number=phone_number)
               print(phone['id'])
               insert_contact_info(full_name=full_name,
                                   user_id= int(entry_exists['id'].values[0]),
                                   description=description,
                                   phone_id=phone['id'])
               print(f"contact info added for user id {int(entry_exists['id'].values[0])}")
    else:
        print(f'Token and full_name and phone_number are required')
