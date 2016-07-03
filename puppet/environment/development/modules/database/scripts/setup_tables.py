#!/usr/bin/python

'''@setup_tables

This file initializes the following database tables within the
'db_machine_learning' database:

    @tbl_dataset_entity, record the dataset instance, and the corresponding
        userid who created, or modified the information, and the model type.

    @tbl_feature_count, record the number of features expected within an
        observation, with respect to a given 'id_entity'.

    @tbl_feature_value, records a tuple of criterion-predictor related values,
        or a tuple of observation-feature related values:

        - observation label: synonymous to dependent variable label, and can be
              'NULL' if the 'criterion value' is defined
        - criterion value: can be 'NULL' if the 'observation label' is defined
        - feature label: synonymous to independent variable label, or predictor
             label
        - feature value: synonymous to independent variable, or predictor value

    @model_type, reference table containing all possible model types.

    @tbl_observation_label, record every unique observation label, with respect
        to a given 'id_entity'.

'''

import yaml
from sys import argv
import MySQLdb as DB

with open('/var/machine-learning/db-trace.txt', 'w') as file:
    file.write("outside: python subprocess worked")
    file.write("outside: argv[1] - " + argv[1])


# define configuration
#
# @argv[1], first passed-in argument from command (argv[0] is the filename)
#
with open(argv[1] + '/hiera/settings.yaml', 'r') as stream:
    with open('/var/machine-learning/db-trace.txt', 'w') as file:
        filefile.write("inside: python subprocess worked")
    # local variables
    settings = yaml.load(stream)
    models = settings['application']['model_type']
    host = settings['general']['host']
    db_ml = settings['database']['name']
    provisioner = settings['database']['provisioner']
    provisioner_password = settings['database']['provisioner_password']

    with open("/var/machine-learning/db-trace.txt", "w") as text_file:
        text_file.write("host: %s" % host)
        text_file.write("provisioner: %s" % provisioner)
        text_file.write("provisioner password: %s" % provisioner_password)
        text_file.write("database: %s" % db_ml)

    # create connection
    conn = DB.connect(
        host,
        provisioner,
        provisioner_password,
        db_ml
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
                            model_type INT NOT NULL,
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

        # populate 'tbl_model_type'
        sql_statement = '''\
                        INSERT INTO tbl_model_type (model) VALUES (%s);
                        '''
        cur.executemany(sql_statement, models)
