### Note: the prefix 'database::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class database::database {
    ## variables
    $module          = 'database'
    $environment     = 'development'
    $environment_dir = "/vagrant/puppet/environment/${environment}"
    $script_dir      = "${environment_dir}/modules/${module}/scripts"

    ## define database tables
    #
    #  @require, syntax involves 'Class Containment'. For more information,
    #      https://puppetlabs.com/blog/class-containment-puppet
    exec {'create-database-tables':
        command => 'python setup_tables.py',
        cwd     => $script_dir,
        path    => '/usr/bin',
    }
}