import os

# Environment variables

# DB configuration
DB_PORT = os.environ.get('DB_PORT')
DB_HOST = os.environ.get('DB_HOST')
DB_SCHEMA = os.environ.get('DB_SCHEMA')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_USER = os.environ.get('DB_USER')

API_TOKEN_KEY = os.environ.get('API_TOKEN_KEY')
PASSWORD_ENCRYPTION_KEY = str.encode(os.environ.get('PASSWORD_ENCRYPTION_KEY'))

NEXMO_SECRET = os.environ.get('NEXMO_SECRET')
NEXMO_KEY = os.environ.get('NEXMO_KEY')

# App config
ALGO = 'HS256'
LOG_TABLE = 'logs'
SMS_COST = 2
INIT_BALANCE = 5
PHONE_NUMBER_LENGHT = 12
PHONE_NUMBER_PREFIX = '9725'
PASSWORD_PATTERN = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

# Messages
REGISTER_MESSAGE = '''
Wellcome {}!, you are now a new member, 
in few seconds you will receive text message with pin code,
please verify your account to start messaging via /verify/<user>/<pin_code>
'''

SEND_PIN_MESSAGE = 'Hi {} welcome!, here is your pin code : {}. its valid for the next 5 minutes'

PUZZLE_RESPONSE = '''
Solve this question and get reworded!
The question is: {} .
submit your answer in /puzzle and you will reword {} coins!
-- clarifications: send your request to the following address on PUT method, body should be json format when the key is "answer" and value 42
'''
