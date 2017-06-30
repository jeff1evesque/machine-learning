#!/usr/bin/python

'''

This file saves the provided dataset(s) into a series of nosql documents,
using the mongodb framework.

'''

from brain.database.query import NoSQL


class Collection(object):
    '''

    This class provides an interface to retrieve, and store the supplied
    dataset(s), into a mongodb collection. Additional methods, are also
    provided, to query varying parameters of the specified collection.

    Note: this class is invoked within 'base_data.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.nosql = NoSQL()

    def query(self, collection, operation, payload):
        '''

        This method executes a query, with respect to the desired 'operation'.

        @operation, the type of operation:
            - insert_one
            - insert_many
            - update_one
            - update_many
            - find
            - find_one
            - map_reduce
            - delete_one
            - delete_many
            - drop_collection

        '''

        # insert / update dataset value(s)
        self.nosql.connect(database, collection)
        response = self.nosql.execute(operation, payload)

        # retrieve any error(s), disconnect from database
        response_error = self.nosql.get_errors()

        # return result
        if response_error:
            return {
                'status': False,
                'result': response['result'],
                'error': response_error
            }
        else:
            return {'status': True, 'result': response['result'], 'error': None}

    def get_count(self, id_entity):
        '''

        This method retrieves the number of features that can be expected in
        any given observation, from a particular dataset instance (id_entity).

        @id_entity, this supplied argument corresponds to the 'id_entity'
            column from the 'tbl_dataset_value' database table.

        @sql_statement, is a sql format string, and not a python string.
            Therefore, '%s' is used for argument substitution.
        '''

        self.sql.connect(self.db_ml)
        sql_statement = 'SELECT count_features '\
            'FROM tbl_feature_count '\
            'WHERE id_entity=%s'
        args = (id_entity)
        response = self.sql.execute('select', sql_statement, args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.disconnect()

        # return result
        if response_error:
            return {
                'status': False,
                'error': response_error,
                'result': None
            }
        else:
            return {
                'status': True,
                'error': None,
                'result': response['result'],
            }
