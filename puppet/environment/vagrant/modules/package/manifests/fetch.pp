### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::fetch {
    ## package: install general packages (npm)
    package { 'whatwg-fetch@0.11.0':
        ensure   => 'present',
        provider => 'npm',
    }
}