###
### install.pp, install nginx.
###
class nginx::service {
    class { 'nginx':
        package_ensure  => $nginx::version
    }
}
