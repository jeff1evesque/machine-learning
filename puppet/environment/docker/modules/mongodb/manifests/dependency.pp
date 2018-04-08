###
### dependency.pp, installs various clients, and modules to interface with
###     the webserver.
###
class webserver::dependency {
    ## local variables
    $root_dir    = $::browserify::root_dir

    $directories = [
        "${root_dir}/log",
        "${root_dir}/log/database",
    ]

    file { $directories:
        ensure => directory,
        mode   => '0700',
        owner  => 'root',
        group  => 'root',
    }
}
