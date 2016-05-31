### Note: the prefix 'system::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class system::build_directory {
    ## local variables
    $root_dir = '/vagrant'

    file { "${root_dir}/build/":
        ensure => 'directory',
    }
}