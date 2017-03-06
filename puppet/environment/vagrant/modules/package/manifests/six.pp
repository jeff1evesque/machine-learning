###
### six.pp, install package.
###
class package::six {
    require python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['six']

    package { 'six':
        ensure   => $version,
        provider => 'pip',
    }
}