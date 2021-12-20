import hashlib
import re
from functools import wraps

import jwt
from flask import request

from src.api.app import app
from src.api.models import User


def convert_list(list):
    json_list = []
    for el in list:
        json_list.append(el.serialize)
    return json_list

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def check_password(database_password, input_password):
    if database_password == input_password:
        return True
    return False


def checking_password(password):
    if len(password) >= 6 and len(password) <= 20 and any(char.isdigit() for char in password) \
            and any(char.isupper() for char in password) and any(char.islower() for char in password):
        return True
    else:
        return False


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check_email(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x_access_token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return 'Unauthorized Access!', 401

        try:

            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(id= data['id']).first()
            if not current_user:
                return 'Unauthorized Access!', 401
        except:
            return 'Unauthorized Access!', 401
        return f(*args, **kwargs)

    return decorated