### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::inotify_tools {
    ## update apt-get
    include apt

    package { 'inotify-tools':
        ensure => 'installed',
    }
}