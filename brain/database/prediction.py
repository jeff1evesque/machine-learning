#!/usr/bin/python

'''

This file saves previous predictions.

'''

import json
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

    def save(self, payload, type, title):
        '''

        This method stores the corresponding prediction.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        Note: 'UTC_TIMESTAMP' returns the universal UTC datetime

        '''

        # local variables
        data = json.loads(payload)
        result = data['result']

        # insert prediction
        self.sql.connect(self.db_ml)

        if type == 'svm':
            classes = data['classes']
            probability = data['probability']
            decision_function = data['decision_function']

            # svm results
            sql_statement = 'INSERT INTO tbl_svm_results '\
                '(title, result, uid_created, datetime_created) '\
                'VALUES(%s, %s, %s, UTC_TIMESTAMP())'
            args = (
                title,
                result,
                self.premodel_data['uid']
            )
            svm_results = self.sql.execute(
                sql_statement,
                'insert',
                args,
            )

            # svm classes
            sql_statement = 'INSERT INTO tbl_svm_results_class '\
                '(id_result, class) VALUES(%s, %s)'
            args = (
                svm_results['id'],
                (classes,)
            )
            self.sql.execute(
                sql_statement,
                'insert',
                args,
            )

            # svm probability
            sql_statement = 'INSERT INTO tbl_svm_results_probability '\
                '(id_result, probability) VALUES(%s, %s)'
            args = (
                svm_results['id'],
                (probability,)
            )
            self.sql.execute(
                sql_statement,
                'insert',
                args,
            )

            # decision function
            sql_statement = 'INSERT INTO tbl_svm_results_decision_function '\
                '(id_result, decision_function) VALUES(%s, %s)'
            args = (
                svm_results['id'],
                (decision_function,)
            )
            self.sql.execute(
                sql_statement,
                'insert',
                args,
            )

        elif type == 'svr':
            # svr results
            sql_statement = 'INSERT INTO tbl_svr_results '\
                '(title, result, uid_created, datetime_created) '\
                'VALUES(%s, %s, %s, UTC_TIMESTAMP())'
            args = (
                title,
                result,
                self.premodel_data['uid']
            )
            svr_results = self.sql.execute(
                sql_statement,
                'insert',
                args,
            )

            # svr r2
            sql_statement = 'INSERT INTO tbl_svm_results_probability '\
                '(id_result, probability) VALUES(%s, %s)'
            args = (
                svr_results['id'],
                result['r2']
            )
            self.sql.execute(
                sql_statement,
                'insert',
                args,
            )

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {'error': response_error, 'result': 1}
        else:
            return {'error': None, 'result': 0}
