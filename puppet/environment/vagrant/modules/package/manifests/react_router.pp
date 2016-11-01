### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::react_router {
    ## local variables
    $hiera_dev = hiera('development')
    $version   = $hiera_dev['npm']['react-router']

    ## package: install general packages (npm)
    package { "react-router@${version}":
        ensure   => 'present',
        provider => 'npm',
    }
}