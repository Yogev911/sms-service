import jwt
import json
from random import randint

import conf
from utilities.dal import DbClient
from utilities.logger import Logger
from utilities.utils import random_question, get_data_by_token
from utilities.exceptions import *

db = DbClient()
logger = Logger(__name__)


def generate_math_question(request):
    '''
    Get user math question
    :param request: flask request object
    '''
    token = None
    try:
        logger.info('Generating math question')
        token = request.headers.get('token', None)
        if not token:
            raise TokenNotExists()
        user_question, user_answer, reword = get_user_puzzle(token, generate=True)
        return conf.PUZZLE_RESPONSE.format(user_question, reword), 200

    except TokenNotExists as e:
        logger.warning(e.__str__())
        return e.__str__(), 401
    except jwt.ExpiredSignatureError:
        logger.exception(f'Token is not authenticated! on request {request.remote_addr}')
        return "Token is not authenticated!, log in again", 401
    except Exception as e:
        logger.exception(f'Failed generate puzzle, token {token}')
        return f'Failed generate puzzle.. try again later {e.__str__()}', 501


def get_user_puzzle(token, generate=False):
    '''
    Returns the user puzzle, question answer reword
    :param token:
    :param generate: bool -> optional, if set to True, function will generate new question if question not exists for the user
    :return: tuple(str,str,str) -> question,  answer, reword
    '''
    user_data = get_data_by_token(token)
    user = db.get_user_by_id(user_data['user_id'])
    puzzle = db.get_user_puzzle(user['id'])

    if puzzle:
        logger.info(f'User {user["user"]} has an unsolved question')
        return puzzle['question'], puzzle['answer'], puzzle['reword']
    elif generate:
        question, answer, reword = set_new_question(user)
        return question, answer, reword
    else:
        return None, None, None


def set_new_question(user):
    '''
    Record new puzzle question for user
    :param user: dict
    :return: tuple(str,str,str) -> question,  answer, reword
    '''
    question, answer = random_question()
    reword = randint(1, 5)
    db.set_user_puzzle(user['id'], question, answer, reword)
    logger.info(
        f'New question generated for user {user["user"]}, question: {question}, reword set for {reword}')
    return question, answer, reword


def submit(request):
    '''
    PUT user answer for latest question
    :param request: flask request object
    '''
    token = None
    try:
        logger.info('Submit puzzle answer')
        token = request.headers.get('token', None)
        if not token:
            raise TokenNotExists()

        data = json.loads(request.data)
        answer = data.get('answer', None)
        user = get_data_by_token(token)
        user_question, user_answer, reword = get_user_puzzle(token)
        if not user_question:
            raise PuzzleNotExists(user['user_id'])
        if user_answer != answer:
            raise WrongAnswer(user['user_id'])
        solve_puzzle(user)
        return "Puzzle solved", 200

    except TokenNotExists as e:
        logger.warning(e.__str__())
        return e.__str__(), 401
    except WrongAnswer as e:
        logger.warning(e.__str__())
        return e.__str__(), 406
    except PuzzleNotExists as e:
        logger.warning(e.__str__())
        return e.__str__(), 404
    except jwt.ExpiredSignatureError:
        logger.exception(f'Token is not authenticated! on request {request.remote_addr}')
        return "Token is not authenticated!, log in again", 401
    except Exception as e:
        logger.exception(f'Failed submitting answer, token {token} Error: {e.__str__()}')
        return f'Failed submitting the answer try again later {e.__str__()}', 501


def solve_puzzle(user):
    '''
    Update puzzle solved in DB and update user balnace with reword
    :param user: dict
    :return: None
    '''
    puzzle = db.get_user_puzzle(user['user_id'])
    current_balance = db.get_user_balance(user_id=user['user_id'])
    db.update_balance(user_id=user['user_id'], new_balance=current_balance + puzzle['reword'])
    db.delete_puzzle_by_id(puzzle['id'])
    logger.info(f'User {user["user_id"]} solved puzzle and reworded with {puzzle["reword"]}')
