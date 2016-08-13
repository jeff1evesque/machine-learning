### Note: the prefix 'system::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class system::set_timezone {
    class { 'timezone':
        region   => 'America',
        locality => 'New_York',
    }
    contain timezone
}