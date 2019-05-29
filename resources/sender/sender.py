from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.sender import service
from resources.sender.swagger_doc import sender_post


class Sender(Resource):
    @swagger.doc(sender_post)
    def post(self):
        return service.send_sms(request)
