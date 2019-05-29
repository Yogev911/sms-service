from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.login import service
from resources.login.swagger_doc import login_post


class Login(Resource):
    @swagger.doc(login_post)
    def post(self):
        return service.login(request)
