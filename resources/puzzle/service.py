import jwt
import json
from random import randint

import conf
from utilities.dal import DbClient
from utilities.logger import get_logger
from utilities.utils import random_question, get_data_by_token

db = DbClient()
logger = get_logger(__name__)


def generate_math_question(request):
    token = None
    try:
        logger.info('Generating math question')
        token = request.headers.get('token', None)
        if not token:
            logger.info(f'Missing token on {request.remote_addr}')
            return "Missing token", 401
        user_data = get_data_by_token(token)
        user = db.get_user_by_id(user_data['user_id'])
        puzzle = db.get_user_puzzle(user['id'])
        if puzzle:
            logger.info(f'User {user["user"]} has an unsolved question')
            return f"Solve this question first... {puzzle['question']}", 200
        else:
            question, answer = random_question()
            reword = randint(1, 5)
            db.set_user_puzzle(user['id'], question, answer, reword)
            logger.info(
                f'New question generated for user {user["user"]}, question: {question}, reword set for {reword}')
            return conf.PUZZLE_RESPONSE.format(question, reword), 201

    except jwt.ExpiredSignatureError:
        logger.exception(f'Token is not authenticated! on request {request.remote_addr}')
        return "Token is not authenticated!, log in again", 401
    except Exception as e:
        logger.exception(f'Failed generate puzzle, token {token} Error: {e.__str__()}')
        return f'Failed generate puzzle.. try again later {e.__str__()}', 501


def submit(request):
    token = None
    try:
        logger.info('Submit puzzle answer')
        token = request.headers.get('token', None)
        if not token:
            logger.info(f'Missing token on {request.remote_addr}')
            return "Missing token", 401
        data = json.loads(request.data)
        answer = data.get('answer', None)
        user = get_data_by_token(token)
        puzzle = db.get_user_puzzle(user['user_id'])

        if not puzzle:
            logger.info(f'User {user["user_id"]} has no unsolved question')
            return 'No questions waiting for you.. use GET method to generate new question', 404
        if puzzle['answer'] == answer:
            x = solve_puzzle(puzzle, user)
            return f"Super! you just earned {puzzle['reword']} coins! ", 200
        else:
            logger.info(f'User {user["user_id"]} submitted wrong answer')
            return "Wrong answer", 406

    except jwt.ExpiredSignatureError:
        logger.exception(f'Token is not authenticated! on request {request.remote_addr}')
        return "Token is not authenticated!, log in again", 401
    except Exception as e:
        logger.exception(f'Failed submitting answer, token {token} Error: {e.__str__()}')
        return f'Failed submitting the answer try again later {e.__str__()}', 501


def solve_puzzle(puzzle, user):
    current_balance = db.get_user_balance(user_id=user['user_id'])
    db.update_balance(user_id=user['user_id'], new_balance=current_balance + puzzle['reword'])
    db.delete_puzzle_by_id(puzzle['id'])
    logger.info(f'User {user["user_id"]} solved puzzle and reworded with {puzzle["reword"]}')
