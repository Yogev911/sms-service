import json

import jwt

from dal_sql import SQL
import traceback
import conf
from random import randint
from utils import random_question, get_data_by_token

db = SQL()


def generate_math_question(request):
    try:
        token = request.headers.get('token', None)
        if not token:
            return "missing token", 401
        try:
            user_data = get_data_by_token(token)
        except jwt.ExpiredSignatureError:
            return "Token is not authenticated!, log in again", 401
        user_id = db.get_user_by_id(user_data['user_id'])
        puzzle = db.get_user_puzzle(user_data['user_id'])
        if puzzle:
            return f"Solve this question first... {puzzle['question']}", 200
        question, answer = random_question()
        reword = randint(1, 5)
        db.set_puzzle(user_id['id'], question, answer, reword)
        return conf.PUZZLE_RESPONSE.format(question,reword), 201
    except:
        return f'Failed generate puzzle.. try again later {traceback.format_exc()}', 501


def submit(request):
    try:
        token = request.headers.get('token', None)
        if not token:
            return "missing token", 401
        try:
            user_data = get_data_by_token(token)
        except jwt.ExpiredSignatureError:
            return "Token is not authenticated!, log in again", 401
        data = json.loads(request.data)
        answer = data.get('answer')

        puzzle = db.get_user_puzzle(user_data['user_id'])
        if puzzle['answer'] == answer:
            current_balance = db.get_user_balance(user_id=user_data['user_id'])
            db.update_balance(user_id=user_data['user_id'], new_balance=current_balance + puzzle['reword'])
            db.delete_puzzle_by_id(puzzle['id'])
            return f"Super! you just earned {puzzle['reword']} coins! "
        else:
            return "Not this time buddy... try again", 406
    except:
        return f'Failed submitting the answer try again later {traceback.format_exc()}', 501
