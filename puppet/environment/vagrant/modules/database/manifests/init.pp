###
### init.pp: install client, and initialize database tables.
###

class database {
    contain database::server
    contain database::client
    contain database::bindings
    contain database::database
}