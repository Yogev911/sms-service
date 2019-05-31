import unittest
from unittest.mock import patch

from resources.login.service import login
import json
from datetime import datetime


class Request:
    def __init__(self):
        self.data = '{}'
        self.remote_addr = 'Unittest'


class TestLoginMethods(unittest.TestCase):

    def test_no_data(self):
        request = Request()
        res = login(request)
        self.assertTrue(res)
        self.assertEqual(res[1], 401)

    def test_login(self):
        request = Request()
        # User not exists
        request.data = json.dumps({'user': f'test-user{datetime.now().__str__()}', 'password': 'test-password'})
        res = login(request)
        self.assertEqual(res[1], 404)

        # User not verified phone number
        request.data = json.dumps({'user': f'test-user1', 'password': 'test-password'})
        res = login(request)
        self.assertEqual(res[1], 401)

        # User wrong password
        request.data = json.dumps({'user': f'test-user1', 'password': 'wrong-password'})
        res = login(request)
        self.assertEqual(res[1], 401)

        # User authenticate and exists
        request.data = json.dumps({'user': f'test-user2', 'password': 'test-password'})
        res = login(request)
        self.assertEqual(res[1], 201)
