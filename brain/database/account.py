#!/usr/bin/python

'''

This file queries the user account information.

'''

from flask import current_app
from brain.database.query import SQL


class Account(object):
    '''

    This class provides an interface to the users account.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('SQL_ML')

    def save_account(self, username, email, password):
        '''

        This method stores a user account, along with their corresponding
        password into an 'EAV data model' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        '''

        # insert / update dataset entity value
        self.sql.connect(self.db_ml)

        sql_statement = 'INSERT INTO tbl_user '\
            '(username, email, password, datetime_joined) '\
            'VALUES(%s, %s, %s, UTC_TIMESTAMP())'
        args = (username, email, password)
        response = self.sql.execute('insert', sql_statement, args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error}
        else:
            return {'status': True, 'error': None, 'id': response['id']}

    def check_username(self, username):
        '''

        This method checks if the supplied username already exists.

        '''

        # select dataset
        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT * '\
            'FROM tbl_user '\
            'WHERE username=%s'
        args = (username)
        response = self.sql.execute('select', sql_statement, args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result']}

    def check_email(self, email):
        '''

        This method checks if the supplied email already exists.

        '''

        # select dataset
        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT * '\
            'FROM tbl_user '\
            'WHERE email=%s'
        args = (email)
        response = self.sql.execute('select', sql_statement, args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result']}

    def get_password(self, username):
        '''

        This method returns the hashed password for a supplied username.

        '''

        # select dataset
        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT password '\
            'FROM tbl_user '\
            'WHERE username=%s'
        args = (username)
        response = self.sql.execute('select', sql_statement, args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result'][0][0]}

    def get_uid(self, username):
        '''

        This method returns the userid (i.e uid) for a supplied username.

        '''

        # select dataset
        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT id_user '\
            'FROM tbl_user '\
            'WHERE username=%s'
        args = (username)
        response = self.sql.execute('select', sql_statement, args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result'][0][0]}
