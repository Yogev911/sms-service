import json
from dal_sql import SQL
import jwt
import conf

db = SQL()


def generate_token(name, password, user_id):
    return jwt.encode({'name': name, 'password': password, 'user_id': user_id}, conf.API_TOKEN_KEY,
                      algorithm='HS256').decode('utf-8')


def login(request):
    try:
        token = request.headers.get('token', None)
        if not token:
            res = json.loads(request.data)
            user = res.get('user', None)
            password = res.get('password', None)
            user_id = db.get_user_by_id()
            token = generate_token(user, password, user_id)

        user = bson_to_json(returned_request(res))
        return (json.dumps(user), 200)

    except:
        return (("failed to login", 401))


def returned_request(res):
    init = False
    user = DB.get_user_by_email(res["email"])
    if user:
        init = True
    return ({"user": user, "Initial": init})
