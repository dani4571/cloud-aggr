from globals import *
from bottle import request, route, view, get, post
from services import test_service


@route('/')
@view('test/login')
def test():
    return {}


@post('/test')
@view('test/user_profile')
def test():
    tenant = request.forms.get('tenant')
    username = request.forms.get('username')
    password = request.forms.get('password')    
    test_service.create_trust(username, password, tenant, config['keystone'])
    return {"name": "John"}


@get('/auth')
def authget(db):
    return "Any non blank api key will work."


@post('/auth')
def auth(db):
    key = request.forms.get('api_key')
    if(key != ""):
        users = db.query(User)
        if (user == null):
            print "No user"
        else:
            return "Key accepted"
    else:
        return "Key denied"
