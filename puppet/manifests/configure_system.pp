## define system timezone
class set_timezone {
    class {'timezone':
        region   => 'America',
        locality => 'New_York',
    }
}

## constructor
class constructor {
    contain set_timezone
}
include constructor