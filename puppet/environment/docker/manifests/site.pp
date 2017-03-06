###
### site.pp: load all necessary modules.
###
### Note: this file is not currently implemented, since the docker environment
###       employs dockerfiles, where corresponding 'init.pp' are included.
###

include package
include sklearn
include redis
include system
include compiler
include database
include webserver