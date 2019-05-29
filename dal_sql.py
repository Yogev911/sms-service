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

    def add_user(self, user, password, phone, pin):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO users (user, password,phone,balance,pin,verify) VALUES (%s, %s,%s,%s,%s,%s)"
            cursor.execute(sql, (user, password, phone, conf.INIT_BALANCE, pin, False))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()
        return cursor.lastrowid - 1

    def get_user_by_params(self, user):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = "SELECT * FROM `users` WHERE `user`=%s"
            cursor.execute(sql, (user,))
            result = cursor.fetchone()
            if not result:
                return None
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()
        return result

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

    def verify_user(self, user_id):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE users SET `verify` = TRUE WHERE `id` = {user_id}"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()

    def is_user_verified(self, user_id):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"SELECT `verify` FROM users WHERE `id`={user_id}"
            cursor.execute(sql)
            return cursor.fetchone()['verify']

    def log_message(self, user_id, dest_number, message):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO message_history (`sender_id`, `dest_number`,`message`) VALUES (%s,%s,%s)"
            cursor.execute(sql, (user_id, dest_number, message))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()

    def get_user_by_id(self, user_id):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"SELECT * FROM users WHERE `id`={user_id}"
            cursor.execute(sql)
            return cursor.fetchone()

    def set_puzzle(self, user_id, question, answer, reword):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO puzzles (`user_id`, `question`,`answer`,`reword`) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (user_id, question, answer, reword))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()

    def get_user_puzzle(self, user_id):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"SELECT * FROM puzzles WHERE `user_id`={user_id}"
            cursor.execute(sql)
            return cursor.fetchone()

    def delete_puzzle_by_id(self, puzzle_id):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = f"DELETE FROM puzzles WHERE `id` = {puzzle_id}"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()

if __name__ == '__main__':
    db = SQL()
    print(db.get_user_puzzle(16))