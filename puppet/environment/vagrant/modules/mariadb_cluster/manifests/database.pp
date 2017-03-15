###
### database.pp, create mariadb database structure.
###
class mariadb_cluster::database {
    include package::pyyaml

    ## variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $vagrant_mounted = $hiera_general['vagrant_implement']
    $environment     = $hiera_general['environment']
    $module          = 'database'
    $environment_dir = "${root_dir}/puppet/environment/${environment}"
    $script_dir      = "${environment_dir}/modules/${module}/scripts"

    ## define database tables
    ##
    ## @require, syntax involves 'Class Containment'. For more information,
    ##     https://puppetlabs.com/blog/class-containment-puppet
    exec { 'create-database-tables':
        command => "python setup_tables.py ${root_dir} ${vagrant_mounted}",
        cwd     => $script_dir,
        path    => '/usr/bin',
        require => Class['package::pyyaml'],
    }
}