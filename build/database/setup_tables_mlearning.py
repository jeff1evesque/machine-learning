#!/usr/bin/python

## @setup_db.py
#  This file initializes database tables related to the 'db_machine_learning'
#      database.
from brain.database.db_query import SQL

## local variables
sql = SQL()

## CREATE DATABASE TABLES
#
#  @tbl_dataset_size
#  @tbl_dataset_entity
#  @tbl_observation_label
#  @tbl_dataset_value
sql.sql_connect('db_machine_learning')

## create 'tbl_dataset_size'
sql_statement = '''\
                CREATE TABLE IF NOT EXISTS tbl_dataset_size (
                    id_size INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    id_entity INT NOT NULL,
                    count_features INT NOT NULL
                );
                '''
sql.sql_command(sql_statement, 'create')

## create 'tbl_dataset_entity'
sql_statement = '''\
                CREATE TABLE IF NOT EXISTS tbl_dataset_entity (
                    id_entity INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR (50) NOT NULL,
                    uid_created INT NOT NULL,
                    datetime_created DATETIME NOT NULL,
                    uid_modified INT NULL,
                    datetime_modified DATETIME NULL
                );
                '''
sql.sql_command(sql_statement, 'create')

## create 'tbl_observation_label'
sql_statement = '''\
                CREATE TABLE IF NOT EXISTS tbl_observation_label (
                    id_label INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    id_entity INT NOT NULL,
                    dep_variable_label VARCHAR(75) NOT NULL
                );
                '''
sql.sql_command(sql_statement, 'create')

## create 'tble_dataset_value'
sql_statement = '''\
                CREATE TABLE IF NOT EXISTS tbl_dataset_value (
                    id_value INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    id_entity INT NOT NULL,
                    dep_variable_label VARCHAR (50) NOT NULL,
                    indep_variable_label VARCHAR (50) NOT NULL,
                    indep_variable_value FLOAT NOT NULL,
                    CONSTRAINT FK_dataset_entity FOREIGN KEY (id_entity) REFERENCES tbl_dataset_entity (id_entity)
                );
                '''
sql.sql_command(sql_statement, 'create')

# retrieve any error(s), disconnect from database
if sql.return_error(): print sql.return_error()
sql.sql_disconnect()
