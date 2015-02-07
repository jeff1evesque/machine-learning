#!/usr/bin/python

## @db_query.py
#  This file contains various generic SQL-related methods.
import MySQLdb as DB
from database.db_settings import Database

## Class: SQL, explicitly inherit 'new-style' class
class SQL(object):

  ## constructor:
  def __init__(self):
    self.db_settings = Database()
    self.list_error  = []

  ## sql_connect: create connection to MySQL / MariaDB
  def sql_connect(self, database=None):
    try:
      if database == None:
        self.conn = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password() )
      else:
        self.conn = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db=database )
      self.cursor = self.conn.cursor()
      return { 'status': True, 'error': None, 'id': None }
    except DB.Error, error:
      self.list_error.append(error)
      return { 'status': False, 'error': self.list_error, 'id': None }

  ## sql_command: execute sql statement.
  #
  #  @sql_args, is a tuple used for argument substitution with the supplied
  #      'sql_statement'.
  def sql_command(self, sql_statement, sql_type, sql_args=None):
    try:
      self.cursor.execute( sql_statement, sql_args )
      if sql_type in ['insert', 'delete', 'update']:
        self.conn.commit()
      return { 'status': True, 'error': None, 'id': self.cursor.lastrowid }
    except DB.Error, error:
      self.conn.rollback()
      self.list_error.append(error)
      return { 'status': False, 'error': self.list_error, 'id': self.cursor.lastrowid }

  ## sql_disconnect: close connection to MySQL / MariaDB
  def sql_disconnect(self):
    try:
      if self.conn:
        self.conn.close()
        return { 'status': True, 'error': None, 'id': self.cursor.lastrowid }
    except DB.Error, error:
      self.list_error.append(error)
      return { 'status': False, 'error': self.list_error, 'id': self.cursor.lastrowid }

  ## return_error: return appended error message(s)
  def return_error(self):
    return self.list_error
