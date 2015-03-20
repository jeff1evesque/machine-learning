#!/usr/bin/python

## @data_new.py
#  This file allows methods defined from the Base, or Base_Data class to be
#      overridden, if needed.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references
from brain.session.base import Base
from brain.session.base_data import Base_Data

## Class: Data_New, inherit base methods from superclass 'Base', 'Base_Data'
#
#  Note: this class is invoked within 'load_data.py'
class Data_New(Base, Base_Data):

    ## constructor: define class properties using the superclass 'Session_Base'
    #               constructor, along with the constructor in this subclass.
    #
    #  @super(), implement 'Session_Base' superclass constructor within this
    #      child class constructor.
    #
    #  Note: the superclass constructor expects the same 'svm_data' argument.
    def __init__(self, svm_data):
        super(Data_New, self).__init__(svm_data)
