###
### log_directory.pp, create log subdirectories.
###
class system::log_directory {
    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    $directories = [
        "${root_dir}/log/database",
        "${root_dir}/log/webcompiler",
        "${root_dir}/log/webserver",
        "${root_dir}/log/application",
        "${root_dir}/log/application/error",
        "${root_dir}/log/application/warning",
        "${root_dir}/log/application/info",
        "${root_dir}/log/application/debug",
    ]

    ## create log directories
    file { $directories:
        ensure => 'directory',
    }
}