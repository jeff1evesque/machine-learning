###
### pytest_flask.pp, install package.
###
class package::pytest_flask {
    require python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['pytest-flask']

    package { 'pytest-flask':
        ensure   => $version,
        provider => 'pip',
    }
}