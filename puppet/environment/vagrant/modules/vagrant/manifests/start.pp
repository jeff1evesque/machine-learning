###
### start.pp, ensure vagrant work around service running.
###
class vagrant::start {
    service { 'workaround-vagrant-bug-6074':
        ensure => 'running',
        enable => true,
    }
}