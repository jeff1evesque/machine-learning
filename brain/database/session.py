#!/usr/bin/python

'''

This file retrieves session related properties from the sql database.

'''

from flask import current_app
from brain.database.query import SQL


class Session:
    '''

    This class provides an interface to retrieve the 'id_entity', and
    'collection' from the 'tbl_dataset_entity' sql database table.

    Note: this class is invoked within 'views.py'

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('SQL_DB')

    def get_session_id(self, collection):
        '''

        This method is responsible for retrieving the 'session_id', given
        that the 'collection' is known.

        '''

        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT id_entity FROM tbl_dataset_entity '\
            'WHERE collection=%s'
        args = (collection,)
        response = self.sql.execute('select', sql_statement, args)

        # retrieve any error(s)
        response_error = self.sql.get_errors()

        # return result
        if response_error:
            return {'result': None, 'error': response_error}
        else:
            return {'result': response['result'][0][0], 'error': None}

    def get_all_collections(self):
        '''

        This method is responsible for retrieving all collections from the
        'tbl_dataset_entity' sql database table.

        '''

        # local variables
        list_session = []

        # sql query
        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT id_entity, collection FROM tbl_dataset_entity'
        response = self.sql.execute('select', sql_statement)

        # rebuild session list, get error(s) if any
        if response['result']:
            for item in response['result']:
                list_session.append({'id': item[0], 'collection': item[1]})
            response_error = self.sql.get_errors()
        else:
            response_error = 'no previous collection found in database'

        # return result
        if response_error:
            return {'result': None, 'error': response_error}
        else:
            return {'result': list_session, 'error': None}
