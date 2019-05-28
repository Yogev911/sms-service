import json

import jwt

from resources.login.service import get_data_by_token
from resources.sender import nexmo
import traceback


def send_sms(request):
    try:
        token = request.headers.get('token', None)
        if not token:
            return "missing token", 401
        try:
            user_data = get_data_by_token(token)
        except jwt.ExpiredSignatureError:
            return "Token is not authenticated!, log in again", 401
        data = json.loads(request.data)
        res = nexmo.send(src=user_data['phone'], dest=data['dest'], msg=data['msg'])
        return "sms sent", 201
    except:
        return f'Failed sending message {traceback.format_exc()}', 401
