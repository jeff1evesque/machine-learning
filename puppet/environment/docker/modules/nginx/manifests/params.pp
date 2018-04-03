###
### init.pp: configure, and start nginx.
###
### @webserver_port, corresponds to an existing webserver.
###
class nginx::params {
    $hiera          = lookup('reverse_proxy')
    $type           = $hiera['type']
    $vhost          = $hiera['vhost']
    $host_port      = $hiera['host_port']
    $listen_port    = $hiera['listen_port']
    $webserver_port = $hiera['webserver_port']
    $proxy          = $hiera['proxy']
    $cert_path      = $hiera['certificate']['cert_path']
    $pkey_path      = $hiera['certificate']['pkey_path']
    $cert_country   = $hiera['certificate']['props']['country']
    $cert_org       = $hiera['certificate']['props']['org']
    $cert_state     = $hiera['certificate']['props']['state']
    $cert_locality  = $hiera['certificate']['props']['locality']
    $cert_unit      = $hiera['certificate']['props']['unit']
    $cert_bit       = $hiera['certificate']['props']['bit']
    $cert_days      = $hiera['certificate']['props']['days']
}
