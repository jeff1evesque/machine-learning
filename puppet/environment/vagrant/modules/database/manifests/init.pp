###
### init.pp: install client, and initialize database tables.
###

class database {
    ## install sql
    class install_sql {
        ## install mariadb
        contain database::server

        ## install mariadb client
        contain database::client

        ## install mariad bindings
        contain database::bindings
    }

    ## create database tables
    class create_db {
        require install_sql
        contain database::database
    }

    ## initiate
    include create_db
}