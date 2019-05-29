from resources.common_modles import Message

sender_post = {
    'tags': ['sender'],
    'description': 'send sms',
    'parameters': [
        {
            'name': 'token',
            'description': 'authentication token',
            'in': 'header',
            'type': 'string',
            'required': True,
        },
        {
            'name': 'mesage',
            'description': 'message model',
            'in': 'body',
            'schema': Message,
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': 'SMS sent',
        },
        '401': {
            'description': 'Token is not authenticated'
        },
        '402': {
            'description': 'Balance is empty'
        },
        '501': {
            'description': 'Internal server error'
        }
    }
}
