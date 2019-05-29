login_post = {
    'tags': ['login'],
    'description': 'login new user',
    'parameters': [
        {
            'name': 'user',
            'description': 'Request users username',
            'in': 'body',
            'schema': 'string',
            'required': True,
        },
        {
            'name': 'password',
            'description': 'Request users password',
            'in': 'body',
            'schema': 'string',
            'required': True
        },
        {
            'name': 'phone',
            'description': 'Request users phone',
            'in': 'body',
            'schema': 'string',
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
