###
### run.pp, start mariadb.
###
class mariadb::run {
    ## local variables
    $start_mariadb = $::mariadb::run

    ## mariadb service
    service { 'mysqld':
        ensure     => $start_mariadb,
        enable     => $start_mariadb,
    }
}
