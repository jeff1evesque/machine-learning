###
### init.pp: install client, and initialize database tables.
###

class mariadb_cluster {
    ## install mariadb
    contain mariadb_cluster::server

    ## install mariadb client
    contain mariadb_cluster::client

    ## install mariad bindings
    contain mariadb_cluster::bindings

    ## create database tables
    contain mariadb_cluster::database
}
contain mariadb_cluster