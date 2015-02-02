#!/usr/bin/python

## @db_query.py
#  This file contains various generic SQL methods.
import MySQLdb as DB
from database.db_settings import Database

## Class: SQL
class SQL:

  ## constructor:
  def __init__(self):
    self.db_setting = Database()
