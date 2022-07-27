from flask import Flask
from flask_restful import Resource, Api
from .notes_routes import Notes

app = Flask(__name__)
api = Api(app)

api.add_resource(Notes, '/notes/', '/notes/<string:title>/', '/notes/add/')