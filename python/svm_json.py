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
  #
  #  Note: since 'row' is a list, with one comma-delimited string element,
  #        the following line is required in this method:
  #
  #            row = row[0].split(',')
  #
  def csv_to_json(self):
    list_dataset       = []
    list_dataset_label = []

    # open temporary 'csvfile'
    with open( self.svm_file, 'rU' ) as csvfile:
      stuff = csv.reader( csvfile, delimiter=' ', quotechar='|' )

      # iterate all rows of csvfile (except first)
      for dep_index, row in enumerate( islice( stuff, 1, None ) ):

        # iterate first element of each row (except first)
        dep_variable_label = row[0].split(',')
        for value in dep_variable_label[:1]:
          list_dataset_label.append( value )

        # iterate each row
        indep_variable = row[0].split(',')
        for indep_index, value in enumerate( islice( indep_variable, 1, None) ):
          list_dataset.append( { list_dataset_label[dep_index]: value } )

    #return json.dumps(columns)
    print list_dataset
  ## xml_to_json: convert xml to JSON object
  def xml_to_json(self):
    print 'dummy code'
