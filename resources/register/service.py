import json

import conf
from utilities.dal import DbClient
from utilities.logger import Logger
from utilities.utils import generate_pin_code
from resources.sender import nexmo_adapter
from utilities.exceptions import *

db = DbClient()
logger = Logger(__name__)


def register(request):
    try:
        data = json.loads(request.data)
        user = data.get('user')
        password = data.get('password')
        phone = data.get('phone')
        if not (user and password and phone):
            raise EmptyForm()

        user_data = db.get_user_by_username(user)
        if user_data:
            raise UserAlreadyExists(user)
        elif not is_phone_valid(phone):
            raise ValueError('Phone number is not valid')
        else:
            register_new_user(password, phone, user)
            return conf.REGISTER_MESSAGE.format(user), 201

    except UserAlreadyExists as e:
        logger.warning(e.__str__())
        return e.__str__(), 401
    except (EmptyForm, ValueError) as e:
        logger.warning(e.__str__())
        return e.__str__(), 406
    except Exception as e:
        logger.exception(f'Failed register')
        return f'Failed register {e.__str__()}', 501


def is_phone_valid(phone_number):
    return not (len(str(phone_number)) != conf.PHONE_NUMBER_LENGHT or not str(phone_number).startswith(
        conf.PHONE_NUMBER_PREFIX))


def register_new_user(password, phone, user):
    '''
    register new user in db and send the verification message
    :param password: str
    :param phone: str
    :param user: str
    :return: None
    '''
    logger.info(f'Adding new user {user}')
    pin = generate_pin_code()
    nexmo_adapter.send(src='Nexmo', dest=phone, msg=conf.SEND_PIN_MESSAGE.format(user, pin))
    db.add_user(user, password, phone, pin)
    logger.info(f'Uuser {user} added successfully')
