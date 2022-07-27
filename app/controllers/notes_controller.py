from models.models import Notes

def add_note(title, description):
    note = Notes(title=title, description=description)
    note.save()
    return {'msg': 'Successfully created', 'code': 200}

def get_notes(**kwargs):
    res = list(Notes.query.filter(Notes.title.like(f"%{kwargs.get('title')}%"))) if kwargs.get('title') else Notes.query.all()
    notes = {}
    if res.__len__() != 0:
        for note in res:
            notes.update({note.id: note.get_data()})
    return notes