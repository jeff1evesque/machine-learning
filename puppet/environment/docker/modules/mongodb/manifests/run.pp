###
### run.pp, run mongod instance.
###
class mongodb::run {
    ## local variables
    $start_mongodb = $::mongodb::run

    ## enforce mongod init script
    ##
    ## @enable, ensure 'mongod' service starts on boot.
    ##
    service { 'mongod':
        ensure  => $start_mongodb,
        enable  => $start_mongodb,
        flags   => [
            '--config',
            '/etc/mongod.conf',
        ],
    }
}
