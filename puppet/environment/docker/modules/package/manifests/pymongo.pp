###
### pymongo.pp, install package.
###
class package::pymongo {
    require python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['custom']['pymongo']

    package { 'pymongo':
        ensure   => $version,
        provider => 'pip',
    }
}