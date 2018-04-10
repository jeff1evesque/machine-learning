###
### install.pp, install gunicorn webserver
###
class webserver::install {
    ## python dependencies
    include python
    include python::flask
    include python::requests

    ## local variables
    $pyyaml_version     = $::webserver::pyyaml_version
    $redis_version      = $::webserver::redis_version
    $pytest_cov_version = $::webserver::pytest_cov_version
    $gunicorn_version   = $::webserver::version

    ## pytest_cov
    if ($pytest_cov_version and $pytest_cov_version != '*') {
        package { 'pytest-cov':
            ensure      => $pytest_cov_version,
            provider    => 'pip',
            require     => Class['python'],
        }
    }
    else {
        package { 'pytest-cov':
            ensure      => 'installed',
            provider    => 'pip',
            require     => Class['python'],
        }
    }

    ## pyyaml
    if ($pyyaml_version and $pyyaml_version != '*') {
        package { 'pyyaml':
            ensure      => $pyyaml_version,
            provider    => 'pip',
            require     => Class['python'],
        }
    }
    else {
        package { 'pyyaml':
            ensure      => 'installed',
            provider    => 'pip',
            require     => Class['python'],
        }
    }

    ## redis client
    if ($redis_version and $redis_version != '*') {
        package { 'redis':
            ensure      => $redis_version,
            provider    => 'pip',
            require     => Class['python'],
        }
    }
    else {
        package { 'redis':
            ensure      => 'installed',
            provider    => 'pip',
            require     => Class['python'],
        }
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
    if ($gunicorn_version and $gunicorn_version != '*') {
        package { 'gunicorn':
            ensure      => $gunicorn_version,
            provider    => 'pip',
        }
    }
    else {
        package { 'gunicorn':
            ensure      => 'installed',
            provider    => 'pip',
        }
    }
}
