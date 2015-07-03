include python
include python::flask
include python::requests

## initialize empty startup script
file {'/etc/init/start_flask.conf':
    ensure => present,
}

## startup script for flask
case $::osfamily {
    'redhat': {
    }
    'debian': {
    }
    default: {
    }
}