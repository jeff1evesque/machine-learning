###
### config.pp, configure nginx.
###
class reverse_proxy::config {
    ## local variables
    $conf_file          = $::webserver::conf_file
    $user               = $::webserver::user
    $group              = $::webserver::group
    $root_dir           = $::webserver::root_dir
    $gunicorn_conf      = $::webserver::conf
    $gunicorn_bind      = $::webserver::bind
    $gunicorn_port      = $::webserver::port
    $gunicorn_workers   = $::webserver::workers
    $gunicorn_log_path  = $::webserver::gunicorn_log

    ## gunicorn service
    file { $conf_file:
        ensure  => file,
        content => dos2unix(template('webserver/gunicorn.erb')),
    }
}
