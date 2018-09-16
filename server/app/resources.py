from flask_restplus import Resource, reqparse
from app.models import User, RevokedToken, InUseToken
from app.parsers import login_parser, register_parser
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt, decode_token
from flask_login import current_user, login_user, logout_user, login_required
from jwt.exceptions import ExpiredSignatureError

class UserLogin(Resource):
    def post(self):
            data = login_parser.parse_args()
            user = User.objects(username=data['username']).first()
            if user is None or not user.check_password(data['password']):
                return {'message': 'Username or password are incorrect'}
            elif not user.check_unique_id(data['unique_id']):
                #phone who is sending request is not registered
                return {'message': 'This telephone is not registered'}
            try:
                login_user(user)
                in_use = InUseToken.objects(user=user).first()
                if in_use is not None:
                    print('in_use')
                    access_token = in_use.jwt_access
                    print('get access')
                    try:
                        revoked_token = RevokedToken(jti=decode_token(access_token)['jti'])
                        revoked_token.save()
                        print('revoked')
                    except ExpiredSignatureError:
                        print('already been revoked')
                    access_token = create_access_token(identity=data['username'])
                    in_use.jwt_access = access_token
                    in_use.save()
                    refresh_token = in_use.jwt_refresh
                else:
                    access_token = create_access_token(identity=data['username'])
                    refresh_token = create_refresh_token(identity=data['username'])
                    new_in_use = InUseToken(jwt_access=access_token, jwt_refresh=refresh_token, user=user)
                    new_in_use.hash_unique_id(data['unique_id'])
                    new_in_use.save()
                return {
                    'message': 'Login was succesful',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            except:
                print(sys.exc_info())
                return {'message': 'Unknown error'}

class UserRegister(Resource):
    def post(self):
        errors = 0
        data = register_parser.parse_args()

        #This is the worst idea to deal with already in use data
        if User.objects(username=data['username']):
            errors += 1
        if User.objects(email=data['email']):
            errors += 2
        if User.objects(phone_number=data['phone_number']):
            errors += 4

        if(errors == 0):
            new_user = User(username=data['username'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'], phone_number=data['phone_number'])
            new_user.hash_password(data['password'])
            new_user.hash_unique_id(data['unique_id'])
            try:
                new_user.save()
                login_user(new_user)
                in_use = InUseToken.objects(user=new_user).first()
                if in_use is None:
                    access_token = in_use.jwt_access
                    try:
                        revoked_token = RevokedToken(jti=decode_token(access_token)['jti'])
                        revoked_token.save()
                    except ExpiredSignatureError:
                        print('already been revoked')
                    access_token = create_access_token(identity=data['username'])
                    in_use.jwt_access = access_token
                    in_use.save()
                    refresh_token = in_use.jwt_refresh
                else:
                    access_token = create_access_token(identity=data['username'])
                    refresh_token = create_refresh_token(identity=data['username'])
                    in_use = InUseToken(jti_access=access_token, jti_refresh=refresh_token, user=new_user)
                    in_use.hash_unique_id(data['unique_id'])
                    in_use.save()
                return {
                    'message': 'User registered',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            except:
                return {'message': 'Unknown error'}
        elif(errors == 1):
            return {'message': 'Username is already in use'}
        elif(errors == 2):
            return {'message': 'Email is already in use'}
        elif(errors == 3):
            return {'message': 'Username and email are already in use'}
        elif(errors == 4):
            return {'message': 'Phone number is already in use'}
        elif(errors == 5):
            return {'message': 'Phone number and username are already in use'}
        elif(errors == 6):
            return {'message': 'Phone number and email are already in use'}
        elif(errors == 7):
            return {'message': 'Phone number, email and username are already in use'}

#refresh the access token providing refresh token
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        #create new access token for user
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        user = User.objects(username=current_user).first()
        in_use = InUseToken.objects(user=user).first()
        #revoke last access token
        revoked_token = RevokedToken(jti=decode_token(in_use.jwt_access)['jti'])
        revoked_token.save()
        #reload access token in in use tokens
        in_use.jwt_access = access_token
        in_use.save()
        return {
            'access_token': access_token
        }

#revoke user access token, loggout partially
class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.save()
            return{'message': 'Revoked access token'}
        except:
            return{'message': 'Error in revoking access token'}

#revoke user refresh token, loggout permanent
class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.save()
            return{'message': 'Revoked refresh token'}
        except:
            return{'message': 'Error in revoking refresh token'}

#loggout a user by session and token
class UserLogout(Resource):
    @login_required
    def post(self):
        try:
            user = User.objects(username=current_user.username).first()
            in_use = InUseToken.objects(user=user).first()
            jti_access = decode_token(in_use.jwt_access)['jti']
            jti_refresh = decode_token(in_use.jwt_refresh)['jti']
            revoked_access_token = RevokedToken(jti=jti_access)
            revoked_access_token.save()
            revoked_refresh_token = RevokedToken(jti=jti_refresh)
            revoked_refresh_token.save()
            in_use.delete()
            logout_user()
            return{'message': 'User was log out its tokens revoked'}
        except:
            try:
                logout_user()
                return{'message': 'User was log out'}
            except:
                return{'message': 'Error when logging out user'}
