import click
import pandas as pd
from utils.utils_pandas.user import check_token_expiration



@click.command()
@click.option('--token')
@click.option('--contact_id')
def delete_contact(token: str, contact_id: int):
    df_user = pd.read_csv('./data/user.csv')
    if token:
        entry_exists = df_user[df_user['token'] == token]
        if not entry_exists.empty:
            validated = check_token_expiration(user=entry_exists, input_token=token, expire_minutes=3)
            if not validated:
                print('Your token is expired')
            else:
                df_contact = pd.read_csv('./data/contact.csv')
                
                if contact_id in df_contact['id'].values:
                    df_contact = df_contact[df_contact['id'] != contact_id]
                    df_contact.to_csv('./data/contact.csv', index=False)
                    print(f'Contact with id {contact_id} deleted successfully.')
                else:
                    print(f'Contact with id {contact_id} does not exist.')
        else:
            print('Invalid token.')
    else:
        print('Token is required.')