import traceback

from dal_sql import SQL

db = SQL()


def verify(user, pin):
    try:
        user_data = db.get_user_by_params(user)

        if db.is_user_verified(user_data['id']):
            return 'Account is already activated', 200
        if pin == user_data['pin']:
            db.verify_user(user_data['id'])
            return 'Account activated successfully', 200
        return 'PIN code is incorrect, try again', 401
    except:
        return f'Failed verify account {traceback.format_exc()}', 501
