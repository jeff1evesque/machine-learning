class nodejs::params {
  $legacy_debian_symlinks      = false
  $nodejs_debug_package_ensure = 'absent'
  $nodejs_dev_package_ensure   = 'absent'
  $nodejs_package_ensure       = 'present'
  $repo_enable_src             = false
  $repo_ensure                 = 'present'
  $repo_pin                    = false
  $repo_priority               = 'absent'
  $repo_proxy                  = 'absent'
  $repo_proxy_password         = 'absent'
  $repo_proxy_username         = 'absent'
  $repo_url_suffix             = 'node_0.10'
  $use_flags                   = ['npm', 'snapshot']

  # The full path to cmd.exe is required on Windows. The system32 fact is only
  # available from Facter 2.3
  $cmd_exe_path = $::osfamily ? {
    'Windows' => 'C:\Windows\system32\cmd.exe',
    default   => undef,
  }

  case $::osfamily {
    'Debian': {
      if $::operatingsystemrelease =~ /^6\.(\d+)/ {
        fail("The ${module_name} module is not supported on Debian Squeeze.")
      }
      if $::operatingsystemrelease =~ /^7\.(\d+)/ {
        $manage_package_repo       = true
        $nodejs_debug_package_name = 'nodejs-dbg'
        $nodejs_dev_package_name   = undef
        $nodejs_package_name       = 'nodejs'
        $npm_package_ensure        = 'absent'
        $npm_package_name          = undef
        $npm_path                  = '/usr/bin/npm'
        $repo_class                = '::nodejs::repo::nodesource'
      }
      elsif $::operatingsystemrelease =~ /^10.04$/ {
        $manage_package_repo       = true
        $nodejs_debug_package_name = 'nodejs-dbg'
        $nodejs_dev_package_name   = undef
        $nodejs_package_name       = 'nodejs'
        $npm_package_ensure        = 'absent'
        $npm_package_name          = undef
        $npm_path                  = '/usr/bin/npm'
        $repo_class                = '::nodejs::repo::nodesource'
      }
      elsif $::operatingsystemrelease =~ /^12.04$/ {
        $manage_package_repo       = true
        $nodejs_debug_package_name = 'nodejs-dbg'
        $nodejs_dev_package_name   = 'nodejs-dev'
        $nodejs_package_name       = 'nodejs'
        $npm_package_ensure        = 'absent'
        $npm_package_name          = 'npm'
        $npm_path                  = '/usr/bin/npm'
        $repo_class                = '::nodejs::repo::nodesource'
      }
      elsif $::operatingsystemrelease =~ /^14.04$/ {
        $manage_package_repo       = true
        $nodejs_debug_package_name = 'nodejs-dbg'
        $nodejs_dev_package_name   = 'nodejs-dev'
        $nodejs_package_name       = 'nodejs'
        $npm_package_ensure        = 'absent'
        $npm_package_name          = 'npm'
        $npm_path                  = '/usr/bin/npm'
        $repo_class                = '::nodejs::repo::nodesource'
      }
      else {
        warning("The ${module_name} module might not work on ${::operatingsystem} ${::operatingsystemrelease}. Sensible defaults will be attempted.")
        $manage_package_repo       = true
        $nodejs_debug_package_name = 'nodejs-dbg'
        $nodejs_dev_package_name   = 'nodejs-dev'
        $nodejs_package_name       = 'nodejs'
        $npm_package_ensure        = 'absent'
        $npm_package_name          = 'npm'
        $npm_path                  = '/usr/bin/npm'
        $repo_class                = '::nodejs::repo::nodesource'
      }
    }
    'RedHat': {
      if $::operatingsystemrelease =~ /^[5-7]\.(\d+)/ {
        $manage_package_repo       = true
        $nodejs_debug_package_name = 'nodejs-debuginfo'
        $nodejs_dev_package_name   = 'nodejs-devel'
        $nodejs_package_name       = 'nodejs'
        $npm_package_ensure        = 'absent'
        $npm_package_name          = 'npm'
        $npm_path                  = '/usr/bin/npm'
        $repo_class                = '::nodejs::repo::nodesource'
      }
      elsif ($::operatingsystem == 'Fedora') and ($::operatingsystemrelease > '18') {
        $manage_package_repo       = true
        $nodejs_debug_package_name = 'nodejs-debuginfo'
        $nodejs_dev_package_name   = 'nodejs-devel'
        $nodejs_package_name       = 'nodejs'
        $npm_package_ensure        = 'absent'
        $npm_package_name          = 'npm'
        $npm_path                  = '/usr/bin/npm'
        $repo_class                = '::nodejs::repo::nodesource'
      }
      else {
        fail("The ${module_name} module is not supported on ${::operatingsystem} ${::operatingsystemrelease}.")
      }
    }
    'Suse': {
      $manage_package_repo       = false
      $nodejs_debug_package_name = 'nodejs-debuginfo'
      $nodejs_dev_package_name   = 'nodejs-devel'
      $nodejs_package_name       = 'nodejs'
      $npm_package_ensure        = 'present'
      $npm_package_name          = 'npm'
      $npm_path                  = '/usr/bin/npm'
      $repo_class                = undef
    }
    'Archlinux': {
      $manage_package_repo       = false
      $nodejs_debug_package_name = undef
      $nodejs_dev_package_name   = undef
      $nodejs_package_name       = 'nodejs'
      $npm_package_ensure        = 'present'
      $npm_package_name          = undef
      $npm_path                  = '/usr/bin/npm'
      $repo_class                = undef
    }
    'FreeBSD': {
      $manage_package_repo       = false
      $nodejs_debug_package_name = undef
      $nodejs_dev_package_name   = 'www/node-devel'
      $nodejs_package_name       = 'www/node'
      $npm_package_ensure        = 'present'
      $npm_package_name          = 'www/npm'
      $npm_path                  = '/usr/bin/npm'
      $repo_class                = undef
    }
    'OpenBSD': {
      $manage_package_repo       = false
      $nodejs_debug_package_name = undef
      $nodejs_dev_package_name   = undef
      $nodejs_package_name       = 'node'
      $npm_package_ensure        = 'absent'
      $npm_package_name          = undef
      $npm_path                  = '/usr/local/bin/npm'
      $repo_class                = undef
    }
    'Darwin': {
      $manage_package_repo       = false
      $nodejs_debug_package_name = undef
      $nodejs_dev_package_name   = 'nodejs-devel'
      $nodejs_package_name       = 'nodejs'
      $npm_package_ensure        = 'present'
      $npm_package_name          = 'npm'
      $npm_path                  = '/opt/local/bin/npm'
      $repo_class                = undef
      Package { provider => 'macports' }
    }
    'Windows': {
      $manage_package_repo       = false
      $nodejs_debug_package_name = undef
      $nodejs_dev_package_name   = undef
      $nodejs_package_name       = 'nodejs'
      $npm_package_ensure        = 'absent'
      $npm_package_name          = 'npm'
      $npm_path                  = '"C:\Program Files\nodejs\npm.cmd"'
      $repo_class                = undef
      Package { provider => 'chocolatey' }
    }
    # Gentoo was added as its own $::osfamily in Facter 1.7.0
    'Gentoo': {
      $manage_package_repo       = false
      $nodejs_debug_package_name = undef
      $nodejs_dev_package_name   = undef
      $nodejs_package_name       = 'net-libs/nodejs'
      $npm_package_ensure        = 'absent'
      $npm_package_name          = undef
      $npm_path                  = '/usr/bin/npm'
      $repo_class                = undef
    }
    'Linux': {
    # Before Facter 1.7.0 Gentoo did not have its own $::osfamily
      case $::operatingsystem {
        'Gentoo': {
          $manage_package_repo       = false
          $nodejs_debug_package_name = undef
          $nodejs_dev_package_name   = undef
          $nodejs_package_name       = 'net-libs/nodejs'
          $npm_package_ensure        = 'absent'
          $npm_package_name          = undef
          $npm_path                  = '/usr/bin/npm'
          $repo_class                = undef
        }
        'Amazon': {
          $manage_package_repo       = true
          $nodejs_debug_package_name = 'nodejs-debuginfo'
          $nodejs_dev_package_name   = 'nodejs-devel'
          $nodejs_package_name       = 'nodejs'
          $npm_package_ensure        = 'absent'
          $npm_package_name          = 'npm'
          $npm_path                  = '/usr/bin/npm'
          $repo_class                = '::nodejs::repo::nodesource'
        }
        default: {
          fail("The ${module_name} module is not supported on an ${::operatingsystem} distribution.")
        }
      }
    }

    default: {
      fail("The ${module_name} module is not supported on a ${::osfamily} based system.")
    }
  }
}
