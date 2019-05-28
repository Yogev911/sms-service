from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.verify.service import verify
from resources.verify.swagger_doc import login_post


class Verify(Resource):
    @swagger.doc(login_post)
    def put(self, user, pin):
        return verify(user, pin)
