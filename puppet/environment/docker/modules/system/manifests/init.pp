###
### init.pp: configure system with general requirements.
###

class system {
    ## ensure log directory
    require system::log_directory

    ## define system timezone
    contain system::set_timezone
}
contain system