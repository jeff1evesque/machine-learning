###
### init.pp: configure system with general requirements.
###

class system {
    ## define system timezone
    contain system::set_timezone
}
contain system