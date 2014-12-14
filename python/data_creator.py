#!/usr/bin/python

## @data_creator.py
import json
import MySQLdb as DB

## Class: Training
class Training:

  ## constructor
  def __init__(self, svm_data):
    self.svm_data = svm_data

  ## db_save_dataset
  def db_save_dataset(self):
    print self.svm_data

## Class: Analysis
class Analysis:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data
