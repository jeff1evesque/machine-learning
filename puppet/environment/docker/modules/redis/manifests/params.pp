###
### params.pp: default class parameters.
###
class redis::params {
    $hiera            = lookup( { 'name' => 'redis', 'default_value' => false } )
    $run              = true
    $version          = '*'

    if $hiera {
        $bind_address = $hiera['bind_address']
        $config_file  = $hiera['config_file']
    }

    else {
        $bind_address = '0.0.0.0'
        $config_file  = '/etc/redis/redis.conf'
    }
}
