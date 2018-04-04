###
### config.pp, configure nginx.
###
class reverse_proxy::config {
    ## local variables
    $self_signed       = $reverse_proxy::self_signed
    $vhost             = $reverse_proxy::vhost
    $cert_path         = $reverse_proxy::cert_path
    $pkey_path         = $reverse_proxy::pkey_path
    $cert_country      = $reverse_proxy::cert_country
    $cert_org          = $reverse_proxy::cert_org
    $cert_state        = $reverse_proxy::cert_state
    $cert_locality     = $reverse_proxy::cert_locality
    $cert_unit         = $reverse_proxy::cert_unit
    $cert_bit          = $reverse_proxy::cert_bit
    $cert_days         = $reverse_proxy::cert_days

    ## nginx reverse proxy
    ##
    ## @497, redirect 'http://' to 'https://'
    ##
    reverse_proxy::resource::vhost { $reverse_proxy::vhost:
        ssl             => true,
        ssl_cert        => "${::reverse_proxy::cert_path}/${::reverse_proxy::vhost}_${::reverse_proxy::type}.crt",
        ssl_key         => "${::reverse_proxy::pkey_path}/${::reverse_proxy::vhost}_${::reverse_proxy::type}.key",
        listen_port     => $reverse_proxy::listen_port,
        ssl_port        => $reverse_proxy::listen_port,
        error_pages     => {
            '497' => "https://\$host:${::reverse_proxy::host_port}\$request_uri",
        },
        proxy           => "${::ngnix::proxy}:${webserver_port}",
    }

    ## create ssl certificate
    if $self_signed {
        file { "/root/build/ssl-nginx-${::reverse_proxy::type}":
            ensure         => present,
            content        => dos2unix(template("webserver/ssl-${::reverse_proxy::type}.erb")),
            owner          => 'root',
            group          => 'root',
            mode           => '0700',
            require        => File['/root/build'],
            notify         => Exec["create-certificate-${::reverse_proxy::type}"],
        }

        exec { "create-certificate-${::reverse_proxy::type}":
            command        => "./ssl-nginx-${::reverse_proxy::type}",
            cwd            => '/root/build',
            path           => '/usr/bin',
            provider       => shell,
            refreshonly    => true,
        }
    }

    else {
        notify {'Please remember to provide your own certificate!':}
    }
}
