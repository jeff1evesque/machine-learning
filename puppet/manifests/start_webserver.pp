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
            path    => '/etc/init/start_flask.conf',
            ensure  => 'present',
            content => @(EOT),
                       #!upstart
                       description 'start flask server'

                       ## start job defined in this file after system services, and processes have already loaded
                       #       (to prevent conflict).
                       #
                       #  @filesystem, ensure job in this file executes after filesystems have been mounted
                       #  @[2345], represents all configuration states with general linux, and networking access
                       start on filesystem or runlevel [2345]

                       ## stop flask server when machine gracefully shuts down
                       stop on shutdown

                       ## start flask server (via bash shell)
                       #
                       #  $$, the process id (pid) of the current script
                       script
                           exec echo > /vagrant/log/flask_server.pid $$
                           python /vagrant/app.py
                       end script

                       ## log start-up date
                       pre-start script
                           exec echo >> /vagrant/log/flask_server.log "[`date`] flask server starting"
                       end script

                       ## log shut-down date, and remove process id log
                       pre-stop script
                           exec echo > /vagrant/flask_server.pid ''
                           exec echo >> /vagrant/log/flask_server.log "[`date`] flask server stopping"
                       end script
                       | EOT
            notify  => Exec['start-webserver'],
        }

        ## start webserver
        exec {'start-webserver':
            command => 'service start_flask start',
            refreshonly => true,
		}
    }
    default: {
    }
}