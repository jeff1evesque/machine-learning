###
### Configures mongodb instance.
###
class mongodb (
    $run                    = $::mongodb::params::run,
    $root_dir               = $::mongodb::params::root_dir,
    $dbPath                 = $::mongodb::params::dbPath,
    $journal                = $::mongodb::params::journal,
    $verbosity              = $::mongodb::params::verbosity,
    $destination            = $::mongodb::params::destination,
    $logAppend              = $::mongodb::params::logAppend,
    $systemLogPath          = $::mongodb::params::systemLogPath,
    $port                   = $::mongodb::params::port,
    $bindIp                 = $::mongodb::params::bindIp,
    $pidfilepath            = $::mongodb::params::pidfilepath,
    $keyserver              = $::mongodb::params::keyserver,
    $mongodb_key            = $::mongodb::params::mongodb_key,
    $mongodb_source_list    = $::mongodb::params::mongodb_source_list,
    $authorization          = $::mongodb::params::authorization,
    $hostname               = $::mongodb::params::hostname,
    $username               = $::mongodb::params::username,
    $password               = $::mongodb::params::password,
    $security_authorization = $::mongodb::params::security_authorization,
) inherits ::mongodb::params {
    class { 'mongodb::install': } ->
    class { 'mongodb::config': } ~>
    class { 'mongodb::run': } ->
    Class['mongodb']
}
