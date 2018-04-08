###
### Configures mongodb instance.
###
class mongodb (
    $root_dir            = $::mongodb::params::root_dir,
    $process             = $::mongodb::params::processManagement,
    $dbPath              = $::mongodb::params::dbPath,
    $journal             = $::mongodb::params::journal_enabled,
    $verbosity           = $::mongodb::params::verbosity,
    $destination         = $::mongodb::params::destination,
    $logAppend           = $::mongodb::params::logAppend,
    $systemLogPath       = $::mongodb::params::systemLogPath,
    $port                = $::mongodb::params::port,
    $bindIp              = $::mongodb::params::bindIp,
    $pidfilepath         = $::mongodb::params::pidfilepath,
    $keyserver           = $::mongodb::params::keyserver,
    $mongodb_key         = $::mongodb::params::mongodb_key,
    $mongodb_source_list = $::mongodb::params::mongodb_source_list,
    $authorization       = $::mongodb::params::authorization,
    $hostname            = $::mongodb::hostname,
    $username            = $::mongodb::username,
    $password            = $::mongodb::password,
) inherits ::mongodb::params {
    class { 'mongodb::dependency': } ->
    class { 'mongodb::install' } ->
    class { 'mongodb::config' } ~>
    class { 'mongodb::create_users' } ~>
    class { 'mongodb::run' } ->
    Class['mongodb']
}
