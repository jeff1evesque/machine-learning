#!/usr/bin/python

## @retrieve_dataset.py
#  This file retrieves SVM related data from corresponding 'EAV data model' database
#      table(s), from the 'db_machine_learning' database.
from brain.database.db_query import SQL

## Class: Retrieve_Dataset, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'views.py'
class Retrieve_Dataset(object):

  ## constructor:
  def __init__(self, svm_data):
    # class variables
    self.svm_data   = svm_data
    self.list_error = []
    self.sql        = SQL()

  ## get_dataset: retrieve an SVM dataset from corresponding 'EAV data model'
  #               database table(s).
  #
  #  @id_entity, this supplied argument corresponds to the 'id_entity' column from the
  #      'tbl_dataset_value' database table.
  #
  #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s' 
  #      is used for argument substitution.
  def get_dataset(self, id_entity):
    # select dataset
    self.sql.sql_connect('db_machine_learning')
    sql_statement = 'SELECT dep_variable_label, indep_variable_label, indep_variable_value FROM tbl_dataset_value where id_entity=%s'
    args          = ( id_entity )
    response      = self.sql.sql_command( sql_statement, 'select', args )

    # retrieve any error(s), disconnect from database
    response_error = sql.return_error()
    self.sql.sql_disconnect()

    # return result
    if response_error: return { 'status': False, 'error': response_error, 'result': None }
    else: return { 'status': True, 'error': None, 'result': response['result'] }
