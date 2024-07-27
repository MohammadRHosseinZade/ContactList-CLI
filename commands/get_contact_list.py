import click
import pandas as pd
from utils.utils_pandas.contact import get_all_contact_based_on_user
from utils.utils_pandas.user import check_token_expiration



@click.command()
@click.option('--token')
def retrieve_contact_list(token):
    df = pd.read_csv('./data/user.csv')
    if token:
        entry_exists = df[df['token'] == token]
        if not entry_exists.empty:
            validated = check_token_expiration(user= entry_exists,input_token=token, expire_minutes=3)
            if validated == False:
               print('Your token is expired')
            else:
                result = get_all_contact_based_on_user(user_id=entry_exists['id'].values[0])
                print(result)
    else:
        print(f'Token is required required')