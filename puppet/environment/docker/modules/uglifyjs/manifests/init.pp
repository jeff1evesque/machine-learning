###
### init.pp: install, configure, and run initial compile against source files.
###
### Note: this module has the following dependencies:
###
###    - https://github.com/voxpupuli/puppet-nodejs
###
class uglifyjs (
    $run                = $::uglifyjs::params::run,
    $node_version       = $::uglifyjs::params::node_version,
    $uglifyjs_version   = $::uglifyjs::params::node_version,
    $root_dir           = $::uglifyjs::params::root_dir,
    $root_puppet        = $::uglifyjs::params::root_puppet,
    $user               = $::uglifyjs::params::user,
    $group              = $::uglifyjs::params::group,
) inherits ::uglifyjs::params {
    class { 'uglifyjs::dependency': } ->
    class { 'uglifyjs::install': } ->
    class { 'uglifyjs::config': } ~>
    class { 'uglifyjs::run': } ->
    Class['uglifyjs']
}
