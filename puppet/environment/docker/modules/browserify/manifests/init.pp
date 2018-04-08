###
### init.pp: install, configure, and run initial compile against source files.
###
### Note: this module has the following dependencies:
###
###    - https://github.com/voxpupuli/puppet-nodejs
###
class browserify (
    $run                = $::browserify::params::run,
    $node_version       = $::browserify::params::node_version,
    $browserify_version = $::browserify::params::node_version,
    $babel_core_version = $::browserify::params::babel_core_version,
    $babelify_version   = $::browserify::params::babelify_version,
    $root_dir           = $::browserify::params::root_dir,
    $root_puppet        = $::browserify::params::root_puppet,
    $user               = $::browserify::params::user,
    $group              = $::browserify::params::group,
) inherits ::browserify::params {
    class { 'browserify::dependency': } ->
    class { 'browserify::install': } ->
    class { 'browserify::config': } ~>
    class { 'browserify::run': } ->
    Class['browserify']
}
