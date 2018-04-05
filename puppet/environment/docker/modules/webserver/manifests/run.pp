###
### run.pp, start webserver.
###
class webserver::run {
    ## local variables
    $start_webserver = $::webserver::run

    ## webserver service
    service { 'gunicorn':
        ensure       => $start_webserver,
        enable       => $start_webserver,
    }
}
