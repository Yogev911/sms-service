balance_get = {
    'tags': ['balance'],
    'description': 'Get user current balance',
    'parameters': [
        {
            'name': 'token',
            'description': 'authentication token',
            'in': 'header',
            'type': 'string',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'User balance amount',
        },
        '401': {
            'description': 'Token is not authenticated'
        },
        '501': {
            'description': 'Internal server error'
        }
    }
}
