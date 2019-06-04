from datetime import datetime, timedelta
import jwt
import conf
from random import randint
import operator
import random
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import re

OPERATIONS = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
]


def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1") if encode else data


def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = source[:AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding


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


def is_password_valid(password):
    pattern = re.compile(conf.PASSWORD_PATTERN)
    return bool(re.search(pattern, password))


if __name__ == '__main__':
    x = str.encode('yogev')
    en = encrypt(conf.PASSWORD_ENCRYPTION_KEY, x)
    de = str(decrypt(conf.PASSWORD_ENCRYPTION_KEY, en))
    print(de)
    print(de == str(x))
    print(x,en,de)
