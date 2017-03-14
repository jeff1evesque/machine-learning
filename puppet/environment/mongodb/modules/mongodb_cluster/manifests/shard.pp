###
### Configures mongodb cluster (shard1).
###
class mongodb_cluster::shard {
    ## local variables
    $hiera_database    = lookup('database')
    $hiera_mongodb     = lookup('mongodb_node')
    $hiera_user        = $hiera_database['mongodb_cluster']['user']
    $admin_user        = $hiera_user['admin']['name']
    $admin_password    = $hiera_user['admin']['password']
    $mongodb_host      = $hiera_mongodb['host']
    $mongodb_port      = $hiera_mongodb['port']
    $mongodb_auth      = $hiera_mongodb['auth']
    $mongodb_configsvr = $hiera_mongodb['configsvr']
    $mongodb_shardsvr  = $hiera_mongodb['shardsvr']
    $mongodb_replset   = $hiera_mongodb['replset']
    $mongodb_verbose   = $hiera_mongodb['verbose']
    $mongodb_keyfile   = $hiera_mongodb['keyfile']
    $mongodb_key       = $hiera_mongodb['key']

    ## mongodb node
    class { '::mongodb::server':
        port           => $mongodb_port,
        verbose        => $mongodb_verbose,
        auth           => $mongodb_auth,
        configsvr      => $mongodb_configsvr,
        shardsvr       => $mongodb_shardsvr,
        replset        => $mongodb_replset,
        keyfile        => $mongodb_keyfile,
        key            => $mongodb_key,
        admin_username => $admin_user,
        admin_password => $admin_password,
        replset_config => {
            $mongodb_replset => {
                ensure  => present,
                members => "${mongodb_host}:${mongodb_port}"
            }
        }
    }

    ## add node to the shard
    mongodb_shard { $mongodb_shardsvr:
        member => "${mongodb_shardsvr}/${mongodb_host}:${mongodb_port}",
        keys   => [{$mongodb_keyfile => {'name' => $mongodb_key}}],
    }
}
