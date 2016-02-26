## include puppet modules: this (also) runs 'apt-get update'
include git

## create '/vagrant/build/' directory
class create_build_directory {
    file {'/vagrant/build/':
        ensure => 'directory',
        before => Vcsrepo['/vagrant/build/scikit-learn'],
    }
}

## download scikit-learn
class download_sklearn {
    ## set dependency
    require create_build_directory

    vcsrepo {'/vagrant/build/scikit-learn':
        ensure   => present,
        provider => git,
        source   => 'https://github.com/scikit-learn/scikit-learn',
        revision => '0.16.1',
        before   => Exec['build-sklearn'],
        notify   => Exec['build-sklearn'],
    }
}

## build scikit-learn
class build_sklearn {
    ## set dependency
    require create_build_directory
    require download_sklearn

    exec {'build-sklearn':
        command     => 'python setup.py build',
        cwd         => '/vagrant/build/scikit-learn/',
        notify      => Exec['install-sklearn'],
        refreshonly => true,
        path        => '/usr/bin',
    }
}

## install scikit-learn
class install_sklearn {
    ## set dependency
    require create_build_directory
    require download_sklearn
    require build_sklearn

    exec {'install-sklearn':
        command     => 'python setup.py install',
        cwd         => '/vagrant/build/scikit-learn/',
        refreshonly => true,
        path        => '/usr/bin',
    }
}

## constructor
class constructor {
    contain create_build_directory
    contain download_sklearn
    contain build_sklearn
    contain install_sklearn
}
include constructor