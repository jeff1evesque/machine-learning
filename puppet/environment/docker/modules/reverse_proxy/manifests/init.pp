###
### init.pp: configure, and start nginx reverse_proxy.
###
class reverse_proxy (
    $run            = $::reverse_proxy::params::run,
    $type           = $::reverse_proxy::params::type,
    $vhost          = $::reverse_proxy::params::vhost,
    $host_port      = $::reverse_proxy::params::host_port,
    $listen_port    = $::reverse_proxy::params::listen_port,
    $webserver_port = $::reverse_proxy::params::webserver_port,
    $proxy          = $::reverse_proxy::params::proxy,
    $self_signed    = $::reverse_proxy::params::self_signed,
    $cert_path      = $::reverse_proxy::params::cert_path,
    $pkey_path      = $::reverse_proxy::params::pkey_path,
    $cert_country   = $::reverse_proxy::params::country,
    $cert_org       = $::reverse_proxy::params::org,
    $cert_state     = $::reverse_proxy::params::state,
    $cert_locality  = $::reverse_proxy::params::locality,
    $cert_unit      = $::reverse_proxy::params::unit,
    $cert_bit       = $::reverse_proxy::params::bit,
    $cert_days      = $::reverse_proxy::params::days,
) inherits ::reverse_proxy::params {
    class { 'reverse_proxy::install': } ->
    class { 'reverse_proxy::config': } ~>
    class { 'reverse_proxy::service': } ->
    Class['reverse_proxy']
}
