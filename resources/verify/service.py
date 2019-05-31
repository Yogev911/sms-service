from utilities.dal import DbClient
from utilities.logger import get_logger
from utilities.exceptions import *

db = DbClient()
logger = get_logger(__name__)


def verify(user, pin):
    try:
        logger.info(f'Verify {user} PIN Code')
        user_data = db.get_user_by_username(user)
        if not user_data:
            raise UserNotExists()
        if user_data['verify']:
            return 'Account is already activated', 200
        elif pin != user_data['pin']:
            raise ValueError(f"Wrong PIN code for user {user_data['user']}")
        else:
            db.verify_user(user_data['id'])
            logger.info(f'User {user} is not activated')
            return 'Account activated successfully', 200
    except (ValueError, UserNotExists) as e:
        logger.warning(e.__str__())
        return e.__str__(), 401
    except Exception as e:
        logger.exception(f'Failed verify account for user {user}, Error {e.__str__()}')
        return f'Failed verify account', 501
