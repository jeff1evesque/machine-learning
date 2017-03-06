###
### configuration.pp, configure redis-server.
###
class redis::configuration {
    ## variables
    $hiera_redis   = lookup('redis')
    $bind_address  = $hiera_redis['bind_address']
    $config_file   = $hiera_redis['path']
    $template_path = 'redis/configuration.erb'

    ## configure redis-server
    file { $config_file:
        ensure  => file,
        owner   => 'root',
        group   => 'root',
        content => dos2unix(template($template_path)),
        mode    => '770',
    }
}