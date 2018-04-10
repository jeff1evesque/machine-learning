###
### init.pp: install sklearn, with all necessary dependencies.
###
### Note: this module has the following dependency:
###
###     - https://github.com/counsyl/puppet-python.git
###
class sklearn (
    $python_numpy      = $::sklearn::params::python_numpy,
    $python_scipy      = $::sklearn::params::python_scipy,
    $libatlas_dev      = $::sklearn::params::libatlas_dev,
    $gplus             = $::sklearn::params::gplus,
    $ipython           = $::sklearn::params::ipython,
    $python_dev        = $::sklearn::params::python_dev,
    $python_matplotlib = $::sklearn::params::python_matplotlib,
    $root_dir          = $::sklearn::params::root_dir,
) inherits ::sklearn::params {
    class { 'sklearn::dependency': } ->
    class { 'sklearn::install': } ->
    Class['sklearn']
}
