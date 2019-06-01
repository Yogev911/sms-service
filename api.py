from flask_cors import CORS
from flask import Flask
from flask_restful_swagger_2 import Api

from resources.login.login import Login
from resources.sender.sender import Sender
from resources.register.register import Register
from resources.verify.verify import Verify
from resources.puzzle.puzzle import Puzzle
from resources.balance.balance import Balance
from utilities.logger import Logger

logger = Logger(__name__)

app = Flask(__name__)

CORS(app)
api = Api(app, api_version='0.1')

api.add_resource(Login, "/login")
api.add_resource(Register, "/register")
api.add_resource(Puzzle, "/puzzle")
api.add_resource(Verify, "/verify/<string:user>/<int:pin>")
api.add_resource(Sender, "/send")
api.add_resource(Balance, "/user/balance")

if __name__ == '__main__':
    logger.info('Starting API')
    app.run(host="0.0.0.0", port=5000)
