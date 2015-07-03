include python
include python::flask
include python::requests

$debian_startup_description = "description 'start flask sever'"

## startup script for flask
case $::osfamily {
    'redhat': {
    }
    'debian': {
        ## define startup script using heredoc syntax
        file {'/etc/init/start_flask.conf':
            ensure => present,
            source => @(EOT)
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
                      exec python /vagrant/app.py
                      | EOT,
        }
		
    }
    default: {
    }
}