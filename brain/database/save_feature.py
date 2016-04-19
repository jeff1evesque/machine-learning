#!/usr/bin/python

'''@save_feature

This file saves the feature count, as well as the feature instances within
corresponding database tables.

'''

from brain.database.db_query import SQL


class Save_Feature(object):
    '''@Save_Feature

    This class provides an interface to store the expected number of features
    that can be expected in a given dataset, and each feature instance into
    corresponding database tables (using EAV data model).

    Note: this class is invoked within 'base_data.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, svm_data):
        '''@__init__

        This constructor is responsible for defining class variables.

        '''

        self.svm_data = svm_data
        self.list_error = []
        self.sql = SQL()

    def save_count(self):
        '''@save_count

        This method stores the number of features that can be expected in a
        given observation.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        '''

        # insert / update dataset value(s)
        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'INSERT INTO tbl_feature_count (id_entity, '\
            'count_features) VALUES(%s, %s)'
        args = (
            self.svm_data['id_entity'],
            self.svm_data['count_features'],
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

    def save_feature(self):
        '''@save_feature

        This method can store, or update an existing SVM dataset stored in
        corresponding database tables (using EAV data model).

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        Note: 'UTC_TIMESTAMP' returns the universal UTC datetime

        '''

        # insert / update dataset value(s)
        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'INSERT INTO tbl_feature_value (id_entity, '\
            'dep_variable_label, indep_variable_label, indep_variable_value) '\
            'VALUES(%s, %s, %s, %s)'
        dataset = self.svm_data['svm_dataset']
        args = (
            self.svm_data['id_entity'],
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
