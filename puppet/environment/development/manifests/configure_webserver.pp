### configure_webserver.pp: implement webserver, with necessary dependencies.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## create log directory
include system::log_directory

## install webserver
include webserver::service