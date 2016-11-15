#!/usr/bin/python

'''@save_account

This file saves a user account during registration.

'''

from flask import current_app
from brain.database.db_query import SQL


class Save_Account(object):
    '''@Save_Account

    This class provides an interface to save a username, and their
    corresponding password.
    

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''@__init__

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')

    def save_account(self, username, email, password):
        '''@save_account

        This method stores a user account, along with their corresponding
        password into an 'EAV data model' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        '''

        # insert / update dataset entity value
        self.sql.sql_connect(self.db_ml)

        sql_statement = 'INSERT INTO tbl_user '\
            '(username, email, password, datetime_joined) '\
            'VALUES(%s, %s, %s, UTC_TIMESTAMP())'
        args = (username, email, password)
        response = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error}
        else:
            return {'status': True, 'error': None, 'id': response['id']}
