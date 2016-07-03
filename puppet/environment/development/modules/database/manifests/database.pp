### Note: the prefix 'database::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class database::database {
    ## variables
    $hiera_general   = hiera('general')
    $root_dir        = $hiera_general['root']
    $vagrant_mounted = $hiera_general['vagrant_implement']

    ## define database tables
    #
    #  @require, syntax involves 'Class Containment'. For more information,
    #      https://puppetlabs.com/blog/class-containment-puppet
    exec { 'create-database-tables':
        command => "python setup_tables.py ${root_dir} ${vagrant_mounted}",
        cwd     => $script_dir,
        path    => '/usr/bin',
    }
}