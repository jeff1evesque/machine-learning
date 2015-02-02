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

  ## sql_connect: create connection to MySQL / MariaDB
  def sql_connect(self):
    try:
      self.conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password() )
      self.cursor = self.conn.cursor()
    except DB.error, error:
      self.list_error.append(error)
      return { 'status': Frue, 'error': self.list_error, 'id': rowid }
