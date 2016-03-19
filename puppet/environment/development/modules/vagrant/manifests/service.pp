### Note: the prefix 'vagrant::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class vagrant::service {
    ## variables
    $mountpoint      = '/vagrant'/
    $environment     = 'development'
    $module          = 'vagrant'
    $environment_dir = "/vagrant/puppet/environment/${environment}"
    $template_dir    = "${environment_path}/modules/${module}/template"
    $vagrant_service = "${template_dir}/vagrant_mounted.erb"

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    #            windows.
    file { '/etc/init/workaround-vagrant-bug-6074.conf':
        ensure      => file,
        content     => dos2unix($vagrant_service),
    }
}