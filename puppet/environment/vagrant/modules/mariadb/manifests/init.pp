###
### init.pp: install client, and initialize database tables.
###

class mariadb {
    contain database::server
    contain database::client
    contain database::bindings
    contain database::database
}