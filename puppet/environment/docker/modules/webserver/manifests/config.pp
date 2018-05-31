###
### config.pp, ensure directories exists.
###
class webserver::config {
    ## local variables
    $root_dir           = $::webserver::root_dir
    $flask_log_path     = $::webserver::flask_log_path
    $root_puppet        = $::webserver::root_puppet

    $directories = [
        "${root_dir}/log",
        '/var/log/webserver',
        "${root_dir}/log/application",
        "${root_dir}/log/application/error",
        "${root_dir}/log/application/warning",
        "${root_dir}/log/application/info",
        "${root_dir}/log/application/debug",
    ]

    ## create log directories
    file { $directories:
        ensure => 'directory',
        owner   => 'root',
        group   => 'root',
        mode    => '755',
    }

    ## ensure flask logfile
    file { $flask_log_path:
        ensure  => 'present',
        owner   => 'root',
        group   => 'root',
        mode    => '644',
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
