import conf
import json

from utilities.dal import DbClient
from utilities.logger import get_logger
from utilities.utils import generate_token

db = DbClient()
logger = get_logger(__name__)


def login(request):
    try:
        data = json.loads(request.data)
        user = data.get('user', None)
        password = data.get('password', None)
        if not (user and password):
            logger.info(f'Login failed on {request.remote_addr}, missing credentials')
            return "missing credentials", 401

        user_data = db.get_user_by_username(user)
        if not user_data:
            logger.info(f'User {user} not exists')
            return 'User not exists', 404
        elif not (user_data['user'] == user and user_data['password'] == password):
            logger.info(f'Invalid credentials for user {user}')
            return 'Invalid credentials', 401
        elif not user_data['verify']:
            logger.info(f'Account for user {user} is not verified')
            return conf.ACCOUNT_NOT_VERIFIED, 401
        else:
            token = generate_token(user_data['id'], user_data['phone'])
            logger.info(f'Token for user {user} created. token: {token}')
            return token, 201
    except Exception as e:
        logger.exception(f'Failed login from {request.remote_addr}, Error: {e.__str__()} ')
        return f'Failed login {e.__str__()}', 501
