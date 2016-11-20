#!/usr/bin/python

'''@retrieve_account

This file retrieves user account values.

'''

from flask import current_app
from brain.database.db_query import SQL


class Retrieve_Account(object):
    '''
    @Retrieve_Username

    This class provides an interface to check if a username already exists,
    and retrieves the corresponding password.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''@__init__

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')

    def check_username(self, username):
        '''@check_username

        This method checks if the supplied username already exists.

        '''

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT * '\
            'FROM tbl_user '\
            'WHERE username=%s'
        args = (username)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result']}


    def check_email(self, email):
        '''@get_email

        This method checks if the supplied email already exists.

        '''

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT * '\
            'FROM tbl_user '\
            'WHERE email=%s'
        args = (email)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result'][0][0]}


    def get_password(self, username):
        '''@get_password

        This method returns the hashed password for a supplied username.

        '''

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT password '\
            'FROM tbl_user '\
            'WHERE username=%s'
        args = (username)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result'][0][0]}
