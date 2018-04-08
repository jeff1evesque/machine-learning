###
### dependency.pp, installs various clients, and modules to interface with
###     the webserver.
###
class webserver::dependency {
    ## python dependencies
    contain python
    contain python::flask
    contain python::requests

    ## local variables
    $root_dir           = $::webserver::root_dir
    $pyyaml_version     = $::webserver::pyyaml_version
    $redis_version      = $::webserver::redis_version
    $pytest_cov_version = $::webserver::pytest_cover_version

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

    package { 'pytest-cov':
        ensure          => $pytest_cov_version,
        provider        => 'pip',
        require         => Class['python'],
    }

    package { 'pyyaml':
        ensure          => $pyyaml_version,
        provider        => 'pip',
        require         => Class['python'],
    }

    ## redis client
    package { 'redis'
        ensure          => $redis_version,
        provider        => 'pip',
        require         => Class['python'],
    }

    ## mariadb client
    class { '::mysql::client':
        package_name => 'mariadb-client',
    }

    ## mariadb bindings
    class { '::mysql::bindings':
        python_enable => true,
    }
}
