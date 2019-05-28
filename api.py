from flask_cors import CORS
from flask import Flask
from flask_restful_swagger_2 import Api


from resources.login.login import Login
from resources.register.register import Register
from resources.users import Users

app = Flask(__name__)

CORS(app)
api = Api(app, api_version='0.1')

api.add_resource(Users, "/users")
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
