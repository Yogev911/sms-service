import json
import traceback

import conf
from dal_sql import SQL
from utils import generate_pin_code
from resources.sender import nexmo_adapter


def register(request):
    try:
        db = SQL()
        data = json.loads(request.data)
        user = data.get('user', None)
        password = data.get('password', None)
        phone = data.get('phone', None)
        if not (user and password and phone):
            print(user,password,phone)
            return "missing parameters", 406
        user_data = db.get_user_by_params(user)
        if user_data:
            return 'User is already registered, please log in to get your token', 401
        if len(str(phone)) != 12 or not str(phone).startswith('9725'):
            return 'Phone number is not valid', 406
        pin = generate_pin_code()
        res = nexmo_adapter.send(src='Nexmo', dest=phone, msg=conf.SEND_PIN_MESSAGE.format(user, pin))
        print(res)
        db.add_user(user, password, phone, pin)

        return conf.REGISTER_MESSAGE.format(user), 201

    except:
        return f'Failed register {traceback.format_exc()}', 501
