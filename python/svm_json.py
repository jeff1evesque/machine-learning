#!/usr/bin/python

## @svm_json.py
#  This file contains methods to convert svm data to a JSON object.
import csv
from collections import defaultdict

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
    columns = defaultdict( list )

    with open( self.svm_file, 'rU' ) as f:
      reader = csv.DictReader(f)
      for row in reader:
        for (k,v) in row.items():
          columns[k].append(v)

    print json.dumps(columns)
  ## xml_to_json: convert xml to JSON object
  def xml_to_json(self):
    print 'dummy code'
