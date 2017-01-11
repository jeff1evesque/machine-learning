#!/usr/bin/python

'''@model_generate

This file receives data (i.e. settings) required to query from the database,
a previously stored session, involving one or more stored dataset uploads, and
generates a corresponding model, respectively. The new model, is then stored
into respective database table(s), which later can be retrieved within
'model_predict.py'.

'''

from brain.session.base import Base
from brain.database.retrieve_feature import Retrieve_Feature
from brain.session.model.sv import sv_model


class Model_Generate(Base):
    '''@Model_Generate

    This class provides an interface to generate a corresponding model, within
    a NoSQL datastore.
    Note: inherit base methods from superclass 'Base'

    '''

    def __init__(self, premodel_data):
        '''@__init__

        This constructor is responsible for defining class variables, using the
        superclass 'Base' constructor, along with the
        constructor in this subclass.

        @super(), implement 'Base', and 'Base_Data' superclass constructor
            within this child class constructor.

        Note: the superclass constructor expects the same 'premodel_data'
              argument.

        '''

        super(Model_Generate, self).__init__(premodel_data)
        self.kernel = str(premodel_data['data']['settings']['sv_kernel_type'])
        self.session_id = premodel_data['data']['settings']['session_id']
        self.feature_request = Retrieve_Feature()
        self.list_error = []

    def generate_model(self):
        '''@generate_model

        This method generates a corresponding model, using a chosen dataset
        from the SQL database. The resulting model is stored into a NoSQL
        datastore.

        '''

        # local variables
        result = None
        model_type = self.premodel_data['data']['settings']['model_type']

        # case 1: svm model, or svr model
        if (model_type == 'svm') or (model_type == 'svr'):
            result = sv_model(
                model_type,
                self.kernel,
                self.session_id,
                self.feature_request,
                self.list_error
            )

        # store any errors
        if result and result['error']:
            self.list_error.extend(result['error'])

    def return_error(self):
        '''@return_error

        This method returns all errors corresponding to this class instance.

        '''

        return self.list_error
