###
### bindings.pp, ensure mariadb bindings.
###
class database::bindings {
    class { '::mysql::bindings':
        python_enable => true,
    }
    contain mysql::bindings
}