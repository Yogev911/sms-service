from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.puzzle import service
from resources.puzzle.swagger_doc import puzzle_get, puzzle_put


class Puzzle(Resource):
    @swagger.doc(puzzle_get)
    def get(self):
        return service.generate_math_question(request)

    @swagger.doc(puzzle_put)
    def put(self):
        return service.submit(request)
