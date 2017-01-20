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

    Note: this class is invoked within 'db_query.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.db_host = current_app.config.get('DB_HOST')
        self.db_username = current_app.config.get('DB_USERNAME')
        self.db_password = current_app.config.get('DB_PASSWORD')

    def get_db_host(self):
        '''

        This method is responsible for getting the database host.

        '''

        return self.db_host

    def get_db_username(self):
        '''

        This method is responsible for getting the database username.

        '''

        return self.db_username

    def get_db_password(self):
        '''

        This method is responsible for getting the database user password.

        '''

        return self.db_password

    def set_db_host(self, host):
        '''

        This method is responsible for setting the database host.

        '''

        self.db_host = host

    def set_db_username(self, user):
        '''

        This method is responsible for setting the database username.

        '''

        self.db_username = user

    def set_db_password(self, pwd):
        '''

        This method is responsible for setting the database user password.

        '''

        self.db_password = pwd
