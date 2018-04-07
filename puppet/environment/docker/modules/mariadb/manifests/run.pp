###
### run.pp, start mariadb.
###
class webserver::run {
    ## local variables
    $start_mariadb = $::mariadb::run

    ## mariadb service
    service { 'mysqld':
        ensure     => $start_mariadb,
        enable     => $start_mariadb,
    }
}
