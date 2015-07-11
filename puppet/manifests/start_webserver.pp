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
        #  @notify, after the upstart script is created, ensure the service is (re)started. This is similar to
        #      an exec statement, where the 'refreshonly => true' would be implemented on the corresponding
        #      listening end point. But, the 'service' end point does not require the 'refreshonly' attribute.
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

                       ## run upstart as a background process
                       expect fork

                       ## start flask server
                       exec python /vagrant/app.py

                       ## log start-up date
                       pre-start script
                           echo "[`date`] flask server starting" >> /vagrant/log/flask_server.log 
                       end script

                       ## log shut-down date, remove process id from log
                       #
                       #  @[`date`], current date script executed
                       post-stop script
                           echo "[`date`] flask server stopped" >> /vagrant/log/flask_server.log
                           rm -f /vagrant/flask_server.pid
                       end script
                       | EOT
            notify  => Service['flask'],
        }

        ## start webserver
        service {'flask':
            ensure   => 'running',
            enable   => 'true',
        }
    }
    default: {
    }
}