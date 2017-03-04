### Note: the prefix 'sklearn::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class sklearn::build_sklearn {
    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    ## build sklearn
    exec { 'build-sklearn':
        command => 'python setup.py build',
        cwd     => "${root_dir}/build/scikit-learn/",
        path    => '/usr/bin',
        timeout => 1800,
    }
}