include python
include python::flask
include python::requests

## startup script for flask
case $::osfamily {
    'redhat': {
    }
    'debian': {
        ## initialize empty startup script
        file {'/etc/init/start_flask.conf':
            ensure => present,
        }
    }
    default: {
    }
}