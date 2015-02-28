#!/usr/bin/python

## @converter_json.py
#  This file contains methods needed to correctly format input data.

## Class: Convert_Data, explicitly inherit 'new-style class
class Convert_Data(object):

  ## constructor
  def __init__(self, settings, files=None):
    self.list_error = []
    self.settings   = settings
    self.files      = files

  ## format: restructure input data
  def format(self):

  ## get_errors: returns all errors corresponding to this class instance
  def get_errors(self):
    if len(self.list_error) > 0: return { 'error': self.list_error }
    else: return { 'error': None }
