## include puppet modules: this (also) runs 'apt-get update'
include python
include apt
include nodejs

## variables
case $::osfamily {
  'redhat': {
    $packages_general = ['dos2unix', 'inotify-tools', 'ruby-devel']
  }
  'debian': {
    $packages_general = ['dos2unix', 'inotify-tools', 'ruby-dev']
  }
  default: {
  }
}

$packages_build_dep   = ['matplotlib', 'scikit-learn']
$packages_general_pip = ['redis', 'jsonschema', 'xmltodict', 'six', 'matplotlib']
$packages_general_npm = ['uglify-js', 'imagemin', 'node-sass']
$packages_build_size  = size($packages_build_dep) - 1

## define $PATH for all execs, and packages
Exec {
  path => ['/usr/bin/', '/bin/', '/usr/local', '/usr/sbin/', '/sbin/'],
}

## enable 'multiverse' repository (part 1, replace line)
exec {'enable-multiverse-repository-1':
  command => 'sed -i "s/# deb http:\/\/security.ubuntu.com\/ubuntu trusty-security multiverse/deb http:\/\/security.ubuntu.com\/ubuntu trusty-security multiverse/g" /etc/apt/sources.list',
  notify  => Exec["build-package-dependencies-${packages_build_size}"],
}

## enable 'multiverse' repository (part 2, replace line)
exec {'enable-multiverse-repository-2':
  command => 'sed -i "s/# deb-src http:\/\/security.ubuntu.com\/ubuntu trusty-security multiverse/deb-src http:\/\/security.ubuntu.com\/ubuntu trusty-security multiverse/g" /etc/apt/sources.list',
  notify  => Exec["build-package-dependencies-${packages_build_size}"],
}

## build package dependencies
each($packages_build_dep) |$index, $package| {
  exec {"build-package-dependencies-${index}":
    command     => "apt-get build-dep $package -y",
    before      => Package[$packages_general],
    refreshonly => true,
    timeout     => 1400,
  }
}

## packages: install general packages (apt, yum)
package {$packages_general:
  ensure => 'installed',
  before => Package[$packages_general_pip],
}

## packages: install general packages (pip)
package {$packages_general_pip:
  ensure   => 'installed',
  provider => 'pip',
  before   => Package[$packages_general_npm],
}

## packages: install general packages (npm)
package {$packages_general_npm:
  ensure   => 'present',
  provider => 'npm',
  require  => Package['npm'],
}

## package: install redis-server
package {'redis-server':
  ensure => 'installed',
}