### Note: the prefix 'sklearn::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
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