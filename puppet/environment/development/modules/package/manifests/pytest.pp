### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::pytest {
    require python

    package { 'pytest':
        ensure   => '2.9.2',
        provider => 'pip',
    }
}