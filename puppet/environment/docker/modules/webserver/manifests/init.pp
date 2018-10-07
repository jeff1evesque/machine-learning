###
### init.pp: start webserver, and ensure all client services exist, and
###          properly configured.
###
### Note: this module has one dependency:
###
###     - https://github.com/voxpupuli/puppet-nodejs.git
###     - https://github.com/counsyl/puppet-python.git
###
class webserver (
    $run                    = $::webserver::params::run,
    $gunicorn_bind          = $::webserver::params::gunicorn_bind,
    $gunicorn_port          = $::webserver::params::gunicorn_port,
    $gunicorn_workers       = $::webserver::params::gunicorn_workers,
    $gunicorn_type          = $::webserver::params::gunicorn_type,
    $gunicorn_version       = $::webserver::params::gunicorn_version,
    $root_dir               = $::webserver::params::root_dir,
    $version                = $::webserver::params::version,
    $flask_log_path         = $::webserver::params::flask_log_path,
    $pyyaml_version         = $::webserver::params::pyyaml_version,
    $redis_version          = $::webserver::params::redis_version,
    $libmysqlclient_version = $::webserver::params::libmysqlclient_version,
    $mysqlclient_version    = $::webserver::params::mysqlclient_version,
    $pytest_cov_version     = $::webserver::params::pytest_cov_version,
    $root_puppet            = $::webserver::params::root_puppet,
    $platform               = $::webserver::params::platform,
) inherits ::webserver::params {
    class { 'webserver::install': } ->
    class { 'webserver::config': } ~>
    class { 'webserver::run': } ->
    Class['webserver']
}
