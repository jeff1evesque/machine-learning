###
### init.pp: install jest.
###

class jest (
    $version = $::jest::params::version,
) inherits ::jest::params {
    class { 'jest::install': } ->
    Class['jest']
}
