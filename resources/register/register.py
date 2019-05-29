from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.register import service
from resources.register.swagger_doc import register_post


class Register(Resource):
    @swagger.doc(register_post)
    def post(self):
        return service.register(request)
