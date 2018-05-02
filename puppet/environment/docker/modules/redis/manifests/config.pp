###
### config.pp, configure redis-server.
###
class redis::config {
    ## variables
    $bind_address  = $::redis::bind_address
    $config_file   = $::redis::config_file

    ## configure redis-server
    file { $config_file:
        ensure  => file,
        owner   => 'root',
        group   => 'root',
        content => dos2unix(template('redis/config.erb')),
        mode    => '770',
    }
}