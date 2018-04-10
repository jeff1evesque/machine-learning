###
### dependency.pp, install sklearn dependencies.
###
class sklearn::dependency {
    ## local variables
    $root_dir  = $::sklearn::root_dir

    ## build directory
    file { "${root_dir}/build/":
        ensure => 'directory',
    }
}