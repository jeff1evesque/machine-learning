#!/usr/bin/python

'''

This file saves the feature count, as well as the feature instances within
corresponding database tables.

'''

from flask import current_app
from brain.database.db_query import SQL


class Save_Feature(object):
    '''

    This class provides an interface to store the expected number of features
    that can be expected in a given dataset, and each feature instance into
    corresponding database tables (using EAV data model).

    Note: this class is invoked within 'base_data.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data):
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
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'INSERT INTO tbl_feature_count (id_entity, '\
            'count_features) VALUES(%s, %s)'
        args = (
            self.premodel_data['id_entity'],
            self.premodel_data['count_features'],
        )
        response = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

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
        self.sql.sql_connect(self.db_ml)
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
        response = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error}
        else:
            return {'status': True, 'error': None, 'id': response['id']}
