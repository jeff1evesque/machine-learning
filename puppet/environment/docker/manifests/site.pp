###
### site.pp: load all necessary modules.
###
### Note: this file is not currently implemented, since the docker environment
###       employs dockerfiles, where corresponding 'init.pp' are containd.
###

contain package
contain sklearn
contain redis
contain system
contain compiler
contain database
contain webserver