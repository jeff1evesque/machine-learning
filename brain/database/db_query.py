#!/usr/bin/python

## @db_query.py
#  This file contains various generic SQL-related methods.
import MySQLdb as DB
from brain.database.db_settings import Database

## Class: SQL, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'save_xx.py', and 'retrieve_xx.py'
#        files.
class SQL(object):

    ## constructor:
    def __init__(self, host=None, user=None, passwd=None):
        self.db_settings = Database()
        self.list_error  = []
        self.proceed     = True

        # host address
        if host:
            self.host = host
        else:
            self.host = self.db_settings.get_db_host()

        # sql username for above host address
        if user:
            self.user = user
        else:
            self.user = self.db_settings.get_db_username()

        # sql password for above username
        if passwd:
            self.passwd = passwd
        else:
            self.passwd = self.db_settings.get_db_password()

    ## sql_connect: create connection to MySQL / MariaDB
    def sql_connect(self, database=None):
        try:
            if database == None:
                self.conn = DB.connect(self.host, self.user, self.passwd)
            else:
                self.conn = DB.connect(self.host, self.user, self.passwd, db=database)
            self.cursor = self.conn.cursor()
            return {'status': True, 'error': None, 'id': None}

        except DB.Error, error:
            self.proceed = False
            self.list_error.append(error)
            return {'status': False, 'error': self.list_error, 'id': None}

    ## sql_command: execute sql statement.
    #
    #  @sql_args, is a tuple used for argument substitution with the supplied
    #      'sql_statement'.
    def sql_command(self, sql_statement, sql_type, sql_args=None):
        if self.proceed:
            try:
                self.cursor.execute(sql_statement, sql_args)

                # commit change(s), return lastrowid
                if sql_type in ['insert', 'delete', 'update']:
                    self.conn.commit()
                # fetch all the rows, return as list of lists.
                elif sql_type == 'select':
                    result = self.cursor.fetchall()

            except DB.Error, error:
                self.conn.rollback()
                self.list_error.append(error)
                return {'status': False, 'error': self.list_error, 'result': None}

        if sql_type in ['insert', 'delete', 'update']: return {'status': False, 'error': self.list_error, 'id': self.cursor.lastrowid}
        elif sql_type == 'select': return {'status': False, 'error': self.list_error, 'result': result}

    ## sql_disconnect: close connection to MySQL / MariaDB
    def sql_disconnect(self):
        if self.proceed:
            try:
                if self.conn:
                    self.conn.close()
                    return {'status': True, 'error': None, 'id': self.cursor.lastrowid}
            except DB.Error, error:
                self.list_error.append(error)
                return {'status': False, 'error': self.list_error, 'id': self.cursor.lastrowid}

    ## get_errors: return appended error message(s)
    def get_errors(self):
        return self.list_error
