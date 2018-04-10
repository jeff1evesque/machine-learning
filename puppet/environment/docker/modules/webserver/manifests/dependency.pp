###
### dependency.pp, installs various clients, and modules to interface with
###     the webserver.
###
class webserver::dependency {
    ## python dependencies
    include python
    include python::flask
    include python::requests

    ## local variables
    $root_dir           = $::webserver::root_dir
    $pyyaml_version     = $::webserver::pyyaml_version
    $redis_version      = $::webserver::redis_version
    $pytest_cov_version = $::webserver::pytest_cov_version

    $directories = [
        "${root_dir}/log",
        "${root_dir}/log/webserver",
        "${root_dir}/log/application",
        "${root_dir}/log/application/error",
        "${root_dir}/log/application/warning",
        "${root_dir}/log/application/info",
        "${root_dir}/log/application/debug",
    ]

    ## create log directories
    file { $directories:
        ensure => 'directory',
    }

    ## pytest_cov
    if ($pytest_cov_version and $pytest_cov_version != '*') {
        package { 'pytest-cov':
            ensure          => $pytest_cov_version,
            provider        => 'pip',
            require         => Class['python'],
        }
    }
    else {
        package { 'pytest-cov':
            ensure          => 'installed',
            provider        => 'pip',
            require         => Class['python'],
        }
    }

    ## pyyaml
    if ($pyyaml_version and $pyyaml_version != '*') {
        package { 'pyyaml':
            ensure          => $pyyaml_version,
            provider        => 'pip',
            require         => Class['python'],
        }
    }
    else {
        package { 'pyyaml':
            ensure          => 'installed',
            provider        => 'pip',
            require         => Class['python'],
        }
    }

    ## redis client
    if ($redis_version and $redis_version != '*') {
        package { 'redis':
            ensure          => $redis_version,
            provider        => 'pip',
            require         => Class['python'],
        }
    }
    else {
        package { 'redis':
            ensure          => 'installed',
            provider        => 'pip',
            require         => Class['python'],
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
}
