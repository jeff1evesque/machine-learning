###
### config.pp, ensure directories exists.
###
class webserver::config {
    ## local variables
    $root_dir           = $::webserver::root_dir
    $flask_log_path     = $::webserver::flask_log_path

    $directories = [
        "${root_dir}/log",
        "${root_dir}/log/webserver",
        "${root_dir}/log/application",
        "${root_dir}/log/application/error",
        "${root_dir}/log/application/warning",
        "${root_dir}/log/application/info",
        "${root_dir}/log/application/debug",
        $flask_log_path
    ]

    ## create log directories
    file { $directories:
        ensure => 'directory',
    }

    ## configure docker entrypoint
    file { "${root_dir}/entrypoint":
        ensure  => file,
        owner   => 'root',
        group   => 'root',
        content => dos2unix(template('webserver/entrypoint.erb')),
        mode    => '700',
    }
}
