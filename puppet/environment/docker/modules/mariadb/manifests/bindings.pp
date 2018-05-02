###
### bindings.pp, ensure mariadb bindings.
###
class mariadb::bindings {
    class { '::mysql::bindings':
        python_enable => true,
    }
}