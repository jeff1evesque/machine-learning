###
### set_timezone.pp, set system timezone.
###
class system::set_timezone {
    class { 'timezone':
        region   => 'America',
        locality => 'New_York',
    }
    contain timezone
}