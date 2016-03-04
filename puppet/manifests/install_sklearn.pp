## install git
class install_git {
    include git
}

## create '/vagrant/build/' directory
class create_build_directory {
    file {'/vagrant/build/':
        ensure => 'directory',
    }
}

## install sklearn dependencies
class install_sklearn_dependencies {
    ## 'path' satisfies: apt-get, sh, rm, tar, ldconfig, start-stop-daemon
    exec { 'install-sklearn-dependencies':
        command => 'apt-get build-dep scikit-learn -y',
        timeout => 1400,
        path    => ['/usr/bin', '/bin', '/sbin'],
    }
}

## download scikit-learn
class download_sklearn {
    ## set dependency
    require create_build_directory
    require install_git
    require install_sklearn_dependencies

    vcsrepo {'/vagrant/build/scikit-learn':
        ensure   => present,
        provider => git,
        source   => 'https://github.com/scikit-learn/scikit-learn',
        revision => '0.16.1',
    }
}

## build scikit-learn
class build_sklearn {
    ## set dependency
    require create_build_directory
    require install_git
    require install_sklearn_dependencies
    require download_sklearn

    exec {'build-sklearn':
        command => 'python setup.py build',
        cwd     => '/vagrant/build/scikit-learn/',
        path    => '/usr/bin',
    }
}

## install scikit-learn
class install_sklearn {
    ## set dependency
    require create_build_directory
    require install_git
    require download_sklearn
    require install_sklearn_dependencies
    require build_sklearn

    exec {'install-sklearn':
        command => 'python setup.py install',
        cwd     => '/vagrant/build/scikit-learn/',
        path    => '/usr/bin',
    }
}

## constructor
class constructor {
    contain create_build_directory
    contain install_git
    contain download_sklearn
    contain build_sklearn
    contain install_sklearn_dependencies
    contain install_sklearn
}
include constructor