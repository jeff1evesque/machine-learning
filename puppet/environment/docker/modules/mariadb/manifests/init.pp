###
### init.pp: install client, and initialize database tables.
###

class mariadb {
    ## install mariadb
    contain mariadb::server

    ## install mariadb client
    contain mariadb::client

    ## install mariad bindings
    contain mariadb::bindings

    ## create database tables
    contain mariadb::database
}
contain mariadb