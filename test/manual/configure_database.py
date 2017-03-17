'''

This module will truncate corresponding database tables, which allow manual
unit tests to be run as many times as needed.

'''

import yaml
import MySQLdb as DB


def configure_database():
    '''

    Empties corresponding database tables, and checks each row count is zero.

    '''

    # local variables
    configuration = '/vagrant/hiera/test/hiera/settings.yaml'

    # yaml configuration: database attributes
    with open(configuration + '/database.yaml', 'r') as stream:
        settings = yaml.load(stream)
        db_ml = settings['database']['name']
        tester = settings['database']['tester']
        tester_password = settings['database']['tester_password']

    # yaml configuration: general attributes
    with open(configuration + '/common.yaml', 'r') as stream:
        settings = yaml.load(stream)
        host = settings['general']['host']

    # create connection
    conn = DB.connect(
        host,
        tester,
        tester_password,
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
            'SELECT COUNT(*) AS n FROM tbl_feature_count HAVING n > 0;'
        )
        count_entity = cur.execute(
            'SELECT COUNT(*) AS n FROM tbl_dataset_entity HAVING n > 0;'
        )
        count_label = cur.execute(
            'SELECT COUNT(*) AS n FROM tbl_observation_label HAVING n > 0;'
        )
        count_svm = cur.execute(
            'SELECT COUNT(*) AS n FROM tbl_svm_data HAVING n > 0;'
        )
        count_svr = cur.execute(
            'SELECT COUNT(*) AS n FROM tbl_svr_data HAVING n > 0;'
        )

    # assert truncate succeeded
    assert count_feature == 0
    assert count_entity == 0
    assert count_label == 0
    assert count_svm == 0
    assert count_svr == 0
