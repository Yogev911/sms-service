import json
from datetime import datetime, timedelta
from dal_sql import SQL
import jwt
import conf
import traceback
db = SQL()


def generate_token(user_id):
    return jwt.encode(
        {'user_id': user_id, 'exp': datetime.utcnow() + timedelta(days=1)},
        conf.API_TOKEN_KEY,
        algorithm=conf.ALGO).decode('utf-8')


def register(request):
    try:

        user = request.form['user']
        password = request.form['password']
        phone = request.form['phone']

        if not user and password and phone:
            return "missing parameters", 401

        user_id = db.add_user(user, password,phone)
        token = generate_token(user_id)

        return token, 200

    except:
        return f"failed to register {traceback.format_exc()}", 501
