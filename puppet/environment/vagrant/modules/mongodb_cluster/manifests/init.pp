###
### Configures mongodb cluster
###

## local variables: conditionally load hiera
$hiera_mongodb = lookup('mongodb_cluster')
$shard2        = $hiera_mongodb['shard']['shard1']['implement']

## implement mongodb cluster
contain mongodb_cluster::dependencies
contain mongodb_cluster::shard1
if ($shard2) {
    contain mongodb_cluster::shard2
}
contain mongodb_cluster::databases
