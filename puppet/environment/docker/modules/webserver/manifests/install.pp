###
### install.pp, install gunicorn webserver
###
class webserver::config {
    ## python dependency
    contain python

    ## local variables
    $gunicorn_version  = $::webserver::version

    ## install gunicorn
    package { 'gunicorn':
        ensure   => $gunicorn_version,
        provider => 'pip',
    }
}
