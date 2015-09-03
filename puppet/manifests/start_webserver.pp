include python
include python::flask
include python::requests

## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/']}

## install, and configure nginx
class { 'nginx': }

## install, and configure uwsgi
class { 'uwsgi::app':
    ensure => 'present',
    config => {
        socket => '127.0.0.1:5000',
        chdir => '/vagrant/',
        wsgi-file => 'webserver.wsgi',
    },
}

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
            content => @(EOT),
                       #!upstart
                       description 'start flask server'

                       ## start job defined in this file after system services, and processes have already loaded
                       #       (to prevent conflict).
                       #
                       #  @vagrant-mounted, an event that executes after the shared folder is mounted
                       #  @[2345], represents all configuration states with general linux, and networking access
                       start on (vagrant-mounted and runlevel [2345])

                       ## stop upstart job
                       stop on runlevel [!2345]

                       ## restart upstart job continuously
                       respawn

                       # required for permission to write to '/vagrant/' files (pre-stop stanza)
                       setuid vagrant
                       setgid vagrant

                       ## run upstart job as a background process
                       expect fork

                       ## start upstart job
                       exec python /vagrant/app.py

                       ## log start-up date
                       #
                       #  @[`date`], current date script executed
                       pre-start script
                           echo "[`date`] flask server starting" >> /vagrant/log/flask_server.log 
                       end script

                       ## log shut-down date, remove process id from log before '/vagrant' is unmounted
                       #
                       #  @[`date`], current date script executed
                       pre-stop script
                            echo "[`date`] flask server stopping" >> /vagrant/log/flask_server.log
                       end script
                       | EOT
            notify  => Exec['dos2unix-flask'],
        }

        ## convert clrf (windows to linux) in case host machine is windows.
        #
        #  @notify, ensure the webserver service is started. This is similar to an exec statement, where the
        #      'refreshonly => true' would be implemented on the corresponding listening end point. But, the
        #      'service' end point does not require the 'refreshonly' attribute.
        exec {'dos2unix-flask':
            command => 'dos2unix /etc/init/flask.conf',
            refreshonly => true,
            notify => Service['flask'],
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