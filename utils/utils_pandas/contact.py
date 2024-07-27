import pandas as pd
from pandas import DataFrame



def insert_phone_number(number):
    df = pd.read_csv('./data/contact.csv')
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

def insert_contact_info(full_name: str, phone_id:int, user_id: int, description:str=''):
    df = pd.read_csv('./data/contact.csv')
    df1 = pd.read_csv('./data/usercontact.csv')
    new_entry = {
        'id': df['id'].max() + 1 if not df.empty else 1,
        'full_name': full_name,
        'description': description,
        'phone_id': phone_id,
    }
    new_entry_for_usercontact= {'id': df['id'].max() + 1 if not df.empty else 1,
                                'user_id': user_id,
                                'contact_id': int(new_entry['id'])}
    df = df._append(new_entry, ignore_index=True)
    df.to_csv('./data/contact.csv', index=False)
    df1 = df1._append(new_entry_for_usercontact, ignore_index=True)
    df1.to_csv('./data/usercontact.csv', index=True)

import pandas as pd

def get_all_contact_based_on_user(user_id: int) -> list:
    result = []
    df_usercontact = pd.read_csv('./data/usercontact.csv')
    df_contact = pd.read_csv('./data/contact.csv')
    df_phone = pd.read_csv('./data/phone.csv')
    
    user_contacts = df_usercontact[df_usercontact['user_id'] == user_id]
    
    for _, user_contact in user_contacts.iterrows():
        contact_id = user_contact['contact_id']
        contact_detail = df_contact[df_contact['id'] == contact_id].iloc[0]
        phone_number = df_phone[df_phone['id'] == contact_detail['phone_id']].iloc[0]
        
        result.append((phone_number.to_dict(), contact_detail.to_dict()))
    
    return result


    