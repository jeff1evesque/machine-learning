### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::fetch {
    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['npm']['fetch']

    ## package: install general packages (npm)
    package { "whatwg-fetch@${version}":
        ensure   => 'present',
        provider => 'npm',
    }
}