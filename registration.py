from re import fullmatch


RE_LOGIN = '[a-zA-Z0-9._]{3,10}'
RE_PWD = '[a-zA-Z0-9._!&#]{8,15}'


users_db = {}


def check_input(reg_exp, user_input):
    
    if not fullmatch(reg_exp, user_input):
        raise ValueError(f'Input should be {reg_exp}')
    
    return True


login_check_result = False  
pwd_check_result = False

while True:
    
    if not login_check_result:
        user_login = input('New login: ')
    if not pwd_check_result:
        user_pwd = input('New password: ')
        
    try:
        login_check_result = check_input(RE_LOGIN, user_login)
        pwd_check_result = check_input(RE_PWD, user_pwd)
    except ValueError as error:
        print(error)
    else:
        if user_login in users_db:
            login_check_result = False
            print('Login has been already taken')
            continue
        break
    
users_db[user_login] = {'pwd': user_pwd}

