###
### dependency.pp, installs various clients, and modules to interface with
###     the webserver.
###
class webserver::dependency {
    file { '/root/build':
        ensure => directory,
        mode   => '0700',
        owner  => 'root',
        group  => 'root',
    }
}
