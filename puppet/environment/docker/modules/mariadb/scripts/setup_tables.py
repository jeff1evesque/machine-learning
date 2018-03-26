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
    model_types = settings['application']['model_type']
    result_types = settings['application']['result_type']

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
    cur.executemany(sql_statement, model_types)

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

    # ################################################################################# #
    #                                                                                   #
    # user and roles                                                                    #
    #                                                                                   #
    # @RoleOwner, whether role is owned, or given.                                      #
    #                                                                                   #
    # ################################################################################# #
    query = '''\
            CREATE TABLE IF NOT EXISTS Account (
                UserID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR (50) NOT NULL,
                Password VARCHAR (1069) NOT NULL,
                Joined DATETIME NOT NULL
            );
            '''
    cur.execute(query)

    query = '''\
            CREATE TABLE IF NOT EXISTS RoleType (
                RoleTypeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                RoleType VARCHAR (1069) NOT NULL
            );
            '''
    cur.execute(query)

    query = '''\
            CREATE TABLE IF NOT EXISTS Role (
                RoleID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                RoleOwner INT NOT NULL,
                RoleTypeID INT NOT NULL,
                UserID INT NOT NULL,
                UNIQUE (RoleTypeID, UserID),
                FOREIGN KEY (RoleTypeID) REFERENCES RoleType(RoleTypeID),
                FOREIGN KEY (UserID) REFERENCES Account(UserID)
            );
            '''
    cur.execute(query)

    # ################################################################################# #
    #                                                                                   #
    # collection                                                                        #
    #                                                                                   #
    # ################################################################################# #
    query = '''\
            CREATE TABLE IF NOT EXISTS Collection (
                CollectionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                CollectionName VARCHAR (50) NOT NULL,
                CollectionVersion INT NOT NULL
            );
            '''
    cur.execute(query)

    # ################################################################################# #
    #                                                                                   #
    # model                                                                             #
    #                                                                                   #
    # ################################################################################# #
    query = '''\
            CREATE TABLE IF NOT EXISTS ModelType (
                ModelTypeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                ModelType VARCHAR (50) NOT NULL
            );
            '''
    cur.execute(query)

    query = '''\
            CREATE TABLE IF NOT EXISTS Model (
                ModelID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                ModelName VARCHAR (50) NOT NULL,
                Model BLOB NOT NULL,
                ModelTypeID INT NOT NULL,
                FOREIGN KEY (ModelTypeID) REFERENCES ModelType(ModelTypeID)
            );
            '''
    cur.execute(query)

    # ################################################################################# #
    #                                                                                   #
    # results                                                                           #
    #                                                                                   #
    # ################################################################################# #
    query = '''\
            CREATE TABLE IF NOT EXISTS ResultType (
                ResultTypeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                ResultType VARCHAR (50) NOT NULL
            );
            '''
    cur.execute(query)

    query = '''\
            CREATE TABLE IF NOT EXISTS Result (
                ResultID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                ResultValue DECIMAL (65,12) NOT NULL,
                ModelTypeID INT (50) NOT NULL,
                ResultTypeID INT NOT NULL,
                FOREIGN KEY (ModelTypeID) REFERENCES ModelType(ModelTypeID),
                FOREIGN KEY (ResultTypeID) REFERENCES ResultType(ResultTypeID)
            );
            '''
    cur.execute(query)

    # ################################################################################# #
    #                                                                                   #
    # applied permission                                                                #
    #                                                                                   #
    # ################################################################################# #
    query = '''\
            CREATE TABLE IF NOT EXISTS PermissionCollection (
                PermissionCollectionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                PermissionValueCode INT NOT NULL,
                CollectionID INT NOT NULL,
                UserID INT NOT NULL,
                RoleID INT DEFAULT 0,
                UNIQUE (CollectionID, UserID, RoleID),
                FOREIGN KEY (CollectionID) REFERENCES Collection(CollectionID),
                FOREIGN KEY (UserID) REFERENCES Account(UserID),
                FOREIGN KEY (RoleID) REFERENCES Role(RoleID)
            );
            '''
    cur.execute(query)

    query = '''\
            CREATE TABLE IF NOT EXISTS PermissionModel (
                PermissionModelID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                PermissionValueCode INT NOT NULL,
                ModelID INT NOT NULL,
                UserID INT NOT NULL,
                RoleID INT DEFAULT 0,
                UNIQUE (ModelID, UserID, RoleID),
                FOREIGN KEY (ModelID) REFERENCES Model(ModelID),
                FOREIGN KEY (UserID) REFERENCES Account(UserID),
                FOREIGN KEY (RoleID) REFERENCES Role(RoleID)
            );
            '''
    cur.execute(query)

    query = '''\
            CREATE TABLE IF NOT EXISTS PermissionResult (
                PermissionResultID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                PermissionValueCode INT NOT NULL,
                ResultID INT NOT NULL,
                UserID INT NOT NULL,
                RoleID INT DEFAULT 0,
                UNIQUE (ResultID, UserID, RoleID),
                FOREIGN KEY (ResultID) REFERENCES Result(ResultID),
                FOREIGN KEY (UserID) REFERENCES Account(UserID),
                FOREIGN KEY (RoleID) REFERENCES Role(RoleID)
            );
            '''
    cur.execute(query)

    # ################################################################################# #
    #                                                                                   #
    # populate User, and Role                                                                     #
    #                                                                                   #
    # ################################################################################# #
    query = '''\
            INSERT INTO Account (Username, Password, Joined) VALUES (%s, %s, %s);
            '''
    cur.execute(query, ('anonymous', '0', '2018-01-25 12:00:00'))

    query = '''\
            INSERT INTO RoleType (RoleType) VALUES (%s);
            '''
    cur.execute(query, 'default')

    query = '''\
            INSERT INTO Role (RoleType) VALUES (%s, %s);
            '''
    cur.execute(query, 0)

    # ################################################################################# #
    #                                                                                   #
    # populate ModelType                                                                #
    #                                                                                   #
    # ################################################################################# #
    query = '''\
            INSERT INTO ModelType (ModelType) VALUES (%s);
            '''
    cur.execute(query, model_types)

    # ################################################################################# #
    #                                                                                   #
    # populate ResultType                                                               #
    #                                                                                   #
    # ################################################################################# #
    query = '''\
            INSERT INTO ResultType (ResultType) VALUES (%s);
            '''
    cur.execute(query, result_types)
