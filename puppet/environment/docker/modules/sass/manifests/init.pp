###
### init.pp: install, configure, and run initial compile against source files.
###
### Note: this module has the following dependencies:
###
###    - https://github.com/voxpupuli/puppet-nodejs
###
class sass (
    $run               = $::sass::params::run
    $node_version      = $::sass::params::node_version
    $node_sass_version = $::sass::params::sass_version
    $root_dir          = $::sass::params::root_dir
    $root_puppet       = $::sass::params::root_puppet
    $user              = $::sass::params::user
    $group             = $::sass::params::group
) inherits ::sass::params {
    class { 'sass::dependency': } ->
    class { 'sass::install': } ->
    class { 'sass::config': } ~>
    class { 'sass::run': } ->
    Class['sass']
}
