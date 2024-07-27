import pandas as pd
from pandas import DataFrame
from ..random_token import random_token_generator
from datetime import datetime, timedelta

df = pd.read_csv('./data/user.csv')

def search_user(email: str) -> DataFrame:
    entry_exists = df[df['email'] == email]
    if not entry_exists.empty:
        return entry_exists
    return None

def check_password(user: DataFrame, password: str) -> bool:
    
    return str(user['password'].values[0]) == password

def change_token(user: DataFrame):
    user_index = df[df['email'] == user['email'].values[0]].index[0]
    token = random_token_generator()
    df.at[user_index, "token"] = token
    df.at[user_index, "token_creation_time"] = datetime.now()
    df.to_csv('./data/user.csv', index=False)
    return token

def insert_user(email: str, password: str, token: str, token_time: datetime):
    df = pd.read_csv('./data/user.csv')
    new_entry = {
        'id': df['id'].max() + 1 if not df.empty else 1,
        'email': email,
        'password': password,
        'token': token,
        'token_creation_time': token_time
    }
    
    df = df._append(new_entry, ignore_index=True)
    df.to_csv('./data/user.csv', index=False)

def check_token_expiration(user: DataFrame, input_token: str, expire_minutes: int):
    if input_token == user['token'].values[0]:
        token_creation_time = pd.to_datetime(user['token_creation_time'].values[0])
        expiration_time = token_creation_time + timedelta(minutes=expire_minutes)
        if not datetime.now() > expiration_time:
            return int(user['id'].values[0])
    return False
