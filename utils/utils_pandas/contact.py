import pandas as pd
from pandas import DataFrame

df = pd.read_csv('./data/contact.csv')

def insert_phone_number(number):
    df3 = pd.read_csv('./data/phone.csv')
    entry_exists = df3[df3['number'] == number]
    if not entry_exists.empty:
        return entry_exists
    else:
        new_entry = {
        'id': df['id'].max() + 1 if not df.empty else 1,
        'number': number
        }
        df3 = df3._append(new_entry, ignore_index=True)
        df3.to_csv('./data/phone.csv', index=False)
        return new_entry

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

def get_all_contact_based_on_user(user_id: int)-> list:
    result = []
    df1 = pd.read_csv('./data/usercontact.csv')
    contacts = df1[df1['user_id']] == user_id
    for contact in contacts:
        df2 = pd.read_csv('./data/contact.csv')
        contact_detail = df2[df2['id']] == contact['id']
        df3 = pd.read_csv('./data/phone.csv')
        phone_number = df3[df3['id']]== contact_detail['phone_id'].values[0]
        result.append((phone_number.to_dict(), contact_detail.to_dict()))
    return result

    