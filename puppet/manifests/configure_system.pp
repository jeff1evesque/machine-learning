## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/']}

## define system timezone
class {'timezone':
    region   => 'America',
    locality => 'New_York',
}

## recursively convert to unix line endings in /vagrant directory
#exec {'recursive-line-endings':
#    command => 'find /vagrant -type f -print0 | xargs -0 -n 1 -P 4 dos2unix',
#}
