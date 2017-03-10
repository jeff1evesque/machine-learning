###
### Configures mongodb cluster (shard1).
###
class mongodb_cluster::shard1 {
    ## local variables
    $hiera_database = lookup('database')
    $hiera_mongodb  = $hiera_database['mongodb_cluster']
    $hiera_user     = $hiera_mongodb['user']
    $shard1         = $hiera_mongodb['cluster']['shard1']
    $plato          = $shard1['node1']
    $aristotle      = $shard1['node2']
    $admin_user     = $hiera_user['admin']['name']
    $admin_password = $hiera_user['admin']['password']

    ## shard 1: master
    class { '::mongodb::server':
        port           => $plato['port'],
        verbose        => true,
        auth           => true,
        configsvr      => true,
        shardsvr       => true,
        replset        => 'shard1',
#        keyfile        => $plato['keyfile'],
#        key            => $plato['key']
        admin_username => $admin_user,
        admin_password => $admin_password,
        replset_config => {
            'shard1' => {
                ensure  => present,
                members => [
                    "${plato['host']}:${plato['port']}",
                    "${aristotle['host']}:${aristotle['port']}",
                ]
            }
        }
    }

    ## shard 1: replication slave (configuration sever)
    class { '::mongodb::server':
        port           => $aristotle['port'],
        verbose        => true,
        auth           => true,
        replset        => 'shard1',
#        keyfile        => $aristotle['keyfile'],
#        key            => $aristotle['key']
        admin_username => $admin_user,
        admin_password => $admin_password,
    }

    ## shard 1: add members to the shard
#    mongodb_shard { 'shard1':
#        member => "${plato['host']}:${plato['port']}",
#        keys   => [{
#            $plato['keyfile'] => {'name' => $plato['key1']}
#            $plato['keyfile'] => {'name' => $plato['key2']}
#        }],
#    }
#    mongodb_shard { 'shard1':
#        member => "${aristotle['host']}:${aristotle['port']}",
#        keys   => [{
#            $plato['keyfile'] => {'name' => $plato['key1']}
#            $plato['keyfile'] => {'name' => $plato['key2']}
#        }],
#    }
}
