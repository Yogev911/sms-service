from flask_restful_swagger_2 import Schema


class UserModel(Schema):
    type = 'object'
    properties = {
        'user': {
            'type': 'string'
        },
        'password': {
            'type': 'string'
        },
        'phone': {
            'type': 'string'
        }
    }
