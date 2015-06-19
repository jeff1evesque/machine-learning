class apt::backports (
  $location = undef,
  $release  = undef,
  $repos    = undef,
  $key      = undef,
  $pin      = 200,
){
  if $location {
    validate_string($location)
    $_location = $location
  }
  if $release {
    validate_string($release)
    $_release = $release
  }
  if $repos {
    validate_string($repos)
    $_repos = $repos
  }
  if $key {
    unless is_hash($key) {
      validate_string($key)
    }
    $_key = $key
  }
  unless is_hash($pin) {
    unless (is_numeric($pin) or is_string($pin)) {
      fail('pin must be either a string, number or hash')
    }
  }

  if ($::apt::xfacts['lsbdistid'] == 'debian' or $::apt::xfacts['lsbdistid'] == 'ubuntu') {
    unless $location {
      $_location = $::apt::backports['location']
    }
    unless $release {
      $_release = "${::apt::xfacts['lsbdistcodename']}-backports"
    }
    unless $repos {
      $_repos = $::apt::backports['repos']
    }
    unless $key {
      $_key =  $::apt::backports['key']
    }
  } else {
    unless $location and $release and $repos and $key {
      fail('If not on Debian or Ubuntu, you must explicitly pass location, release, repos, and key')
    }
  }

  apt::source { 'backports':
    location => $_location,
    release  => $_release,
    repos    => $_repos,
    key      => $_key,
    pin      => $pin,
  }

}
