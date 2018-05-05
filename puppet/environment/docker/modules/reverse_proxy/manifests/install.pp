###
### install.pp, install nginx.
###
class reverse_proxy::install {
    ## local variables
    $package_version     = $::reverse_proxy::version
    $reverse_proxy_start = $::reverse_proxy::run

    ## install reverse proxy
    class { 'nginx':
        package_ensure => $package_version,
        service_ensure => $reverse_proxy_start,
    }
}
