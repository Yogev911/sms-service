import os

# local
# db_user = 'root'
# db_password = ''
# db_schema_name = 'sms'
# db_hostname = 'localhost'
# db_port = 3306
# LOG_TABLE = 'logs'

# DB configuration

DB_HOST = 'remotemysql.com'
DB_PORT = 3306
DB_SCHEMA = os.environ.get('db_schema_name', None)
DB_PASSWORD = os.environ.get('db_password', None)
DB_USER = os.environ.get('db_user', None)

API_TOKEN_KEY = os.environ.get('API_TOKEN_KEY', None)
NEXMO_SECRET = os.environ.get('NEXMO_SECRET', None)
NEXMO_KEY = os.environ.get('NEXMO_KEY', None)

# App config
ALGO = 'HS256'
INIT_BALANCE = 5
SMS_COST = 2
PHONE_NUMBER_PREFIX = '9725'
PHONE_NUMBER_LENGHT = 12

# Messages
REGISTER_MESSAGE = '''
Wellcome {}!, you are now a new member, 
in few seconds you will receive text message with pin code,
please verify your account to start messaging via https://yogev-sms-service.herokuapp.com/verify/<user>/<pin_code>
'''

SEND_PIN_MESSAGE = 'Hi {} welcome!, here is your pin code : {}. its valid for the next 5 minutes'

PUZZLE_RESPONSE = '''
Solve this question and get reworded!
The question is: {} .
submit your answer in https://yogev-sms-service.herokuapp.com/puzzle and you will reword {} coins!
-- clarifications: send your request to the following address on PUT method, body should be json format when the key is "answer" and value 42
'''

ACCOUNT_NOT_VERIFIED = f'Account is not verified, please verify your account to start messaging via https://yogev-sms-service.herokuapp.com/verify/<user_id>/<pin_code>'
