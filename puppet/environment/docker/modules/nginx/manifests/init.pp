###
### init.pp: configure, and start nginx.
###
class nginx (
    $type           = $::nginx::params::type,
    $vhost          = $::nginx::params::vhost,
    $host_port      = $::nginx::params::host_port,
    $listen_port    = $::nginx::params::listen_port,
    $webserver_port = $::nginx::params::webserver_port,
    $proxy          = $::nginx::params::proxy,
    $self_signed    = $::nginx::params::self_signed,
    $cert_path      = $::nginx::params::cert_path,
    $pkey_path      = $::nginx::params::pkey_path,
    $cert_country   = $::nginx::params::country,
    $cert_org       = $::nginx::params::org,
    $cert_state     = $::nginx::params::state,
    $cert_locality  = $::nginx::params::locality,
    $cert_unit      = $::nginx::params::unit,
    $cert_bit       = $::nginx::params::bit,
    $cert_days      = $::nginx::params::days,
) inherits ::nginx::params {
    class { 'nginx::install': } ->
    class { 'nginx::config': } ->
    class { 'nginx::ssl': } ~>
    class { 'nginx::service': } ->
    Class['nginx']
}
