#!/usr/bin/python

## @db_settings.py
#  This file contains various python configuration settings.

## Database: when instantiating this class, or defining any of the class variables,
#            make sure they are defined within the DBMS. This can be achieved via
#            the terminal console (or phpMyAdmin):
#
#                $ mysql -u root -p
#                MariaDB> CREATE USER 'authenticated'@'localhost' IDENTIFIED BY
#                    ->'password';
#                MariaDB> GRANT, CREATE, DELETE, DROP, EXECUTE, SELECT, SHOW
#                    -> DATABASES ON *.* TO 'authenticated'@'localhost';
#                MariaDB> FLUSH PRIVILEGES;
class Database:

  ## constructor:
  def __init__(self):
    self.db_host     = 'localhost'
    self.db_username = 'authenticated'
    self.db_password = 'password'

  ## get_db_host: get the database host
  def get_db_host(self):
    return self.db_host

  ## get_db_username: get the database username
  def get_db_username(self):
    return self.db_username

  ## get_db_password: get the database user password
  def get_db_password(self):
    return self.db_password

  ## set_db_host: define the database host
  def set_db_host(self, host):
    self.db_host = host

  ## set_db_username: define the database user
  def set_db_username(self, user):
    self.db_username = user

  ## set_db_password: define the database user password
  def set_db_password(self, pwd):
    self.db_password = pwd
