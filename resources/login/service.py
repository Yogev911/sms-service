import json

from utilities.dal import DbClient
from utilities.logger import get_logger
from utilities.utils import generate_token
from utilities.exceptions import *

db = DbClient()
logger = get_logger(__name__)


def login(request):
    try:
        form = request.form
        user = form.get('user', None)
        password = form.get('password', None)
        if not (user and password):
            logger.info(f'Login failed on {request.remote_addr}, missing credentials')
            raise InvalidCredentials(user, password)

        user_data = db.get_user_by_username(user)
        if not user_data:
            raise UserNotExists(user)

        elif not (user_data['user'] == user and user_data['password'] == password):
            raise InvalidCredentials(user)

        elif not user_data['verify']:
            raise UserNotVerified()

        else:
            token = generate_token(user_data['id'], user_data['phone'])
            logger.info(f'Token for user {user} created. token: {token}')
            return token, 201

    except UserNotVerified as e:
        logger.warning(e.__str__())
        return e.__str__(), 401
    except UserNotExists as e:
        logger.warning(e.__str__())
        return e.__str__(), 404
    except InvalidCredentials as e:
        logger.warning(e.__str__())
        return e.__str__(), 401
    except Exception as e:
        logger.exception(f'Failed login from {request.remote_addr}')
        return f'Failed login {e.__str__()}', 501
