###
### init.pp: install client, and initialize database tables.
###

class mariadb {
    contain mariadb::server
    contain mariadb::client
    contain mariadb::bindings
    contain mariadb::database
}