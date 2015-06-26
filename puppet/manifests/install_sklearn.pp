## include puppet modules: this (also) runs 'apt-get update'
include git

## define $PATH for all execs
Exec {path => ['/usr/bin/']}

## create '/vagrant/build/' directory
file {'/vagrant/build/':
    ensure => 'directory',
    before => Vcsrepo['/vagrant/build/scikit-learn'],
}

## download scikit-learn
vcsrepo {'/vagrant/build/scikit-learn':
    ensure => present,
    provider => git,
    source => 'https://github.com/scikit-learn/scikit-learn',
    revision => '0.16.1',
    before => Exec['build-sklearn'],
    notify => Exec['build-sklearn'],
}

## build scikit-learn
exec {'build-sklearn':
    command => 'python setup.py build',
    cwd => '/vagrant/build/scikit-learn/',
    notify => Exec['install-sklearn'],
    refreshonly => true,
}

## install scikit-learn
exec {'install-sklearn':
    command => 'python setup.py install',
    cwd => '/vagrant/build/scikit-learn/',
    refreshonly => true,
}