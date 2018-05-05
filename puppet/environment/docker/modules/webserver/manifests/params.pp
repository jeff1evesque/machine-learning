###
### params.pp: default class parameters.
###
class webserver::params {
    $hiera                 = lookup( { 'name' => 'webserver', 'default_value' => false } )
    $run                   = true
    $version               = '*'
    $pyyaml_version        = '*'
    $redis_version         = '*'
    $pytest_cov_version    = '*'
    $root_puppet           = '/etc/puppetlabs'

    if $hiera {
        $root_dir          = $hiera['root_dir']
        $flask_log_path    = $hiera['flask']['log_path']
        $gunicorn_bind     = $hiera['gunicorn']['bind']
        $gunicorn_port     = $hiera['gunicorn']['port']
        $gunicorn_workers  = $hiera['gunicorn']['workers']
        $gunicorn_type     = $hiera['gunicorn']['type']
    }

    else {
        $root_dir          = '/var/machine-learning'
        $flask_log_path    = '/var/log/webserver/flask.log'
        $gunicorn_bind     = '0.0.0.0'
        $gunicorn_port     = ''
        $gunicorn_workers  = 6
        $gunicorn_type     = 'web'
    }
}
