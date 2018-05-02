###
### run.pp, start redis-server.
###
class redis::run {
    ## local variables
    $start_redis = $::redis::run

    ## mariadb service
    service { 'redis-server':
        ensure   => $start_redis,
        enable   => $start_redis,
    }
}
