#!/usr/bin/python

'''

This file saves previous predictions.

'''

from flask import current_app
from brain.database.query import SQL


class Prediction(object):
    '''

    This class provides an interface to save, a previous generated svm or svr
    prediction result.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()
        self.db_ml = current_app.config.get('DB_ML')

    def save(self, data, type):
        '''

        This method stores the corresponding prediction.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        Note: 'UTC_TIMESTAMP' returns the universal UTC datetime

        '''

        # insert / update dataset entity value
        self.sql.connect(self.db_ml)
