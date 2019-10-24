from . import parser, users1
from flask import Blueprint
import json, dpath.util
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt, JWTManager)



module = Blueprint("module", __name__)

@module.route('/test')
def test():
    data = parser.parse_args()
    username = data['username']
    password = data['password']
    if  password == dpath.util.get(users1, username): 
        return 'Sucess'

    return json.dumps(data)

@module.route('/userRegistration')
def userRegistration():
    return 'Registered'

@module.route('/userLogin')
def userLogin():
    data = parser.parse_args()
    username = data['username']
    password = data['password']
    try:
        if  password == dpath.util.get(users1, username): 
            access_token = create_access_token(identity = username)
            refresh_token = create_refresh_token(identity = username)
            return json.dumps({'message': 'Logged in as %s' %username, 'access_token': access_token, 'refresh_token': refresh_token})
    except KeyError:
            return 'User doenot exists'

    return 'Wrong username and password!'



@module.route('/protected')
@jwt_required
def protected():
    return json.dumps({'CurrentUser': get_jwt_identity()})