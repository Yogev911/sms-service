import unittest
from unittest.mock import patch

from resources.puzzle.service import generate_math_question, solve_puzzle, submit
import json

from utilities.utils import generate_token


class Request:
    def __init__(self):
        self.data = '{}'
        self.remote_addr = 'Unittest'
        self.headers = {'token': generate_token(20, '972527777777')}


class TestPuzzleMethods(unittest.TestCase):

    def test_no_token(self):
        request = Request()
        request.headers = {}
        res = generate_math_question(request)
        self.assertTrue(res)
        self.assertEqual(res[1], 401)
        res = submit(request)
        self.assertTrue(res)
        self.assertEqual(res[1], 401)

    @patch("utilities.dal.DbClient.get_user_by_id")
    @patch("utilities.dal.DbClient.get_user_puzzle")
    @patch("utilities.dal.DbClient.set_user_puzzle")
    def test_generate_math_question(self, set_user_puzzle, get_user_puzzle, get_user_by_id):
        get_user_by_id.return_value = {'id': 20, 'user': 'test-user22',
                                       'password': 'test-password', 'phone': '972527777777',
                                       'balance': 5555, 'pin': 5555, 'verify': 1}
        get_user_puzzle.return_value = {'question': '9-2', 'answer': 2.0, 'user_id': 20, 'reword': 3, 'id': 4}
        request = Request()
        # Puzzle already exists for user
        res = generate_math_question(request)
        self.assertEqual(res[1], 200)

        # Generate new puzzle
        get_user_puzzle.return_value = None
        res = generate_math_question(request)
        self.assertEqual(res[1], 200)

    @patch("utilities.dal.DbClient.get_user_puzzle")
    @patch("resources.puzzle.service.solve_puzzle")
    def test_submit(self, solve_puzzle, get_user_puzzle):
        request = Request()
        get_user_puzzle.return_value = {'question': '9-2', 'answer': 2.0, 'user_id': 20, 'reword': 3, 'id': 4}

        # Puzzle answered correctly
        request.data = json.dumps({'answer': 2})
        res = submit(request)
        self.assertEqual(res[1], 200)

        # Puzzle answered incorrect
        request.data = json.dumps({'answer': 6})
        res = submit(request)
        self.assertEqual(res[1], 406)

