### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::dos2unix {
    ## update apt-get
    include apt

    package { 'dos2unix':
        ensure => 'installed',
    }
}