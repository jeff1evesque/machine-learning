#!/usr/bin/python

## @save_label.py
#  This file saves SVM related data into corresponding 'EAV data model' database
#      table(s), from the 'db_machine_learning' database.
from brain.database.db_query import SQL

## Class: Save_Label, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'data_new.py'
class Save_Label(object):

    ## constructor: stores an SVM label (python dict), database configurations
    #               into their own corresponding class variable.
    def __init__(self, svm_data, session_type):
        # class variables
        self.svm_data     = svm_data
        self.session_type = session_type
        self.list_error   = []
        self.sql          = SQL()
