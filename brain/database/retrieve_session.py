#!/usr/bin/python

"""@retrieve_session

This file retrieves the 'svm_title', and 'id_entity' properties.

"""

from brain.database.db_query import SQL


class Retrieve_Session(object):
    """
    @Retrieve_Session

    This class provides an interface to retrieve the 'svm_title', and
    'id_entity' from the 'tbl_dataset_entity' sql database table.

    Note: this class is invoked within 'views.py'

    Note: this class explicitly inherits the 'new-style' class.

    """

    def __init__(self):
        """@__init__

        This constructor is responsible for defining class variables.

        """

        self.list_error = []
        self.sql        = SQL()

    def get_all_sessions(self):
        """@get_all_sessions

        This method is responsible for retrieving all sessions from the
        'tbl_dataset_entity' sql database table.

        """

        # local variables
        list_session = []

        # sql query
        self.sql.sql_connect('db_machine_learning')
        sql_statement = 'SELECT id_entity, title FROM tbl_dataset_entity'
        response      = self.sql.sql_command(sql_statement, 'select')

        # rebuild session list, get error(s) if any
        if response['result']:
            for item in response['result']:
                list_session.append({'id': item[0], 'title': item[1]})
            response_error = self.sql.get_errors()
        else:
            response_error = 'no previous session found in database'

        # disconnect from database
        self.sql.sql_disconnect()

        # return result
        if response_error:
            return {'result': None, 'error': response_error}
        else:
            return {'result': list_session, 'error': None}