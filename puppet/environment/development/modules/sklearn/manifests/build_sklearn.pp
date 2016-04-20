### Note: the prefix 'sklearn::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class sklearn::build_sklearn {
    exec { 'build-sklearn':
        command => 'python setup.py build',
        cwd     => '/vagrant/build/scikit-learn/',
        path    => '/usr/bin',
    }
}