###
### database.pp, create mariadb database structure.
###
class mariadb::database {
    include package::pyyaml

    ## variables
    $hiera       = lookup('general')
    $root_dir    = $hiera['root']
    $root_puppet = $hiera['root_puppet']

    ## define database tables
    ##
    ## @require, syntax involves 'Class Containment'. For more information,
    ##     https://puppetlabs.com/blog/class-containment-puppet
    exec { 'create-database-tables':
        command => "python setup_tables.py ${root_dir}",
        cwd     => "${root_puppet}/code/modules/mariadb/scripts",
        path    => '/usr/bin',
        require => Class['package::pyyaml'],
    }
}