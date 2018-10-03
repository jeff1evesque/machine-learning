###
### install.pp, install gunicorn webserver
###
class webserver::install {
    ## python dependencies
    include system::packages

    ## local variables
    $pyyaml_version     = $::webserver::pyyaml_version
    $redis_version      = $::webserver::redis_version
    $pytest_cov_version = $::webserver::pytest_cov_version
    $jest_cli_version   = $::webserver::jest_cli_version
    $gunicorn_version   = $::webserver::version
    $platform           = $::webserver::platform

    ## development packages
    if ($platform == 'development') {
        package { 'pytest-cov':
            ensure      => $pytest_cov_version,
            provider    => 'pip3',
            require     => Class['system::packages'],
        }
    }

    ## pyyaml
    package { 'pyyaml':
        ensure          => $pyyaml_version,
        provider        => 'pip3',
        require         => Class['system::packages'],
    }

    ## redis client
    package { 'redis':
        ensure          => $redis_version,
        provider        => 'pip3',
        require         => Class['system::packages'],
    }

    ## mariadb client
    class { '::mysql::client':
        package_name    => 'mariadb-client',
    }

    ## mariadb bindings
    class { '::mysql::bindings':
        python_enable   => true,
    }

    ## install gunicorn
    package { 'gunicorn':
        ensure          => $gunicorn_version,
        provider        => 'pip3',
        require         => Class['system::packages'],
    }
}
