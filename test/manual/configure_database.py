'''@configure_database

This module will truncate database tables.

'''

import yaml
import MySQLdb as DB


def configure_database():
    # local variables
    configuration = '/vagrant/hiera/test/hiera/settings.yaml'

    # define configuration
    with open(configuration, 'r') as stream:
        # local variables
        settings = yaml.load(stream)
        host = settings['general']['host']
        db_ml = settings['database']['name']
        provisioner = settings['database']['provisioner']
        provisioner_password = settings['database']['provisioner_password']

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

            # truncate 'tbl_feature_count'
            sql_statement = 'TRUNCATE TABLE tbl_feature_count;'
            cur.execute(sql_statement)

            # create 'tbl_dataset_entity'
            sql_statement = 'TRUNCATE TABLE tbl_dataset_entity;'
            cur.execute(sql_statement)

            # create 'tbl_observation_label'
            sql_statement = 'TRUNCATE TABLE tbl_observation_label;'
            cur.execute(sql_statement)

            # create 'tbl_svm_data'
            sql_statement = 'TRUNCATE TABLE tbl_svm_data;'
            cur.execute(sql_statement)

            # create 'tbl_svr_data'
            sql_statement = 'TRUNCATE TABLE tbl_svr_data;'
            cur.execute(sql_statement)
