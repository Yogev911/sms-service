import pymysql.cursors

import conf


class DbClient(object):
    def __init__(self):
        self.connection = None
        self.connection = pymysql.connect(host=conf.DB_HOST,
                                          user=conf.DB_USER,
                                          password=conf.DB_PASSWORD,
                                          db=conf.DB_SCHEMA,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor,
                                          autocommit=True,
                                          connect_timeout=31536000)

    def __del__(self):
        if self.connection:
            self.connection.close()

    def add_user(self, user, password, phone, pin):
        try:
            with self.connection.cursor() as cursor:
                sql = f"INSERT INTO users (user, password,phone,balance,pin,verify) VALUES (%s, %s,%s,%s,%s,%s)"
                cursor.execute(sql, (user, password, phone, conf.INIT_BALANCE, pin, False))
            return cursor.lastrowid - 1
        except:
            self.connection.rollback()

    def get_user_by_username(self, user):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `users` WHERE `user`=%s"
                cursor.execute(sql, (user,))
                result = cursor.fetchone()
                return result if result else None
        except:
            self.connection.rollback()

    def update_balance(self, user_id, new_balance):
        try:
            with self.connection.cursor() as cursor:
                sql = f"UPDATE users SET `balance` = {new_balance} WHERE `id` = {user_id}"
                cursor.execute(sql)
        except:
            self.connection.rollback()

    def get_user_balance(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT `balance` FROM users WHERE `id`={user_id}"
                cursor.execute(sql)
                return cursor.fetchone()['balance']
        except:
            self.connection.rollback()

    def verify_user(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                sql = f"UPDATE users SET `verify` = TRUE WHERE `id` = {user_id}"
                cursor.execute(sql)
        except:
            self.connection.rollback()

    def log_message(self, user_id, dest_number, message):
        try:
            with self.connection.cursor() as cursor:
                sql = f"INSERT INTO message_history (`sender_id`, `dest_number`,`message`) VALUES (%s,%s,%s)"
                cursor.execute(sql, (user_id, dest_number, message))
        except:
            self.connection.rollback()

    def get_user_by_id(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM users WHERE `id`={user_id}"
                cursor.execute(sql)
                return cursor.fetchone()
        except:
            self.connection.rollback()

    def set_user_puzzle(self, user_id, question, answer, reword):
        try:
            with self.connection.cursor() as cursor:
                sql = f"INSERT INTO puzzles (`user_id`, `question`,`answer`,`reword`) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql, (user_id, question, answer, reword))
        except:
            self.connection.rollback()

    def get_user_puzzle(self, user_id):
        with self.connection.cursor() as cursor:
            sql = f"SELECT * FROM puzzles WHERE `user_id`={user_id}"
            cursor.execute(sql)
            return cursor.fetchone()

    def delete_puzzle_by_id(self, puzzle_id):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM puzzles WHERE `id` = {puzzle_id}"
                cursor.execute(sql)
        except:
            self.connection.rollback()
