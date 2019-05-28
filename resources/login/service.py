import json
from dal_sql import SQL
import jwt
import conf
import traceback
from utils import generate_token, get_data_by_token

db = SQL()


def login(request):
    try:
        token = request.headers.get('token', None)
        if token:
            try:
                get_data_by_token(token)
            except jwt.ExpiredSignatureError:
                return "Token is expired!, insert credentials again and dismiss the old token", 401
        data = json.loads(request.data)
        user = data.get('user', None)
        password = data.get('password', None)
        phone = data.get('phone', None)
        if not user and password and phone:
            return "missing parameters", 401

        user_data = db.get_user_by_params(user)
        if not user_data:
            return 'User not exists', 404
        if not (user_data['user'] == user and user_data['password'] == password):
            return 'Invalid credentials', 401
        if not db.is_user_verified(user_data['id']):
            return 'Account is not verified, please verify your account to start messaging via http://localhost:8080/verify/<user_id>/<pin_code>', 401
        token = generate_token(user_data['id'], phone)
        return token, 201

    except:
        return f'Failed log in {traceback.format_exc()}', 401
