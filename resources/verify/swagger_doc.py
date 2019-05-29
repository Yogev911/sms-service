verify_post = {
    'tags': ['verify'],
    'description': 'verify pin code',
    'parameters': [
        {
            'name': 'user',
            'description': 'Request users username',
            'in': 'path',
            'type': 'string',
            'required': True,
        },
        {
            'name': 'pin',
            'description': 'Request users pin code',
            'in': 'path',
            'type': 'string',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Account activated successfully',
        },
        '401': {
            'description': 'PIN code is incorrect'
        },
        '501': {
            'description': 'Internal server error'
        }
    }
}
