### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::six {
    require python

    package { 'six':
        ensure   => '1.5.2',
        provider => 'pip',
    }
}