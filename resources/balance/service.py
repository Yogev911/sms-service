import jwt

from utilities.dal import DbClient
from utilities.logger import get_logger
from utilities.exceptions import *
from utilities.utils import get_data_by_token

db = DbClient()
logger = get_logger(__name__)


def balance(request):
    try:
        logger.info(f'Get user current balance')
        token = request.headers.get('token', None)
        if not token:
            raise TokenNotExists()
        user_data = get_data_by_token(token)
        current_balance = db.get_user_balance(user_id=user_data['user_id'])
        return current_balance, 200

    except TokenNotExists as e:
        logger.warning(e.__str__())
        return e.__str__(), 401
    except jwt.ExpiredSignatureError:
        logger.exception(f'Token is not authenticated! on request {request.remote_addr}')
        return "Token is not authenticated!, log in again", 401
    except Exception as e:
        logger.exception(f'Failed sending message {e.__str__()}')
        return f'Failed sending message {e.__str__()}', 501
