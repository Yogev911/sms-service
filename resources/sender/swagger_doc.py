products_post = {
    'tags': ['users'],
    'description': 'Adds a user',
    'parameters': [
        {
            'name': 'body',
            'description': 'Request body',
            'in': 'body',
            'schema': 'string',
            'required': True,
        }
    ],
    'responses': {
        '201': {
            'description': 'Created user',
            'headers': {
                'Location': {
                    'type': 'string',
                    'description': 'Location of the new item'
                }
            },
            'examples': {
                'application/json': {
                    'id': 1
                }
            }
        }
    }
}

users_post = {
    'tags': ['users'],
    'description': 'Adds a user',
    'parameters': [
        {
            'name': 'body',
            'description': 'Request body',
            'in': 'body',
            'schema': 'string',
            'required': True,
        }
    ],
    'responses': {
        '201': {
            'description': 'Created user',
            'headers': {
                'Location': {
                    'type': 'string',
                    'description': 'Location of the new item'
                }
            },
            'examples': {
                'application/json': {
                    'id': 1
                }
            }
        }
    }
}

login_post = {
    'tags': ['login'],
    'description': 'Logs in a user',
    'parameters': [
        {
            'name': 'email',
            'description': 'Request users email',
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
        }
    ],
    'responses': {
        '200': {
            'description': 'user logged in successfully',
            'headers': {
                'Location': {
                    'type': 'string',
                    'description': 'Location of the new item'
                }
            },
            'examples': {
                'application/json': {
                    'id': 1
                }
            }
        },
        '401': {
            'description': 'email or password incorrect'
        }
    }
}
