### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
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