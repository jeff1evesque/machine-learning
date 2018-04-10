###
### run.pp, start webserver.
###
class webserver::run {
    ## local variables
    $start_webserver = $::webserver::run
    $root_dir        = $::webserver::root_dir
    $bind            = $::webserver::gunicorn_bind
    $port            = $::webserver::gunicorn_port
    $workers         = $::webserver::gunicorn_workers
    $type            = $::webserver::gunicorn_type

    ## enforce webserver
    if $start_mongodb {
        exec { 'start-gunicorn':
            command => "gunicorn -b ${bind}:${port} --workers=${workers} 'factory:create_app(args={\"instance\": ${type}})'",
            cwd     => $root_dir,
            path    => '/usr/bin',
            unless  => 'pgrep gunicorn',
        }
    }
}
