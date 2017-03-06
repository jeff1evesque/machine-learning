###
### init.pp: configure system with general requirements.
###

class system {
    include system::set_timezone
}