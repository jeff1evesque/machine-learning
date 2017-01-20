#!/usr/bin/python

'''

This file retrieves model type, when provided the model id.

'''

from flask import current_app
from brain.database.db_query import SQL


class Retrieve_Model_Type(object):
    '''

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')

    def get_model_type(self, id_entity):
        '''

        This method is responsible for retrieving the model type, from the
        SQL database, using a fixed 'model_id'.

        @id_entity, this supplied argument corresponding to the 'id_entity'
            column from the 'tbl_dataset_entity' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        '''

        # select dataset
        self.sql.sql_connect(self.db_ml)
        sql_statement = 'SELECT mtype.model'\
            ' FROM tbl_dataset_entity mid'\
            ' INNER JOIN tbl_model_type mtype'\
            ' ON mid.model_type = mtype.id_model'\
            ' WHERE mid.id_entity=%s'
        args = (id_entity)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result'][0][0]}
