#!/usr/bin/python

'''@retrieve_feature

This file retrieves feature characteristics.

'''

from brain.database.db_query import SQL


class Retrieve_Feature(object):
    '''@Retrieve_Feature

    This class provides an interface to retrieve an svm dataset, using a fixed
    supplied 'id_entity'.  The 'id_entity' is a reference, indicating which
    dataset to get.

    Note: this class is invoked within 'model_generate.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''@__init__

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.sql = SQL()

    def get_dataset(self, id_entity):
        '''@get_dataset

        This method retrieves an SVM dataset, from corresponding 'EAV data
        model' database table(s), using a fixed 'id_entity'.

        @id_entity, this supplied argument corresponds to the 'id_entity'
            column from the 'tbl_dataset_value' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.

        '''

        # select dataset
        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'SELECT dep_variable_label, indep_variable_label, '\
            'indep_variable_value FROM tbl_feature_value where id_entity=%s'
        args = (id_entity)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error, 'result': None}
        else:
            return {
                'status': True,
                'error': None,
                'result': response['result'],
            }

    def get_count(self, id_entity):
        '''@get_count

        This method retrieves the number of features that can be expected in
        any given observation, from a particular dataset instance (id_entity).

        @id_entity, this supplied argument corresponds to the 'id_entity'
            column from the 'tbl_dataset_value' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.
        '''

        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'SELECT count_features FROM tbl_feature_count '\
            'where id_entity=%s'
        args = (id_entity)
        response = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'status': False, 'error': response_error, 'result': None}
        else:
            return {
                'status': True,
                'error': None,
                'result': response['result'],
            }
