###
### init.pp: install redis client, and redis server.
###

class redis (
    $run          = $::redis::params::run,
    $version      = $::redis::params::version,
    $bind_address = $::redis::params::bind_address,
    $config_file  = $::redis::params::config_file,
) inherits ::redis::params {
    class { 'redis::install': } ->
    class { 'redis::config': } ~>
    class { 'redis::run': } ->
    Class['redis']
}
