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

def update_note(title, **kwargs):
    new_title, new_description = kwargs.get('new_title'), kwargs.get('new_description')
    if new_title or new_description:
        note = Notes.query.filter_by(title=title).first()
        if note:
            if new_title:
                note.title = new_title
            if new_description:
                note.description = new_description
            note.save()
            return {'msg': 'Successfully updated', 'code': 200}
        else:
            return {'msg': 'Not found the specified key', 'code': 200}
    else:
        return {'error': 'Invalid fields', 'code': 400}

def delete_note(title):
    note = Notes.query.filter_by(title=title).first()
    if note:
        deleted_note = note
        note.delete()
        return {'msg': 'Successfully deleted', 'code': 200, 'deleted_object': deleted_note.get_data()}
    else:
        return {'msg': 'Not found the specified key', 'code': 200}