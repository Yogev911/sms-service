from datetime import datetime, timedelta
import jwt
import conf
from random import randint
import operator
import random

OPERATIONS = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
]


def generate_token(user_id, phone):
    '''
    generate JWT token from id and phone number
    :param user_id: int
    :param phone: str
    :return: str
    '''
    return jwt.encode(
        {'user_id': user_id, 'phone': phone, 'exp': datetime.utcnow() + timedelta(days=1)},
        conf.API_TOKEN_KEY, algorithm=conf.ALGO).decode('utf-8')


def get_data_by_token(token):
    '''
    decode JWT token to dict
    :param token: str
    :return: dict
    '''
    return jwt.decode(token, conf.API_TOKEN_KEY, algorithm=conf.ALGO)


def generate_pin_code():
    return randint(1000, 9999)


def random_question():
    '''
    generate math question
    :return: (str,str) - > question and answer
    '''
    binary_operations, operand_range = OPERATIONS, range(0, 21)
    op_sym, op_func = random.choice(binary_operations)
    n1 = random.randint(min(operand_range), max(operand_range))
    n2 = random.randint(min(operand_range), max(operand_range))
    question = '{} {} {}'.format(n1, op_sym, n2)
    answer = op_func(n1, n2)
    return question, answer
