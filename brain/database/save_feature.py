#!/usr/bin/python

## @save_feature.py
#  This file saves the number of features that can be expected in a given
#      observation with respect to 'id_entity'.
from brain.database.db_query import SQL

## Class: Save_Feature, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Save_Feature(object):

    ## constructor:
    def __init__(self, svm_data):
        # class variables
        self.svm_data   = svm_data
        self.list_error = []
        self.sql        = SQL()

    ## save_count: store the number of features that can be expected in a given
    #              observation.
    #
    #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s'
    #      is used for argument substitution.
    def save_count(self):
        # insert / update dataset value(s)
        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'INSERT INTO tbl_feature_count (id_entity, count_features) VALUES(%s, %s)'
        args          = (self.svm_data['id_entity'], self.svm_data['count_features'])
        response      = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error: return {'status': False, 'error': response_error}
        else: return {'status': True, 'error': None, 'id': response['id']}

    ## save_feature: store, or update SVM dataset(s) into corresponding 'EAV data model'
    #                database table(s).
    #
    #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s'
    #      is used for argument substitution.
    #
    #  Note: 'UTC_TIMESTAMP' returns the universal UTC datetime
    def save_feature(self):
        # insert / update dataset value(s)
        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'INSERT INTO tbl_dataset_value (id_entity, dep_variable_label, indep_variable_label, indep_variable_value) VALUES(%s, %s, %s, %s)'
        dataset       = self.svm_data['svm_dataset']
        args          = (self.svm_data['id_entity'], dataset['dep_variable_label'], dataset['indep_variable_label'], dataset['indep_variable_value'])
        response      = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error: return {'status': False, 'error': response_error}
        else: return {'status': True, 'error': None, 'id': response['id']}
