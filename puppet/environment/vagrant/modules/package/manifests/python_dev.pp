### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::python_dev {
    ## update apt-get
    require apt

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['apt']['python-dev']

    package { "python-dev=${version}":
        ensure => 'installed',
    }
}
