#!/usr/bin/python

## @data_retriever.py
#  This file retrieves SVM related data from corresponding 'EAV data model' database
#      table(s), from the 'db_machine_learning' database.
from database.db_query import SQL

## Class: Data_Retrieve, explicitly inherit 'new-style' class
class Data_Retrieve(object):

  ## constructor:
  def __init__(self, svm_data, cmd, session_type):
    # class variables
    self.svm_data     = svm_data
    self.svm_cmd      = cmd
    self.session_type = session_type
    self.list_error   = []

  ## db_data_retrieve: retrieve an SVM dataset from corresponding 'EAV data model'
  #                    database table(s).
  #
  #  @id_entity, this supplied argument corresponds to the 'id_entity' column from the
  #      'tbl_dataset_value' database table.
  #
  #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s' 
  #      is used for argument substitution.
  def db_data_retrieve(self, id_entity):
    # local variables
    sql = SQL()

    # select dataset
    sql.sql_connect('db_machine_learning')
    sql_statement = 'SELECT dep_variable_label, indep_variable_label, indep_variable_value FROM tbl_dataset_value where id_entity=%s'
    args          = ( id_entity )
    response      = sql.sql_command( sql_statement, 'select', args )

    # retrieve any error(s), disconnect from database
    response_error = sql.return_error()
    sql.sql_disconnect()

    # return result
    if response_error: return { 'status': False, 'error': response_error, 'id': response['id'], 'result': response['result'] }
    else: return { 'status': True, 'error': None, 'id': response['id'], 'result': None }
