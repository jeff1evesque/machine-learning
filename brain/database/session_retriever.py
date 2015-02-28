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
