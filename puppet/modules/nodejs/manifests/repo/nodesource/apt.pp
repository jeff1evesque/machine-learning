# PRIVATE CLASS: Do not use directly.
class nodejs::repo::nodesource::apt {

  $enable_src = $nodejs::repo::nodesource::enable_src
  $ensure     = $nodejs::repo::nodesource::ensure
  $pin        = $nodejs::repo::nodesource::pin
  $url_suffix = $nodejs::repo::nodesource::url_suffix

  include ::apt

  if ($ensure == 'present') {
    apt::source { 'nodesource':
      include_src       => $enable_src,
      key               => '9FD3B784BC1C6FC31A8A0A1C1655A0AB68576280',
      key_source        => 'https://deb.nodesource.com/gpgkey/nodesource.gpg.key',
      location          => "https://deb.nodesource.com/${url_suffix}",
      pin               => $pin,
      release           => $::lsbdistcodename,
      repos             => 'main',
      required_packages => 'apt-transport-https ca-certificates',
    }
  }

  else {
    apt::source { 'nodesource':
      ensure => 'absent',
    }
  }
}
