import json

import conf
from utilities.dal import DbClient
from utilities.logger import get_logger
from utilities.utils import generate_pin_code
from resources.sender import nexmo_adapter

db = DbClient()
logger = get_logger(__name__)


def register(request):
    try:
        data = json.loads(request.data)
        user = data.get('user', None)
        password = data.get('password', None)
        phone = data.get('phone', None)
        if not (user and password and phone):
            return "missing parameters", 406
        user_data = db.get_user_by_username(user)
        if user_data:
            return 'User is already registered, please log in to get your token', 401
        elif not is_phone_valid(phone):
            logger.info(f'Phone number {phone} is not valid')
            return 'Phone number is not valid', 406
        else:
            register_new_user(password, phone, user)
            return conf.REGISTER_MESSAGE.format(user), 201
    except Exception as e:
        logger.exception(f'Failed register {e.__str__()}')
        return f'Failed register {e.__str__()}', 501


def is_phone_valid(phone_number):
    return not(len(str(phone_number)) != conf.PHONE_NUMBER_LENGHT or not str(phone_number).startswith(
        conf.PHONE_NUMBER_PREFIX))


def register_new_user(password, phone, user):
    logger.info(f'Adding new user {user}')
    pin = generate_pin_code()
    nexmo_adapter.send(src='Nexmo', dest=phone, msg=conf.SEND_PIN_MESSAGE.format(user, pin))
    db.add_user(user, password, phone, pin)
    logger.info(f'Uuser {user} added successfully')
