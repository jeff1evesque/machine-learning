###
### Configures mongodb cluster dependencies.
###
class mongodb_cluster::dependencies {
    ## local variables
    $hiera_mongodb  = lookup('mongodb_cluster')
    $shard1         = $hiera_mongodb['shard']['shard1']
    $plato          = $shard1['cluster1']['node1']
    $aristotle      = $shard1['cluster1']['node2]

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
