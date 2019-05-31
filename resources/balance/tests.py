import unittest
from unittest.mock import patch

from resources.verify.service import verify


class TestVerifyMethods(unittest.TestCase):

    @patch("utilities.dal.DbClient.get_user_by_username")
    @patch("utilities.dal.DbClient.verify_user")
    def test_verify(self, verify_user, get_user_by_username):
        # user is not verified
        get_user_by_username.return_value = {'id': 20, 'user': 'test-user22',
                                             'password': 'test-password', 'phone': '972527777777',
                                             'balance': 5555, 'pin': 5555, 'verify': 1}

        res = verify('user-test', 5555)
        self.assertEqual(res[1], 200)

        get_user_by_username.return_value = {'id': 20, 'user': 'test-user22',
                                             'password': 'test-password', 'phone': '972527777777',
                                             'balance': 5555, 'pin': 5555, 'verify': 0}
        # user is verified
        res = verify('user-test', 5555)
        self.assertEqual(res[1], 200)

        # Incorrect PIN
        res = verify('user-test', 6666)
        self.assertEqual(res[1], 401)
