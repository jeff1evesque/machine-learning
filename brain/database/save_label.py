#!/usr/bin/python

## @save_label.py
#  This file saves SVM related data into corresponding 'EAV data model' database
#      table(s), from the 'db_machine_learning' database.
from brain.database.db_query import SQL

## Class: Save_Label, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'data_new.py'
class Save_Label(object):

    ## constructor: stores an SVM label (python dict), database configurations
    #               into their own corresponding class variable.
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
        # insert / update feature label(s)
        self.sql.sql_connect('db_machine_learning')

        # add labels (append case)
        if self.session_type in ['data_append', 'data_new']:

            # check if observation label exists in database
            sql_statement = 'SELECT * FROM tbl_observation_label WHERE dep_variable_label=%s AND id_entity=%s'
            args          = (self.svm_data['label'], self.svm_data['id_entity'])
            response      = self.sql.sql_command(sql_statement, 'select', args)

            # add labels if not exist
            if not response['result']:
                sql_statement  = 'INSERT INTO tbl_observation_label (id_entity, dep_variable_label) VALUES(%s, %s)'
                args           = (self.svm_data['id_entity'], self.svm_data['label'])
                response_added = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error: return {'status': False, 'error': response_error}
        else: return {'status': True, 'error': None}
