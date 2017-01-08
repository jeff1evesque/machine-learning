#!/usr/bin/python

'''## @data_new

This file allows methods defined from the Base, or Base_Data superclass to be
overridden, if needed.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from flask import current_app
from flask import session
from brain.session.base import Base
from brain.session.base_data import Base_Data
from brain.database.save_entity import Save_Entity


class Data_New(Base, Base_Data):
    '''@Data_New

    This class provides a generic constructor interface.

    Note: this class is invoked within 'load_data.py'

    Note: inherit base methods from superclass 'Base', 'Base_Data

    '''

    def __init__(self, premodel_data):
        '''@__init__

        This constructor defines class properties using the superclass 'Base',
        and 'Base_Data' constructor, along with the constructor in this
        subclass.

        @super(), implement 'Base', and 'Base_Data' superclass constructor
            within this child class constructor.

        @self.uid, the logged-in user (i.e. userid).

        Note: the superclass constructor expects the same 'premodel_data'
              argument.

        '''

        super(Data_New, self).__init__(premodel_data)
        self.observation_labels = []
        self.list_error = []
        self.dataset = []
        self.list_model_type = current_app.config.get('MODEL_TYPE')
        self.model_type = premodel_data['data']['settings']['model_type']

        if 'uid' in session:
            self.uid = session['uid']
        else:
            self.uid = current_app.config.get('USER_ID')

    def save_entity(self, session_type, id_entity=None):
        '''@save_entity

        This method overrides the identical method from the inherited
        superclass, 'Base_Data'. Specifically, this method updates an
        existing entity within the corresponding database table,
        'tbl_dataset_entity'.

        @session_id, is synonymous to 'entity_id', and provides context to
            update 'modified_xx' columns within the 'tbl_dataset_entity'
            database table.

        @numeric_model_type, list indices begin at 0, and needs to be corrected
            by adding 1. This allows the numeric representation of the
            'model_type' to relate to another database table, which maps
            integer values with the corresponding 'model_type' name. The
            integer column of the mapping table begins at 1.

        '''

        # assign numerical representation
        numeric_model_type = self.list_model_type.index(self.model_type) + 1

        # store entity values in database
        premodel_settings = self.premodel_data['data']['settings']
        premodel_entity = {
            'title': premodel_settings.get('session_name', None),
            'model_type': numeric_model_type,
            'uid': self.uid,
        }
        db_save = Save_Entity(premodel_entity, session_type)

        # save dataset element
        db_return = db_save.save()

        # return
        if db_return['status']:
            return {'status': True, 'error': None, 'id': db_return['id']}
        else:
            self.list_error.append(db_return['error'])
            return {'status': False, 'error': self.list_error}
