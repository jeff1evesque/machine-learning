#!/usr/bin/python

## @retrieve_session.py
#  This file queries, and returns 'svm_title', and 'id_entity from the
#      'tbl_dataset_entity' database table of 'db_machine_learning'.
from brain.database.db_query import SQL

## Class: Retrieve_Session, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'views.py'
class Retrieve_Session(object):

    ## constructor:
    def __init__(self):
        self.list_error = []
        self.sql        = SQL()

    ## get_all_sessions: get all sessions from 'tbl_dataset_entity'
    def get_all_sessions(self):
        # local variables
        list_session = []

        # sql query
        self.sql.sql_connect('db_machine_learning')
        sql_statement  = 'SELECT id_entity, title FROM tbl_dataset_entity'
        response       = self.sql.sql_command(sql_statement, 'select')

        # rebuild session list
        for item in response['result']:
            list_session.append({'id': item[0], 'title': item[1]})

        # retrieve any error(s), disconnect from database
        response_error = self.sql.return_error()
        self.sql.sql_disconnect()

        # return result
        if response_error: return {'result': None, 'error': response_error}
        else: return {'result': list_session, 'error': None}
