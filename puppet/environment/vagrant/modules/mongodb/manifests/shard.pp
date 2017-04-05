###
### Run mongod instance.
###
class mongodb_cluster::shard {
    ## local variables
    ##
    ## @replset, yaml hash converted to a json string.
    ##
    $mongodb_node  = lookup('mongodb_node')
    $replication   = $mongodb_node['replication']
    $sharding      = $mongodb_node['sharding']
    $initiate_ip   = $sharding['initiate']['ip']
    $initiate_port = $sharding['initiate']['port']
    $replset       = inline_template("<%= require 'json'; @replication['replset'].to_json %>")

    ## initiate config server
    exec { 'initiate-replset-configsrv':
        command  => "mongo --host ${initiate_ip} --port ${initiate_port} --eval 'rs.initiate(${replset});'",
        onlyif   => [
            "mongo --host ${initiate_ip} --port ${initiate_port} --quiet --eval 'quit();'",
            "mongo --host ${initiate_ip} --port ${initiate_port} --quiet --eval 'rs.status()[\"ok\"]');",
        ],
        path     => '/usr/bin',
    }
}