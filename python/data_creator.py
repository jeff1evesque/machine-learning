#!/usr/bin/python

## @data_creator.py
import json

## Class: Validator
class Training:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data
    print json.dumps({'key1':'val1'}, separators=(',', ': '))
    print json.dumps({'key2':'val2'}, separators=(',', ': '))
