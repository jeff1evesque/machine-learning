###
### config.pp, pre-installation configuration.
###
class sklearn::config {
    ## local variables
    $root_dir  = $::sklearn::root_dir

    ## build directory
    file { "${root_dir}/build":
        ensure => 'directory',
    }
}