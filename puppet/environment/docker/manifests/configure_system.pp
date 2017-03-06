###
### configure_system.pp: configure system with general requirements.
###

## ensure log directory
require system::log_directory

## define system timezone
include system::set_timezone