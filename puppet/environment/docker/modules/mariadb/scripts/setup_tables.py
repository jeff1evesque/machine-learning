#!/usr/bin/python

'''

This file initializes the following database tables within the
'db_machine_learning' database:

    @tbl_dataset_entity, record the dataset instance, and the corresponding
        userid who created, or modified the information, and the model type.

        @model_type, reference table containing all possible model types.

    @tbl_prediction_results, record the prediction result, with respect to the
        corresponding 'model_type' column. The following are associated tables:

        svm model type:

            @tbl_svm_results_class, record predicted classes, with respect
                to a given 'id_result'.
            @tbl_svm_results_probability, record predicted probabilities,
                with respect to a given 'id_result'.
            @tbl_svm_results_decision_function, record predicted decisision
                function, with respect to a given 'id_result'.

        svr model type:

            @tbl_svr_results_results_r2, record predicted r^2, with respect
                to a given 'id_result'.

'''

import yaml
from sys import argv
import MySQLdb as DB


# local variables
#
# @argv[1], first passed-in argument from command (argv[0] is the filename),
#     indicating the project root directory.
#
# @argv[2], second passed-in argument from command, or boolean value
#     indicating if build is vagrant instance.
if argv[2] == 'true':
    prepath = argv[1] + '/hiera'
else:
    prepath = argv[1] + '/hiera/test/hiera'

# yaml configuration: database attributes
with open(prepath + '/database.yaml', 'r') as stream:
    settings = yaml.load(stream)
    database = settings['database']['mariadb']
    db_ml = database['name']
    provisioner = database['provisioner']
    provisioner_password = database['provisioner_password']

# yaml configuration: application attributes
with open(prepath + '/application.yaml', 'r') as stream:
    settings = yaml.load(stream)
    models = settings['application']['model_type']

# yaml configuration: general attributes
with open(prepath + '/common.yaml', 'r') as stream:
    settings = yaml.load(stream)
    host = settings['general']['host']

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

    # general permission
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS Permission (
                        PermissionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        foreign key (PermissionEntityID) references PermissionEntity(PermissionEntityID),
                        foreign key (PermissionValueID) references PermissionValue(PermissionEntityID),
                    );
                    '''
    cur.execute(sql_statement)

    # superclass for PermissionEntityXXX subclasses
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS PermissionEntity (
                        PermissionEntityID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    );
                    '''
    cur.execute(sql_statement)

    # PermissionEntity subclass
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS PermissionEntityCollection (
                        PermissionEntityID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    );
                    '''
    cur.execute(sql_statement)

    # PermissionEntity subclass
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS PermissionEntityModel (
                        PermissionEntityID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    );
                    '''
    cur.execute(sql_statement)

    # PermissionEntity subclass
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS PermissionEntityResult (
                        PermissionEntityId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    );
                    '''
    cur.execute(sql_statement)

    # numeric codified permission value
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS PermissionValue (
                        PermissionValueID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        PermissionValueCode INT NOT NULL,
                    );
                    '''
    cur.execute(sql_statement)
