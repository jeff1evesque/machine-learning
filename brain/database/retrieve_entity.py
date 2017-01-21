#!/usr/bin/python

'''

This file retrieves dataset entity related properties.

'''

from flask import current_app
from brain.database.db_query import SQL


class Retrieve_Entity(object):
    '''

    This class provides an interface to get an SVM entity title, from the
    'tbl_dataset_entity' sql database table.

    Note: this class is invoked within 'model_generate.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')

    def get_title(self, id_entity):
        '''

        This method is responsible for retrieving an SVM entity title, from the
        SQL database, using a fixed 'id_entity'.

        @id_entity, this supplied argument corresponds to the 'id_entity'
            column from the 'tbl_dataset_value' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        '''

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT title '\
            'FROM tbl_dataset_entity '\
            'WHERE id_entity=%s'
        args = (id_entity)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result']}
