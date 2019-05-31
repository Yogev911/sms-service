import unittest
from unittest.mock import patch

from resources.login.service import login
import json
from datetime import datetime


class Request:
    def __init__(self):
        self.form = {}
        self.remote_addr = 'Unittest'


class TestLoginMethods(unittest.TestCase):

    def test_no_data(self):
        request = Request()
        res = login(request)
        self.assertTrue(res)
        self.assertEqual(res[1], 401)

    @patch("utilities.dal.DbClient.get_user_by_username")
    def test_login(self, get_user_by_username):

        request = Request()
        # User not exists
        get_user_by_username.return_value = None
        request.form = {'user': f'test-user', 'password': 'test-password'}
        res = login(request)
        self.assertEqual(res[1], 404)

        # User not verified phone number
        get_user_by_username.return_value = {'id': 20, 'user': 'test-user-exists',
                                             'password': 'test-password', 'phone': '972527777777',
                                             'balance': 5555, 'pin': 5555, 'verify': 0}
        request.form = {'user': f'test-user-exists', 'password': 'test-password'}
        res = login(request)
        self.assertEqual(res[1], 401)

        # User wrong password
        get_user_by_username.return_value = {'id': 20, 'user': 'test-user-exists',
                                             'password': 'wrong-pass', 'phone': '972527777777',
                                             'balance': 5555, 'pin': 5555, 'verify': 1}
        request.form = {'user': f'test-user1', 'password': 'wrong-password'}
        res = login(request)
        self.assertEqual(res[1], 401)

        # User authenticate and exists
        get_user_by_username.return_value = {'id': 20, 'user': 'test-user',
                                             'password': 'test-password', 'phone': '972527777777',
                                             'balance': 5555, 'pin': 5555, 'verify': 1}
        request.form = {'user': f'test-user', 'password': 'test-password'}
        res = login(request)
        self.assertEqual(res[1], 201)
