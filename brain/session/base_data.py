#!/usr/bin/python

'''@base_data

This file serves as the superclass for 'data_xx.py' files.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.session.base import Base
from flask import current_app
from flask import session
from brain.session.data.save_feature_count import feature_count
from brain.session.data.validate_file_extension import reduce_dataset
from brain.session.data.save_entity import entity
from brain.session.data.save_dataset import dataset
from brain.session.data.save_observation_label import observation_label
from brain.session.data.dataset_to_dict import dataset_dictionary


class Base_Data(Base):
    '''@Base_Data

    This class provides an interface to save, and validate the provided
    dataset, into logical ordering within the sql database.

    @self.uid, the logged-in user (i.e. userid).

    Note: this class is invoked within 'data_xx.py'.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data):
        '''@__init__

        This constructor inherits additional class properties, from the
        constructor of the 'Base' superclass.

        @self.uid, the logged-in user (i.e. userid).

        '''

        # superclass constructor
        Base.__init__(self, premodel_data)

        # class variable
        self.observation_labels = []
        self.list_error = []
        self.dataset = []
        self.model_type = premodel_data['data']['settings']['model_type']

        if 'uid' in session:
            self.uid = session['uid']
        else:
            self.uid = current_app.config.get('USER_ID')

    def save_feature_count(self):
        '''@save_feature_count

        This method saves the number of features that can be expected in a
        given observation with respect to 'id_entity'.

        Note: this method needs to execute after 'dataset_to_dict'

        '''

        # save feature count
        response = feature_count(self.dataset[0])

        # return result
        if response['error']:
            self.list_error.append(response['error'])

    def validate_file_extension(self):
        '''@validate_file_extension

        This method validates the file extension for each uploaded dataset,
        and returns the unique (non-duplicate) dataset.

        @self.session_type, defined from 'base.py' superclass.

        '''

        # validate and reduce dataset
        response = reduce_dataset(self.premodel_data, self.session_type)

        # return result
        if response['error']:
            self.list_error.append(response['error'])
        else:
            self.upload = response['dataset']

    def validate_id(self, session_id):
        '''@validate_id

        This method validates if the session id, is a positive integer.

        '''

        error = '\'session_id\' ' + str(session_id) + ' not a positive integer'

        try:
            if not int(session_id) > 0:
                self.list_error.append(error)
        except Exception, error:
            self.list_error.append(str(error))

    def save_entity(self, session_type):
        '''@save_entity

        This method saves the current entity into the database, then returns
        the corresponding entity id.

        '''

        # save entity description
        response = entity(self.premodel_data, session_type, self.uid)

        # return result
        if response['error']:
            self.list_error.append(response['error'])
            return {'status': False, 'id': None, 'error': response['error']}
        else:
            return {'status': True, 'id': response['id'], 'error': None}

    def save_premodel_dataset(self):
        '''@save_premodel_dataset

        This method saves each dataset element (independent variable value)
        into the sql database.

        @self.dataset, defined from the 'dataset_to_dict' method.

        '''

        # save dataset
        response = dataset(self.dataset, self.model_type)

        # return result
        if response['error']:
            self.list_error.append(response['error'])

    def save_observation_label(self, session_type, session_id):
        '''save_observation_label

        This method saves the list of unique independent variable labels,
        which can be expected in any given observation, into the sql
        database. This list of labels, is predicated on a supplied session
        id (entity id).

        @self.observation_labels, list of features (independent variables),
            defined after invoking the 'dataset_to_dict' method.

        @session_id, the corresponding returned session id from invoking the
            'save_entity' method.

        '''

        # save observation labels
        response = observation_label(
            session_type,
            session_id,
            self.observation_labels[0],
            self.premodel_data['data']['dataset']['file_upload']
        )

        # return result
        if response['error']:
            self.list_error.append(response['error'])

    def dataset_to_dict(self, id_entity):
        '''@dataset_to_dict

        This method converts the supplied csv, or xml file upload(s) to a
            uniform dict object.

        @self.upload, defined from 'validate_file_extension'.

        '''

        # convert to dictionary
        response = dataset_dictionary(id_entity, self.model_type, self.upload)

        # return result
        if response['error']:
            self.list_error.append(response['error'])
        else:
            self.observation_labels.append(response['observation_labels'])
            self.dataset = response['dataset']

    def get_errors(self):
        '''get_errors

        This method gets all current errors. associated with this class
        instance.

        '''

        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
