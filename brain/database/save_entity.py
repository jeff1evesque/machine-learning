#!/usr/bin/python

## @save_entity.py
#  This file saves SVM related entity into corresponding 'EAV data model' database
#      table(s), from the 'db_machine_learning' database.
from brain.database.db_query import SQL

## Class: Save_Entity, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py', and 'data_append.py'
class Save_Entity(object):

    ## constructor: stores an SVM entity (python dict), database configurations
    #               into their own corresponding class variable.
    #
    #  Note: during the SVM entity instance, 'self.svm_data' is a dictionary with the
    #        following elements:
    #
    #            {'uid': xx, 'id_entity': xx, 'title': yyy}
    #
    #        where 'xx' denotes an integer value, 'yyy' a unicode string, and 'zz'
    #        representing a float value.
    def __init__(self, svm_data, session_type):
        # class variables
        self.svm_data     = svm_data
        self.session_type = session_type
        self.list_error   = []
        self.sql          = SQL()

    ## save: store, or update SVM entity into corresponding 'EAV data model'
    #        database table.
    #
    #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s'
    #      is used for argument substitution.
    #
    #  Note: 'UTC_TIMESTAMP' returns the universal UTC datetime
    def save(self):
        # insert / update dataset entity value
        self.sql.sql_connect('db_machine_learning')

        if self.session_type == 'data_append':
            sql_statement = 'UPDATE tbl_dataset_entity SET uid_modified=%s, datetime_modified=UTC_TIMESTAMP() WHERE id_entity=%s'
            args          = (self.svm_data['uid'], self.svm_data['id_entity'])
            response      = self.sql.sql_command(sql_statement, 'update', args)

        elif self.session_type == 'data_new':
            sql_statement = 'INSERT INTO tbl_dataset_entity (title, uid_created, datetime_created) VALUES(%s, %s, UTC_TIMESTAMP())'
            args          = (self.svm_data['title'], self.svm_data['uid'])
            response      = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error: return {'status': False, 'error': response_error}
        else: return {'status': True, 'error': None, 'id': response['id']}
