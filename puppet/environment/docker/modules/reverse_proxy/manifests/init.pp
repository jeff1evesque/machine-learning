###
### init.pp: install, configure, and start nginx reverse_proxy.
###
### Note: this module has one dependency:
###
###     - https://github.com/voxpupuli/puppet-nginx
###
class reverse_proxy (
    $run            = $::reverse_proxy::params::run,
    $type           = $::reverse_proxy::params::type,
    $vhost          = $::reverse_proxy::params::vhost,
    $host_port      = $::reverse_proxy::params::host_port,
    $listen_port    = $::reverse_proxy::params::listen_port,
    $members        = $::reverse_proxy::params::members,
    $proxy          = $::reverse_proxy::params::proxy,
    $self_signed    = $::reverse_proxy::params::self_signed,
    $cert_path      = $::reverse_proxy::params::cert_path,
    $pkey_path      = $::reverse_proxy::params::pkey_path,
    $cert_country   = $::reverse_proxy::params::cert_country,
    $cert_org       = $::reverse_proxy::params::cert_org,
    $cert_state     = $::reverse_proxy::params::cert_state,
    $cert_locality  = $::reverse_proxy::params::cert_locality,
    $cert_unit      = $::reverse_proxy::params::cert_unit,
    $cert_bit       = $::reverse_proxy::params::cert_bit,
    $cert_days      = $::reverse_proxy::params::cert_days,
    $access_log     = $::reverse_proxy::params::access_log,
    $error_log      = $::reverse_proxy::params::error_log,
) inherits ::reverse_proxy::params {
    class { 'reverse_proxy::install': } ->
    class { 'reverse_proxy::config': } ->
    Class['reverse_proxy']
}
