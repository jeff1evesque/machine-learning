#!/usr/bin/python

## @save_size.py
#  This file saves the number of features that can be expected in a given
#      observation with respect to 'id_entity'.
from brain.database.db_query import SQL

## Class: Save_Size, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Save_Size(object):

    ## constructor:
    def __init__(self, svm_data):
        # class variables
        self.svm_data     = svm_data
        self.list_error   = []
        self.sql          = SQL()
