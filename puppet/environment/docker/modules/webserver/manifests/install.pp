###
### install.pp, install gunicorn webserver
###
class webserver::install {
    ## local variables
    $gunicorn_version  = $::webserver::version

    ## install gunicorn
    if ($gunicorn_version and $gunicorn_version != '*') {
        package { 'gunicorn':
            ensure   => $gunicorn_version,
            provider => 'pip',
        }
    }
    else {
        package { 'gunicorn':
            ensure   => 'installed',
            provider => 'pip',
        }
    }
}
