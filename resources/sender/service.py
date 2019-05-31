import jwt
import json

import conf
from utilities.dal import DbClient
from resources.sender import nexmo_adapter
from utilities.logger import get_logger
from utilities.utils import get_data_by_token

db = DbClient()
logger = get_logger(__name__)


def send_sms(request):
    try:
        logger.info(f'Sending sms')
        token = request.headers.get('token', None)
        if not token:
            logger.info(f'Missing token on {request.remote_addr}')
            return "Missing token", 401
        user_data = get_data_by_token(token)
        current_balance = db.get_user_balance(user_id=user_data['user_id'])
        if current_balance - conf.SMS_COST <= 0:
            logger.info(f'User {user_data["user_id"]} balance is below of {conf.SMS_COST}')
            return 'Balance is empty.. load up with some kins to keep running', 402
        else:
            data = json.loads(request.data)
            if not data or not ('msg' in data and 'dest' in data):
                raise ValueError('Empty data')
            _send_sms(current_balance, data['msg'], data['dest'], user_data['phone'], user_data['user_id'])
        return "sms sent", 201
    except jwt.ExpiredSignatureError:
        logger.exception(f'Token is not authenticated! on request {request.remote_addr}')
        return "Token is not authenticated!, log in again", 401
    except Exception as e:
        logger.exception(f'Failed sending message {e.__str__()}')
        return f'Failed sending message {e.__str__()}', 501


def _send_sms(current_balance, message, dest_number, src_number, user_id):
    nexmo_adapter.send(src=src_number, dest=dest_number, msg=message)
    db.log_message(user_id=user_id, dest_number=dest_number, message=message)
    db.update_balance(user_id=user_id, new_balance=current_balance - conf.SMS_COST)
    logger.info(f'SMS sent from {src_number} to {dest_number}, message {message}')
