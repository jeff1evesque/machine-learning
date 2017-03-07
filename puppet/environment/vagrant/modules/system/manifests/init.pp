###
### init.pp: configure system with general requirements.
###

class system {
    contain system::set_timezone
}