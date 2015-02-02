#!/usr/bin/python

## @db_query.py
#  This file contains various generic SQL methods.
import MySQLdb as DB
from database.db_settings import Database

## Class: SQL
class SQL:

  ## constructor:
  def __init__(self):
    self.db_settings = Database()

  ## sql_connect: create connection to MySQL / MariaDB
  def sql_connect(self):
    try:
      self.conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password() )
      self.cursor = self.conn.cursor()
      return { 'status': True, 'error': None, 'id': None }
    except DB.error, error:
      self.list_error.append(error)
      return { 'status': False, 'error': self.list_error, 'id': None }

  ## sql_command: execute sql statement
  def sql_command(self, sql_statement, sql_type, sql_args=None):
    try:
      self.cursor.execute( sql_statement, sql_args )
      if sql_type in ['insert', 'update']:
        self.conn.commit()
        return { 'status': True, 'error': None, 'id': self.cursor.lastrowid }
    except DB.error, error:
      self.conn.rollback()
      self.list_error.append(error)
      return { 'status': False, 'error': self.list_error, 'id': self.cursor.lastrowid }
