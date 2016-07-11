### configure_system.pp: configure system with general requirements.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## ensure log directory
require system::log_directory

## define system timezone
include system::set_timezone