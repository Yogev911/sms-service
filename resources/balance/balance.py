from flask import request
from flask_restful_swagger_2 import Resource, swagger
from resources.balance import service
from resources.balance.swagger_doc import balance_get


class Balance(Resource):
    @swagger.doc(balance_get)
    def get(self):
        return service.balance(request)
