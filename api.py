from flask_cors import CORS
from flask import Flask
from flask_restful_swagger_2 import Api

from resources.login.login import Login
from resources.sender.sender import Sender
from resources.register.register import Register
from resources.verify.verify import Verify

app = Flask(__name__)

CORS(app)
api = Api(app, api_version='0.1')

api.add_resource(Login, "/login")
api.add_resource(Sender, "/send")
api.add_resource(Register, "/register")
api.add_resource(Verify, "/verify")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
