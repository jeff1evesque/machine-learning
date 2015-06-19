## variables
$packages_general_apt = ['inotify-tools', 'python-pip']
$packages_general_pip = ['redis', 'jsonschema', 'xmltodict', 'six', 'matplotlib']
$packages_flask_pip   = ['flask', 'requests']
$packages_mariadb_apt = ['mariadb-server', 'mariadb-client', 'python-mysqldb']
$packages_nodejs_apt  = ['ruby', 'nodejs']

## packages: install general packages
package {$packages_general_apt:
    ensure => present,
    before => Package[$packages_general_pip],
}

## packages: install general packages
package {$packages_general_pip:
    ensure => present,
    provider => 'pip',
    before => Package[$packages_nodejs_apt],
}

## packages: install flask via 'pip'
package {$packages_flask_pip:
    ensure => present,
    provider => 'pip',
    before => Package[$packages_nodejs_apt],
}

## packages: install mariadb
package {$packages_mariadb_apt:
    ensure => present,
    before => Package[$packages_nodejs_apt],
}

## packages: install nodejs with ruby
package {$packages_nodejs_apt:
    ensure => present,
    notify => Exec['install-nodejs-ppa'],
    before => Exec['install-nodejs-ppa'],
}

## install nodejs PPA
exec {'install-nodejs-ppa':
    command => 'curl -sL https://deb.nodesource.com/setup | sudo bash -',
    refreshonly => true,
    before => Package['install-add-apt-repository'],
}

## package: install add-apt-repository
package {'install-add-apt-repository':
    ensure => present,
    notify => Exec['install-redis-ppa'],
}

## update apt-get
exec {'update-apt-get':
    command => 'apt-get update',
    refreshonly => true,
    before => Package['redis-server'],
}

## package: install redis-server
package {'redis-server':
    ensure => present,
    before => Package[$packages_nodejs_apt],
}

## package: install ruby, and nodejs
package {$packages_nodejs_apt:
    ensure => present,
    before => Package['sass'],
}

## package: install sass
package {'sass':
    ensure => present,
    provider => 'gem',
    before => Package['uglify-js'],
}

## package: install uglify-js
package {'uglify-js':
    ensure => present,
    provider => 'npm',
    install_options => '-g',
    before => Package['imagemin'],
}

## package: install uglify-js
package {'imagemin':
    ensure => present,
    provider => 'npm',
    install_options => '--global',
    notify => Exec['install-scikit-learn'],
    before => Exec['install-scikit-learn'],
}

## package: install scikit-learn (and dependencies)
exec {'install-scikit-learn':
    command => 'apt-get build-dep scikit-learn',
    refreshonly => true,
}
