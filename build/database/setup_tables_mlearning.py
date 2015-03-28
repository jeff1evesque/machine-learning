#!/usr/bin/python

## @setup_db.py
#  This file initializes the following database tables within the 'db_machine_learning'
#      database:
#
#  @tbl_dataset_entity, record the dataset instance, and the corresponding userid
#      who created, or modified the information.
#
#  @tbl_feature_count, record the number of features expected within an observation,
#      with respect to a given 'id_entity'.
#
#  @tbl_feature_value, record each feature value with its corresponding feature label,
#      and observation label.
#
#  @tbl_observation_label, record every unique observation label, with respect to a
#      given 'id_entity'.
from brain.database.db_query import SQL

## local variables
sql = SQL()

## connect to database
sql.sql_connect('db_machine_learning')

## create 'tbl_feature_count'
sql_statement = '''\
                CREATE TABLE IF NOT EXISTS tbl_feature_count (
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

## create 'tbl_feature_value'
sql_statement = '''\
                CREATE TABLE IF NOT EXISTS tbl_feature_value (
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
if sql.get_errors(): print sql.return_error()
sql.sql_disconnect()
