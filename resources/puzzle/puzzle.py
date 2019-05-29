from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.puzzle import service
from resources.puzzle.swagger_doc import login_post


class Puzzle(Resource):
    @swagger.doc(login_post)
    def get(self):
        return service.generate_math_question(request)

    @swagger.doc(login_post)
    def put(self):
        return service.submit(request)
