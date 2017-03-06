###
### site.pp: load all necessary modules.
###

include package
include sklearn
include vagrant
include redis
include system
include compiler
include database
include webserver