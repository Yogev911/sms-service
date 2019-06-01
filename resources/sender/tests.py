import unittest
from unittest.mock import patch

from resources.sender.service import send_sms, _send_sms
import json

from utilities.utils import generate_token


class Request:
    def __init__(self):
        self.data = '{}'
        self.remote_addr = 'Unittest'
        self.headers = {'token': generate_token(20, '972527777777')}


class TestSenderMethods(unittest.TestCase):

    def test_no_token(self):
        request = Request()
        request.headers = {}
        res = send_sms(request)
        self.assertTrue(res)
        self.assertEqual(res[1], 401)

    @patch("utilities.dal.DbClient.get_user_balance")
    @patch("resources.sender.service._send_sms")
    def test_send_sms(self, _send_sms, get_user_balance):
        request = Request()

        # bad data
        request.data = json.dumps({'destr': '663', 'msdvdvffvfg': 'hello'})
        res = send_sms(request)
        self.assertEqual(res[1], 501)
        get_user_balance.return_value = 50

        # balance if above minimum
        request.data = json.dumps({'dest': '972528282663', 'msg': 'hello'})
        get_user_balance.return_value = 50
        res = send_sms(request)
        self.assertEqual(res[1], 201)

        # balance is empty
        get_user_balance.return_value = 0
        res = send_sms(request)
        self.assertEqual(res[1], 402)
