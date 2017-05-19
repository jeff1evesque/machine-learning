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

    def connect(self, database, collection):
        '''

        This method is responsible for defining the necessary interface to
        connect to a NoSQL database.

        '''

        try:
            self.client = MongoClient(self.host + ',' + self.port)
            self.database = self.client[database]
            self.collection = self.database[collection]

            return {
                'status': True,
                'error': None,
            }

        except MongoClient.errors, error:
            self.proceed = False
            self.list_error.append(error)

            return {
                'status': False,
                'error': self.list_error,
            }

    def execute(self, operation, payload):
        '''

        This method is responsible for defining the necessary interface to
        perform NoSQL commands.

        Note: collection level operations can be further reviewed:

          - http://api.mongodb.com/python/current/api/pymongo/collection.html

        '''

        if self.proceed:
            try:
                collection = self.collection

                if operation == 'insert_one':
                    result = collection.dataset.insert_one(payload)
                if operation == 'insert_many':
                    result = collection.insert_many(payload)
                elif operation == 'update_one':
                    result = collection.update_one(payload)
                elif operation == 'update_many':
                    result = collection.update_many(payload)
                elif operation == 'delete_one':
                    result = collection.delete_one(payload)
                elif operation == 'delete_many':
                    result = collection.delete_many(payload)
                elif operation == 'find':
                    result = collection.find(payload)
                elif operation == 'find_one':
                    result = collection.find_one(payload)
                elif operation == 'map_reduce':
                    result = collection.map_reduce(
                        payload['map'],
                        payload['reduce'],
                        payload['out'],
                        payload['full_response'],
                        payload['kwargs']
                    )
                elif operation == 'delete_one':
                    result = collection.delete_one(payload)
                elif operation == 'delete_many':
                    result = collection.delete_many(payload)
                elif operation == 'drop_collection':
                    result = collection.drop_collection(payload)

            except db.Error, error:
                self.list_error.append(error)

                return {
                    'status': False,
                    'result': result,
                    'error': self.list_error,
                }

            return {'status': True, 'result': result, 'error': None}

    def disconnect(self):
        '''

        This method is responsible for defining the necessary interface to
        disconnect from a NoSQL database.

        '''

        if self.proceed:
            try:
                self.client.disconnect()

                return {
                    'status': True,
                    'error': None,
                }

            except MongoClient.errors, error:
                self.list_error.append(error)

                return {
                    'status': False,
                    'error': self.list_error,
                }

    def get_errors(self):
        '''

        This method returns all errors pertaining to the instantiated class.

        '''

        return self.list_error


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

    def execute(self, operation, statement, sql_args=None):
        '''

        This method is responsible for defining the necessary interface to
        perform SQL commands.

        @sql_args, is a tuple used for argument substitution with the supplied
            'statement'.

        '''

        if self.proceed:
            try:
                self.cursor.execute(statement, sql_args)

                # commit change(s), return lastrowid
                if operation in ['insert', 'delete', 'update']:
                    self.conn.commit()
                # fetch all the rows, return as list of lists.
                elif operation == 'select':
                    result = self.cursor.fetchall()

            except MariaClient.Error, error:
                self.conn.rollback()
                self.list_error.append(error)
                return {
                    'status': False,
                    'error': self.list_error,
                    'result': None,
                }

        if operation in ['insert', 'delete', 'update']:
            return {
                'status': True,
                'error': self.list_error,
                'id': self.cursor.lastrowid,
            }
        elif operation == 'select':
            return {
                'status': True,
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
