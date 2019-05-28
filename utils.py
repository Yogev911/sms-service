from datetime import datetime, timedelta
import jwt
import conf


def generate_token(user_id, phone):
    return jwt.encode(
        {'user_id': user_id, 'phone': phone, 'exp': datetime.utcnow() + timedelta(days=1)},
        conf.API_TOKEN_KEY,
        algorithm=conf.ALGO).decode('utf-8')

def get_data_by_token(token):
    return jwt.decode(token, conf.API_TOKEN_KEY,
                      algorithm='HS256')