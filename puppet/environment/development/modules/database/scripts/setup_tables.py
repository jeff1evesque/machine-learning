#!/usr/bin/python

'''@setup_tables

This file initializes the following database tables within the
'db_machine_learning' database:

    @tbl_dataset_entity, record the dataset instance, and the corresponding
        userid who created, or modified the information.

    @tbl_feature_count, record the number of features expected within an
        observation, with respect to a given 'id_entity'.

    @tbl_feature_value, records a tuple of criterion-predictor related values,
        or a tuple of observation-feature related values:

        - observation label: synonymous to dependent variable label, and can be
              'NULL' if the 'criterion value' is defined
        - criterion value: can be 'NULL' if the 'observation label' is defined
        - model type: generally the model type (i.e. svm, svr)
        - feature label: synonymous to independent variable label, or a
             predictor label
        - feature value: synonymous to independent variable, or a predictor value

    @model_type, reference table containing all possible model types.

    @tbl_observation_label, record every unique observation label, with respect
        to a given 'id_entity'.

'''

import yaml
from sys import argv
import MySQLdb as DB

# define configuration
#
# @argv[1], first passed-in argument from command (argv[0] is the filename)
#
with open(argv[1] + '/hiera/settings.yaml', 'r') as stream:
    # local variables
    settings = yaml.load(stream)
    host = settings['general']['host']
    db = settings['database']['name']
    provisioner = settings['database']['provisioner']
    provisioner_password = settings['database']['provisioner_password']

    # create connection
    conn = DB.connect(
        host,
        provisioner,
        provisioner_password,
        db
    )

    with conn:
        # create cursor object
        cur = conn.cursor()

        # create 'tbl_feature_count'
        sql_statement = '''\
                        CREATE TABLE IF NOT EXISTS tbl_feature_count (
                            id_size INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            id_entity INT NOT NULL,
                            count_features INT NOT NULL
                        );
                        '''
        cur.execute(sql_statement)

        # create 'tbl_dataset_entity'
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

        # create 'tbl_observation_label'
        sql_statement = '''\
                        CREATE TABLE IF NOT EXISTS tbl_observation_label (
                            id_label INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            id_entity INT NOT NULL,
                            dep_variable_label VARCHAR(75) NOT NULL
                        );
                        '''
        cur.execute(sql_statement)

        # create 'tbl_feature_value'
        sql_statement = '''\
                        CREATE TABLE IF NOT EXISTS tbl_feature_value (
                            id_value INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            id_entity INT NOT NULL,
                            dep_variable_label VARCHAR (50) NULL,
                            criterion FLOAT NULL,
                            model_type INT NOT NULL,
                            indep_variable_label VARCHAR (50) NOT NULL,
                            indep_variable_value FLOAT NOT NULL
                        );
                        '''
        cur.execute(sql_statement)

        # create 'tbl_model_type'
        sql_statement = '''\
                        CREATE TABLE IF NOT EXISTS tbl_model_type (
                            id_model INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            model VARCHAR (50) NOT NULL
                        );
                        '''
        cur.execute(sql_statement)

        # preload 'tbl_model_type'
        sql_statement = '''\
                        INSERT INTO tbl_model_type (model) VALUES ('svm');
                        INSERT INTO tbl_model_type (model) VALUES ('svr');
                        '''
        cur.execute(sql_statement)
