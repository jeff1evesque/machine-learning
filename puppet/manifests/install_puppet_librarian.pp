## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/', '/bin/', '/usr/local/', '/usr/local/bin/', '/usr/sbin/', '/sbin/']}

## download dependencies
exec {'download-dependencies':
    command => 'apt-get build-dep librarian-puppet -y',
    before => Package['git'],
}

## download git
package {'git':
    ensure => 'installed',
    before => Exec['download-librarian-puppet'],
    notify => Exec['download-librarian-puppet'],
}

## download librarian-puppet
exec {'download-librarian-puppet':
    command => 'gem install librarian-puppet',
    refreshonly => true,
    notify => Exec['install-librarian-puppet'],
}

## install librarian-puppet
exec {'install-librarian-puppet':
    command => 'librarian-puppet install',
    cwd => '/vagrant/puppet/',
    refreshonly => true,
}