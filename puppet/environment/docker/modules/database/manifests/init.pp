###
### init.pp: install client, and initialize database tables.
###

class database {
    ## install mariadb
    contain database::server

    ## install mariadb client
    contain database::client

    ## install mariad bindings
    contain database::bindings

    ## create database tables
    contain database::database
}
