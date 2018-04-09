###
### run.pp, run mongod instance.
###
class mongodb::run {
    ## local variables
    $start_mongodb = $::mongodb::run

    ## enforce mongod
    if $start_mongodb {
        exec { 'start-mongod':
            command => 'mongod --config /etc/mongod.conf',
            path    => '/usr/bin',
            unless  => 'pgrep mongod',
        }
    }
}
