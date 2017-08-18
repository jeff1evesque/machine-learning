#!/usr/bin/python

'''

This file allows methods defined from the Base, or BaseData superclass to be
overridden, if needed.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from flask import current_app, session
from brain.database.dataset import Collection
from brain.session.base_data import BaseData
from brain.database.entity import Entity


class DataAppend(BaseData):
    '''

    This class provides an interface to update existing stored entities within
    the sql database.

    Note: this class is invoked within 'load_data.py'

    Note: inherit base methods from the superclass 'BaseData'

    '''

    def __init__(self, premodel_data):
        '''

        This constructor inherits additional class properties, from the
        constructor of the 'BaseData' superclass.

        '''

        # superclass constructor
        BaseData.__init__(self, premodel_data)

        # class variable
        if session.get('uid'):
            self.max_document = current_app.config.get('MAXDOC_AUTH')
        else:
            self.max_document = current_app.config.get('MAXDOC_ANON')

    def save_entity(self, session_type, session_id):
        '''

        This method overrides the identical method from the inherited
        superclass, 'BaseData'. Specifically, this method updates an
        existing entity within the corresponding database table,
        'tbl_dataset_entity'.

        @session_id, is synonymous to 'entity_id', and provides context to
            update 'modified_xx' columns within the 'tbl_dataset_entity'
            database table.

        '''

        # local variables
        cursor = Collection()
        document_count = cursor.query(collection_adjusted, 'count_documents')

        premodel_settings = self.premodel_data['properties']
        premodel_entity = {
            'title': premodel_settings.get('session_name', None),
            'uid': self.uid,
            'id_entity': session_id,
        }

        # save dataset element
        if document_count < self.max_document:
            db_save = Entity(premodel_entity, session_type)
            db_return = db_save.save()

            if db_return['status']:
                return {'status': True, 'error': None}

            else:
                self.list_error.append(db_return['error'])
                return {'status': False, 'error': self.list_error}

        else:
            return {'status': True, 'error': None}
