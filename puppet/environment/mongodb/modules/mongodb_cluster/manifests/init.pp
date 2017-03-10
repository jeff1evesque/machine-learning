###
### Configures mongodb cluster
###

class mongodb_cluster {
    contain mongodb_cluster::dependencies
    contain mongodb_cluster::shard
    contain mongodb_cluster::databases
}