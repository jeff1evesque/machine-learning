### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::pytest_flask {
    require python

    package { 'pytest-flask':
        ensure   => '0.10.0',
        provider => 'pip',
    }
}