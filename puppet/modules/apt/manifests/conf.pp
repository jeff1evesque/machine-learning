define apt::conf (
  $content  = undef,
  $ensure   = present,
  $priority = '50',
) {

  unless $ensure == 'absent' {
    unless $content {
      fail('Need to pass in content parameter')
    }
  }

  apt::setting { "conf-${name}":
    ensure   => $ensure,
    priority => $priority,
    content  => template('apt/_header.erb', 'apt/conf.erb'),
  }
}
