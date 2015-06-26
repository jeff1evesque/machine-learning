## include puppet modules: this (also) runs 'apt-get update'
include git

## define $PATH for all execs
Exec {path => ['/usr/bin/']}

## install scikit-learn
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
    refreshonly => true,
}