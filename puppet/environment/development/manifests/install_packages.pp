## define $PATH for all execs, and packages
Exec {
  path => ['/usr/bin/', '/bin/', '/usr/local', '/usr/sbin/', '/sbin/'],
}

class webcompiler_packages {
    include apt

    ## variables
    case $::osfamily {
        'redhat': {
            $packages_general = ['dos2unix', 'inotify-tools']
        }
        'debian': {
            $packages_general = ['dos2unix', 'inotify-tools']
        }
        default: {
        }
    }

    $packages_general_npm = [
        'uglify-js',
        'imagemin',
        'node-sass',
        'babel-core',
        'browserify',
        'babelify'
    ]

    ## install nodejs (with npm)
    class { 'nodejs':
        repo_url_suffix => '5.x',
    }

    ## packages: install general packages (apt, yum)
    package { $packages_general:
        ensure => 'installed',
        notify => Exec['update-npm-packages'],
    }

    ## update all npm global packages
    exec { 'update-npm-packages':
        command => 'npm update -g',
        refreshonly => true,
        before => Package[$packages_general_npm],
        path => '/usr/bin',
    }

    ## packages: install general packages (npm)
    package { $packages_general_npm:
        ensure   => 'present',
        provider => 'npm',
        notify   => Exec['install-babelify-presets'],
        require  => Class['nodejs'],
    }

    ## packages: install babelify presets for reactjs (npm)
    exec { 'install-babelify-presets':
        command     => 'npm install --no-bin-links',
        cwd         => '/vagrant/src/jsx/',
        refreshonly => true,
    }
}

class create_directories {
    $compilers.each |String $compiler, Hash $resource| {
        ## create asset directories (if not exist)
        if ($resource['asset_dir']) {
            file { "/vagrant/interface/static/${resource['asset']}/":
                ensure => 'directory',
            }
        }

        ## create src directories (if not exist)
        if ($resource['src_dir']) {
            file { "/vagrant/src/${resource['src']}/":
                ensure => 'directory',
            }
        }
    }
}

class application_packages {
    include python

    $packages_general_pip = [
        'jsonschema',
        'xmltodict',
        'six'
    ]

    ## packages: install general packages (pip)
    package { $packages_general_pip:
        ensure   => 'installed',
        provider => 'pip',
    }
}

## constructor
class constructor {
    contain application_packages
}
include constructor