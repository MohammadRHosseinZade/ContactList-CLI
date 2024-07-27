import pandas as pd
from pandas import DataFrame

df = pd.read_csv('./data/contact.csv')


def insert_contact_info(full_name: str,description:str, phone_id:int):
    new_entry = {
        'id': df['id'].max() + 1 if not df.empty else 1,
        'full_name': full_name,
        'description': description,
        'phone_id': phone_id,
    }
    global df
    df = df.append(new_entry, ignore_index=True)
    df.to_csv('./data/contact.csv', index=False)

def get_all_contact_based_on_user()