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
            return {'error': None, 'result': response['result']}

    def get_email(self, username):
        '''@get_email

        This method returns an email for a supplied username.

        '''

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT email '\
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


    def get_user(self, id):
        '''@get_user

        Takes a unicode id (eg. u'1') and returns a dict containing enough
        info to build a `User` object.
        '''
        print("Got {} of type {}".format(id, type(id)))

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT id_user, username, email '\
            'FROM tbl_user '\
            'WHERE id_user=%s'
        args = (int(id))
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        print("Results: {}".format(response["result"]))

        # return result
        if response_error:
            print("Got Error, returning None")
            return {'error': response_error, 'result': None}

        print("Len of results: {}".format(len(response["result"])))

        # No errors-- but do we have a single user returned?
        if response['result'] and len(response['result']) == 1:
            user_row = response['result'][0]
            print("Looks good-- returning no errors and user info")
            return {
                'error': None,
                'result': {
                    'uid': user_row[0],
                    'username': user_row[1],
                    'email': user_row[2],
                }
            }
        else:
            print("Results empty or too many, returning None")
            return {'error': None, 'result': None}



    def get_uid(self, username):
        '''@get_uid

        This method returns the userid (i.e uid) for a supplied username.

        '''

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT id_user '\
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

    def get_username(self, uid):
        '''@get_uid

        This method returns the username for a user id (i.e uid).

        '''

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT username '\
            'FROM tbl_user '\
            'WHERE id_user=%s'
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
