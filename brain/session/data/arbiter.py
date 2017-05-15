#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.database.entity import Entity


def save_info(dataset, session_type, userid):
    '''

    This method saves the current entity into the database, then returns the
    corresponding entity id.

    '''

    list_error = []
    premodel_settings = dataset['data']['settings']
    premodel_entity = {
        'title': premodel_settings.get('session_name', None),
        'uid': userid,
        'id_entity': None
    }
    db_save = Entity(premodel_entity, session_type)

    # save dataset element
    db_return = db_save.save()

    # return error(s)
    if not db_return['status']:
        list_error.append(db_return['error'])
        return {'id': None, 'error': list_error}

    # return session id
    elif db_return['status'] and session_type == 'data_new':
        return {'id': db_return['id'], 'error': None}
