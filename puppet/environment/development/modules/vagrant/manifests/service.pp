### Note: the prefix 'vagrant::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class vagrant::service {
    ## variables
    $mountpoint  = '/vagrant/'
    $environment = 'development'

    ## create startup script: for 'vagrant-mounted' event
    file { 'vagrant-startup-script':
        path    => '/etc/init/workaround-vagrant-bug-6074.conf',
        ensure  => 'present',
        content => template("/vagrant/puppet/environment/${development}/template/vagrant_mounted.erb"),
        notify  => Exec['dos2unix-upstart-vagrant'],
    }

    ## dos2unix upstart: convert clrf (windows to linux) in case host machine
    #                    is windows.
    #
    #  @notify, ensure the webserver service is started. This is similar to an
    #      exec statement, where the 'refreshonly => true' would be implemented
    #      on the corresponding listening end point. But, the 'service' end point
    #      does not require the 'refreshonly' attribute.
    exec { 'dos2unix-upstart-vagrant':
        command => 'dos2unix /etc/init/workaround-vagrant-bug-6074.conf',
        refreshonly => true,
    }
}