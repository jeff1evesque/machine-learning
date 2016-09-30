### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
###
class package::dos2unix {
    ## local variables
    $hiera_dev = hiera('development')
    $version   = $hiera_dev['apt']['dos2unix']

    package { 'tofrodos':
        ensure => $version,
    }
}