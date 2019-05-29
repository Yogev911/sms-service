# DB configuration
# local
# db_user = 'root'
# db_password = ''
# db_schema_name = 'sms'
# db_hostname = 'localhost'
# db_port = 3306


# remote
db_user = '7mnLL3HbSb'
db_password = 'RRuldgiBG6'
db_schema_name = '7mnLL3HbSb'
db_hostname = 'remotemysql.com'
db_port = 3306

API_TOKEN_KEY = 'thisismykey'
ALGO = 'HS256'

INIT_BALANCE = 5
SMS_COST = 2

REGISTER_MESSAGE = '''
Wellcome {}!, you are now a new member, 
in few seconds you will receive text message with pin code,
please verify your account to start messaging via http://localhost:8080/verify/<user>/<pin_code>
'''

SEND_PIN_MESSAGE = 'Hi {} welcome!, here is your pin code : {}. its valid for the next 5 minutes'

PUZZLE_RESPONSE = '''
Solve this question and get reworded!
The question is: {} .
submit your answer in http://localhost:8080/puzzle and you will reword {} coins!
-- clarifications: send your request to the following address on PUT method, body should be json format when the key is "answer" and value 42
'''
