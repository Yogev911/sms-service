from flask_restful_swagger_2 import Resource, swagger

from resources import service
from resources.login.swagger_doc import users_post


class Users(Resource):
    @swagger.doc(users_post)
    def post(self):
        return service.BLA

    @swagger.doc(users_post)
    def get(self):
        return service.BLA

    @swagger.doc(users_post)
    def put(self):
        return service.BLA

    @swagger.doc(users_post)
    def delete(self):
        return service.BLA
