#!/usr/bin/python

'''

This file contains various SQL, and NoSql related methods.

'''

import MySQLdb as MariaClient
from pymongo import MongoClient
from brain.database.settings import Database


class NoSQL(object):
    '''

    This class provides an interface to connect, execute commands, and
    disconnect from a NoSQL database.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, host=None, user=None, passwd=None):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.settings = Database()

        # host address
        if host:
            self.host = host
        else:
            self.host = self.settings.get_db_host()

        # sql username for above host address
        if user:
            self.user = user
        else:
            self.user = self.settings.get_db_username()

        # sql password for above username
        if passwd:
            self.passwd = passwd
        else:
            self.passwd = self.settings.get_db_password()

    def connect(self):
        '''

        This method is responsible for defining the necessary interface to
        connect to a SQL database.

        '''

        self.client = MongoClient(self.host + ':' + self.port)

    def execute(self, sql_type, payload=None):
        '''

        This method is responsible for defining the necessary interface to
        perform NoSQL commands.

        @find, returns a cursor instance, which can be iterated over every
            matching document.
        @find_one, returns a single document, matching a query.
        @remove, removes a document entirely, or conditionally.
        @drop, removes an entire specified collection.

        Note: document(s) are inserted into a mongodb collection.

        '''

        db = self.client().ml_database

        if sql_type == 'insert':
            db.dataset.insert(payload)
        elif sql_type == 'save':
            db.dataset.save(payload)
        elif sql_type == 'update':
            db.dataset.update(payload)
        elif sql_type == 'find':
            db.dataset.find(payload)
        elif sql_type == 'find_one':
            db.dataset.find_one(payload)
        elif sql_type == 'remove':
            db.dataset.remove(payload)
        elif sql_type == 'drop':
            db.dataset.drop()

    def disconnect(self):
        '''

        This method is responsible for defining the necessary interface to
        disconnect from a NoSQL database.

        '''

        self.client.disconnect()


class SQL(object):
    '''

    This class provides an interface to connect, execute commands, and
    disconnect from a SQL database.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, host=None, user=None, passwd=None):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.settings = Database()
        self.list_error = []
        self.proceed = True

        # host address
        if host:
            self.host = host
        else:
            self.host = self.settings.get_db_host()

        # sql username for above host address
        if user:
            self.user = user
        else:
            self.user = self.settings.get_db_username()

        # sql password for above username
        if passwd:
            self.passwd = passwd
        else:
            self.passwd = self.settings.get_db_password()

    def connect(self, database=None):
        '''

        This method is responsible for defining the necessary interface to
        connect to a SQL database.

        '''

        try:
            if database is None:
                self.conn = MariaClient.connect(
                    self.host,
                    self.user,
                    self.passwd,
                )
            else:
                self.conn = MariaClient.connect(
                    self.host,
                    self.user,
                    self.passwd,
                    db=database,
                )
            self.cursor = self.conn.cursor()

            return {
                'status': True,
                'error': None,
                'id': None,
            }

        except MariaClient.Error, error:
            self.proceed = False
            self.list_error.append(error)

            return {
                'status': False,
                'error': self.list_error,
                'id': None,
            }

    def execute(self, sql_type, sql_statement, sql_args=None):
        '''

        This method is responsible for defining the necessary interface to
        perform SQL commands.

        @sql_args, is a tuple used for argument substitution with the supplied
            'sql_statement'.

        '''

        if self.proceed:
            try:
                self.cursor.execute(sql_statement, sql_args)

                # commit change(s), return lastrowid
                if sql_type in ['insert', 'delete', 'update']:
                    self.conn.commit()
                # fetch all the rows, return as list of lists.
                elif sql_type == 'select':
                    result = self.cursor.fetchall()

            except MariaClient.Error, error:
                self.conn.rollback()
                self.list_error.append(error)
                return {
                    'status': False,
                    'error': self.list_error,
                    'result': None,
                }

        if sql_type in ['insert', 'delete', 'update']:
            return {
                'status': False,
                'error': self.list_error,
                'id': self.cursor.lastrowid,
            }
        elif sql_type == 'select':
            return {
                'status': False,
                'error': self.list_error,
                'result': result,
            }

    def disconnect(self):
        '''

        This method is responsible for defining the necessary interface to
        disconnect from a SQL database.

        '''

        if self.proceed:
            try:
                if self.conn:
                    self.conn.close()

                    return {
                        'status': True,
                        'error': None,
                        'id': self.cursor.lastrowid,
                    }
            except MariaClient.Error, error:
                self.list_error.append(error)

                return {
                    'status': False,
                    'error': self.list_error,
                    'id': self.cursor.lastrowid,
                }

    def get_errors(self):
        '''

        This method returns all errors pertaining to the instantiated class.

        '''

        return self.list_error
