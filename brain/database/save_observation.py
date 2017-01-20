#!/usr/bin/python

'''

This file saves the observation labels.

'''

from flask import current_app
from brain.database.db_query import SQL


class Save_Observation(object):
    '''

    This class provides an interface to store observation labels, provided
    from corresponding dataset(s) into corresponding database tables.

    Note: this class is invoked within 'base_data.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data, session_type):
        '''

        This constructor is responsible for defining class variables.

        '''

        # class variables
        self.premodel_data = premodel_data
        self.session_type = session_type
        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')

    def save_label(self):
        '''

        This method can store, or update an existing set of observation labels
        in corresponding database tables (using EAV data model).

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        Note: 'UTC_TIMESTAMP' returns the universal UTC datetime

        '''

        # insert / update feature label(s)
        self.sql.sql_connect(self.db_ml)

        # add labels (append case)
        if self.session_type in ['data_append', 'data_new']:

            # check if observation label exists in database
            sql_statement = 'SELECT * FROM tbl_observation_label '\
                'WHERE dep_variable_label=%s '\
                'AND id_entity=%s'
            args = (
                self.premodel_data['label'],
                self.premodel_data['id_entity']
            )
            response = self.sql.sql_command(sql_statement, 'select', args)

            # add labels if not exist
            if not response['result']:
                sql_statement = 'INSERT INTO tbl_observation_label '\
                    '(id_entity, dep_variable_label) VALUES(%s, %s)'
                args = (
                    self.premodel_data['id_entity'],
                    self.premodel_data['label']
                )
                self.sql.sql_command(
                    sql_statement,
                    'insert',
                    args,
                )

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error}
        else:
            return {'status': True, 'error': None}
