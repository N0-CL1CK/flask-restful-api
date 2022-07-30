from flask_restful import Resource, request
from controllers import notes_controller
from json import loads

class Notes(Resource):
    def get(self, **kwargs):
        path = str(request.url_rule)
        if path == '/notes/' or path == '/notes/<string:title>/':
            return notes_controller.get_notes(title=kwargs.get('title'))
        else:
            return 404
    
    def post(self):
        if str(request.url_rule) == '/notes/add/':
            title, description = request.json.get('title'), request.json.get('description')
            return notes_controller.add_note(title, description) if title and description else {'msg': 'invalid fields', 'code': 400}
        else:
            return 404

    def put(self, title):
        if str(request.url_rule) == '/notes/<string:title>/':
            new_t, new_d = request.json.get('title'), request.json.get('description')
            if new_t or new_d:
                return notes_controller.update_note(title, new_title=new_t, new_description=new_d)
            else:
                return 400
        else:
            return 404
    
    def delete(self, title):
        if str(request.url_rule) == '/notes/<string:title>/':
            return notes_controller.delete_note(title)
        else:
            return 404