#!/usr/bin/python

## @session_data_new.py
#  This file receives data (i.e. settings), including one or more dataset(s)
#      provided during the current session, and stores them into corresponding
#      database tables. The stored dataset(s) can later be retrieved from
#      'session_data_append.py', or 'session_generate_model.py'.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
from session.session_data_append import Data_Append

## Class: Data_New, inherit base methods from superclass 'Data_Append'
class Data_New(Data_Append):

  ## constructor: instantiate superclass constructor from 'Data_Append'
  #
  #  @super(), implement 'Data_Append' superclass constructor within this
  #      child class constructor.
  #
  #  Note: the superclass constructor expects the same 'svm_data' argument.
  def __init__(self, svm_data):
    super(Data_Add, self).__init__(svm_data)
