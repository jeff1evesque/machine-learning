#!/usr/bin/python

'''

This file retrieves the 'session_name', and 'id_entity' properties.

'''

from flask import current_app
from brain.database.query import SQL


class Session(object):
    '''

    This class provides an interface to retrieve the 'session_name', and
    'id_entity' from the 'tbl_dataset_entity' sql database table.

    Note: this class is invoked within 'views.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('SQL_ML')

    def get_all_sessions(self):
        '''

        This method is responsible for retrieving all sessions from the
        'tbl_dataset_entity' sql database table.

        '''

        # local variables
        list_session = []

        # sql query
        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT id_entity, title FROM tbl_dataset_entity'
        response = self.sql.execute('select', sql_statement)

        # rebuild session list, get error(s) if any
        if response['result']:
            for item in response['result']:
                list_session.append({'id': item[0], 'title': item[1]})
            response_error = self.sql.get_errors()
        else:
            response_error = 'no previous session found in database'

        # disconnect from database
        self.sql.disconnect()

        # return result
        if response_error:
            return {'result': None, 'error': response_error}
        else:
            return {'result': list_session, 'error': None}
