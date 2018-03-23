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

    # ################################################################################# #
    # LEGACY TABLES: these tables will be iteratively phased out, as corresponding      #
    #                backend and frontend are developed.                                #
    # ################################################################################# #

    # create 'tbl_user'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_user (
                        id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR (50) NOT NULL,
                        email VARCHAR (255) NOT NULL,
                        password VARCHAR (1069) NOT NULL,
                        datetime_joined DATETIME NOT NULL,
                        INDEX (username)
                    );
                    '''
    cur.execute(sql_statement)

    # create 'tbl_dataset_entity'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_dataset_entity (
                        id_entity INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR (50) NOT NULL,
                        collection VARCHAR (50) NOT NULL UNIQUE,
                        model_type INT NOT NULL,
                        uid_created INT NOT NULL,
                        datetime_created DATETIME NOT NULL,
                        uid_modified INT NULL,
                        datetime_modified DATETIME NULL,
                        INDEX (id_entity)
                    );
                    '''
    cur.execute(sql_statement)

    # create 'tbl_model_type'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_model_type (
                        id_model INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        model VARCHAR (50) NOT NULL,
                        INDEX (id_model)
                    );
                    '''
    cur.execute(sql_statement)

    # populate 'tbl_model_type'
    sql_statement = '''\
                    INSERT INTO tbl_model_type (model) VALUES (%s);
                    '''
    cur.executemany(sql_statement, models)

    # create 'tbl_prediction_results'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_prediction_results (
                        id_result INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        model_type INT NOT NULL,
                        title VARCHAR (50) NOT NULL,
                        result VARCHAR (30) NOT NULL,
                        uid_created INT NOT NULL,
                        datetime_created DATETIME NOT NULL,
                        INDEX (title)
                    );
                    '''
    cur.execute(sql_statement)

    # create 'tbl_svm_results_class'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_svm_results_class (
                        id_class INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_result INT NOT NULL,
                        class VARCHAR (50) NOT NULL
                    );
                    '''
    cur.execute(sql_statement)

    # create 'tbl_svm_results_probability'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_svm_results_probability (
                        id_probability INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_result INT NOT NULL,
                        probability DECIMAL (65,12) NOT NULL
                    );
                    '''
    cur.execute(sql_statement)

    # create 'tbl_svm_results_decision_function'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_svm_results_decision_function (
                        id_decision_function INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_result INT NOT NULL,
                        decision_function DECIMAL (65,12) NOT NULL
                    );
                    '''
    cur.execute(sql_statement)

    # create 'tbl_svr_results_r2'
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_svr_results_r2 (
                        id_r2 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_result INT NOT NULL,
                        r2 DECIMAL (65,12) NOT NULL
                    );
                    '''
    cur.execute(sql_statement)

    # ################################################################################# #
    # NEW STRUCTURE: when the above legacy tables have been completely phased out, the  #
    #                below tables will completely define our sql implementation.        #
    # ################################################################################# #

    # stored functions: time based uuid
    #
    # Note: https://mariadb.com/kb/en/library/guiduuid-performance/#code-to-do-it
    #
    sql_statement = '''\
                    CREATE FUNCTION UuidToBin(_uuid BINARY(36))
                        RETURNS BINARY(16)
                        LANGUAGE SQL  DETERMINISTIC  CONTAINS SQL  SQL SECURITY INVOKER
                    RETURN
                        UNHEX(CONCAT(
                            SUBSTR(_uuid, 15, 4),
                            SUBSTR(_uuid, 10, 4),
                            SUBSTR(_uuid,  1, 8),
                            SUBSTR(_uuid, 20, 4),
                            SUBSTR(_uuid, 25))
                        );
                    '''
    cur.execute(sql_statement)

    sql_statement = '''\
                    CREATE FUNCTION UuidFromBin(_bin BINARY(16))
                        RETURNS BINARY(36)
                        LANGUAGE SQL  DETERMINISTIC  CONTAINS SQL  SQL SECURITY INVOKER
                    RETURN
                        LCASE(CONCAT_WS('-',
                            HEX(SUBSTR(_bin,  5, 4)),
                            HEX(SUBSTR(_bin,  3, 2)),
                            HEX(SUBSTR(_bin,  1, 2)),
                            HEX(SUBSTR(_bin,  9, 2)),
                            HEX(SUBSTR(_bin, 11))
                    ));
                    '''
    cur.execute(sql_statement)

    # user and roles
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS User (
                        UserID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        UserName VARCHAR (50) NOT NULL,
                        Password VARCHAR (1069) NOT NULL,
                        Joined DATETIME NOT NULL,
                    );

                    CREATE TABLE IF NOT EXISTS Role (
                        RoleID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        Role VARCHAR (50) NOT NULL,
                        foreign key (RoleID) references Role(RoleID),
                    );
                    '''
    cur.execute(sql_statement)

    # general permission
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS PermissionUUID (
                        PermissionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        PermissionType INT NOT NULL,
                    );

                    CREATE TABLE IF NOT EXISTS Permission (
                        PermissionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        foreign key (PermissionValueID) references PermissionValue(PermissionValueID),
                        foreign key (UserID) references User(UserID),
                        foreign key (PermissionType) references PermissionUUID(PermissionType),
                    );

                    CREATE TABLE IF NOT EXISTS PermissionCollection (
                        PermissionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        foreign key (OwnID) references Own(OwnID),
                    );

                    CREATE TABLE IF NOT EXISTS PermissionModel (
                        PermissionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        foreign key (OwnID) references Own(OwnID),
                    );

                    CREATE TABLE IF NOT EXISTS PermissionResult (
                        PermissionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        foreign key (OwnID) references Own(OwnID),
                    );

                    CREATE TABLE IF NOT EXISTS PermissionValue (
                        PermissionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        foreign key (OwnID) references Own(OwnID),
                    );
                    '''
    cur.execute(sql_statement)

    # permission based
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS OwnUUID (
                        OwnID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        OwnType INT NOT NULL,
                    );

                    CREATE TABLE IF NOT EXISTS Own (
                        OwnID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        foreign key (UserID) references User(UserID),
                        foreign key (OwnType) references OwnUUID(OwnType),
                    );

                    CREATE TABLE IF NOT EXISTS Collection (
                        OwnID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        CollectionTitle VARCHAR (50) NOT NULL,
                        CollectionVersion VARCHAR (50) NOT NULL,
                    );

                    CREATE TABLE IF NOT EXISTS Model (
                        PermissionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        Model BLOB NOT NULL,
                    );

                    CREATE TABLE IF NOT EXISTS Result (
                        OwnID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        foreign key (ResultValueID) references ResultValue(ResultValueID),
                        foreign key (ModelTypeID) references ModelType(ModelTypeID),
                    );

                    CREATE TABLE IF NOT EXISTS ModelType (
                        ModelTypeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        ModelType VARCHAR (50) NOT NULL,
                    );

                    CREATE TABLE IF NOT EXISTS ResultValue (
                        ResultValueID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        ResultValueActual DECIMAL (65,12) NOT NULL,
                        foreign key (ResultValueParameterID) references ResultValueParameter(ResultValueParameterID),
                        foreign key (ResultID) references Result(ResultID),
                    );
                    '''
    cur.execute(sql_statement)
