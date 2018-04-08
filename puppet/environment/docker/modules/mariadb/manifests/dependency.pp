###
### dependency.pp, ensure directories.
###
class mariadb::dependency {
    ## local variables
    $root_dir    = $::browserify::root_dir

    $directories = [
        "${root_dir}/log",
        "${root_dir}/log/database",
    ]

    ## create log directories
    file { $directories:
        ensure => 'directory',
    }
}
