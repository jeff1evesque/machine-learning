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
