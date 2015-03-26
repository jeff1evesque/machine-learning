#!/usr/bin/python

## @save_size.py
#  This file saves the number of features that can be expected in a given
#      observation with respect to 'id_entity'.
from brain.database.db_query import SQL

## Class: Save_Size, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Save_Size(object):

    ## constructor:
    def __init__(self, svm_data):
        # class variables
        self.svm_data   = svm_data
        self.list_error = []
        self.sql        = SQL()

    ## save: store the number of features that can be expected in a given observation
    #
    #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s'
    #      is used for argument substitution.
    def save(self):
        # insert / update dataset value(s)
        self.sql.sql_connect('db_machine_learning')
        sql_statement  = 'INSERT INTO tbl_dataset_value (id_entity, count_features) VALUES(%s, %s)'
        args          = (self.svm_data['id_entity'], self.svm_data['count_features'])
        response      = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.return_error()
        self.sql.sql_disconnect()

        # return result
        if response: return {'status': False, 'error': response_error, 'id': response['id']}
        else: return {'status': True, 'error': None, 'id': response['id']}
