#parsers to use in resources

from flask_restplus import reqparse

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', help='username not given', required=True)
login_parser.add_argument('password', help='password not given', required=True)
login_parser.add_argument('unique_id', help='unique_id not given', required=True)

register_parser = reqparse.RequestParser()
register_parser.add_argument('username', help='username must be given', required=True)
register_parser.add_argument('first_name', help='first_name must be given', required=True)
register_parser.add_argument('last_name', help='last_name must be given', required=True)
register_parser.add_argument('phone_number', help='phone_number must be given', required=True)
register_parser.add_argument('email', help='email must be given', required=True)
register_parser.add_argument('unique_id', help='unique_id must be given', required=True)
register_parser.add_argument('password', help='password must be given', required=True)
