### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::inotify_tools {
    ## update apt-get
    require apt

    package { 'inotify-tools':
        ensure => '3.14-1ubuntu1',
    }
}