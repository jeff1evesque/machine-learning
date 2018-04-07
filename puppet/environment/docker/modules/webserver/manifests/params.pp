###
### params.pp: default class parameters.
###
class webserver::params {
    $hiera              = lookup( { 'name' => 'webserver', 'default_value' => false } )
    $run                = true
    $version            = 'latest'
    $pyyaml_version     = 'latest'
    $pytest_cov_version = 'latest'

    if $hiera {
        $conf_file      = $hiera['gunicorn']['conf_file']
        $user           = $hiera['gunicorn']['user']
        $group          = $hiera['gunicorn']['group']
        $root_dir       = $hiera['root_dir']
        $flask_log      = $hiera['flask']['log_path']
        $bind           = $hiera['gunicorn']['bind']
        $port           = $hiera['gunicorn']['port']
        $workers        = $hiera['gunicorn']['workers']
        $gunicorn_log   = $hiera['gunicorn']['log_path']
    }

    else {
        $conf_file      = '/etc/init/gunicorn.conf'
        $user           = 'root'
        $group          = 'root'
        $root_dir       = '/var/machine-learning'
        $flask_log      = '/var/log/webserver/flask.log'
        $bind           = 0.0.0.0
        $port           = ''
        $workers        = 6
        $gunicorn_log   = '/var/log/webserver/gunicorn.log'
    }
}
