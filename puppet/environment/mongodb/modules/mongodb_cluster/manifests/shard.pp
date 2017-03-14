###
### Configures mongodb cluster (shard1).
###
class mongodb_cluster::shard {
    ## local variables
    $hiera_database    = lookup('database')
    $hiera_mongodb     = lookup('mongodb_node')
    $mongodb_node      = $hiera_mongodb['mongodb_node']
    $hiera_user        = $hiera_database['mongodb_cluster']['user']
    $admin_user        = $hiera_user['admin']['name']
    $admin_password    = $hiera_user['admin']['password']
    $mongodb_host      = $mongodb_node['host']
    $mongodb_port      = $mongodb_node['port']
    $mongodb_auth      = $mongodb_node['auth']
    $mongodb_configsvr = $mongodb_node['configsvr']
    $mongodb_shardsvr = $mongodb_node['shardsvr']
    $mongodb_replset   = $mongodb_node['replset']
    $mongodb_verbose   = $mongodb_node['verbose']
    $mongodb_keyfile   = $mongodb_node['keyfile']
    $mongodb_key       = $mongodb_node['key']

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
