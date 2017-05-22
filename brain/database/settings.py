#!/usr/bin/python

'''

This file defines SQL database configurations.

'''

from flask import current_app


class Database(object):
    '''

    This class provides an interface to get, or set the following database
    parameters:

        - host
        - username
        - password

    Additionally, this class provides an interface to get, or set the log
    directory path.

    When instantiating this class, or defining any of the class variables, make
    sure the respective sql user is defined within the DBMS, and has adequate
    permissions. This can be done via the terminal console (or phpMyAdmin):

        $ mysql -u root -p
        MariaDB> CREATE USER 'authenticated'@'localhost' IDENTIFIED BY
            ->'password';
        MariaDB> GRANT, CREATE, DELETE, DROP, EXECUTE, SELECT, SHOW
            -> DATABASES ON *.* TO 'authenticated'@'localhost';
        MariaDB> FLUSH PRIVILEGES;

    Note: this class is invoked within 'query.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.sql_host = current_app.config.get('SQL_HOST')
        self.sql_username = current_app.config.get('SQL_USERNAME')
        self.sql_password = current_app.config.get('SQL_PASSWORD')
        self.nosql_host = current_app.config.get('NOSQL_HOST')
        self.nosql_username = current_app.config.get('NOSQL_USERNAME')
        self.nosql_password = current_app.config.get('NOSQL_PASSWORD')
        self.nosql_db = current_app.config.get('NOSQL_DB')

    def get_db_host(self, type='sql'):
        '''

        This method is responsible for getting the database host.

        '''

        if type == 'sql':
            return self.sql_host
        elif type == 'nosql':
            return self.nosql_host

    def get_db(self, type='sql'):
        '''

        This method is responsible for getting the database host.

        '''

        if type == 'sql':
            return self.sql_db
        elif type == 'nosql':
            return self.nosql_db

    def get_db_username(self, type='sql'):
        '''

        This method is responsible for getting the database username.

        '''

        if type == 'sql':
            return self.sql_username
        elif type == 'nosql':
            return self.nosql_username

    def get_db_password(self, type='sql'):
        '''

        This method is responsible for getting the database user password.

        '''

        if type == 'sql':
            return self.sql_password
        elif type == 'nosql':
            return self.nosql_password

    def set_db_host(self, host, type='sql'):
        '''

        This method is responsible for setting the database host.

        '''

        if type == 'sql':
            self.sql_host = host
        elif type == 'nosql':
            self.nosql_host = host

    def set_db_username(self, user, type='sql'):
        '''

        This method is responsible for setting the database username.

        '''

        if type == 'sql':
            self.sql_username = user
        elif type == 'nosql':
            self.nosql_username = user

    def set_db_password(self, pwd, type='sql'):
        '''

        This method is responsible for setting the database user password.

        '''

        if type == 'sql':
            self.sql_password = pwd
        elif type == 'nosql':
            self.nosql_password = pwd
