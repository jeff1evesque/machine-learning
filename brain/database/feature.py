#!/usr/bin/python

'''

This file saves the feature count, as well as the feature instances within
corresponding database tables.

'''

from flask import current_apps
from brain.database.query import SQL


class Feature(object):
    '''

    This class provides an interface to retrieve, and store the expected
    number of features that can be expected in a given dataset, and each
    feature instance into corresponding database tables (using EAV data
    model).

    Note: this class is invoked within 'base_data.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data=None):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.premodel_data = premodel_data
        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')
        self.classification = current_app.config.get('MODEL_TYPE')[0]
        self.regression = current_app.config.get('MODEL_TYPE')[1]

    def save_count(self):
        '''

        This method stores the number of features that can be expected in a
        given observation.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        '''

        # insert / update dataset value(s)
        self.sql.connect(self.db_ml)
        sql_statement = 'INSERT INTO tbl_feature_count (id_entity, '\
            'count_features) VALUES(%s, %s)'
        args = (
            self.premodel_data['id_entity'],
            self.premodel_data['count_features'],
        )
        response = self.sql.execute(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error}
        else:
            return {'status': True, 'error': None, 'id': response['id']}

    def save_feature(self, model_type):
        '''

        This method can store, or update an existing SVM dataset stored in
        corresponding database tables (using EAV data model).

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        Note: 'UTC_TIMESTAMP' returns the universal UTC datetime

        '''

        # insert / update dataset value(s)
        self.sql.connect(self.db_ml)
        if model_type == self.classification:
            sql_statement = 'INSERT INTO tbl_svm_data (id_entity, '\
                'dep_variable_label, indep_variable_label, '\
                'indep_variable_value) VALUES(%s, %s, %s, %s)'
        elif model_type == self.regression:
            sql_statement = 'INSERT INTO tbl_svr_data (id_entity, '\
                'criterion, indep_variable_label, indep_variable_value) '\
                'VALUES(%s, %s, %s, %s)'
        dataset = self.premodel_data['premodel_dataset']
        args = (
            self.premodel_data['id_entity'],
            dataset['dep_variable_label'],
            dataset['indep_variable_label'],
            dataset['indep_variable_value'],
        )
        response = self.sql.execute(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error}
        else:
            return {'status': True, 'error': None, 'id': response['id']}

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
        response = self.sql.execute(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

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
        response = self.sql.execute(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

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
