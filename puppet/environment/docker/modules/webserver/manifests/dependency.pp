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
    $pyyaml_version     = $::webserver::pyyaml_version
    $pytest_cov_version = $::webserver::pytest_cover_version

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

    ## mariadb client
    contain mariadb::client
    contain mariadb::bindings

    ## redis client
    contain package::redis_client
}
