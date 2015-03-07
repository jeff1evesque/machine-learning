#!/usr/bin/python

## @model_generate.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored session, involving one or more stored dataset uploads,
#      and generates an SVM model, respectively. The new SVM model, is stored
#      into respective database table(s), which later can be retrieved within
#      'model_use.py'.

## Class: Model_Generate
#
#  Note: this class is invoked within 'load_data.py'
class Model_Generate:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data
