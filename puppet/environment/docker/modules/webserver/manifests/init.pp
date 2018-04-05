###
### init.pp: start webserver, and ensure all client services exist, and
###          properly configured.
###
### Note: this module has one dependency:
###
###     - https://github.com/voxpupuli/puppet-nginx
###
class webserver (
    $run                = $::webserver::params::run
    $conf_file          = $::webserver::params::conf_file
    $user               = $::webserver::params::user
    $group              = $::webserver::params::group
    $root_dir           = $::webserver::params::root_dir
    $version            = $::webserver::params::version
    $flask_log          = $::webserver::params::log_path
    $bind               = $::webserver::params::bind
    $port               = $::webserver::params::port
    $workers            = $::webserver::params::workers
    $gunicorn_log       = $::webserver::params::log_path
    $pyyaml_version     = $::webserver::params::pyyaml
    $pytest_cov_version = $::webserver::params::pytest_cov
) inherits ::webserver::params {
    class { 'webserver::dependency': } ->
    class { 'webserver::install': } ->
    class { 'webserver::config': } ~>
    class { 'webserver::run': } ~>
    Class['webserver']
}
