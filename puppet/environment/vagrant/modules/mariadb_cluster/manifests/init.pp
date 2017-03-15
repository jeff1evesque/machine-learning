###
### init.pp: install client, and initialize database tables.
###

class mariadb_cluster {
    contain mariadb_cluster::server
    contain mariadb_cluster::client
    contain mariadb_cluster::bindings
    contain mariadb_cluster::database
}