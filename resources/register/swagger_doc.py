from resources.common_modles import UserModel
register_post = {
    'tags': ['register'],
    'description': 'register new user',
    'parameters': [
        {
            'name': 'user',
            'description': 'Request users credentials',
            'in': 'body',
            'schema': UserModel,
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': 'User register successfully',
        },
        '401': {
            'description': 'User already registered'
        },
        '406': {
            'description': 'Phone number or other params are incorrect'
        },
        '501': {
            'description': 'Internal server error'
        }
    }
}
