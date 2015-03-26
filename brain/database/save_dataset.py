#!/usr/bin/python

## @save_dataset.py
#  This file saves SVM related data into corresponding 'EAV data model' database
#      table(s), from the 'db_machine_learning' database.
from brain.database.db_query import SQL

## Class: Save_Dataset, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Save_Dataset(object):

    ## constructor: stores an SVM dataset (python dict), database configurations
    #               into their own corresponding class variable.
    # 
    #  Note: during the SVM dataset instance, 'self.svm_data' is a list of dictionary
    #        elements. One dictionary element, is represented as follows:
    #
    #            {'svm_dataset': {'dep_variable_label': 'yyy',
    #                               'indep_variable_label': 'yyy',
    #                               'indep_variable_value': zz.zz}},
    def __init__(self, svm_data, session_type):
        # class variables
        self.svm_data     = svm_data
        self.session_type = session_type
        self.list_error   = []
        self.sql          = SQL()

    ## save: store, or update SVM dataset(s) into corresponding 'EAV data model'
    #        database table(s).
    #
    #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s'
    #      is used for argument substitution.
    #
    #  Note: 'UTC_TIMESTAMP' returns the universal UTC datetime
    def save(self):
        # insert / update dataset value(s)
        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'INSERT INTO tbl_dataset_value (id_entity, dep_variable_label, indep_variable_label, indep_variable_value) VALUES(%s, %s, %s, %s)'
        dataset       = self.svm_data['svm_dataset']
        args          = (self.svm_data['id_entity'], dataset['dep_variable_label'], dataset['indep_variable_label'], dataset['indep_variable_value'])
        response      = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.return_error()
        self.sql.sql_disconnect()

        # return result
        if response_error: return {'status': False, 'error': response_error, 'id': response['id']}
        else: return {'status': True, 'error': None, 'id': response['id']}
