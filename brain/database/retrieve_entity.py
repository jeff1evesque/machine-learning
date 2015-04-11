#!/usr/bin/python

## @retrieve_entity.py
#  This file retrieves SVM related enity from corresponding 'EAV data model' database
#      table(s), from the 'db_machine_learning' database.
from brain.database.db_query import SQL

## Class: Retrieve_Entity, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'model_generate.py'
class Retrieve_Entity(object):

    ## constructor:
    def __init__(self):
        # class variables
        self.list_error = []
        self.sql        = SQL()

    ## get_title: retrieve an SVM entity tile from corresponding 'EAV data model'
    #             database table(s), using a fixed 'id_entity'.
    #
    #  @id_entity, this supplied argument corresponds to the 'id_entity' column from the
    #      'tbl_dataset_value' database table.
    #
    #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s' 
    #      is used for argument substitution.
    def get_title(self, id_entity):
        # select dataset
        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'SELECT title FROM tbl_dataset_entity where id_entity=%s'
        args          = (id_entity)
        response      = self.sql.sql_command(sql_statement, 'select', args)

        # retrieve any error(s), disconnect from database
        response_error = self.sql.get_errors()
        self.sql.sql_disconnect()

        # return result
        if response_error: return {'error': response_error, 'result': None}
        else: return {'error': None, 'result': response['result']}
