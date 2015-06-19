# PRIVATE CLASS: do not call directly
class nodejs::install {
  if $caller_module_name != $module_name {
    fail("Use of private class ${name} by ${caller_module_name}")
  }

  # npm is a Gentoo USE flag
  if $::operatingsystem == 'Gentoo' {
    package_use { $nodejs::nodejs_package_name:
      ensure => present,
      target => 'nodejs-flags',
      use    => $nodejs::use_flags,
      before => Package[$nodejs::nodejs_package_name],
    }
  }

  # nodejs
  package { $nodejs::nodejs_package_name:
    ensure => $nodejs::nodejs_package_ensure,
  }

  # nodejs-development
  if $nodejs::nodejs_dev_package_name {
    package { $nodejs::nodejs_dev_package_name:
      ensure => $nodejs::nodejs_dev_package_ensure,
    }
  }

  # nodejs-debug
  if $nodejs::nodejs_debug_package_name {
    package { $nodejs::nodejs_debug_package_name:
      ensure => $nodejs::nodejs_debug_package_ensure,
    }
  }

  # Replicates the nodejs-legacy package functionality
  if ($::osfamily == 'Debian' and $nodejs::legacy_debian_symlinks) {
    file { '/usr/bin/node':
      ensure => 'link',
      target => '/usr/bin/nodejs',
    }
    file { '/usr/share/man/man1/node.1.gz':
      ensure => 'link',
      target => '/usr/share/man/man1/nodejs.1.gz',
    }
  }

  # npm
  if $nodejs::npm_package_name {
    package { $nodejs::npm_package_name:
      ensure => $nodejs::npm_package_ensure,
    }
  }
}

