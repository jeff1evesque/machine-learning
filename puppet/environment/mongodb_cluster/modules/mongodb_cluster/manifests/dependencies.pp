###
### Configures mongodb cluster dependencies.
###
class mongodb_cluster::dependencies {
    ## local variables
    $hiera_database = lookup('database')
    $hiera_mongodb  = $hiera_database['mongodb_cluster']
    $shard1         = $hiera_mongodb['cluster']['shard1']
    $shard2         = $hiera_mongodb['cluster']['shard2']
    $plato          = $shard1['node1']
    $aristotle      = $shard1['node2']
    $socrates       = $shard2['node1']
    $confucius      = $shard2['node2']

    ## recommended repository
    class { '::mongodb::globals':
        manage_package_repo => true,
    }

    ## install mongos server for sharding support
    class { '::mongodb::mongos':
        ensure         => true,
        configdb       => [
            "${plato['host']}:${plato['port']}",
            "${aristotle['host']}:${aristotle['port']}",
            "${socrates['host']}:${socrates['port']}",
            "${confucius['host']}:${confucius['port']}",
        ],
        service_enable => true,
        service_ensure => true,
    }
}
