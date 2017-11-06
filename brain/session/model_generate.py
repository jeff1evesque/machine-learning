#!/usr/bin/python

'''

This file receives data (i.e. settings) required to query from the database,
a previously stored session, involving one or more stored dataset uploads, and
generates a corresponding model, respectively. The new model, is then stored
into respective database table(s), which later can be retrieved within
'model_predict.py'.

'''

from brain.session.base import Base
from brain.session.model.sv import generate
from brain.session.model.bagger import baggen
from flask import current_app

class ModelGenerate(Base):
    '''

    This class provides an interface to generate a corresponding model, within
    a NoSQL datastore.

    Note: inherit base methods from superclass 'Base'

    '''

    def __init__(self, premodel_data):
        '''

        This constructor is responsible for defining class variables, using the
        superclass 'Base' constructor, along with the constructor in this
        subclass.

        @super(), implement 'Base', and 'BaseData' superclass constructor
            within this child class constructor.

        Note: the superclass constructor expects the same 'premodel_data'
              argument.

        '''

        super(ModelGenerate, self).__init__(premodel_data)
        self.list_error = []

    def generate_model(self):
        '''

        This method generates a corresponding model, using a chosen dataset
        from the SQL database. The resulting model is stored into a NoSQL
        datastore.

        '''

        # local variables
        result = None
        premodel_settings = self.premodel_data['properties']
        model_type = self.premodel_data['properties']['model_type']
        self.collection = premodel_settings['collection']
        payload = [{'$project': {'dataset': 1}}]

        # case 1: svm model, or svr model
        if (model_type == 'svm') or (model_type == 'svr'):
            kernel = str(premodel_settings['sv_kernel_type'])
            result = generate(
                model_type,
                kernel,
                self.collection,
                payload,
                self.list_error
            )

        # case 2: ensemble bagger
        if model_type == 'bagc':
            rand = current_app.config.get('RANDOM_STATE')
            rand = None if rand == 'None' else rand
            result = baggen(
                model_type,
                self.collection,
                payload,
                self.list_error,
                random_state=rand
            )

        # store any errors
        if result and result['error']:
            self.list_error.extend(result['error'])

    def return_error(self):
        '''

        This method returns all errors corresponding to this class instance.

        '''

        return self.list_error
