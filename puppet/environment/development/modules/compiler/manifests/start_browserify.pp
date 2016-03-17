### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_browserify {
    service { 'browserify':
        ensure => 'running',
        enable => true,
    }
}