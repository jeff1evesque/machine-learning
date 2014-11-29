#!/usr/bin/python

## @svm_json.py
#  This file contains methods to convert svm data to a JSON object.
import json, csv

## Class: JSON
class JSON:

  ## constructor
  def __init__(self, svm_file):
    self.svm_file = svm_file

  ## csv_to_json: convert csv file to JSON object
  def csv_to_json(self):
    file_csv  = open( self.svm_file, 'r' )
    reader = csv.DictReader( file_csv )

    for row in reader:
      json_object = json.dump( row )
  ## xml_to_json: convert xml to JSON object
  def xml_to_json(self):
    print 'dummy code'
