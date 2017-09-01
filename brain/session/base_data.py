#!/usr/bin/python

'''

This file serves as the superclass for 'data_xx.py' files.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

import datetime
from brain.session.base import Base
from flask import current_app, session
from brain.session.data.dataset import dataset2dict
from brain.database.dataset import Collection
from brain.database.entity import Entity


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
        self.model_type = premodel_data['properties']['model_type']
        self.premodel_data = premodel_data

        if 'uid' in session:
            self.uid = session['uid']
            self.max_collection = current_app.config.get('MAXCOL_AUTH')
            self.max_document = current_app.config.get('MAXDOC_AUTH')

        else:
            self.uid = current_app.config.get('USER_ID')
            self.max_collection = current_app.config.get('MAXCOL_ANON')
            self.max_document = current_app.config.get('MAXDOC_ANON')

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

    def save_premodel_dataset(self):
        '''

        This method saves the entire the dataset collection, as a json
        document, into the nosql implementation.

        '''

        # local variables
        entity = Entity()
        cursor = Collection()
        collection = self.premodel_data['properties']['collection']
        collection_adjusted = collection.lower().replace(' ', '_')
        collection_count = entity.get_collection_count(self.uid)
        document_count = cursor.query(collection_adjusted, 'count_documents')

        # enfore collection limit for anonymous users
        if (
            not self.uid and
            collection_count and
            collection_count['result'] >= self.max_collection and
            collection_adjusted
        ):
            cursor.query(collection_adjusted, 'drop_collection')

        # save dataset
        if (
            collection_adjusted and
            collection_count and
            collection_count['result'] < self.max_collection and
            document_count and
            document_count['result'] < self.max_document
        ):
            current_utc = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            self.premodel_data['properties']['datetime_saved'] = current_utc
            self.premodel_data['properties']['uid'] = self.uid
            document = {
                'properties': self.premodel_data['properties'],
                'dataset': self.dataset
            }

            response = cursor.query(
                collection_adjusted,
                'insert_one',
                document
            )

        else:
            response = None

        # return result
        if response and response['error']:
            self.list_error.append(response['error'])
            return {'result': None, 'error': response['error']}

        elif response and response['result']:
            return {'result': response['result'], 'error': None}

        else:
            return {'result': None, 'error': 'no dataset provided'}

    def convert_dataset(self):
        '''

        This method converts the supplied csv, or xml file upload(s) to a
            uniform dict object.

        '''

        # convert to dictionary
        response = dataset2dict(self.model_type, self.premodel_data)

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
