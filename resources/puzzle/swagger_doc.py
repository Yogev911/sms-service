puzzle_get = {
    'tags': ['puzzle'],
    'description': 'get fresh question',
    'parameters': [
        {
            'name': 'token',
            'description': 'authentication token',
            'in': 'header',
            'schema': 'string',
            'required': True,
        }
    ],
    'responses': {
        '200': {
            'description': 'Question is still unsolved',
        },
        '201': {
            'description': 'Question set',
        },
        '401': {
            'description': 'Token is not authenticated'
        },
        '501': {
            'description': 'Internal server error'
        }
    }
}

puzzle_put = {
    'tags': ['puzzle'],
    'description': 'solve puzzle',
    'parameters': [
        {
            'name': 'token',
            'description': 'authentication token',
            'in': 'header',
            'schema': 'string',
            'required': True,
        }
    ],
    'responses': {
        '200': {
            'description': 'Question solved',
        },
        '401': {
            'description': 'Token is not authenticated'
        },
        '404': {
            'description': 'Question not found'
        },
        '406': {
            'description': 'Wrong answer for question'
        },
        '501': {
            'description': 'Internal server error'
        }
    }
}
