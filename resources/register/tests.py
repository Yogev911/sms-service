import unittest
from unittest.mock import patch

from resources.register.service import register, is_phone_valid, register_new_user
import json



class Request:
    def __init__(self):
        self.data = '{}'
        self.remote_addr = 'Unittest'


class TestRegisterMethods(unittest.TestCase):

    def test_no_data(self):
        request = Request()
        request.data = '{}'
        res = register(request)
        self.assertTrue(res)
        self.assertEqual(res[1], 406)

    @patch("utilities.dal.DbClient.get_user_by_username")
    @patch("resources.register.service.register_new_user")
    def test_register(self, register_new_user, get_user_by_username):
        # User already exists
        request = Request()
        request.data = json.dumps({'user': 'test-user-exists', 'password': '1234', 'phone': '9728282663'})
        get_user_by_username.return_value = {'id': 20, 'user': 'test-user-exists',
                                             'password': 'test-password', 'phone': '972527777777',
                                             'balance': 5555, 'pin': 5555, 'verify': 1}
        res = register(request)
        self.assertEqual(res[1], 401)

        # Register new user
        request.data = json.dumps({'user': 'test-user-exists', 'password': '1234', 'phone': '972528282663'})
        get_user_by_username.return_value = None
        res = register(request)
        self.assertEqual(res[1], 201)

    def test_is_phone_valid(self):
        # Invalid phone number
        self.assertTrue(is_phone_valid('972528282663'))
