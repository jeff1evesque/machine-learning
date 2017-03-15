###
### bindings.pp, ensure mariadb bindings.
###
class mariadb_cluster::bindings {
    class { '::mysql::bindings':
        python_enable => true,
    }
    contain mysql::bindings
}