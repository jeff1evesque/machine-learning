### Note: the prefix 'vagrant::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class vagrant::service {
    ## set dependency
    require stdlib

    ## variables
    $environment      = 'development'
    $environment_path = "/vagrant/puppet/environment/${environment}"
    $vagrant_service  = template("${environment_path}/template/vagrant_mounted.erb")

    ## dos2unix upstart: convert clrf (windows to linux) in case host machine
    #                    is windows.
    file { '/etc/init/workaround-vagrant-bug-6074.conf':
        ensure      => file,
        content     => dos2unix($vagrant_service),
    }
}