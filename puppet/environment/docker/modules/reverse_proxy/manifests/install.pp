###
### install.pp, install nginx.
###
class reverse_proxy::service {
    class { 'nginx':
        package_ensure  => $nginx::version
    }
}
