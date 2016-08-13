### Note: the prefix 'database::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class database::bindings {
    class { '::mysql::bindings':
        python_enable => true,
    }
    contain mysql::bindings
}