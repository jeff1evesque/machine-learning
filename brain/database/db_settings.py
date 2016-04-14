#!/usr/bin/python

"""@db_settings

This file defines SQL database configurations.

"""

from settings import HOST, DB_USERNAME, DB_PASSWORD, DB_LOG


class Database(object):
    """@Database

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

    """

    def __init__(self):
        """@__init__

        This constructor is responsible for defining class variables.

        """

        self.db_host = HOST
        self.db_username = DB_USERNAME
        self.db_password = DB_PASSWORD
        self.db_log = DB_LOG

    def get_db_host(self):
        """@get_db_host

        This method is responsible for getting the database host.

        """

        return self.db_host

    def get_db_username(self):
        """@get_db_username

        This method is responsible for getting the database username.

        """

        return self.db_username

    def get_db_password(self):
        """@get_db_password

        This method is responsible for getting the database user password.

        """

        return self.db_password

    def get_db_log(self):
        """@get_db_log

        This method is responsible for getting the database log directory path.

        """

        return self.db_log

    def set_db_host(self, host):
        """@set_db_host

        This method is responsible for setting the database host.

        """

        self.db_host = host

    def set_db_username(self, user):
        """@set_db_username

        This method is responsible for setting the database username.

        """

        self.db_username = user

    def set_db_password(self, pwd):
        """@set_db_password

        This method is responsible for setting the database user password.

        """

        self.db_password = pwd

    def set_db_log(self, path):
        """@set_db_log

        This method is responsible for setting the database log directory path.

        """

        self.db_log = path
