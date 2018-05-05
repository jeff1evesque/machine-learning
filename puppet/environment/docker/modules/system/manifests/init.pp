###
### init.pp: configure system with general requirements.
###
### Note: this module has the following dependency:
###
###     - https://github.com/puppetlabs/puppetlabs-apt.git
###     - https://github.com/counsyl/puppet-python.git
###     - https://github.com/BashtonLtd/puppet-timezone.git
###
class system (
    $region         = $::system::params::region,
    $locality       = $::system::params::locality,
    $packages       = $::system::params::packages,
) inherits ::system::params {
    class { 'system::timezone': } ->
    class { 'system::packages': } ->
    Class['system']
}
