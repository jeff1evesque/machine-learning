###
### dependency.pp, ensure directories.
###
class mariadb::dependency {
    contain system::packages

    ## local variables
    $root_dir       = $::mariadb::root_dir
    $pyyaml_version = $::mariadb::pyyaml_version

    ## install dependency
    if ($redis_version and $redis_version != '*') {
        package { 'pyyaml':
            ensure      => $pyyaml_version,
            provider    => 'pip3',
            require     => Class['system::packages'],
        }
    }
    else {
        package { 'pyyaml':
            ensure      => 'installed',
            provider    => 'pip3',
            require     => Class['system::packages'],
        }
    }

    $directories = [
        "${root_dir}/log",
        "${root_dir}/log/database",
    ]

    ## create log directories
    file { $directories:
        ensure => 'directory',
    }
}
