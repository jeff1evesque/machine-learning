###
### redis_client.pp, install package.
###
class package::redis_client {
    require python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['custom']['redis']

    package { 'redis':
        ensure   => $version,
        provider => 'pip',
    }
}