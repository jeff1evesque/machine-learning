## define system timezone
class { 'timezone':
  region   => 'America',
  locality => 'New_York',
}