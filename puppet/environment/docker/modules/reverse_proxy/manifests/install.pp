###
### install.pp, install nginx.
###
class reverse_proxy::install {
    class { 'nginx':
        package_ensure => $reverse_proxy::version,
    }
}
