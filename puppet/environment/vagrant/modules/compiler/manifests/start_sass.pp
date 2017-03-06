###
### start_sass.pp, ensure custom sass service running.
###
class compiler::start_sass {
    service { 'sass':
        ensure => 'running',
        enable => true,
    }
}