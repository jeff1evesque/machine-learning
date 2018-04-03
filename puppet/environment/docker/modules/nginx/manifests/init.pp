###
### init.pp: configure, and start nginx.
###
class nginx (
    $type        = $::nginx::params::type,
    $vhost       = $::nginx::params::vhost,
    $host_port   = $::nginx::params::host_port,
    $listen_port = $::nginx::params::listen_port,
    $proxy       = $::nginx::params::proxy,
) inherits ::nginx::params {
    ## ensure log directory
    require system::log_directory

    ## configure nginx
    class { 'nginx::install': } ->
    class { 'nginx::config': } ->
    class { 'nginx::ssl': } ~>
    class { 'nginx::service': } ->
    Class['nginx']
}
contain nginx
