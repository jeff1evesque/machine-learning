#!/usr/bin/python

'''@setup_tables

This file initializes the following database tables within the
'db_machine_learning' database:

    @tbl_dataset_entity, record the dataset instance, and the corresponding
        userid who created, or modified the information.

    @tbl_feature_count, record the number of features expected within an
        observation, with respect to a given 'id_entity'.

    @tbl_feature_value, record each feature value with its corresponding
        feature label, and observation label.

    @tbl_observation_label, record every unique observation label, with respect
        to a given 'id_entity'.

'''

import MySQLdb as DB

## create connection
conn = DB.connect('localhost', 'provisioner', 'password', 'db_machine_learning')

with conn:
    ## create cursor object
    cur = conn.cursor()

    ## create 'tbl_feature_count'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_feature_count (
                        id_size INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_entity INT NOT NULL,
                        count_features INT NOT NULL
                    );
                    '''
    cur.execute(sql_statement)

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
    cur.execute(sql_statement)

    ## create 'tbl_observation_label'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_observation_label (
                        id_label INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_entity INT NOT NULL,
                        dep_variable_label VARCHAR(75) NOT NULL
                    );
                    '''
    cur.execute(sql_statement)

    ## create 'tbl_feature_value'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_feature_value (
                        id_value INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_entity INT NOT NULL,
                        dep_variable_label VARCHAR (50) NOT NULL,
                        indep_variable_label VARCHAR (50) NOT NULL,
                        indep_variable_value FLOAT NOT NULL
                    );
                    '''
    cur.execute(sql_statement)
