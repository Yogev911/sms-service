import unittest

from utilities.utils import generate_pin_code, generate_token, get_data_by_token


class TestUtilsMethods(unittest.TestCase):

    def test_utils(self):
        test_user_id = 1234
        test_phone = '972529999444'
        token = generate_token(test_user_id, test_phone)
        token_data = get_data_by_token(token)
        self.assertEqual(token_data['phone'], test_phone)
        self.assertEqual(token_data['user_id'], test_user_id)
        self.assertIn('user_id', token_data)
        self.assertIn('phone', token_data)
        self.assertIn('exp', token_data)
