## create '/vagrant/build/' directory
file {'/vagrant/build/':
    ensure => 'directory',
}

## install scikit-learn
vcsrepo {'/vagrant/build/':
    ensure => present,
    provider => git,
    source => 'https://github.com/scikit-learn/scikit-learn',
    revision => '0.16.1',
}