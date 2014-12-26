#!/usr/bin/python

## @svm_json.py
#  This file contains methods to convert svm data to a JSON object.
import json, csv
from collections import defaultdict
from itertools import islice

## Class: JSON
class JSON:

  ## constructor
  def __init__(self, svm_file):
    self.svm_file = svm_file

  ## csv_to_json: convert csv file to JSON object
  #
  #  Note: we use the 'Universal Newline Support' with the 'U" parameter
  #        when opening 'self.svm_file'. This allows newlines to be
  #        understood regardless, if the newline character was created in
  #        osx, windows, or linux.
  def csv_to_json(self):
    list_dataset       = []
    dict_dataset_label = []

    # open temporary 'csvfile'
    with open( self.svm_file, 'rU' ) as csvfile:
      stuff = csv.reader( csvfile, delimiter=' ', quotechar='|' )

      for row in islice( stuff, 0, 1 ):

        row = row[0].split(',')
        for value in row:
          dict_dataset_label.append( value )

      # iterate each csv row, except the first
      for row in islice( stuff, 1, None ):

        # split comma-delimited string
        row = row[0].split(',')

        # iterate 'row' list
        for index, value in enumerate( row ):

    #return json.dumps(columns)
  ## xml_to_json: convert xml to JSON object
  def xml_to_json(self):
    print 'dummy code'
