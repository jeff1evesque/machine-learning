### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::sklearn_dependencies {
    ## variables
    $dependencies = [
        'python-dev',
        'python-numpy',
        'python-numpy-dev',
        'python-scipy',
        'libatlas-dev',
        'g++',
        'python-matplotlib',
        'ipython'
    ]

    ## install dependencies
    ensure_packages( $dependencies )
}