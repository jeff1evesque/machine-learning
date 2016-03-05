## include puppet modules: this (also) runs 'apt-get update'
include python
include apt

## variables
case $::osfamily {
  'redhat': {
    $packages_general = ['dos2unix', 'ruby-devel']
  }
  'debian': {
    $packages_general = ['dos2unix', 'ruby-dev']
  }
  default: {
  }
}

$packages_build_dep   = ['matplotlib']
$packages_general_pip = [
    'jsonschema',
    'xmltodict',
    'six',
    'python-matplotlib'
]
$packages_build_size  = size($packages_build_dep) - 1

## define $PATH for all execs, and packages
Exec {
  path => ['/usr/bin/', '/bin/', '/usr/local', '/usr/sbin/', '/sbin/'],
}

## matplotlib: enable 'multiverse' repository (part 1, replace line)
exec {'enable-multiverse-repository-1':
  command => template('/vagrant/puppet/template/enable_multiverse_1.erb'),
  notify  => Exec["enable-multiverse-repository-2"],
}

## matplotlib: enable 'multiverse' repository (part 2, replace line)
exec {'enable-multiverse-repository-2':
  command => template('/vagrant/puppet/template/enable_multiverse_2.erb'),
  notify  => Exec["build-package-dependencies-${packages_build_size}"],
  refreshonly => true,
}

## build package dependencies
each($packages_build_dep) |$index, $package| {
  exec {"build-package-dependencies-${index}":
    command     => "apt-get install build-essential ${package} -y",
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
