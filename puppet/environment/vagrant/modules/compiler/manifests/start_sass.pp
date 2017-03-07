###
### start_sass.pp, ensure custom sass service running.
###
class compiler::start_sass {
    include compiler::webcompilers

    service { 'sass':
        ensure  => 'running',
        enable  => true,
        require => Class['compiler::webcompilers'],
    }
}