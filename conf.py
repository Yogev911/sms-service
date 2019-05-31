import os

# DB configuration
# local
db_user = 'root'
db_password = ''
db_schema_name = 'sms'
db_hostname = 'localhost'
db_port = 3306
LOG_TABLE = 'logs'
# remote
# db_schema_name = os.environ.get('db_schema_name', None)
# db_password = os.environ.get('db_password', None)
# db_user = os.environ.get('db_user', None)
# db_hostname = 'remotemysql.com'
# db_port = 3306
HOST = 'https://yogev-sms-service.herokuapp.com'
API_TOKEN_KEY = os.environ.get('API_TOKEN_KEY', 'thisismykey')

ALGO = 'HS256'

NEXMO_SECRET = os.environ.get('NEXMO_SECRET', '3fdf633b')
NEXMO_KEY = os.environ.get('NEXMO_KEY', 'mVZW9LHrKGS7IFn7')
INIT_BALANCE = 5
SMS_COST = 2
PHONE_NUMBER_PREFIX = '9725'
PHONE_NUMBER_LENGHT = 12
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
