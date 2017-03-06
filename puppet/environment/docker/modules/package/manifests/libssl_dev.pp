###
### @libssl_dev.pp, install package.
###
class package::libssl_dev {
    ## update apt-get
    require apt

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['apt']['libssl-dev']

    package { "libssl-dev=${version}":
        ensure => 'installed',
    }
}
