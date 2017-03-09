###
### Configures mongodb cluster
###

class mongodb_cluster {
    contain mongodb_cluster::dependencies
    contain mongodb_cluster::shard1
    contain mongodb_cluster::shard2
    contain mongodb_cluster::databases
}