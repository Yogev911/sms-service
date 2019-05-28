import datetime
import pymysql.cursors

import conf


# Connect to the database

class SQL(object):
    def __init__(self):
        self.db = pymysql.connect(host=conf.db_hostname,
                                  user=conf.db_user,
                                  password=conf.db_password,
                                  db=conf.db_schema_name,
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

    def add_user(self, user, password, phone):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO users (name, password,phone,balance) VALUES (%s, %s,%s,%s)"
            cursor.execute(sql, (user, password, phone, conf.INIT_BALANCE))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()
        return cursor.lastrowid - 1

    def get_user_by_params(self, user, password, phone):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = "SELECT `id` FROM `users` WHERE `name`=%s"
            cursor.execute(sql, (user,))
            result = cursor.fetchone()
            if not result:
                return self.add_user(user, password, phone)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()
        return result['id']

    def update_balance(self, user_id, new_balance):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE users SET `balance` = {new_balance} WHERE `id` = {user_id}"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()

    def get_user_balance(self, user_id):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"SELECT `balance`FROM users WHERE `id`={user_id}"
            cursor.execute(sql)
            return cursor.fetchone()['balance']

    def log_message(self, user_id, dest_number, message):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO message_history (`sender_id`, `dest_number`,`message`) VALUES (%s,%s,%s)"
            cursor.execute(sql, (user_id, dest_number, message))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()


if __name__ == '__main__':
    db = SQL()
    db.log_message(10, '98765432', 'testing')
