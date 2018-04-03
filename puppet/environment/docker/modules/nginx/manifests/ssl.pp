###
### ssl.pp, configure ssl certificates for nginx.
###
class nginx::ssl {
    ## local variables
    $self_signed       = $nginx::self_signed
    $vhost             = $nginx::vhost
    $cert_path         = $nginx::cert_path
    $pkey_path         = $nginx::pkey_path
    $cert_country      = $nginx::cert_country
    $cert_org          = $nginx::cert_org
    $cert_state        = $nginx::cert_state
    $cert_locality     = $nginx::cert_locality
    $cert_unit         = $nginx::cert_unit
    $cert_bit          = $nginx::cert_bit
    $cert_days         = $nginx::cert_days

    ## create ssl certificate
    if $self_signed {
        file { "/root/build/ssl-nginx-${::nginx::type}":
            ensure         => present,
            content        => dos2unix(template("webserver/ssl-${::nginx::type}.erb")),
            owner          => 'root',
            group          => 'root',
            mode           => '0700',
            require        => File['/root/build'],
            notify         => Exec["create-certificate-${::nginx::type}"],
        }

        exec { "create-certificate-${::nginx::type}":
            command        => "./ssl-nginx-${::nginx::type}",
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
