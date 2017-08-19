#!/usr/bin/python

'''

This file saves the provided dataset(s) into a series of nosql documents,
using the mongodb framework.

'''

from brain.database.query import NoSQL


class Collection(object):
    '''

    This class provides an interface to retrieve, and store various parameters,
    of the specified collection, from the mongodb.

    Note: this class is invoked within 'base_data.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.nosql = NoSQL()

    def query(self, collection, operation, payload=None):
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
            - count_documents
            - drop_collection

        '''

        # execute query
        if operation == 'drop_collection':
            self.nosql.connect()
            response = self.nosql.execute(operation, collection)
        else:
            self.nosql.connect(collection)
            response = self.nosql.execute(operation, payload)

        # retrieve any error(s)
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
