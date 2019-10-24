from flask import  Flask
from flask_restful import Resource, reqparse
from flask_jwt_extended import JWTManager

parser = reqparse.RequestParser()
parser.add_argument('username', required = False)
parser.add_argument('password', required = False) 


users1 = {"tadeos": "pass", "tadeos1": "pass"}

def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY']= 'thisisthekey'
    
    jwt = JWTManager(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    

    from .module import module as module_blueprint
    app.register_blueprint(module_blueprint)

    return app