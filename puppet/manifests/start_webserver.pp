include python
include python::flask
include python::requests

## detect os family: create startup script, start flask server
case $::osfamily {
    'redhat': {
    }
    'debian': {
        ## create startup script (heredoc syntax)
        file {'/etc/init/start_flask.conf':
            ensure  => present,
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
                          echo $$ > /vagrant/log/flask_server.pid
                          exec python /vagrant/app.py
                      end script

                      ## log start-up date
                      pre-start script
                          echo "[`date`] flask server starting" >> /vagrant/log/flask_server.log
                      end script

                      ## log shut-down date, and remove file containing process id
					  pre-stop script
                          rm /vagrant/flask_server.pid
                          echo "[`date`] flask server stopping" >> /vagrant/log/flask_server.log
                      | EOT
        }

        ## start webserver
        exec {'start-webserver':
            command => 'service start_flask start',
            require => File['/etc/init/start_flask.conf'],
		}
    }
    default: {
    }
}