###
### start.pp, ensure vagrant workaround service running.
###
class vagrant::start {
    service { 'workaround-vagrant-bug-6074':
        ensure => 'running',
        enable => true,
    }
}