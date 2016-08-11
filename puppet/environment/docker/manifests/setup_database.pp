### setup_database.pp: install client, and initialize database tables.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## install sql
class install_sql {
    ## install mariadb
    include database::server

    ## install mariadb client
    include database::client

    ## install mariad bindings
    include database::bindings
}

## create database tables
class create_db {
    require install_sql
    include database::database
}

## initiate
include create_db

