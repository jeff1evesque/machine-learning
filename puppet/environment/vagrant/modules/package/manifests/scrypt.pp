###
### scrypt.pp, install package.
###
class package::scrypt {
    require python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['scrypt']

    package { 'scrypt':
        ensure   => $version,
        provider => 'pip',
    }
}
