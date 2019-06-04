from resources.common_modles import UserCredential

login_post = {
    'tags': ['login'],
    'description': 'login new user',
    'parameters': [
        {
            'name': 'user',
            'description': 'Request users credentials',
            'in': 'body',
            'schema': UserCredential,
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': 'Token achieved',
        },
        '401': {
            'description': 'Missing parameters or wrong credentials'
        },
        '404': {
            'description': 'User not found'
        },
        '501': {
            'description': 'Internal server error'
        }
    }
}
