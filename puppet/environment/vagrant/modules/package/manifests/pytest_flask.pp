### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
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