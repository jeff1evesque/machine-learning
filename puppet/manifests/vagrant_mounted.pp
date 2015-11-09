## variables
$mountpoint = '/vagrant/'

## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/']}

## create startup script: for 'vagrant-mounted' event
file {'vagrant-startup-script':
    path    => '/etc/init/workaround-vagrant-bug-6074.conf',
    ensure  => 'present',
    content => template('/vagrant/puppet/template/vagrant_mounted.erb'),
    notify  => Exec['dos2unix-upstart-vagrant'],
}

## dos2unix upstart: convert clrf (windows to linux) in case host machine
#                    is windows.
#
#  @notify, ensure the webserver service is started. This is similar to an
#      exec statement, where the 'refreshonly => true' would be implemented
#      on the corresponding listening end point. But, the 'service' end point
#      does not require the 'refreshonly' attribute.
exec {'dos2unix-upstart-vagrant':
    command => 'dos2unix /etc/init/workaround-vagrant-bug-6074.conf',
    notify  => Service['workaround-vagrant-bug-6074'],
}

## start 'workaround-vagrant-bug-6074' service
service {'workaround-vagrant-bug-6074':
    ensure => 'running',
    enable => true,
}