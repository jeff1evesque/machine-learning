###
### init.pp: install client, and initialize database tables.
###
### Note: this module has the following dependency:
###
###     - https://github.com/puppetlabs/puppetlabs-mysql.git
###
class mariadb (
    $run                  = $::mariadb::params::run,
    $root_dir             = $::mariadb::params::root_dir,
    $root_puppet          = $::mariadb::params::root_puppet,
    $pyyaml_version       = $::mariadb::params::pyyaml_version,
    $db_host              = $::mariadb::params::db_host,
    $db                   = $::mariadb::params::db,
    $db_user              = $::mariadb::params::db_user,
    $db_password          = $::mariadb::params::db_password,
    $provisioner          = $::mariadb::params::provisioner,
    $provisioner_password = $::mariadb::params::provisioner_password,
    $tester               = $::mariadb::params::tester,
    $tester_password      = $::mariadb::params::tester_password,
    $root_password        = $::mariadb::params::root_password,
    $bind_address         = $::mariadb::params::bind_address,
) inherits ::mariadb::params {
    class { 'mariadb::dependency': } ->
    class { 'mariadb::server': } ->
    class { 'mariadb::client': } ->
    class { 'mariadb::bindings': } ->
    Class['mariadb']
}
