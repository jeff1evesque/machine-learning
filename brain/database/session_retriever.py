#!/usr/bin/python

## @session_retriever.py
#  This file queries, and returns 'svm_title', and 'id_entity from the
#      'tbl_dataset_entity' database table of 'db_machine_learning'.
from brain.database.db_query import SQL

## Class: Retrieve_Session, explicitly inherit 'new-style' class
class Retrieve_Session(object):

  ## constructor:
  def __init__(self):
    self.list_error = []
    self.sql        = SQL()

  ## get_all_sessions: get all sessions from 'tbl_dataset_entity'
  def get_all_sessions(self):
    sql.sql_connect('db_machine_learning')
    sql_statement  = ' $sql = 'SELECT id_entity, title FROM tbl_dataset_entity'
    response       = sql.sql_command( sql_statement, 'select' )

    # retrieve any error(s), disconnect from database
    response_error = sql.return_error()
    sql.sql_disconnect()

    # return result
    if response_error: return { 'result': None, 'error': response_error }
    else: return { 'result': response['result'], 'error': None }
