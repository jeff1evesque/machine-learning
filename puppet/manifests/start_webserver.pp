include python
include python::flask
include python::requests

## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/']}

## create log directory
file {'/vagrant/log/':
  ensure => 'directory',
  before => File['server-startup-script'],
}

## detect os family: create startup script, start flask server
case $::osfamily {
  'redhat': {
  }
  'debian': {
    ## create startup script (heredoc syntax)
    file {'server-startup-script':
      path    => '/etc/init/flask.conf',
      ensure  => 'present',
      content => '/vagrant/puppet/scripts/flask_server',
      notify  => Exec['dos2unix-flask'],
    }

    ## convert clrf (windows to linux) in case host machine is windows.
    #
    #  @notify, ensure the webserver service is started. This is similar to an
    #      exec statement, where the 'refreshonly => true' would be implemented
    #      on the corresponding listening end point. But, the 'service' end
    #      point does not require the 'refreshonly' attribute.
    exec {'dos2unix-flask':
      command     => 'dos2unix /etc/init/flask.conf',
      refreshonly => true,
      notify      => Service['flask'],
    }

    ## start webserver
    service {'flask':
      ensure => 'running',
      enable => 'true',
    }
  }
  default: {
  }
}