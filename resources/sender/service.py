import json

import jwt

from dal_sql import SQL
from resources.login.service import get_data_by_token
from resources.sender import nexmo_adapter
import traceback
import conf

db = SQL()


def send_sms(request):
    try:
        token = request.headers.get('token', None)
        if not token:
            return "missing token", 401
        try:
            user_data = get_data_by_token(token)
        except jwt.ExpiredSignatureError:
            return "Token is not authenticated!, log in again", 401
        current_balance = db.get_user_balance(user_id=user_data['user_id'])
        if current_balance - conf.SMS_COST < 0:
            return 'Balance is empty.. load up with some kins to keep running', 402
        data = json.loads(request.data)
        res = nexmo_adapter.send(src=user_data['phone'], dest=data['dest'], msg=data['msg'])
        db.log_message(user_id=user_data['user_id'], dest_number=data['dest'], message=data['msg'])
        db.update_balance(user_id=user_data['user_id'], new_balance=current_balance - conf.SMS_COST)

        return "sms sent", 201
    except:
        return f'Failed sending message {traceback.format_exc()}', 401
