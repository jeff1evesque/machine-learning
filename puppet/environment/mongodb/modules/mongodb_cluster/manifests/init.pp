###
### Configures mongodb cluster
###

class mongodb_cluster {
    contain mongodb_cluster::install
    contain mongodb_cluster::databases
}