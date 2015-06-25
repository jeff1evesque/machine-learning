## create '/vagrant/build/' directory
file {'/vagrant/build/':
    ensure => 'directory',
    before => Vcsrepo['/vagrant/build/'],
}

## install scikit-learn
vcsrepo {'/vagrant/build/':
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
