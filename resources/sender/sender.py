from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.sender import service
from resources.sender import swagger_doc


class Sender(Resource):
    @swagger.doc(swagger_doc.login_post)
    def post(self):
        return service.send_sms(request)
