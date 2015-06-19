# PRIVATE CLASS: Do not use directly.
class nodejs::repo::nodesource::yum {
  $baseurl        = $nodejs::repo::nodesource::baseurl
  $descr          = $nodejs::repo::nodesource::descr
  $enable_src     = $nodejs::repo::nodesource::enable_src
  $ensure         = $nodejs::repo::nodesource::ensure
  $priority       = $nodejs::repo::nodesource::priority
  $proxy          = $nodejs::repo::nodesource::proxy
  $proxy_password = $nodejs::repo::nodesource::proxy_password
  $proxy_username = $nodejs::repo::nodesource::proxy_username
  $source_baseurl = $nodejs::repo::nodesource::source_baseurl
  $source_descr   = $nodejs::repo::nodesource::source_descr

  $yum_source_enabled = $enable_src ? {
    true    => '1',
    default => '0',
  }

  if ($ensure == 'present') {

    yumrepo { 'nodesource':
      descr          => $descr,
      baseurl        => $baseurl,
      enabled        => '1',
      failovermethod => 'priority',
      gpgkey         => 'file:///etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL',
      gpgcheck       => '1',
      priority       => $priority,
      proxy          => $proxy,
      proxy_password => $proxy_password,
      proxy_username => $proxy_username,
    }

    yumrepo { 'nodesource-source':
      descr          => $source_descr,
      baseurl        => $source_baseurl,
      enabled        => $yum_source_enabled,
      failovermethod => 'priority',
      gpgkey         => 'file:///etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL',
      gpgcheck       => '1',
      priority       => $priority,
      proxy          => $proxy,
      proxy_password => $proxy_password,
      proxy_username => $proxy_username,
    }

    file { '/etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL':
      ensure => present,
      group  => 'root',
      mode   => '0644',
      owner  => 'root',
      source => "puppet:///modules/${module_name}/repo/nodesource/NODESOURCE-GPG-SIGNING-KEY-EL",
    }

    gpg_key{ 'nodesource':
      path   => '/etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL',
      before => [ Yumrepo['nodesource'], Yumrepo['nodesource-source'], ],
    }
  }

  else {

    yumrepo { 'nodesource':
      enabled => 'absent',
    }

    yumrepo { 'nodesource-source':
      enabled => 'absent',
    }
  }
}
