### Note: the prefix 'vagrant::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class vagrant::service {
    ## variables
    $hiera_general   = lookup('general')
    $mountpoint      = $hiera_general['root']
    $vagrant_mounted = $hiera_general['vagrant']
    $template_path   = 'vagrant/vagrant_mounted.erb'

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    #            windows.
    file { '/etc/init/workaround-vagrant-bug-6074.conf':
        ensure  => file,
        content => dos2unix(template($template_path)),
    }
}