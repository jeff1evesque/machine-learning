## install puppet modules
class install_modules {
    include git
    include stdlib
}

## create '/vagrant/build/' directory
class create_build_directory {
    file {'/vagrant/build/':
        ensure => 'directory',
    }
}

## install sklearn dependencies
class install_sklearn_dependencies {
    ## set dependency
    require install_modules

    ## variables
    $dependencies = [
        'python-dev',
        'python-numpy',
        'python-numpy-dev',
        'python-scipy',
        'libatlas-dev',
        'g++',
        'python-matplotlib',
        'ipython'
    ]

    ## install dependencies
    ensure_packages( $dependencies )
}

## download scikit-learn
class download_sklearn {
    ## set dependency
    require create_build_directory
    require install_modules
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
    require install_modules
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
    require install_modules
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
    contain install_modules
    contain download_sklearn
    contain build_sklearn
    contain install_sklearn_dependencies
    contain install_sklearn
}
include constructor