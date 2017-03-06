###
### install_sklearn.pp, install sklearn, after dependencies built.
###
class sklearn::install_sklearn {
    ## set dependency
    require python

    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    ## install sklearn
    exec { 'install-sklearn':
        command => 'python setup.py install',
        cwd     => "${root_dir}/build/scikit-learn/",
        path    => '/usr/bin',
    }
}