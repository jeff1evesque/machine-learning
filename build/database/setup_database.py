#!/usr/bin/python

## @setup_db.py
#  This file initializes any required database(s).
from brain.database.db_query import SQL

## local variables
sql = SQL()

## CREATE DATABASE
#
#  @db_machine_learning
sql.sql_connect()

## create 'db_machine_learning
sql_statement = 'CREATE DATABASE IF NOT EXISTS db_machine_learning CHARACTER SET utf8 COLLATE utf8_general_ci'
sql.sql_command(sql_statement, 'create')

# retrieve any error(s), disconnect from database
if sql.get_errors(): print sql.return_error()
sql.sql_disconnect()
