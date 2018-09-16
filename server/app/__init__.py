from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
from flask_restplus import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__) #create flask app
app.config.from_object(Config) #load app configuration from Config object
api = Api(app) #api for resources in app
db = MongoEngine(app) #db management
login = LoginManager(app)
app.session_interface = MongoEngineSessionInterface(db) #database login session
jwt = JWTManager(app)

from app import models, resources
from app.resources import UserLogin, UserRegister, TokenRefresh, UserLogoutAccess, UserLogoutRefresh, UserLogout

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedToken.is_jti_blacklisted(jti)

#adding resources list into the app api, with its route and class
api.add_resource(UserLogin, '/app/login')
api.add_resource(UserRegister, '/app/register')
api.add_resource(TokenRefresh, '/app/refresh')
api.add_resource(UserLogoutAccess, '/app/logout/access')
api.add_resource(UserLogoutRefresh, '/app/logout/refresh')
api.add_resource(UserLogout, '/app/loggout')
