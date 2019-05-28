import datetime
import pymysql.cursors

import conf

cnx = None


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
            cursor.execute(sql, (user, password, phone, 58))

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
                return self.add_user(user,password,phone)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.db.commit()
        return result['id']