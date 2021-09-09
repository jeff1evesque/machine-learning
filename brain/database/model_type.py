#!/usr/bin/python

'''

This file retrieves model type, when provided the corresponding collection.

'''

from flask import current_app
from brain.database.query import SQL


class ModelType:
    '''

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This class provides and interface between the model_type.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('SQL_DB')

    def get_model_type(self, collection):
        '''

        This method is responsible for retrieving the model type, from the
        SQL database, using a fixed 'collection'.

        @collection, this supplied argument corresponding to the 'collection'
            column from the 'tbl_dataset_entity' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        '''

        # select dataset
        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT mtype.model'\
            ' FROM tbl_dataset_entity mid'\
            ' INNER JOIN tbl_model_type mtype'\
            ' ON mid.model_type = mtype.id_model'\
            ' WHERE mid.collection=%s'
        args = (collection,)
        response = self.sql.execute('select', sql_statement, args)

        # retrieve any error(s)
        response_error = self.sql.get_errors()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result'][0][0]}
