###
### Install required components for mongodb cluster.
###
class mongodb_cluster::install {
    ## local variables
    $hiera_database     = lookup('database')
    $hiera_mongodb      = lookup('mongodb_node')
    $hiera_user         = $hiera_database['mongodb_cluster']['user']
    $admin_user         = $hiera_user['admin']['name']
    $admin_password     = $hiera_user['admin']['password']
    $mongodb_ip         = $hiera_mongodb['ip']
    $mongodb_host       = $hiera_mongodb['host']
    $mongodb_port       = $hiera_mongodb['port']
    $mongodb_auth       = $hiera_mongodb['auth']
    $mongodb_replset    = $hiera_mongodb['replset']
    $mongodb_smallfiles = $hiera_mongodb['smallfiles']
    $mongodb_configsvr  = $hiera_mongodb['configsvr']
    $mongodb_verbose    = $hiera_mongodb['verbose']
    $mongodb_keyfile    = $hiera_mongodb['keyfile']
    $mongodb_key        = $hiera_mongodb['key']
    $mongodb_10gen      = $hiera_mongodb['manage_package_repo']

    ## recommended repository
    class { '::mongodb::globals':
        manage_package_repo => $mongodb_10gen,
    }

    ## mongodb node
    class { '::mongodb::server':
        bind_ip        => $mongodb_ip,
        port           => $mongodb_port,
        verbose        => $mongodb_verbose,
        auth           => $mongodb_auth,
        smallfiles     => $mongodb_smallfiles,
        configsvr      => $mongodb_configsvr,
        admin_username => $admin_user,
        admin_password => $admin_password,
        replset        => $mongodb_replset,
    }
}
