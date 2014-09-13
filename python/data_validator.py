#!/usr/bin/python

## @data_validator.py
#  This script performs various data sanitation on the form data, and 
#  validates the same data to ensure that the SVM algorithm will work
#  on the given dataset.
import json

## Class: Validator
class Validator:

  ## constructor: saves a subset of the passed-in form data
  def __init__(self, form_data):
    self.form_data = form_data

  ## form_sanitation(): sanitizes a subset of the passed-in form data
  def form_sanitation(self):

  ## form_validation(): validates a subset of the passed-in form data
  def form_validation(self):
