#!/usr/bin/python

'''

This file retrieves dataset entity related properties.

'''

from flask import current_app
from brain.database.query import SQL


class Entity(object):
    '''

    This class provides an interface to save, retrieve an SVM entity title,
    from the 'tbl_dataset_entity' sql database table.

    Note: this class is invoked within 'model_generate.py', or 'base_data.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data=None, session_type=None):
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
        self.db_ml = current_app.config.get('SQL_DB')

    def save(self):
        '''

        This method stores, or updates dataset entities into its corresponding
        'EAV data model' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        Note: 'UTC_TIMESTAMP' returns the universal UTC datetime

        '''

        # insert / update dataset entity value
        self.sql.connect(self.db_ml)

        if self.session_type == 'data_new':
            sql_statement = 'INSERT INTO tbl_dataset_entity '\
                '(title, model_type, uid_created, datetime_created) '\
                'VALUES(%s, %s, %s, UTC_TIMESTAMP())'
            args = (
                self.premodel_data['title'],
                self.premodel_data['model_type'],
                self.premodel_data['uid']
            )
            response = self.sql.execute('insert', sql_statement, args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error}
        else:
            return {'status': True, 'error': None, 'id': response['id']}

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
        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT title '\
            'FROM tbl_dataset_entity '\
            'WHERE id_entity=%s'
        args = (id_entity)
        response = self.sql.execute('select', sql_statement, args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': None}
        else:
            return {'error': None, 'result': response['result']}
