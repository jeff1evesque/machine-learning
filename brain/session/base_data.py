#!/usr/bin/python

'''

This file serves as the superclass for 'data_xx.py' files.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.session.base import Base
from flask import current_app, session
from brain.session.data.arbiter import save_info
from brain.session.data.dataset import save_dataset, dataset2dict
from brain.database.dataset import save_collection


class BaseData(Base):
    '''

    This class provides an interface to save, and validate the provided
    dataset, into logical ordering within the sql database.

    @self.uid, the logged-in user (i.e. userid).

    Note: this class is invoked within 'data_xx.py'.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data):
        '''

        This constructor inherits additional class properties, from the
        constructor of the 'Base' superclass.

        @self.uid, the logged-in user (i.e. userid).

        '''

        # superclass constructor
        Base.__init__(self, premodel_data)

        # class variable
        self.list_error = []
        self.dataset = []
        self.model_type = premodel_data['data']['settings']['model_type']
        self.premodel_data = premodel_data

        if 'uid' in session:
            self.uid = session['uid']
        else:
            self.uid = current_app.config.get('USER_ID')

    def validate_id(self, session_id):
        '''

        This method validates if the session id, is a positive integer.

        '''

        error = '\'session_id\' ' + str(session_id) + ' not a positive integer'

        try:
            if not int(session_id) > 0:
                self.list_error.append(error)
        except Exception, error:
            self.list_error.append(str(error))

    def save_entity(self, session_type):
        '''

        This method saves the current entity into the database, then returns
        the corresponding entity id.

        '''

        # save entity description
        response = save_info(self.premodel_data, session_type, self.uid)

        # return result
        if response['error']:
            self.list_error.append(response['error'])
            return {'status': False, 'id': None, 'error': response['error']}
        else:
            return {'status': True, 'id': response['id'], 'error': None}

    def save_premodel_dataset(self):
        '''

        This method saves the entire the dataset collection, as a json
        document, into the nosql implementation.

        '''

        # save dataset
        cursor = Collection()
        response = cursor.query('insert_one', self.dataset)

        # return result
        if response['error']:
            self.list_error.append(response['error'])
            return {'result': None, 'error': response['error']}

        else:
            return {'result': response['result'], error: None}

    def convert_dataset(self, id_entity):
        '''

        This method converts the supplied csv, or xml file upload(s) to a
            uniform dict object.

        '''

        # convert to dictionary
        response = dataset2dict(id_entity, self.model_type, self.premodel_data)

        # return result
        if response['error']:
            self.list_error.append(response['error'])
        else:
            self.dataset = response['dataset']

    def get_errors(self):
        '''

        This method gets all current errors. associated with this class
        instance.

        '''

        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
