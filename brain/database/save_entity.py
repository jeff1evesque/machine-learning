#!/usr/bin/python

'''

This file saves a dataset entity into corresponding 'EAV data model' database
table(s), from the 'db_machine_learning' database.

'''

from flask import current_app
from brain.database.db_query import SQL


class Save_Entity(object):
    '''

    This class provides an interface to save dataset(s) later used to generate
    corresponding model(s).

    Note: this class is invoked within 'base_data.py', and 'data_append.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data, session_type):
        '''

        This constructor is responsible for defining class variables.

        @self.premodel_data, a dictionary with the following elements:

            {'uid': xx, 'id_entity': xx, 'title': yyy}

        Note: 'xx' denotes an integer value, 'yyy' a unicode string, and 'zz'
              representing a float value.

        '''

        self.premodel_data = premodel_data
        self.session_type = session_type
        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')

    def save(self):
        '''

        This method stores, or updates dataset entities into its corresponding
        'EAV data model' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        Note: 'UTC_TIMESTAMP' returns the universal UTC datetime

        '''

        # insert / update dataset entity value
        self.sql.sql_connect(self.db_ml)

        if self.session_type == 'data_append':
            sql_statement = 'UPDATE tbl_dataset_entity '\
                'SET uid_modified=%s, datetime_modified=UTC_TIMESTAMP() '\
                'WHERE id_entity=%s'
            args = (self.premodel_data['uid'], self.premodel_data['id_entity'])
            response = self.sql.sql_command(sql_statement, 'update', args)

        elif self.session_type == 'data_new':
            sql_statement = 'INSERT INTO tbl_dataset_entity '\
                '(title, model_type, uid_created, datetime_created) '\
                'VALUES(%s, %s, %s, UTC_TIMESTAMP())'
            args = (
                self.premodel_data['title'],
                self.premodel_data['model_type'],
                self.premodel_data['uid']
            )
            response = self.sql.sql_command(sql_statement, 'insert', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error}
        else:
            return {'status': True, 'error': None, 'id': response['id']}
