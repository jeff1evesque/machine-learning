## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/']}

## define system timezone
class {'timezone':
    region   => 'America',
    locality => 'New_York',
}