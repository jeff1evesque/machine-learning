###
### Configures mongodb cluster dependencies.
###
class mongodb_cluster::dependencies {
    ## local variables
    $hiera_mongodb = lookup('mongodb_node')
    $mongodb_host  = $hiera_mongodb['fqdn']
    $mongodb_port  = $hiera_mongodb['port']
    $mongodb_10gen = $hiera_mongodb['manage_package_repo']

    ## recommended repository
    class { '::mongodb::globals':
        manage_package_repo => $mongodb_10gen,
    }

    ## install mongos server for sharding support
    class { '::mongodb::mongos':
        ensure         => true,
        configdb       => "${mongodb_host}:${mongodb_port}",
        service_enable => true,
        service_ensure => true,
    }
}
