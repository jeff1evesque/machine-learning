###
### Configures mongodb cluster (shard2).
###
class mongodb_cluster::shard2 {
    ## local variables
    $hiera_database = lookup('database')
    $hiera_mongodb  = $hiera_database['mongodb_cluster']
    $hiera_user     = $hiera_mongodb['user']
    $shard2         = $hiera_mongodb['cluster']['shard2']
    $socrates       = $shard2['node1']
    $confucius      = $shard2['node2']
    $admin_user     = $hiera_user['admin']['name']
    $admin_password = $hiera_user['admin']['password']

    ## shard 2: master
    class { '::mongodb::server':
        port           => $socrates['port'],
        verbose        => true,
        auth           => true,
        configsvr      => true,
        shardsvr       => true,
        replset        => 'shard2',
#        keyfile        => $socrates['keyfile'],
#        key            => $socrates['key']
        admin_username => $admin_user,
        admin_password => $admin_password,
        replset_config => {
            'shard2' => {
                ensure  => present,
                members => [
                    "${socrates['host']}:${socrates['port']}",
                    "${confucius['host']}:${confucius['port']}",
                ]
            }
        }
    }

    ## shard 2: replication slave (configuration server)
    class { '::mongodb::server':
        port           => $confucius['port'],
        verbose        => true,
        auth           => true,
        replset        => 'shard2',
#        keyfile        => $confucius['keyfile'],
#        key            => $confucius['key']
        admin_username => $admin_user,
        admin_password => $admin_password,
    }

    ## shard 2: add members to the shard
#    mongodb_shard { 'shard2':
#        member => "${socrates['host']}:${socrates['port']}",
#        keys   => [{
#            $socrates['keyfile'] => {'name' => $socrates['key1']}
#            $socrates['keyfile'] => {'name' => $socrates['key2']}
#        }],
#    }
#    mongodb_shard { 'shard2':
#        member => "${confucius['host']}:${confucius['port']}",
#        keys   => [{
#            $confucius['keyfile'] => {'name' => $confucius['key1']}
#            $confucius['keyfile'] => {'name' => $confucius['key2']}
#        }],
#    }
}
