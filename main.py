from fastapi import FastAPI, Depends, HTTPException
from auth import AuthenticationHandler
from schemas import AuthDetails


app = FastAPI()

authentication_handler = AuthenticationHandler()
users = []


@app.get('/')
def landing_page():
    return {'hello': 'world'}


@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(user['username'] == auth_details.username for user in users):
        raise HTTPException(status_code=400, detail='This username has already been taken. Please choose another one.')
    hashed_password = authentication_handler.get_hashed_password(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password
    })
    return f'User {auth_details.username} has been successfully created.'


@app.post('/login')
def login(auth_details: AuthDetails):
    user_details = None
    for detail in users:
        if detail['username'] == auth_details.username:
            user_details = detail
            break
    if (user_details is None) or (not authentication_handler.verify_password(auth_details.password, user_details['password'])):
        raise HTTPException(status_code=401, detail='Invalid username or password.')
    token = authentication_handler.create_token(user_details['username'])
    return {'token': token}


@app.get('/protected')
def protected(username=Depends(authentication_handler.auth_wrapper)):
    return {'username': username}


@app.get('/evaluate')
def evaluate(result=Depends(authentication_handler.auth_wrapper)):
    result
    return f'The result is: {result}'
