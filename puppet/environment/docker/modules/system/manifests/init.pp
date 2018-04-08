###
### init.pp: configure system with general requirements.
###
class system  (
    $region   = $::system::params::region
    $locality = $::system::params::locality
) inherits ::system::params {
    class { 'system::timezone': } ->
    Class['system']
}
