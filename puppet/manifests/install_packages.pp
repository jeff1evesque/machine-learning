## variables
$packages_general_apt = ['inotify-tools', 'python-pip']
$packages_general_pip = ['redis', 'jsonschema', 'xmltodict', 'six', 'matplotlib']
$packages_flask_pip   = ['flask', 'requests']
$packages_mariadb_apt = ['mariadb-server', 'mariadb-client', 'python-mysqldb']

## define $PATH for all execs
Exec{path => ['/usr/bin/']}

## packages: install general packages
package {$packages_general_apt:
    ensure => 'installed',
    before => Package[$packages_general_pip],
}

## packages: install general packages
package {$packages_general_pip:
    ensure => 'installed',
    provider => 'pip',
    before => Package['nodejs'],
}

## packages: install flask via 'pip'
package {$packages_flask_pip:
    ensure => 'installed',
    provider => 'pip',
    before => Package['nodejs'],
}

## packages: install mariadb
package {$packages_mariadb_apt:
    ensure => 'installed',
    before => Package['nodejs'],
}

## packages: install nodejs
package {'nodejs':
    ensure => 'installed',
    notify => Exec['install-nodejs-ppa'],
    before => Exec['install-nodejs-ppa'],
}

## install nodejs PPA
exec {'install-nodejs-ppa':
    command => 'curl -sL https://deb.nodesource.com/setup | sudo bash -',
    refreshonly => true,
    before => Package['python-software-properties'],
}

## package: install add-apt-repository
package {'python-software-properties':
    ensure => 'installed',
    notify => Exec['update-apt-get'],
    before => Exec['update-apt-get'],
}

## update apt-get
exec {'update-apt-get':
    command => 'apt-get update',
    refreshonly => true,
    before => Package['redis-server'],
}

## package: install redis-server
package {'redis-server':
    ensure => 'installed',
    before => Package[$packages_nodejs_apt],
}

## package: install ruby, and nodejs
package {$packages_nodejs_apt:
    ensure => 'installed',
    before => Package['sass'],
}

## package: install sass
package {'sass':
    ensure => 'installed',
    provider => 'gem',
    notify => Exec['install-uglify-js'],
    before => Exec['install-uglify-js'],
}

## package: install uglify-js
exec {'install-uglify-js':
    command => 'npm install uglify-js -g',
    refreshonly => true,
    notify => Exec['install-imagemin'],
}

## package: install uglify-js
exec {'install-imagemin':
    command => 'npm install --global imagemin',
    refreshonly => true,
    notify => Exec['install-scikit-learn'],
}

## package: install scikit-learn (and dependencies)
exec {'install-scikit-learn':
    command => 'apt-get build-dep scikit-learn',
    refreshonly => true,
}
