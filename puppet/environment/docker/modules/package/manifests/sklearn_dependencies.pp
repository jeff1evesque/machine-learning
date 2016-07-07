### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::sklearn_dependencies {
    ## variables
    $dependencies = [
        'python-dev=2.7.5-5ubuntu3',
        'python-numpy=1:1.8.2-0ubuntu0.1',
        'python-scipy=0.13.3-1build1',
        'libatlas-dev=3.10.1-4',
        'g++=4:4.8.2-1ubuntu6',
        'python-matplotlib=1.3.1-1ubuntu5',
        'ipython=1.2.1-2'
    ]

    ## install dependencies
    ensure_packages( $dependencies )
}