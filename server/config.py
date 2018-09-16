import os

#base directory where file is located
basedir = os.path.abspath(os.path.dirname(__file__))

#configuration class to configurate app
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'sodilhi021inunrdks9d0spkcl__'
	MONGO_URI = os.environ.get('DB')
	JWT_SECRET_KEY = 'seila'
	JWT_BLACKLIST_ENABLED = True
	JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
