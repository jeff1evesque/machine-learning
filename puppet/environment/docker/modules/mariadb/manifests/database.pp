###
### database.pp, create mariadb database structure.
###
class mariadb::database {
    ## python dependencies
    contain python

    ## local variables
    $root_puppet    = $::mariadb::root_puppet
    $pyyaml_version = $::mariadb::pyyaml_version

    ## install dependency
    package { 'pyyaml':
        ensure      => $pyyaml_version,
        provider    => 'pip',
        require     => Class['python'],
        notify      => Exec['create-database-tables'],
    }

    ## define database tables
    exec { 'create-database-tables':
        command     => "python setup_tables.py ${root_puppet}/puppet",
        cwd         => "${root_puppet}/code/modules/mariadb/scripts",
        path        => '/usr/bin',
    }
}