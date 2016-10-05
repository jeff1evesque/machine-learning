'''@configure_database

This module will truncate database tables.

'''

import yaml
import MySQLdb as DB


def configure_database():
    '''

    Empties corresponding database tables, and checks each row count is zero.

    '''

    # local variables
    configuration = '/vagrant/hiera/test/hiera/settings.yaml'

    # truncate tables
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

            # truncate database tables
            cur.execute('TRUNCATE TABLE tbl_feature_count;')
            cur.execute('TRUNCATE TABLE tbl_dataset_entity;')
            cur.execute('TRUNCATE TABLE tbl_observation_label;')
            cur.execute('TRUNCATE TABLE tbl_svm_data;')
            cur.execute('TRUNCATE TABLE tbl_svr_data;')

            # count columns
            count_feature = cur.execute(
                'SELECT COUNT(*) FROM tbl_feature_count;'
            )
            count_entity = cur.execute(
                'SELECT COUNT(*) FROM tbl_dataset_entity;'
            )
            count_label = cur.execute(
                'SELECT COUNT(*) FROM tbl_observation_label;'
            )
            count_svm = cur.execute(
                'SELECT COUNT(*) FROM tbl_svm_data;'
            )
            count_svr = cur.execute(
                'SELECT COUNT(*) FROM tbl_svr_data;'
            )

    # assert truncate succeeded
    assert (
        count_feature == 0 and
        count_entity == 0 and
        count_label == 0 and
        count_svm == 0 and
        count_svr == 0
    )