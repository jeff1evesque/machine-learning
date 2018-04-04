###
### install.pp, install nginx.
###
class reverse_proxy::install {
    ## local variables
    $package_version = $::reverse_proxy::version

    ## install reverse proxy
    class { 'nginx':
        package_ensure => $package_version,
    }
}
