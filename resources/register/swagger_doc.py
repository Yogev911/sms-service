register_post = {
    'tags': ['register'],
    'description': 'register new user',
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
