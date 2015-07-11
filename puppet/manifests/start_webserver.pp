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
        #
        #  @notify, after the upstart script is created, ensure the service is started. This is similar to
        #      an exec statement, where the 'refreshonly => true' would be implemented on the corresponding
        #      listening end point. But, the 'service' end point does not require the 'refreshonly' attribute.
        #      This statement also ensures if the upstart script changes, the corresponding service restarts.
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

                       ## stop flask server
                       stop on runlevel [!2345]

                       ## restart upstart job continuously
                       respawn

                       # required for permission to write to '/vagrant/' files (pre-stop stanza)
                       setuid vagrant
                       setgid vagrant

                       ## run upstart job as a background process
                       expect fork

                       ## start flask server
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
                           if [ $MOUNTPOINT = "/vagrant" ]; then
                               echo "[`date`] flask server stopping" >> /vagrant/log/flask_server.log
                           fi
                       end script
                       | EOT
            notify  => [Exec['dos2unix-line-endings'], Service['flask']],
        }

        ## convert windows to linux line endings
        exec {'dos2unix-line-endings':
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