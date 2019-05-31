from utilities.dal import DbClient
from utilities.logger import get_logger

db = DbClient()
logger = get_logger(__name__)


def verify(user, pin):
    try:
        logger.info(f'Verify {user} PIN Code')
        user_data = db.get_user_by_username(user)
        if user_data['verify']:
            return 'Account is already activated', 200
        elif pin == user_data['pin']:
            db.verify_user(user_data['id'])
            logger.info(f'User {user} is not activated')
            return 'Account activated successfully', 200
        else:
            logger.info(f'User {user} imported wrong PIN Code')
            return 'PIN code is incorrect, try again', 401
    except Exception as e:
        logger.exception(f'Failed verify account for user {user}, Error {e.__str__()}')
        return f'Failed verify account', 501
