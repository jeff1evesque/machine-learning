###
### python_dev.pp, install package.
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
