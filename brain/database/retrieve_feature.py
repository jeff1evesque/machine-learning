#!/usr/bin/python

'''

This file retrieves feature characteristics.

'''

from flask import current_app
from brain.database.db_query import SQL


class Retrieve_Feature(object):
    '''

    This class provides an interface to retrieve corresponding dataset(s),
    using a fixed supplied 'id_entity'.  The 'id_entity' is a reference,
    indicating which dataset to get.

    Note: this class is invoked within 'model_generate.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')

    def get_dataset(self, id_entity, model):
        '''

        This method retrieves a correspondinng dataset, from corresponding
        'EAV data model' database table(s), using a fixed 'id_entity'.

        @id_entity, this supplied argument corresponds to the 'id_entity'
            column from the 'tbl_dataset_value' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        @model, is the model type (i.e. svm, svr)

        '''

        # local variables
        list_model_type = current_app.config.get('MODEL_TYPE')

        # establish connection
        self.sql.sql_connect(self.db_ml)

        # case 1: svm data
        if model == list_model_type[0]:
            sql_statement = 'SELECT dep_variable_label, '\
                'indep_variable_label, indep_variable_value '\
                'FROM tbl_svm_data '\
                'WHERE id_entity=%s'

        # case 2: svr data
        elif model == list_model_type[1]:
            sql_statement = 'SELECT criterion, indep_variable_label, '\
                'indep_variable_value '\
                'FROM tbl_svr_data '\
                'WHERE id_entity=%s'

        # get dataset
        args = (id_entity)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {
                'status': False,
                'error': response_error,
                'result': None
            }
        else:
            return {
                'status': True,
                'error': None,
                'result': response['result'],
            }

    def get_count(self, id_entity):
        '''

        This method retrieves the number of features that can be expected in
        any given observation, from a particular dataset instance (id_entity).

        @id_entity, this supplied argument corresponds to the 'id_entity'
            column from the 'tbl_dataset_value' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.
        '''

        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT count_features '\
            'FROM tbl_feature_count '\
            'WHERE id_entity=%s'
        args = (id_entity)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {
                'status': False,
                'error': response_error,
                'result': None
            }
        else:
            return {
                'status': True,
                'error': None,
                'result': response['result'],
            }
