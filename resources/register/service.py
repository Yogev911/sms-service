import json
from dal_sql import SQL
import traceback
import conf
from utils import generate_pin_code
from resources.sender import nexmo_adapter

db = SQL()


def register(request):
    try:
        data = json.loads(request.data)
        user = data.get('user', None)
        password = data.get('password', None)
        phone = data.get('phone', None)
        if not (user and password and phone):
            return "missing parameters", 401

        user_data = db.get_user_by_params(user)
        if user_data:
            return 'User is already registered, please log in to get your token', 401
        pin = generate_pin_code()
        nexmo_adapter.send(src='Nexmo', dest=phone, msg=conf.SEND_PIN_MESSAGE.format(pin))
        user_id = db.add_user(user, password, phone, pin)

        return conf.REGISTER_MESSAGE.format(user), 201

    except:
        return f'Failed register {traceback.format_exc()}', 401
