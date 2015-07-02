include python
include python::flask
include python::requests

## startup script for flask
case $::osfamily {
    'redhat': {
    }
    'debian': {
    }
    default: {
    }
}