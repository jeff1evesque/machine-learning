###
### init.pp: install client, and initialize database tables.
###
class mariadb (

) inherits ::mariadb::params {
    class { 'mariadb::server' } ->
    class { 'mariadb::client' } ->
    class { 'mariadb::bindings' } ->
    class { 'mariadb::database' } ->
    class { 'mariadb::run' } ->
    Class['mariadb']
}
