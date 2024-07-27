import click
from utils.utils_pandas.user import search_user, check_password, change_token


@click.command()
@click.option('--email')
@click.option('--password')
def login(email, password):
    if email and password:
        user = search_user(email=email)
        if user.empty:
            print('Account does not exist or password is incorrectt')
        else:
            is_password_correct=check_password(user = user, password = password)
            if is_password_correct:
                token = change_token(user=user)
                print(f"Token = {token}")
            else :
                print('Account does not exist or password is incorrect')         
    else:
        print(f'Email and password are required')
